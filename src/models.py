"""
models.py - Full model assembly

Combines:
  - UnifiedBlock(s) from src/layers/unified_block.py
  - Embedding tables for all feature groups
  - CVR prediction head

Architecture:
  Input features -> Embedding -> [UnifiedBlock x N] -> Pooling -> CVR Head -> pCVR

TODO: Implement TAACModel(nn.Module)
"""
