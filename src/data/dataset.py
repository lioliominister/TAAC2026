"""
dataset.py
----------
PyTorch Dataset class for TAAC2026.

Handles:
  - User int scalar features  → LongTensor
  - User int array features   → LongTensor (padded)
  - User dense features       → FloatTensor (normalized)
  - Item int features         → LongTensor
  - Domain sequence features  → LongTensor (padded) + BoolTensor mask
  - Label                     → FloatTensor

TODO: Implement TAAC2026Dataset.__getitem__ and collate_fn
"""

# TODO: implement
