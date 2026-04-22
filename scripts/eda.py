"""
TAAC2026 EDA - 数据探索分析脚本
输出: notebooks/EDA_report.md
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path

DATA_PATH = Path("data/raw/demo_1000.parquet")
OUTPUT_PATH = Path("notebooks/EDA_report.md")

df = pd.read_parquet(DATA_PATH)
lines = []

def w(text=""):
    lines.append(text)

# ==================== 基础信息 ====================
w("# TAAC2026 EDA 报告\n")
w(f"**数据文件**: `{DATA_PATH}`  \n")
w(f"**样本数**: `{df.shape[0]:,}`  \n")
w(f"**特征数**: `{df.shape[1]}`  \n")
w(f"**内存占用**: `{df.memory_usage(deep=True).sum() / 1024 / 1024:.1f} MB`\n")

# ==================== 数据类型分布 ====================
w("---\n## 1. 数据类型分布\n")
dtype_counts = df.dtypes.value_counts()
w("| 类型 | 列数 |")
w("|------|------|")
for dtype, count in dtype_counts.items():
    w(f"| `{dtype}` | {count} |")

# ==================== 列名全览 ====================
w("\n---\n## 2. 列名全览\n")
w("```")
for i, col in enumerate(df.columns):
    w(f"{i:3d}: {col:<40s} {str(df[col].dtype):<15s}")
w("```\n")

# ==================== Label 分析 ====================
w("---\n## 3. Label 分析\n")
if "label_type" in df.columns:
    label_col = "label_type"
elif "label" in df.columns:
    label_col = "label"
else:
    # 找包含 label 的列
    label_candidates = [c for c in df.columns if "label" in c.lower()]
    label_col = label_candidates[0] if label_candidates else df.columns[-1]

w(f"**Label 列**: `{label_col}`\n")
label_dist = df[label_col].value_counts().sort_index()
total = len(df)
w("| Label | 数量 | 占比 |")
w("|-------|------|------|")
for val, cnt in label_dist.items():
    w(f"| {val} | {cnt:,} | {cnt/total*100:.2f}% |")

pos_count = (df[label_col] == 1).sum() if 1 in label_dist.index else 0
neg_count = (df[label_col] == 0).sum() if 0 in label_dist.index else 0
if pos_count > 0 and neg_count > 0:
    w(f"\n**正负比**: {neg_count}:{pos_count} ({neg_count/pos_count:.1f}:1)")
    w(f"**pos_weight 建议** (BCE): `{neg_count/pos_count:.4f}`")

# ==================== Null 值分析 ====================
w("\n---\n## 4. Null 值分析\n")
null_counts = df.isnull().sum()
null_cols = null_counts[null_counts > 0]
if len(null_cols) == 0:
    w("✅ **全量数据无 Null 值**")
else:
    w(f"⚠️ 有 `{len(null_cols)}` 列存在 Null 值:\n")
    w("| 列名 | Null数量 | 占比 |")
    w("|------|---------|------|")
    for col, cnt in null_cols.items():
        w(f"| `{col}` | {cnt:,} | {cnt/total*100:.2f}% |")

# ==================== User Int Scalar 特征分析 ====================
w("\n---\n## 5. User Int Scalar 特征基数\n")
user_int_scalar_cols = [c for c in df.columns if c.startswith("user_int_scalar")]
w(f"共 `{len(user_int_scalar_cols)}` 列\n")
w("| 列名 | 基数(Cardinality) | 最小值 | 最大值 | 零值占比 |")
w("|------|-------------------|--------|--------|----------|")
for col in user_int_scalar_cols:
    nunique = df[col].nunique()
    vmin = df[col].min()
    vmax = df[col].max()
    zero_ratio = (df[col] == 0).sum() / total * 100
    w(f"| `{col}` | {nunique:,} | {vmin} | {vmax} | {zero_ratio:.1f}% |")

# ==================== User Int Array 特征分析 ====================
w("\n---\n## 6. User Int Array 特征分析\n")
user_int_array_cols = [c for c in df.columns if c.startswith("user_int_array")]
w(f"共 `{len(user_int_array_cols)}` 列\n")
w("| 列名 | 非空数量 | 数组长度(平均) | 数组长度(max) | 基数(估计) |")
w("|------|---------|---------------|-------------|------------|")
for col in user_int_array_cols:
    non_null = df[col].notna().sum()
    if non_null > 0:
        avg_len = df[col].dropna().apply(len).mean()
        max_len = df[col].dropna().apply(len).max()
        all_vals = []
        sample = df[col].dropna().head(200)
        for arr in sample:
            all_vals.extend(arr)
        est_card = len(set(all_vals))
        w(f"| `{col}` | {non_null:,} | {avg_len:.1f} | {max_len} | ~{est_card:,} |")
    else:
        w(f"| `{col}` | 0 | - | - | - |")

# ==================== User Dense 特征分析 ====================
w("\n---\n## 7. User Dense 特征分析\n")
user_dense_cols = [c for c in df.columns if c.startswith("user_dense")]
w(f"共 `{len(user_dense_cols)}` 列\n")
w("| 列名 | 非空数量 | 向量维度(一致?) | 均值 | 标准差 |")
w("|------|---------|----------------|------|--------|")
for col in user_dense_cols:
    non_null = df[col].notna().sum()
    if non_null > 0:
        dims = df[col].dropna().apply(len)
        dim_mode = dims.mode().iloc[0] if len(dims.mode()) > 0 else "N/A"
        dim_consistent = "✅" if dims.nunique() == 1 else f"⚠️ ({dims.nunique()}种)"
        sample = df[col].dropna().head(200)
        vals = np.concatenate([np.array(v) for v in sample])
        w(f"| `{col}` | {non_null:,} | {dim_mode} {dim_consistent} | {vals.mean():.4f} | {vals.std():.4f} |")
    else:
        w(f"| `{col}` | 0 | - | - | - |")

# ==================== Item Int 特征分析 ====================
w("\n---\n## 8. Item Int 特征分析\n")
item_int_cols = [c for c in df.columns if c.startswith("item_int")]
w(f"共 `{len(item_int_cols)}` 列\n")
for col in item_int_cols[:3]:  # 看前3个确认类型
    sample = df[col].dropna().iloc[0]
    is_array = isinstance(sample, (list, np.ndarray))
    type_str = f"array (len={len(sample)})" if is_array else f"scalar (val={sample})"
    w(f"- `{col}`: {type_str}, dtype={df[col].dtype}")
w("... (共 {} 列)\n".format(len(item_int_cols)))

# Item Int 基数
item_scalar_cols = [c for c in item_int_cols if not isinstance(df[c].dropna().iloc[0] if len(df[c].dropna())>0 else "", (list, np.ndarray))]
if len(item_scalar_cols) > 0:
    w("| 列名 | 基数 | 最小值 | 最大值 |")
    w("|------|------|--------|--------|")
    for col in item_scalar_cols:
        nunique = df[col].nunique()
        w(f"| `{col}` | {nunique:,} | {df[col].min()} | {df[col].max()} |")

# ==================== Domain Sequence 分析 (核心!) ====================
w("\n---\n## 9. Domain Sequence 分析 ⭐\n")
seq_cols = [c for c in df.columns if "domain_" in c.lower() or "seq" in c.lower()]
w(f"序列相关列共 `{len(seq_cols)}` 列\n")

# 按 domain 分组
domains = {}
for col in seq_cols:
    parts = col.split("_")
    if len(parts) >= 2:
        domain = "_".join(parts[:2])
        domains.setdefault(domain, []).append(col)

w("### 域分组\n")
w("| 域 | 列数 | 列名 |")
w("|----|------|------|")
for domain, cols in sorted(domains.items()):
    w(f"| `{domain}` | {len(cols)} | {', '.join(cols)} |")

# 序列长度分析
w("\n### 序列长度分布\n")
w("| 域 | 样本列 | p50 | p75 | p95 | p99 | max | 平均 |")
w("|----|--------|-----|-----|-----|-----|-----|------|")
for domain, cols in sorted(domains.items()):
    # 取第一列作为代表分析长度
    rep_col = cols[0]
    lengths = df[rep_col].dropna().apply(len)
    if len(lengths) > 0:
        w(f"| `{domain}` | `{rep_col}` | {lengths.quantile(0.50):.0f} | {lengths.quantile(0.75):.0f} | {lengths.quantile(0.95):.0f} | {lengths.quantile(0.99):.0f} | {lengths.max()} | {lengths.mean():.1f} |")
    else:
        w(f"| `{domain}` | `{rep_col}` | - | - | - | - | - | - |")

# 序列内特征基数（每个域取前100个样本估算）
w("\n### 序列内特征基数（前200样本估算）\n")
w("| 域.列 | 唯一值数 |")
w("|-------|---------|")
for domain, cols in sorted(domains.items()):
    for col in cols:
        sample = df[col].dropna().head(200)
        all_vals = []
        for arr in sample:
            all_vals.extend(arr)
        nunique = len(set(all_vals))
        w(f"| `{col}` | ~{nunique:,} |")

# ==================== 时间戳分析 ====================
w("\n---\n## 10. 时间戳分析\n")
ts_candidates = [c for c in df.columns if "time" in c.lower() or "ts" in c.lower() or "date" in c.lower()]
if ts_candidates:
    w(f"时间相关列: {ts_candidates}\n")
    for col in ts_candidates[:3]:
        w(f"### `{col}`")
        vals = df[col].dropna()
        if len(vals) > 0:
            w(f"- 最小值: `{vals.min()}`")
            w(f"- 最大值: `{vals.max()}`")
            w(f"- 唯一值数: `{vals.nunique():,}`\n")

# ==================== 关键发现总结 ====================
w("\n---\n## 11. 关键发现 & 建议\n")
suggestions = []

if pos_count > 0 and neg_count > 0:
    ratio = neg_count / pos_count
    if ratio > 10:
        suggestions.append(f"⚠️ **严重不平衡**: 正负比 1:{ratio:.1f}，建议使用 pos_weight={ratio:.1f} 或 Focal Loss")

# 序列长度建议
for domain, cols in sorted(domains.items()):
    rep_col = cols[0]
    lengths = df[rep_col].dropna().apply(len)
    if len(lengths) > 0:
        p95 = lengths.quantile(0.95)
        p99 = lengths.quantile(0.99)
        suggestions.append(f"📊 `{domain}` 序列: p95={p95:.0f}, p99={p99:.0f}, 建议截断长度 `{int(p95)}`~`{int(p99)}`")

# 高基数特征
for col in user_int_scalar_cols:
    nunique = df[col].nunique()
    if nunique > 100000:
        suggestions.append(f"📌 `{col}` 基数 {nunique:,}，Embedding 表需 Hash 或截断")

if not suggestions:
    suggestions.append("✅ 数据质量良好，无明显异常")

for s in suggestions:
    w(f"- {s}")

# ==================== 写入文件 ====================
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
report = "\n".join(lines)
OUTPUT_PATH.write_text(report, encoding="utf-8")
import sys; sys.stdout.reconfigure(encoding='utf-8')
print(f"EDA report saved to: {OUTPUT_PATH}")
print(f"Total lines: {len(lines)}")
