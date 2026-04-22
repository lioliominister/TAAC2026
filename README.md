# TAAC2026 - Tencent Advertising Algorithm Competition

> **Task**: pCVR (post-Click Conversion Rate) Prediction  
> **Metric**: AUC-ROC  
> **Key Innovation**: Unified Stackable Block that simultaneously handles multi-field non-sequential tokens and sequential behavior tokens in a single homogeneous backbone.

---

## Project Structure

```
TAAC2026/
├── data/                      # Data directory (gitignored)
│   └── raw/                   # Raw parquet files
│
├── src/
│   ├── data/
│   │   ├── schema.py          # Column definitions & groupings (EDA verified)
│   │   ├── dataset.py         # PyTorch Dataset class
│   │   ├── tokenizer.py       # Sequential & Non-Seq tokenizers
│   │   └── feature_eng.py     # Feature engineering utilities
│   │
│   ├── layers/
│   │   └── unified_block.py   # ⭐ Core: Unified Stackable Block
│   │
│   └── models.py              # Full model assembly (Embedding + Blocks + Head)
│
├── configs/                   # Experiment YAML configs
│   ├── baseline.yaml
│   ├── unified_block_v1.yaml
│   └── unified_block_v2.yaml
│
├── notebooks/
│   └── EDA_report.md          # EDA analysis report (from demo data)
│
├── scripts/
│   ├── eda.py                 # Data exploration script
│   ├── preprocess.py          # Data preprocessing entry
│   ├── train.py               # Training entry (thin wrapper)
│   ├── evaluate.py            # Evaluation entry
│   └── submit.py              # Generate submission file
│
├── main.py                    # ⭐ Unified entry point (train/evaluate/submit)
├── inference_test.py          # Inference latency benchmark
├── requirements.txt
└── README.md
```

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run EDA (generates notebooks/EDA_report.md)
python scripts/eda.py

# 3. Train
python main.py --config configs/baseline.yaml --mode train

# 4. Evaluate
python main.py --config configs/baseline.yaml --mode evaluate --ckpt experiments/latest/best.pt

# 5. Test inference latency
python inference_test.py --ckpt experiments/latest/best.pt

# 6. Submit
python main.py --config configs/unified_block_v1.yaml --mode submit --ckpt experiments/latest/best.pt
```

## Data Schema (EDA Verified)

| Group | Cols | Key Findings |
|-------|------|-------------|
| ID & Label | 5 | label_type={1,2}, NOT 0/1 |
| User Int | 46 | Mixed scalar/array, fid not continuous |
| User Dense | 10 | dim=256(fid_61), dim=320(fid_87), others vary |
| Item Int | 14 | Mostly scalar float64, one array(fid_11) |
| Domain Seq | 45 | 4 domains, p95 length: 1215~2461 |

## Competition References

- [DIN](https://arxiv.org/abs/1706.06978) - Deep Interest Network (KDD 2018)
- [DIEN](https://arxiv.org/abs/1809.03672) - Deep Interest Evolution Network (AAAI 2019)
- [SIM](https://arxiv.org/abs/2006.05639) - Search-based Interest Model (CIKM 2020)
- [DCNv2](https://arxiv.org/abs/2008.13535) - Improved Deep & Cross Network (WWW 2021)
- [BST](https://arxiv.org/abs/1905.06874) - Behavior Sequence Transformer (2019)
- [HSTU](https://arxiv.org/abs/2402.17152) - Actions Speak Louder than Words (Meta, 2024)
