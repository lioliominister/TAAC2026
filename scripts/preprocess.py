"""
preprocess.py
-------------
Data preprocessing entry point.

Steps:
  1. Load raw parquet file
  2. Compute and save vocabulary statistics (cardinality per feature)
  3. Compute and save dense feature normalization stats (mean/std)
  4. Perform train/val/test split (time-ordered, no leakage)
  5. Cache processed tensors to data/processed/ for fast DataLoader

Usage:
    python scripts/preprocess.py --data_path data/raw/demo_1000.parquet

TODO: Implement preprocessing pipeline
"""

# TODO: implement
