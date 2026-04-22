"""
cvr_head.py
-----------
CVR Prediction Head.

Takes the output of the last Unified Block and produces a scalar pCVR score.

Input:
  seq_out    : (B, S,  D)  — pooled or CLS token
  nonseq_out : (B, NS, D)  — pooled

Pooling strategies (selectable via config):
  - mean  : Average over valid tokens
  - cls   : Use dedicated [CLS] token prepended to sequence
  - target_aware : Attend using target item embedding (similar to DIN)

Output:
  logit : (B,)   — raw logit (apply sigmoid outside for BCEWithLogitsLoss)

TODO: Implement CVRHead(nn.Module)
"""

# TODO: implement
