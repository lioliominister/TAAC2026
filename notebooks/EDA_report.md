# TAAC2026 EDA 报告

**数据文件**: `data\raw\demo_1000.parquet`  

**样本数**: `1,000`  

**特征数**: `120`  

**内存占用**: `7.7 MB`

---
## 1. 数据类型分布

| 类型 | 列数 |
|------|------|
| `object` | 67 |
| `float64` | 47 |
| `int64` | 5 |
| `int32` | 1 |

---
## 2. 列名全览

```
  0: user_id                                  int64          
  1: item_id                                  int64          
  2: label_type                               int32          
  3: label_time                               int64          
  4: timestamp                                int64          
  5: user_int_feats_1                         int64          
  6: user_int_feats_3                         float64        
  7: user_int_feats_4                         float64        
  8: user_int_feats_15                        object         
  9: user_int_feats_48                        float64        
 10: user_int_feats_49                        float64        
 11: user_int_feats_50                        float64        
 12: user_int_feats_51                        float64        
 13: user_int_feats_52                        float64        
 14: user_int_feats_53                        float64        
 15: user_int_feats_54                        float64        
 16: user_int_feats_55                        float64        
 17: user_int_feats_56                        float64        
 18: user_int_feats_57                        float64        
 19: user_int_feats_58                        float64        
 20: user_int_feats_59                        float64        
 21: user_int_feats_60                        object         
 22: user_int_feats_62                        object         
 23: user_int_feats_63                        object         
 24: user_int_feats_64                        object         
 25: user_int_feats_65                        object         
 26: user_int_feats_66                        object         
 27: user_int_feats_80                        object         
 28: user_int_feats_82                        float64        
 29: user_int_feats_86                        float64        
 30: user_int_feats_89                        object         
 31: user_int_feats_90                        object         
 32: user_int_feats_91                        object         
 33: user_int_feats_92                        float64        
 34: user_int_feats_93                        float64        
 35: user_int_feats_94                        float64        
 36: user_int_feats_95                        float64        
 37: user_int_feats_96                        float64        
 38: user_int_feats_97                        float64        
 39: user_int_feats_98                        float64        
 40: user_int_feats_99                        float64        
 41: user_int_feats_100                       float64        
 42: user_int_feats_101                       float64        
 43: user_int_feats_102                       float64        
 44: user_int_feats_103                       float64        
 45: user_int_feats_104                       float64        
 46: user_int_feats_105                       float64        
 47: user_int_feats_106                       float64        
 48: user_int_feats_107                       float64        
 49: user_int_feats_108                       float64        
 50: user_int_feats_109                       float64        
 51: user_dense_feats_61                      object         
 52: user_dense_feats_62                      object         
 53: user_dense_feats_63                      object         
 54: user_dense_feats_64                      object         
 55: user_dense_feats_65                      object         
 56: user_dense_feats_66                      object         
 57: user_dense_feats_87                      object         
 58: user_dense_feats_89                      object         
 59: user_dense_feats_90                      object         
 60: user_dense_feats_91                      object         
 61: item_int_feats_5                         float64        
 62: item_int_feats_6                         float64        
 63: item_int_feats_7                         float64        
 64: item_int_feats_8                         float64        
 65: item_int_feats_9                         float64        
 66: item_int_feats_10                        float64        
 67: item_int_feats_11                        object         
 68: item_int_feats_12                        float64        
 69: item_int_feats_13                        float64        
 70: item_int_feats_16                        float64        
 71: item_int_feats_81                        float64        
 72: item_int_feats_83                        float64        
 73: item_int_feats_84                        float64        
 74: item_int_feats_85                        float64        
 75: domain_a_seq_38                          object         
 76: domain_a_seq_39                          object         
 77: domain_a_seq_40                          object         
 78: domain_a_seq_41                          object         
 79: domain_a_seq_42                          object         
 80: domain_a_seq_43                          object         
 81: domain_a_seq_44                          object         
 82: domain_a_seq_45                          object         
 83: domain_a_seq_46                          object         
 84: domain_b_seq_67                          object         
 85: domain_b_seq_68                          object         
 86: domain_b_seq_69                          object         
 87: domain_b_seq_70                          object         
 88: domain_b_seq_71                          object         
 89: domain_b_seq_72                          object         
 90: domain_b_seq_73                          object         
 91: domain_b_seq_74                          object         
 92: domain_b_seq_75                          object         
 93: domain_b_seq_76                          object         
 94: domain_b_seq_77                          object         
 95: domain_b_seq_78                          object         
 96: domain_b_seq_79                          object         
 97: domain_b_seq_88                          object         
 98: domain_c_seq_27                          object         
 99: domain_c_seq_28                          object         
100: domain_c_seq_29                          object         
101: domain_c_seq_30                          object         
102: domain_c_seq_31                          object         
103: domain_c_seq_32                          object         
104: domain_c_seq_33                          object         
105: domain_c_seq_34                          object         
106: domain_c_seq_35                          object         
107: domain_c_seq_36                          object         
108: domain_c_seq_37                          object         
109: domain_c_seq_47                          object         
110: domain_d_seq_17                          object         
111: domain_d_seq_18                          object         
112: domain_d_seq_19                          object         
113: domain_d_seq_20                          object         
114: domain_d_seq_21                          object         
115: domain_d_seq_22                          object         
116: domain_d_seq_23                          object         
117: domain_d_seq_24                          object         
118: domain_d_seq_25                          object         
119: domain_d_seq_26                          object         
```

