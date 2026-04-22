"""
schema.py
---------
Column name definitions and groupings for the TAAC2026 dataset.

Dataset: demo_1000.parquet (flat column layout, 120 columns total)
Updated: 2026-04-10 (official dataset v2)

Column categories:
  - ID & Label         : 5 cols
  - User Int Features  : 46 cols (35 scalar + 11 array)
  - User Dense Features: 10 cols (list<float>)
  - Item Int Features  : 14 cols (13 scalar + 1 array)
  - Domain Sequences   : 45 cols (4 behavioral domains)

TODO: Implement column groupings
"""

# ── ID & Label ──────────────────────────────────────────────────────────────
ID_LABEL_COLS = ["user_id", "item_id", "label_type", "label_time", "timestamp"]

# ── User Int Features ────────────────────────────────────────────────────────
# Scalar int64 (35 cols): user_int_feats_{1,3,4,48-59,82,86,92-109}
USER_INT_SCALAR_FIDS = (
    [1, 3, 4]
    + list(range(48, 60))
    + [82, 86]
    + list(range(92, 110))
)
USER_INT_SCALAR_COLS = [f"user_int_feats_{i}" for i in USER_INT_SCALAR_FIDS]

# Array list<int64> (11 cols): user_int_feats_{15,60,62-66,80,89-91}
USER_INT_ARRAY_FIDS = [15, 60] + list(range(62, 67)) + [80] + list(range(89, 92))
USER_INT_ARRAY_COLS = [f"user_int_feats_{i}" for i in USER_INT_ARRAY_FIDS]

# ── User Dense Features ───────────────────────────────────────────────────────
# Array list<float> (10 cols): user_dense_feats_{61-66,87,89-91}
# NOTE: fid shared with user_int_feats means they describe the same entity
USER_DENSE_FIDS = list(range(61, 67)) + [87] + list(range(89, 92))
USER_DENSE_COLS = [f"user_dense_feats_{i}" for i in USER_DENSE_FIDS]

# ── Item Int Features ─────────────────────────────────────────────────────────
# Scalar int64 (13 cols): item_int_feats_{5-10,12-13,16,81,83-85}
ITEM_INT_SCALAR_FIDS = (
    list(range(5, 11))
    + [12, 13, 16, 81]
    + list(range(83, 86))
)
ITEM_INT_SCALAR_COLS = [f"item_int_feats_{i}" for i in ITEM_INT_SCALAR_FIDS]

# Array list<int64> (1 col): item_int_feats_11
ITEM_INT_ARRAY_COLS = ["item_int_feats_11"]

# ── Domain Sequence Features ──────────────────────────────────────────────────
# Each domain has multiple columns representing different attributes of the sequence
# (e.g., item_id, action_type, timestamp, ...). Columns within same domain are
# positionally aligned: domain_cols[i][t] all refer to the same interaction at step t.
DOMAIN_A_COLS = [f"domain_a_seq_{i}" for i in range(38, 47)]           # 9 cols
DOMAIN_B_COLS = [f"domain_b_seq_{i}" for i in list(range(67, 80)) + [88]]  # 14 cols
DOMAIN_C_COLS = [f"domain_c_seq_{i}" for i in list(range(27, 38)) + [47]]  # 12 cols
DOMAIN_D_COLS = [f"domain_d_seq_{i}" for i in range(17, 27)]           # 10 cols

ALL_SEQ_DOMAINS: dict = {
    "domain_a": DOMAIN_A_COLS,
    "domain_b": DOMAIN_B_COLS,
    "domain_c": DOMAIN_C_COLS,
    "domain_d": DOMAIN_D_COLS,
}

# ── Summary ───────────────────────────────────────────────────────────────────
TOTAL_COLS = (
    len(ID_LABEL_COLS)
    + len(USER_INT_SCALAR_COLS)
    + len(USER_INT_ARRAY_COLS)
    + len(USER_DENSE_COLS)
    + len(ITEM_INT_SCALAR_COLS)
    + len(ITEM_INT_ARRAY_COLS)
    + sum(len(v) for v in ALL_SEQ_DOMAINS.values())
)
assert TOTAL_COLS == 120, f"Expected 120 cols, got {TOTAL_COLS}"
