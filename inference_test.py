"""
inference_test.py - Test inference latency

Usage:
    python inference_test.py --ckpt experiments/latest/best.pt --batch_size 256 --warmup 10 --rounds 100

Measures:
    - Average inference time per batch
    - Throughput (samples/sec)
    - P50 / P95 / P99 latency
"""
import argparse
import time

def main():
    parser = argparse.ArgumentParser(description="Inference latency benchmark")
    parser.add_argument("--ckpt", type=str, required=True)
    parser.add_argument("--batch_size", type=int, default=256)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--rounds", type=int, default=100)
    args = parser.parse_args()

    # TODO: implement
    print(f"[inference_test] ckpt={args.ckpt}, batch_size={args.batch_size}, warmup={args.warmup}, rounds={args.rounds}")

if __name__ == "__main__":
    main()