---
## 3. Label 分析

**Label 列**: `label_type`

| Label | 数量 | 占比 |
|-------|------|------|
| 1 | 876 | 87.60% |
| 2 | 124 | 12.40% |

---
## 4. Null 值分析

⚠️ 有 `114` 列存在 Null 值:

| 列名 | Null数量 | 占比 |
|------|---------|------|
| `user_int_feats_3` | 30 | 3.00% |
| `user_int_feats_4` | 30 | 3.00% |
| `user_int_feats_15` | 139 | 13.90% |
| `user_int_feats_48` | 2 | 0.20% |
| `user_int_feats_49` | 7 | 0.70% |
| `user_int_feats_50` | 4 | 0.40% |
| `user_int_feats_51` | 1 | 0.10% |
| `user_int_feats_52` | 1 | 0.10% |
| `user_int_feats_53` | 1 | 0.10% |
| `user_int_feats_54` | 368 | 36.80% |
| `user_int_feats_55` | 19 | 1.90% |
| `user_int_feats_56` | 19 | 1.90% |
| `user_int_feats_57` | 31 | 3.10% |
| `user_int_feats_58` | 150 | 15.00% |
| `user_int_feats_59` | 150 | 15.00% |
| `user_int_feats_60` | 592 | 59.20% |
| `user_int_feats_62` | 70 | 7.00% |
| `user_int_feats_63` | 70 | 7.00% |
| `user_int_feats_64` | 70 | 7.00% |
| `user_int_feats_65` | 80 | 8.00% |
| `user_int_feats_66` | 86 | 8.60% |
| `user_int_feats_80` | 200 | 20.00% |
| `user_int_feats_82` | 204 | 20.40% |
| `user_int_feats_86` | 692 | 69.20% |
| `user_int_feats_89` | 55 | 5.50% |
| `user_int_feats_90` | 91 | 9.10% |
| `user_int_feats_91` | 450 | 45.00% |
| `user_int_feats_92` | 494 | 49.40% |
| `user_int_feats_93` | 171 | 17.10% |
| `user_int_feats_94` | 521 | 52.10% |
| `user_int_feats_95` | 318 | 31.80% |
| `user_int_feats_96` | 678 | 67.80% |
| `user_int_feats_97` | 292 | 29.20% |
| `user_int_feats_98` | 103 | 10.30% |
| `user_int_feats_99` | 812 | 81.20% |
| `user_int_feats_100` | 845 | 84.50% |
| `user_int_feats_101` | 910 | 91.00% |
| `user_int_feats_102` | 877 | 87.70% |
| `user_int_feats_103` | 862 | 86.20% |
| `user_int_feats_104` | 372 | 37.20% |
| `user_int_feats_105` | 309 | 30.90% |
| `user_int_feats_106` | 160 | 16.00% |
| `user_int_feats_107` | 300 | 30.00% |
| `user_int_feats_108` | 516 | 51.60% |
| `user_int_feats_109` | 854 | 85.40% |
| `user_dense_feats_61` | 2 | 0.20% |
| `user_dense_feats_62` | 70 | 7.00% |
| `user_dense_feats_63` | 70 | 7.00% |
| `user_dense_feats_64` | 70 | 7.00% |
| `user_dense_feats_65` | 80 | 8.00% |
| `user_dense_feats_66` | 86 | 8.60% |
| `user_dense_feats_87` | 15 | 1.50% |
| `user_dense_feats_89` | 55 | 5.50% |
| `user_dense_feats_90` | 91 | 9.10% |
| `user_dense_feats_91` | 450 | 45.00% |
| `item_int_feats_5` | 2 | 0.20% |
| `item_int_feats_6` | 2 | 0.20% |
| `item_int_feats_7` | 2 | 0.20% |
| `item_int_feats_8` | 2 | 0.20% |
| `item_int_feats_9` | 2 | 0.20% |
| `item_int_feats_10` | 2 | 0.20% |
| `item_int_feats_11` | 439 | 43.90% |
| `item_int_feats_12` | 2 | 0.20% |
| `item_int_feats_13` | 2 | 0.20% |
| `item_int_feats_16` | 2 | 0.20% |
| `item_int_feats_81` | 2 | 0.20% |
| `item_int_feats_83` | 832 | 83.20% |
| `item_int_feats_84` | 832 | 83.20% |
| `item_int_feats_85` | 832 | 83.20% |
| `domain_a_seq_38` | 5 | 0.50% |
| `domain_a_seq_39` | 5 | 0.50% |
| `domain_a_seq_40` | 5 | 0.50% |
| `domain_a_seq_41` | 5 | 0.50% |
| `domain_a_seq_42` | 5 | 0.50% |
| `domain_a_seq_43` | 5 | 0.50% |
| `domain_a_seq_44` | 5 | 0.50% |
| `domain_a_seq_45` | 5 | 0.50% |
| `domain_a_seq_46` | 5 | 0.50% |
| `domain_b_seq_67` | 12 | 1.20% |
| `domain_b_seq_68` | 12 | 1.20% |
| `domain_b_seq_69` | 12 | 1.20% |
| `domain_b_seq_70` | 12 | 1.20% |
| `domain_b_seq_71` | 12 | 1.20% |
| `domain_b_seq_72` | 12 | 1.20% |
| `domain_b_seq_73` | 12 | 1.20% |
| `domain_b_seq_74` | 12 | 1.20% |
| `domain_b_seq_75` | 12 | 1.20% |
| `domain_b_seq_76` | 12 | 1.20% |
| `domain_b_seq_77` | 12 | 1.20% |
| `domain_b_seq_78` | 12 | 1.20% |
| `domain_b_seq_79` | 12 | 1.20% |
| `domain_b_seq_88` | 12 | 1.20% |
| `domain_c_seq_27` | 2 | 0.20% |
| `domain_c_seq_28` | 2 | 0.20% |
| `domain_c_seq_29` | 2 | 0.20% |
| `domain_c_seq_30` | 2 | 0.20% |
| `domain_c_seq_31` | 2 | 0.20% |
| `domain_c_seq_32` | 2 | 0.20% |
| `domain_c_seq_33` | 2 | 0.20% |
| `domain_c_seq_34` | 2 | 0.20% |
| `domain_c_seq_35` | 2 | 0.20% |
| `domain_c_seq_36` | 2 | 0.20% |
| `domain_c_seq_37` | 2 | 0.20% |
| `domain_c_seq_47` | 2 | 0.20% |
| `domain_d_seq_17` | 80 | 8.00% |
| `domain_d_seq_18` | 80 | 8.00% |
| `domain_d_seq_19` | 80 | 8.00% |
| `domain_d_seq_20` | 80 | 8.00% |
| `domain_d_seq_21` | 80 | 8.00% |
| `domain_d_seq_22` | 80 | 8.00% |
| `domain_d_seq_23` | 80 | 8.00% |
| `domain_d_seq_24` | 80 | 8.00% |
| `domain_d_seq_25` | 80 | 8.00% |
| `domain_d_seq_26` | 80 | 8.00% |

