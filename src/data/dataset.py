"""
dataset.py - PyTorch Dataset for TAAC2026 pCVR Prediction

Handles:
  - Load parquet file into memory
  - Label remapping: {1, 2} -> {0, 1}  (1=neg, 2=pos)
  - Sequence truncation (keep most recent N items per domain)
  - Null / NaN filling (0 for int, 0.0 for float, [] for list)
  - Dynamic type detection: scalar float vs list per column

Output per sample (dict of tensors):
  - "user_id"      : LongScalar
  - "item_id"      : LongScalar
  - "label"        : LongScalar (0 or 1)
  - "timestamp"    : LongScalar

  Non-seq features (for Embedding / MLP):
  - "user_int_scalar" : FloatTensor  [N_user_scalar]   (NaN -> 0.0)
  - "user_int_array"  : LongTensor   [N_user_array, max_array_len]  (padded, null -> all 0)
  - "user_dense"      : FloatTensor  [N_user_dense, dense_dim]     (padded to max_dim)
  - "item_int_scalar" : FloatTensor  [N_item_scalar]   (NaN -> 0.0)
  - "item_int_array"  : LongTensor   [max_item_array_len]           (padded)

  Sequence features (for Unified Token Pool):
  - "seq_{domain}"    : LongTensor   [max_seq_len, n_cols_per_domain]  (truncated + padded)
  - "seq_{domain}_mask": BoolTensor [max_seq_len]  (True = valid)

Usage:
    dataset = TAAC2026Dataset("data/raw/demo_1000.parquet")
    sample = dataset[0]
    loader = DataLoader(dataset, batch_size=64, collate_fn=taac_collate_fn)
"""

import numpy as np
import pandas as pd
import torch
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from src.data.schema import (
    LABEL_COL, LABEL_MAP, ID_COLS, TIME_COLS,
    USER_INT_SCALAR_COLS, USER_INT_ARRAY_COLS,
    USER_DENSE_COLS,
    ITEM_INT_SCALAR_COLS, ITEM_INT_ARRAY_COLS,
    ALL_SEQ_DOMAINS, DEFAULT_SEQ_MAX_LEN,
)


def _is_list_series(series: pd.Series) -> bool:
    """Check if a pandas Series contains list/ndarray values (not scalars)."""
    sample = series.dropna()
    if len(sample) == 0:
        return False
    first = sample.iloc[0]
    return isinstance(first, (list, np.ndarray))


def _to_fixed_len_list(arr, target_len: int, pad_value: int = 0) -> List[int]:
    """Truncate or pad a list to fixed length."""
    if isinstance(arr, (list, np.ndarray)):
        arr = list(arr)
    else:
        arr = [arr]
    if len(arr) >= target_len:
        return arr[:target_len]
    return arr + [pad_value] * (target_len - len(arr))


