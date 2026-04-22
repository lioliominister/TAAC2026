"""
nonseq_encoder.py
-----------------
Non-sequential multi-field feature encoder.

Responsibilities:
  - Embedding lookup for scalar int features
  - Multi-value embedding + pooling for array int features
  - Linear projection for dense float features
  - Concatenate / stack all encoded fields into (NS, D) token matrix

Supported interaction modules (selectable via config):
  - mlp   : Simple MLP projection
  - fm    : Factorization Machine (second-order)
  - dcnv2 : Deep & Cross Network v2 (explicit high-order interaction)

TODO: Implement NonSeqEncoder(nn.Module)
"""

# TODO: implement