---
## 5. User Int Scalar 特征基数

共 `0` 列

| 列名 | 基数(Cardinality) | 最小值 | 最大值 | 零值占比 |
|------|-------------------|--------|--------|----------|

---
## 6. User Int Array 特征分析

共 `0` 列

| 列名 | 非空数量 | 数组长度(平均) | 数组长度(max) | 基数(估计) |
|------|---------|---------------|-------------|------------|

---
## 7. User Dense 特征分析

共 `10` 列

| 列名 | 非空数量 | 向量维度(一致?) | 均值 | 标准差 |
|------|---------|----------------|------|--------|
| `user_dense_feats_61` | 998 | 256 ✅ | -0.0009 | 0.0624 |
| `user_dense_feats_62` | 930 | 2 ⚠️ (5种) | 143618.5625 | 363299.2812 |
| `user_dense_feats_63` | 930 | 2 ⚠️ (10种) | 135774.6719 | 327995.7500 |
| `user_dense_feats_64` | 930 | 2 ⚠️ (16种) | 137007.6875 | 552319.1875 |
| `user_dense_feats_65` | 920 | 1 ⚠️ (33种) | 164115.7188 | 656039.8125 |
| `user_dense_feats_66` | 914 | 1 ⚠️ (41种) | 192983.7344 | 670117.8750 |
| `user_dense_feats_87` | 985 | 320 ✅ | -0.0038 | 0.1090 |
| `user_dense_feats_89` | 945 | 10 ✅ | -0.0000 | 0.3162 |
| `user_dense_feats_90` | 909 | 10 ✅ | -0.0001 | 0.3162 |
| `user_dense_feats_91` | 550 | 10 ✅ | -0.0000 | 0.3162 |