class TAAC2026Dataset(torch.utils.data.Dataset):
    """PyTorch Dataset for TAAC2026 parquet data.

    The entire parquet is loaded into memory at init time.
    Columns are automatically classified as scalar vs list at first load.
    """

    def __init__(
        self,
        data_path: str,
        seq_max_len: Optional[Dict[str, int]] = None,
        max_array_len: int = 64,
        dense_pad_dim: int = 320,
        mode: str = "train",
        val_ratio: float = 0.15,
    ):
        """
        Args:
            data_path: Path to .parquet file.
            seq_max_len: Per-domain max sequence length (truncate longer, pad shorter).
                         Defaults to p95 from EDA via schema.DEFAULT_SEQ_MAX_LEN.
            max_array_len: Max length for multi-value int array features (user_int_array, item_int_array).
            dense_pad_dim: Pad all dense vectors to this dimension (use the largest, 320).
            mode: "train" or "val". Splits by timestamp (time-based split, NOT random).
            val_ratio: Fraction of data to use for validation (oldest timestamps as val).
        """
        self.max_array_len = max_array_len
        self.dense_pad_dim = dense_pad_dim
        self.seq_max_len = seq_max_len or DEFAULT_SEQ_MAX_LEN

        # Load data
        df = pd.read_parquet(data_path)
        assert len(df.columns) == 120, f"Expected 120 columns, got {len(df.columns)}"

        # ── Time-based train/val split ──────────────────────────────────────
        if mode in ("train", "val"):
            df = df.sort_values("timestamp").reset_index(drop=True)
            split_idx = int(len(df) * (1 - val_ratio))
            if mode == "train":
                df = df.iloc[:split_idx].reset_index(drop=True)
            else:
                df = df.iloc[split_idx:].reset_index(drop=True)
        elif mode == "all":
            pass  # use all data
        else:
            raise ValueError(f"Unknown mode: {mode}")

        self.df = df

        # ── Dynamic column type detection ───────────────────────────────────
        # Re-classify columns: some columns marked as "scalar" in schema might
        # actually be lists in the real data, and vice versa. Detect at runtime.
        self.user_int_scalar_cols = [c for c in USER_INT_SCALAR_COLS if not _is_list_series(df[c])]
        self.user_int_array_cols = [c for c in USER_INT_ARRAY_COLS if _is_list_series(df[c])]
        # Also check: any "scalar" columns that are actually lists?
        newly_found_arrays = [c for c in USER_INT_SCALAR_COLS if _is_list_series(df[c])]
        if newly_found_arrays:
            self.user_int_array_cols.extend(newly_found_arrays)
        # And any "array" columns that are actually scalars?
        newly_found_scalars = [c for c in USER_INT_ARRAY_COLS if not _is_list_series(df[c])]
        if newly_found_scalars:
            self.user_int_scalar_cols.extend(newly_found_scalars)

        self.item_int_scalar_cols = [c for c in ITEM_INT_SCALAR_COLS if not _is_list_series(df[c])]
        self.item_int_array_cols = [c for c in ITEM_INT_ARRAY_COLS if _is_list_series(df[c])]
        newly_item_arrays = [c for c in ITEM_INT_SCALAR_COLS if _is_list_series(df[c])]
        if newly_item_arrays:
            self.item_int_array_cols.extend(newly_item_arrays)
        newly_item_scalars = [c for c in ITEM_INT_ARRAY_COLS if not _is_list_series(df[c])]
        if newly_item_scalars:
            self.item_int_scalar_cols.extend(newly_item_scalars)

        # ── Dense dimension detection ───────────────────────────────────────
        # Find actual max dim across all dense cols for padding
        actual_max_dim = 0
        self.dense_dims = {}
        for col in USER_DENSE_COLS:
            sample = df[col].dropna()
            if len(sample) > 0:
                first = sample.iloc[0]
                if isinstance(first, (list, np.ndarray)):
                    dim = len(first)
                else:
                    dim = 1
            else:
                dim = 0
            self.dense_dims[col] = dim
            actual_max_dim = max(actual_max_dim, dim)
        self.dense_pad_dim = max(self.dense_pad_dim, actual_max_dim)

        # Print summary
        print(f"[Dataset] mode={mode}, samples={len(df)}")
        print(f"  user_int_scalar: {len(self.user_int_scalar_cols)} cols")
        print(f"  user_int_array:  {len(self.user_int_array_cols)} cols")
        print(f"  user_dense:      {len(USER_DENSE_COLS)} cols (pad_dim={self.dense_pad_dim})")
        print(f"  item_int_scalar: {len(self.item_int_scalar_cols)} cols")
        print(f"  item_int_array:  {len(self.item_int_array_cols)} cols")
        for domain, cols in ALL_SEQ_DOMAINS.items():
            print(f"  {domain}: {len(cols)} cols, max_len={self.seq_max_len.get(domain, 'N/A')}")

    def __len__(self) -> int:
        return len(self.df)

    def __getitem__(self, idx: int) -> Dict[str, torch.Tensor]:
        row = self.df.iloc[idx]
        return self._parse_row(row)

    def _parse_row(self, row: pd.Series) -> Dict[str, torch.Tensor]:
        result = {}

        # ── IDs & Label ────────────────────────────────────────────────────
        for col in ID_COLS:
            result[col] = torch.tensor(row[col], dtype=torch.long)

        # Label remapping: {1, 2} -> {0, 1}
        label_val = row[LABEL_COL]
        result["label"] = torch.tensor(LABEL_MAP.get(label_val, 0), dtype=torch.long)

        # Timestamp
        result["timestamp"] = torch.tensor(row["timestamp"], dtype=torch.long)

        # ── User Int Scalar (float -> float, NaN -> 0.0) ───────────────────
        scalar_vals = []
        for col in self.user_int_scalar_cols:
            v = row[col]
            if pd.isna(v):
                scalar_vals.append(0.0)
            else:
                scalar_vals.append(float(v))
        result["user_int_scalar"] = torch.tensor(scalar_vals, dtype=torch.float)

        # ── User Int Array (list of int -> padded LongTensor) ───────────────
        if self.user_int_array_cols:
            arrays = []
            for col in self.user_int_array_cols:
                v = row[col]
                if v is None or (isinstance(v, float) and np.isnan(v)) or not isinstance(v, (list, np.ndarray)):
                    arrays.append([0] * self.max_array_len)
                else:
                    arrays.append(_to_fixed_len_list(v, self.max_array_len, pad_value=0))
            result["user_int_array"] = torch.tensor(arrays, dtype=torch.long)
        else:
            result["user_int_array"] = torch.zeros(0, self.max_array_len, dtype=torch.long)

        # ── User Dense (list of float -> padded FloatTensor) ───────────────
        if USER_DENSE_COLS:
            dense_list = []
            for col in USER_DENSE_COLS:
                v = row[col]
                if v is None or (isinstance(v, float) and np.isnan(v)):
                    dense_list.append([0.0] * self.dense_pad_dim)
                elif isinstance(v, (list, np.ndarray)):
                    v = list(v)
                    if len(v) < self.dense_pad_dim:
                        v = v + [0.0] * (self.dense_pad_dim - len(v))
                    dense_list.append(v[:self.dense_pad_dim])
                else:
                    # Scalar value -> [value, 0, 0, ...]
                    padded = [float(v)] + [0.0] * (self.dense_pad_dim - 1)
                    dense_list.append(padded)
            result["user_dense"] = torch.tensor(dense_list, dtype=torch.float)
        else:
            result["user_dense"] = torch.zeros(0, self.dense_pad_dim, dtype=torch.float)

        # ── Item Int Scalar ────────────────────────────────────────────────
        item_scalar_vals = []
        for col in self.item_int_scalar_cols:
            v = row[col]
            if pd.isna(v):
                item_scalar_vals.append(0.0)
            else:
                item_scalar_vals.append(float(v))
        result["item_int_scalar"] = torch.tensor(item_scalar_vals, dtype=torch.float)

        # ── Item Int Array ─────────────────────────────────────────────────
        if self.item_int_array_cols:
            # Flatten all item array features into one tensor
            all_vals = []
            for col in self.item_int_array_cols:
                v = row[col]
                if v is None or (isinstance(v, float) and np.isnan(v)) or not isinstance(v, (list, np.ndarray)):
                    all_vals.extend([0] * self.max_array_len)
                else:
                    all_vals.extend(_to_fixed_len_list(v, self.max_array_len, pad_value=0))
            result["item_int_array"] = torch.tensor(all_vals, dtype=torch.long)
        else:
            result["item_int_array"] = torch.zeros(0, dtype=torch.long)

        # ── Domain Sequences ───────────────────────────────────────────────
        for domain, cols in ALL_SEQ_DOMAINS.items():
            max_len = self.seq_max_len.get(domain, 512)
            n_cols = len(cols)

            # Collect all sequences for this domain
            domain_seqs = []  # list of list[int], one per column
            valid_lens = []

            for col in cols:
                v = row[col]
                if v is None or (isinstance(v, float) and np.isnan(v)) or not isinstance(v, (list, np.ndarray)):
                    domain_seqs.append([])
                    valid_lens.append(0)
                else:
                    seq = list(v)
                    # Take most recent (last) max_len items
                    if len(seq) > max_len:
                        seq = seq[-max_len:]
                    domain_seqs.append(seq)
                    valid_lens.append(len(seq))

            # All columns in same domain should have same length
            # Use the max valid length as the actual sequence length
            actual_len = max(valid_lens) if valid_lens else 0

            # Build (actual_len, n_cols) matrix + pad to (max_len, n_cols)
            if actual_len == 0:
                # All null -> zero matrix
                seq_matrix = torch.zeros(max_len, n_cols, dtype=torch.long)
                seq_mask = torch.zeros(max_len, dtype=torch.bool)
            else:
                # Pad each column to actual_len, then pad to max_len
                padded_cols = []
                for seq in domain_seqs:
                    if len(seq) < actual_len:
                        seq = seq + [0] * (actual_len - len(seq))
                    # Truncate to max_len (should already be done above)
                    seq = seq[:max_len]
                    padded_cols.append(seq)

                # Pad to max_len at the end (prepend zeros = pad old items)
                if actual_len < max_len:
                    pad_width = max_len - actual_len
                    for i in range(len(padded_cols)):
                        padded_cols[i] = [0] * pad_width + padded_cols[i]

                seq_matrix = torch.tensor(padded_cols, dtype=torch.long).T  # (max_len, n_cols)
                seq_mask = torch.zeros(max_len, dtype=torch.bool)
                seq_mask[max_len - actual_len:] = True  # True = valid position

            result[f"seq_{domain}"] = seq_matrix
            result[f"seq_{domain}_mask"] = seq_mask

        return result


