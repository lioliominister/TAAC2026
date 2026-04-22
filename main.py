"""
main.py - Unified training & evaluation entry point

Usage:
    python main.py --config configs/baseline.yaml --mode train
    python main.py --config configs/unified_block_v1.yaml --mode evaluate --ckpt experiments/latest/best.pt
    python main.py --config configs/unified_block_v1.yaml --mode submit --ckpt experiments/latest/best.pt

Modes:
    train     - Train model with config
    evaluate  - Evaluate checkpoint on validation set, print AUC
    submit    - Generate submission file from checkpoint
"""
import argparse

def main():
    parser = argparse.ArgumentParser(description="TAAC2026 pCVR Prediction")
    parser.add_argument("--config", type=str, required=True, help="Path to YAML config")
    parser.add_argument("--mode", type=str, default="train", choices=["train", "evaluate", "submit"])
    parser.add_argument("--ckpt", type=str, default=None, help="Checkpoint path for evaluate/submit")
    parser.add_argument("--gpus", type=str, default="0", help="GPU IDs, e.g. '0,1'")
    args = parser.parse_args()

    # TODO: implement
    print(f"[main] mode={args.mode}, config={args.config}, ckpt={args.ckpt}, gpus={args.gpus}")

if __name__ == "__main__":
    main()