---
## 8. Item Int 特征分析

共 `14` 列

- `item_int_feats_5`: scalar (val=161.0), dtype=float64
- `item_int_feats_6`: scalar (val=893.0), dtype=float64
- `item_int_feats_7`: scalar (val=0.0), dtype=float64
... (共 14 列)

| 列名 | 基数 | 最小值 | 最大值 |
|------|------|--------|--------|
| `item_int_feats_5` | 82 | 4.0 | 325.0 |
| `item_int_feats_6` | 216 | 0.0 | 977.0 |
| `item_int_feats_7` | 349 | 0.0 | 2806.0 |
| `item_int_feats_8` | 226 | -1.0 | 2431.0 |
| `item_int_feats_9` | 24 | 3.0 | 37.0 |
| `item_int_feats_10` | 110 | 2.0 | 309.0 |
| `item_int_feats_12` | 352 | 0.0 | 2777.0 |
| `item_int_feats_13` | 8 | 1.0 | 8.0 |
| `item_int_feats_16` | 662 | 2.0 | 35259.0 |
| `item_int_feats_81` | 3 | 0.0 | 2.0 |
| `item_int_feats_83` | 22 | 1.0 | 31.0 |
| `item_int_feats_84` | 66 | 3.0 | 226.0 |
| `item_int_feats_85` | 103 | 4.0 | 1001.0 |

---
## 9. Domain Sequence 分析 ⭐

序列相关列共 `45` 列

### 域分组

| 域 | 列数 | 列名 |
|----|------|------|
| `domain_a` | 9 | domain_a_seq_38, domain_a_seq_39, domain_a_seq_40, domain_a_seq_41, domain_a_seq_42, domain_a_seq_43, domain_a_seq_44, domain_a_seq_45, domain_a_seq_46 |
| `domain_b` | 14 | domain_b_seq_67, domain_b_seq_68, domain_b_seq_69, domain_b_seq_70, domain_b_seq_71, domain_b_seq_72, domain_b_seq_73, domain_b_seq_74, domain_b_seq_75, domain_b_seq_76, domain_b_seq_77, domain_b_seq_78, domain_b_seq_79, domain_b_seq_88 |
| `domain_c` | 12 | domain_c_seq_27, domain_c_seq_28, domain_c_seq_29, domain_c_seq_30, domain_c_seq_31, domain_c_seq_32, domain_c_seq_33, domain_c_seq_34, domain_c_seq_35, domain_c_seq_36, domain_c_seq_37, domain_c_seq_47 |
| `domain_d` | 10 | domain_d_seq_17, domain_d_seq_18, domain_d_seq_19, domain_d_seq_20, domain_d_seq_21, domain_d_seq_22, domain_d_seq_23, domain_d_seq_24, domain_d_seq_25, domain_d_seq_26 |

### 序列长度分布

| 域 | 样本列 | p50 | p75 | p95 | p99 | max | 平均 |
|----|--------|-----|-----|-----|-----|-----|------|
| `domain_a` | `domain_a_seq_38` | 582 | 1128 | 1674 | 1793 | 1888 | 704.6 |
| `domain_b` | `domain_b_seq_67` | 411 | 928 | 1565 | 1803 | 1952 | 577.7 |
| `domain_c` | `domain_c_seq_27` | 322 | 533 | 1215 | 2527 | 3894 | 450.3 |
| `domain_d` | `domain_d_seq_17` | 1116 | 1781 | 2461 | 2876 | 3951 | 1195.5 |

### 序列内特征基数（前200样本估算）

