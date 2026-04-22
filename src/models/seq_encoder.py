"""
seq_encoder.py
--------------
Sequential behavior encoder.

Responsibilities:
  - Embed each domain's sequence tokens into D-dimensional space
  - Apply positional encoding (learnable or RoPE)
  - Optionally apply a lightweight Transformer before feeding into Unified Blocks

Supported encoder types (selectable via config):
  - transformer : Multi-head self-attention + FFN
  - gru         : Bidirectional GRU (fast baseline)
  - identity    : Raw embedding, let Unified Block handle interaction

TODO: Implement SequentialEncoder(nn.Module)
"""

# TODO: implement
