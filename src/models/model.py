"""
model.py
--------
Full TAAC2026 model assembly.

Wires together:
  SequentialTokenizer  ──┐
                         ├─→ [Unified Block 1] → ... → [Unified Block N] → CVRHead → pCVR
  NonSeqTokenizer      ──┘

Config controls:
  - num_unified_blocks : Number of stacked Unified Blocks (scaling experiment)
  - hidden_dim         : Unified token dimension D
  - seq_encoder_type   : 'transformer' | 'gru' | 'identity'
  - nonseq_encoder_type: 'dcnv2' | 'mlp' | 'fm'
  - pooling_type       : 'mean' | 'cls' | 'target_aware'

TODO: Implement TAAC2026Model(nn.Module)
"""

# TODO: implement