| 域.列 | 唯一值数 |
|-------|---------|
| `domain_a_seq_38` | ~3,834 |
| `domain_a_seq_39` | ~107,689 |
| `domain_a_seq_40` | ~15 |
| `domain_a_seq_41` | ~8 |
| `domain_a_seq_42` | ~295 |
| `domain_a_seq_43` | ~837 |
| `domain_a_seq_44` | ~1,569 |
| `domain_a_seq_45` | ~1,195 |
| `domain_a_seq_46` | ~12 |
| `domain_b_seq_67` | ~101,188 |
| `domain_b_seq_68` | ~23 |
| `domain_b_seq_69` | ~42,009 |
| `domain_b_seq_70` | ~323 |
| `domain_b_seq_71` | ~939 |
| `domain_b_seq_72` | ~2,077 |
| `domain_b_seq_73` | ~1,497 |
| `domain_b_seq_74` | ~4,301 |
| `domain_b_seq_75` | ~20 |
| `domain_b_seq_76` | ~2,768 |
| `domain_b_seq_77` | ~119 |
| `domain_b_seq_78` | ~1,871 |
| `domain_b_seq_79` | ~3,674 |
| `domain_b_seq_88` | ~4,769 |
| `domain_c_seq_27` | ~89,520 |
| `domain_c_seq_28` | ~45 |
| `domain_c_seq_29` | ~44,529 |
| `domain_c_seq_30` | ~410 |
| `domain_c_seq_31` | ~1,853 |
| `domain_c_seq_32` | ~6 |
| `domain_c_seq_33` | ~3 |
| `domain_c_seq_34` | ~4,470 |
| `domain_c_seq_35` | ~1,118 |
| `domain_c_seq_36` | ~17,923 |
| `domain_c_seq_37` | ~2,617 |
| `domain_c_seq_47` | ~60,506 |
| `domain_d_seq_17` | ~4 |
| `domain_d_seq_18` | ~337 |
| `domain_d_seq_19` | ~1,211 |
| `domain_d_seq_20` | ~2,857 |
| `domain_d_seq_21` | ~1,906 |
| `domain_d_seq_22` | ~6,331 |
| `domain_d_seq_23` | ~56,699 |
| `domain_d_seq_24` | ~17 |
| `domain_d_seq_25` | ~11 |
| `domain_d_seq_26` | ~43,280 |

---
## 10. 时间戳分析

时间相关列: ['label_time', 'timestamp', 'user_int_feats_1', 'user_int_feats_3', 'user_int_feats_4', 'user_int_feats_15', 'user_int_feats_48', 'user_int_feats_49', 'user_int_feats_50', 'user_int_feats_51', 'user_int_feats_52', 'user_int_feats_53', 'user_int_feats_54', 'user_int_feats_55', 'user_int_feats_56', 'user_int_feats_57', 'user_int_feats_58', 'user_int_feats_59', 'user_int_feats_60', 'user_int_feats_62', 'user_int_feats_63', 'user_int_feats_64', 'user_int_feats_65', 'user_int_feats_66', 'user_int_feats_80', 'user_int_feats_82', 'user_int_feats_86', 'user_int_feats_89', 'user_int_feats_90', 'user_int_feats_91', 'user_int_feats_92', 'user_int_feats_93', 'user_int_feats_94', 'user_int_feats_95', 'user_int_feats_96', 'user_int_feats_97', 'user_int_feats_98', 'user_int_feats_99', 'user_int_feats_100', 'user_int_feats_101', 'user_int_feats_102', 'user_int_feats_103', 'user_int_feats_104', 'user_int_feats_105', 'user_int_feats_106', 'user_int_feats_107', 'user_int_feats_108', 'user_int_feats_109', 'user_dense_feats_61', 'user_dense_feats_62', 'user_dense_feats_63', 'user_dense_feats_64', 'user_dense_feats_65', 'user_dense_feats_66', 'user_dense_feats_87', 'user_dense_feats_89', 'user_dense_feats_90', 'user_dense_feats_91', 'item_int_feats_5', 'item_int_feats_6', 'item_int_feats_7', 'item_int_feats_8', 'item_int_feats_9', 'item_int_feats_10', 'item_int_feats_11', 'item_int_feats_12', 'item_int_feats_13', 'item_int_feats_16', 'item_int_feats_81', 'item_int_feats_83', 'item_int_feats_84', 'item_int_feats_85']

### `label_time`
- 最小值: `1772725027`
- 最大值: `1772725910`
- 唯一值数: `553`

### `timestamp`
- 最小值: `1772725000`
- 最大值: `1772725781`
- 唯一值数: `501`

### `user_int_feats_1`
- 最小值: `1`
- 最大值: `4`
- 唯一值数: `3`


---
## 11. 关键发现 & 建议

- 📊 `domain_a` 序列: p95=1674, p99=1793, 建议截断长度 `1673`~`1793`
- 📊 `domain_b` 序列: p95=1565, p99=1803, 建议截断长度 `1564`~`1803`
- 📊 `domain_c` 序列: p95=1215, p99=2527, 建议截断长度 `1214`~`2527`
- 📊 `domain_d` 序列: p95=2461, p99=2876, 建议截断长度 `2461`~`2875`