# ── Collate Function ─────────────────────────────────────────────────────────
def taac_collate_fn(batch: List[Dict[str, torch.Tensor]]) -> Dict[str, torch.Tensor]:
    """Collate a list of sample dicts into a batched dict.

    For 1D tensors: stack -> (B, dim)
    For 2D tensors: stack -> (B, dim1, dim2)
    For 0D tensors (scalars): stack -> (B,)
    """
    keys = batch[0].keys()
    result = {}
    for key in keys:
        values = [sample[key] for sample in batch]
        if values[0].dim() == 0:
            result[key] = torch.stack(values)  # (B,)
        else:
            result[key] = torch.stack(values)  # (B, ...)
    return result


# ── Quick Test ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    data_path = "data/raw/demo_1000.parquet"
    dataset = TAAC2026Dataset(data_path, mode="all")

    print(f"\n{'='*60}")
    print("Sample [0] output:")
    sample = dataset[0]
    for key, tensor in sample.items():
        print(f"  {key:25s}: shape={str(list(tensor.shape)):20s} dtype={tensor.dtype}")

    print(f"\n{'='*60}")
    print("DataLoader test (batch_size=4):")
    from torch.utils.data import DataLoader
    loader = DataLoader(dataset, batch_size=4, shuffle=True, collate_fn=taac_collate_fn, num_workers=0)
    batch = next(iter(loader))
    for key, tensor in batch.items():
        print(f"  {key:25s}: shape={str(list(tensor.shape)):20s} dtype={tensor.dtype}")

    # Label check
    labels = dataset.df[LABEL_COL].map(LABEL_MAP)
    print(f"\nLabel distribution: {labels.value_counts().to_dict()}")
    print(f"Positive ratio: {labels.mean():.4f}")
    print(f"pos_weight (for BCE): {(1-labels.mean())/labels.mean():.4f}")
