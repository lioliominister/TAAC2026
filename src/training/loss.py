"""
loss.py
-------
Loss functions.

Available losses:
  - BCEWithLogitsLoss  : Standard binary cross-entropy with pos_weight for imbalance
  - FocalLoss          : Down-weight easy negatives (gamma=2.0 recommended)

The pos_weight for BCE is computed from training set label distribution:
  pos_weight = num_negatives / num_positives

TODO: Implement loss functions
"""

# TODO: implement
