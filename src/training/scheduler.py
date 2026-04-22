"""
scheduler.py
------------
Learning rate scheduling.

Strategy: Cosine Annealing with Linear Warmup

  - Warmup phase  : LR linearly increases from 0 to base_lr over warmup_steps
  - Cosine phase  : LR decays from base_lr to min_lr following cosine curve

TODO: Implement get_cosine_schedule_with_warmup
"""

# TODO: implement
