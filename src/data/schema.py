"""
schema.py - Column definitions aligned with demo_1000.parquet (EDA verified)

Dataset: demo_1000.parquet (flat column layout, 120 columns, 1000 rows)
Updated: 2026-04-22 (EDA verified against real data)

Key findings from EDA:
  - label_type: {1: 876, 2: 124}, NOT 0/1. Must remap to {0, 1} for BCE.
  - Columns are named user_int_feats_X, NOT user_int_scalar/array.
    Same prefix, mixed types (scalar float64 vs list<object>) per column.
  - Dense vectors: dim 256 (fid_61), dim 320 (fid_87), dim 1/2/10 (others).
  - Sequences: domain_a(p95=1674), domain_b(p95=1565), domain_c(p95=1215), domain_d(p95=2461).
  - Null: 114/120 cols have nulls, some >80%.
  - Timestamps: unix format (e.g. 1772725027).
"""

# ── ID & Label (5 cols) ──────────────────────────────────────────────────────
ID_COLS = ["user_id", "item_id"]
LABEL_COL = "label_type"
TIME_COLS = ["label_time", "timestamp"]
ID_LABEL_COLS = ID_COLS + [LABEL_COL] + TIME_COLS

# Label mapping: original {1, 2} -> binary {0, 1}
LABEL_MAP = {1: 0, 2: 1}  # 1=negative, 2=positive(转化)

# ── User Int Features (46 cols) ──────────────────────────────────────────────
# Actual column names: user_int_feats_X where X is the fid number
# FIDs present: 1, 3, 4, 15, 48-60, 62-66, 80, 82, 86, 89-109
# Types are INFERRED from EDA (demo_1000.parquet):
#   - fid 1      : int64 scalar
#   - fid 3, 4   : float64 scalar (with nulls)
#   - fid 15     : object (list) - array type
#   - fid 48-53  : float64 scalar
#   - fid 54-59  : float64 scalar (fid_54 has 36.8% null, fid_60 has 59.2% null)
#   - fid 62-66  : object (list) - array type
#   - fid 80     : object (list) - array type
#   - fid 82     : float64 scalar
#   - fid 86     : float64 scalar (69.2% null!)
#   - fid 89-91  : object (list) - array type
#   - fid 92-109 : float64 scalar (many with high null rates)

ALL_USER_INT_FIDS = (
    [1, 3, 4, 15]
    + list(range(48, 67))
    + [80, 82, 86]
    + list(range(89, 110))
)
assert len(ALL_USER_INT_FIDS) == 46, f"Expected 46 user int cols, got {len(ALL_USER_INT_FIDS)}"

USER_INT_COLS = [f"user_int_feats_{i}" for i in ALL_USER_INT_FIDS]

# Separate by inferred type (from EDA on demo data)
# These should be re-verified on full dataset
USER_INT_SCALAR_FIDS = (
    [1, 3, 4]
    + list(range(48, 60))
    + [82, 86]
    + list(range(92, 110))
)
USER_INT_SCALAR_COLS = [f"user_int_feats_{i}" for i in USER_INT_SCALAR_FIDS]

USER_INT_ARRAY_FIDS = [15, 60] + list(range(62, 67)) + [80] + list(range(89, 92))
USER_INT_ARRAY_COLS = [f"user_int_feats_{i}" for i in USER_INT_ARRAY_FIDS]

# ── User Dense Features (10 cols) ────────────────────────────────────────────
# NOTE: fid shared with user_int_feats means they describe the same entity
# Dimensions from EDA:
#   fid_61: dim=256, fid_62-66: dim varies(1-2, inconsistent!), fid_87: dim=320, fid_89-91: dim=10
USER_DENSE_FIDS = list(range(61, 67)) + [87] + list(range(89, 92))
USER_DENSE_COLS = [f"user_dense_feats_{i}" for i in USER_DENSE_FIDS]

# Known dense vector dimensions (from demo data, may vary in full dataset)
USER_DENSE_DIMS = {
    "user_dense_feats_61": 256,
    "user_dense_feats_87": 320,
    "user_dense_feats_89": 10,
    "user_dense_feats_90": 10,
    "user_dense_feats_91": 10,
    # fid 62-66 have INCONSISTENT dimensions in demo data - needs investigation
}

