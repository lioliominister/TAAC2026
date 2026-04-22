# TAAC2026 - Tencent Advertising Algorithm Competition

> **Task**: pCVR (post-Click Conversion Rate) Prediction  
> **Metric**: AUC-ROC  
> **Key Innovation**: Unified Stackable Block that simultaneously handles multi-field non-sequential tokens and sequential behavior tokens in a single homogeneous backbone.

---

## Project Structure

```
TAAC2026/
├── data/                      # Data directory (gitignored)
│   ├── raw/                   # Raw parquet files from competition
│   ├── processed/             # Preprocessed feature tensors (.pt)
│   └── splits/                # Train / val / test index splits
│
├── src/                       # Core source code
│   ├── data/
│   │   ├── schema.py          # Column definitions & groupings
│   │   ├── dataset.py         # PyTorch Dataset class
│   │   ├── tokenizer.py       # Sequential & Non-Seq tokenizers
│   │   └── feature_eng.py     # Feature engineering utilities
│   │
│   ├── models/
│   │   ├── unified_block.py   # ⭐ Core: Unified Stackable Block
│   │   ├── seq_encoder.py     # Sequential encoder (Transformer)
│   │   ├── nonseq_encoder.py  # Non-sequential encoder (DCNv2/MLP)
│   │   ├── cvr_head.py        # CVR prediction head
│   │   └── model.py           # Full model assembly
│   │
│   ├── training/
│   │   ├── trainer.py         # Training loop
│   │   ├── loss.py            # Loss functions (BCE, Focal)
│   │   └── scheduler.py       # LR scheduler
│   │
│   ├── evaluation/
│   │   ├── metrics.py         # AUC-ROC computation
│   │   └── evaluator.py       # Validation evaluator
│   │
│   └── utils/
│       ├── config.py          # Hyperparameter config (dataclass)
│       ├── logger.py          # Training logger (W&B / TensorBoard)
│       └── seed.py            # Random seed utilities
│
├── configs/                   # Experiment YAML configs
│   ├── baseline.yaml
│   ├── unified_block_v1.yaml
│   └── unified_block_v2.yaml
│
├── experiments/               # Auto-archived experiment runs (gitignored)
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_feature_analysis.ipynb
│   └── 03_model_debug.ipynb
│
├── scripts/
│   ├── preprocess.py          # Data preprocessing entry
│   ├── train.py               # Training entry
│   ├── evaluate.py            # Evaluation entry
│   └── submit.py              # Generate submission file
│
├── requirements.txt
└── README.md
```

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Preprocess data
python scripts/preprocess.py --data_path data/raw/demo_1000.parquet

# 3. Train baseline
python scripts/train.py --config configs/baseline.yaml

# 4. Evaluate
python scripts/evaluate.py --config configs/baseline.yaml --ckpt experiments/latest/best.pt

# 5. Submit
python scripts/submit.py --ckpt experiments/latest/best.pt
```

## Competition References

- [DIN](https://arxiv.org/abs/1706.06978) - Deep Interest Network (KDD 2018)
- [DIEN](https://arxiv.org/abs/1809.03672) - Deep Interest Evolution Network (AAAI 2019)
- [SIM](https://arxiv.org/abs/2006.05639) - Search-based Interest Model (CIKM 2020)
- [DCNv2](https://arxiv.org/abs/2008.13535) - Improved Deep & Cross Network (WWW 2021)
- [BST](https://arxiv.org/abs/1905.06874) - Behavior Sequence Transformer (2019)
- [HSTU](https://arxiv.org/abs/2402.17152) - Actions Speak Louder than Words (Meta, 2024)
