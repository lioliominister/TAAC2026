"""
tokenizer.py
------------
Tokenizers that convert raw feature columns into model-ready token sequences.

Two tokenizer types:
  - SequentialTokenizer   : Converts domain sequence columns → (S, D_seq) token matrix
  - NonSeqTokenizer       : Converts multi-field non-sequential features → (NS, D_ns) token matrix

Both output token matrices of the same hidden dimension D so that Unified Blocks
can process them homogeneously.

TODO: Implement SequentialTokenizer and NonSeqTokenizer
"""

# TODO: implement