# ── Item Int Features (14 cols) ──────────────────────────────────────────────
# FIDs: 5-13, 16, 81, 83-85
# Most are float64 scalar. item_int_feats_11 is object(list) - array type.
ITEM_INT_FIDS = (
    list(range(5, 14))
    + [16, 81]
    + list(range(83, 86))
)
assert len(ITEM_INT_FIDS) == 14, f"Expected 14 item int cols, got {len(ITEM_INT_FIDS)}"

ITEM_INT_COLS = [f"item_int_feats_{i}" for i in ITEM_INT_FIDS]

ITEM_INT_SCALAR_COLS = [f"item_int_feats_{i}" for i in ITEM_INT_FIDS if i != 11]
ITEM_INT_ARRAY_COLS = ["item_int_feats_11"]

# ── Domain Sequence Features (45 cols) ───────────────────────────────────────
# Each domain: multiple columns aligned by position (same timestep)
# domain_a: 9 cols, domain_b: 14 cols, domain_c: 12 cols, domain_d: 10 cols
DOMAIN_A_SEQ_IDS = list(range(38, 47))                    # 9 cols
DOMAIN_B_SEQ_IDS = list(range(67, 80)) + [88]             # 14 cols
DOMAIN_C_SEQ_IDS = list(range(27, 38)) + [47]             # 12 cols
DOMAIN_D_SEQ_IDS = list(range(17, 27))                    # 10 cols

DOMAIN_A_COLS = [f"domain_a_seq_{i}" for i in DOMAIN_A_SEQ_IDS]
DOMAIN_B_COLS = [f"domain_b_seq_{i}" for i in DOMAIN_B_SEQ_IDS]
DOMAIN_C_COLS = [f"domain_c_seq_{i}" for i in DOMAIN_C_SEQ_IDS]
DOMAIN_D_COLS = [f"domain_d_seq_{i}" for i in DOMAIN_D_SEQ_IDS]

ALL_SEQ_DOMAINS: dict = {
    "domain_a": DOMAIN_A_COLS,
    "domain_b": DOMAIN_B_COLS,
    "domain_c": DOMAIN_C_COLS,
    "domain_d": DOMAIN_D_COLS,
}

# Sequence length stats from EDA (demo_1000, 1000 rows)
SEQ_LEN_STATS = {
    "domain_a": {"p50": 582, "p95": 1674, "p99": 1793, "max": 1888, "mean": 704.6},
    "domain_b": {"p50": 411, "p95": 1565, "p99": 1803, "max": 1952, "mean": 577.7},
    "domain_c": {"p50": 322, "p95": 1215, "p99": 2527, "max": 3894, "mean": 450.3},
    "domain_d": {"p50": 1116, "p95": 2461, "p99": 2876, "max": 3951, "mean": 1195.5},
}

# Default truncation lengths (use p95 as starting point)
DEFAULT_SEQ_MAX_LEN = {k: int(v["p95"]) for k, v in SEQ_LEN_STATS.items()}

# ── Null rate warnings (cols with >30% null, from demo data) ─────────────────
HIGH_NULL_COLS = {
    "user_int_feats_60": 0.592, "user_int_feats_86": 0.692,
    "user_int_feats_91": 0.450, "user_int_feats_92": 0.494,
    "user_int_feats_94": 0.521, "user_int_feats_96": 0.678,
    "user_int_feats_99": 0.812, "user_int_feats_100": 0.845,
    "user_int_feats_101": 0.910, "user_int_feats_102": 0.877,
    "user_int_feats_103": 0.862, "user_int_feats_108": 0.516,
    "user_int_feats_109": 0.854, "item_int_feats_11": 0.439,
    "item_int_feats_83": 0.832, "item_int_feats_84": 0.832,
    "item_int_feats_85": 0.832,
}

# ── Summary ───────────────────────────────────────────────────────────────────
TOTAL_COLS = (
    len(ID_LABEL_COLS)
    + len(USER_INT_COLS)
    + len(USER_DENSE_COLS)
    + len(ITEM_INT_COLS)
    + sum(len(v) for v in ALL_SEQ_DOMAINS.values())
)
assert TOTAL_COLS == 120, f"Expected 120 cols, got {TOTAL_COLS}"
