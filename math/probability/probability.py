#!/usr/bin/env python3
"""
概率统计 Python 示例
Probability & Statistics Examples

涵盖：概率计算、常见分布、描述统计、推断统计、贝叶斯定理
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

print("=" * 60)
print("概率统计 Python 示例")
print("=" * 60)

# ============================================================
# 1. 基础概率计算
# ============================================================
print("\n【1. 基础概率计算】")

# 模拟抛硬币
n_flips = 1000
coin_flips = np.random.binomial(n=1, p=0.5, size=n_flips)
print(f"抛硬币 {n_flips} 次")
print(f"正面次数：{np.sum(coin_flips)}")
print(f"正面概率估计：{np.mean(coin_flips):.4f}")

# 模拟掷骰子
n_rolls = 10000
dice_rolls = np.random.randint(1, 7, size=n_rolls)
print(f"\n掷骰子 {n_rolls} 次")
for i in range(1, 7):
    prob = np.sum(dice_rolls == i) / n_rolls
    print(f"点数 {i} 的概率：{prob:.4f} (理论值：{1/6:.4f})")

# ============================================================
# 2. 常见离散分布
# ============================================================
print("\n【2. 常见离散分布】")

# 二项分布 Binomial(n=10, p=0.5)
n, p = 10, 0.5
binom_dist = stats.binom(n, p)

print(f"\n二项分布 B({n}, {p}):")
print(f"期望值 E[X] = {binom_dist.mean():.2f} (公式：np = {n*p})")
print(f"方差 Var(X) = {binom_dist.var():.2f} (公式：np(1-p) = {n*p*(1-p)})")

# 计算 P(X = k)
k = 5
prob_k = binom_dist.pmf(k)
print(f"P(X = {k}) = {prob_k:.4f}")

# 计算 P(X <= k)
prob_leq_k = binom_dist.cdf(k)
print(f"P(X <= {k}) = {prob_leq_k:.4f}")

# 泊松分布 Poisson(λ=3)
lambda_poisson = 3
poisson_dist = stats.poisson(lambda_poisson)

print(f"\n泊松分布 Poi({lambda_poisson}):")
print(f"期望值 E[X] = {poisson_dist.mean():.2f}")
print(f"方差 Var(X) = {poisson_dist.var():.2f}")

for k in range(6):
    prob = poisson_dist.pmf(k)
    print(f"P(X = {k}) = {prob:.4f}")

# ============================================================
# 3. 常见连续分布
# ============================================================
print("\n【3. 常见连续分布】")

# 正态分布 Normal(μ=0, σ=1)
mu, sigma = 0, 1
normal_dist = stats.norm(mu, sigma)

print(f"\n标准正态分布 N({mu}, {sigma}²):")

# 计算概率
prob_1sigma = normal_dist.cdf(1) - normal_dist.cdf(-1)
prob_2sigma = normal_dist.cdf(2) - normal_dist.cdf(-2)
prob_3sigma = normal_dist.cdf(3) - normal_dist.cdf(-3)

print(f"P(-1 ≤ Z ≤ 1) = {prob_1sigma:.4f} (68% 规则)")
print(f"P(-2 ≤ Z ≤ 2) = {prob_2sigma:.4f} (95% 规则)")
print(f"P(-3 ≤ Z ≤ 3) = {prob_3sigma:.4f} (99.7% 规则)")

# 分位数
z_95 = normal_dist.ppf(0.95)
z_975 = normal_dist.ppf(0.975)
print(f"\n95% 分位数 z_0.95 = {z_95:.4f}")
print(f"97.5% 分位数 z_0.975 = {z_975:.4f}")

# 均匀分布
uniform_dist = stats.uniform(0, 10)  # U(0, 10)
print(f"\n均匀分布 U(0, 10):")
print(f"期望值 = {uniform_dist.mean():.2f}")
print(f"方差 = {uniform_dist.var():.2f}")

# 指数分布
exp_dist = stats.expon(scale=1/2)  # λ = 2, scale = 1/λ
print(f"\n指数分布 Exp(λ=2):")
print(f"期望值 = {exp_dist.mean():.2f}")
print(f"方差 = {exp_dist.var():.2f}")

# ============================================================
# 4. 描述统计
# ============================================================
print("\n【4. 描述统计】")

# 生成示例数据
np.random.seed(42)
data = np.random.normal(loc=75, scale=10, size=1000)

print(f"样本大小：{len(data)}")
print(f"\n集中趋势:")
print(f"  均值 (Mean) = {np.mean(data):.4f}")
print(f"  中位数 (Median) = {np.median(data):.4f}")
print(f"  众数 (Mode) ≈ {stats.mode(data, keepdims=True)[0][0]:.4f}")

print(f"\n离散程度:")
print(f"  方差 (Variance) = {np.var(data, ddof=1):.4f}")
print(f"  标准差 (Std Dev) = {np.std(data, ddof=1):.4f}")
print(f"  极差 (Range) = {np.max(data) - np.min(data):.4f}")

print(f"\n分位数:")
percentiles = [25, 50, 75]
for p in percentiles:
    print(f"  Q{p//25} ({p}%) = {np.percentile(data, p):.4f}")

iqr = np.percentile(data, 75) - np.percentile(data, 25)
print(f"  IQR = {iqr:.4f}")

# ============================================================
# 5. 贝叶斯定理应用 - 疾病检测
# ============================================================
print("\n【5. 贝叶斯定理 - 疾病检测问题】")

# 已知条件
p_disease = 0.001  # 患病率 0.1%
p_positive_given_disease = 0.99  # 灵敏度
p_negative_given_healthy = 0.99  # 特异度

# 计算 P(阳性)
p_positive_given_healthy = 1 - p_negative_given_healthy
p_healthy = 1 - p_disease

p_positive = (p_positive_given_disease * p_disease + 
              p_positive_given_healthy * p_healthy)

# 贝叶斯定理：P(患病 | 阳性)
p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive

print(f"已知条件:")
print(f"  患病率 P(患病) = {p_disease}")
print(f"  灵敏度 P(阳性 | 患病) = {p_positive_given_disease}")
print(f"  特异度 P(阴性 | 健康) = {p_negative_given_healthy}")

print(f"\n计算结果:")
print(f"  P(阳性) = {p_positive:.6f}")
print(f"  P(患病 | 阳性) = {p_disease_given_positive:.6f}")
print(f"  ≈ {p_disease_given_positive * 100:.2f}%")

print(f"\n解释：即使检测准确率高达 99%，")
print(f"由于患病率很低，阳性结果中真正患病的比例仍然很低。")
print(f"这是贝叶斯定理的经典应用！")

# ============================================================
# 6. 中心极限定理演示
# ============================================================
print("\n【6. 中心极限定理演示】")

# 从均匀分布中抽样
np.random.seed(42)
n_samples = 10000
sample_size = 30

# 每次抽取 sample_size 个样本，计算均值
sample_means = []
for _ in range(n_samples):
    sample = np.random.uniform(0, 1, sample_size)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# 理论值
theoretical_mean = 0.5
theoretical_std = np.sqrt(1/12 / sample_size)

print(f"从 U(0,1) 中抽取 {n_samples} 个样本，每个样本大小 n={sample_size}")
print(f"\n样本均值的分布:")
print(f"  实际均值 = {np.mean(sample_means):.6f}")
print(f"  理论均值 = {theoretical_mean}")
print(f"  实际标准差 = {np.std(sample_means):.6f}")
print(f"  理论标准差 = {theoretical_std:.6f}")

print(f"\n中心极限定理验证：样本均值近似服从正态分布 ✓")

# ============================================================
# 7. 假设检验
# ============================================================
print("\n【7. 假设检验】")

# 单样本 t 检验
# H0: μ = 1000 (产品平均寿命为 1000 小时)
# H1: μ ≠ 1000

np.random.seed(42)
sample_data = np.random.normal(loc=980, scale=50, size=25)

mu_0 = 1000  # 零假设的均值

# 执行 t 检验
t_stat, p_value = stats.ttest_1samp(sample_data, mu_0)

print(f"产品寿命检验:")
print(f"  样本均值 = {np.mean(sample_data):.2f} 小时")
print(f"  样本标准差 = {np.std(sample_data, ddof=1):.2f} 小时")
print(f"  样本大小 = {len(sample_data)}")
print(f"  零假设 H0: μ = {mu_0}")
print(f"  t 统计量 = {t_stat:.4f}")
print(f"  p 值 = {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"  结论：p < {alpha}，拒绝 H0，产品寿命与声称值有显著差异")
else:
    print(f"  结论：p ≥ {alpha}，不拒绝 H0，没有足够证据否定声称")

# ============================================================
# 8. 练习解答
# ============================================================
print("\n【8. 练习题解答】")

print("\n练习 1：贝叶斯疾病检测")
print(f"P(患病 | 阳性) = {p_disease_given_positive * 100:.2f}%")
print(f"这就是著名的'基础率谬误'示例！")

print("\n练习 2：正态分布应用")
exam_dist = stats.norm(75, 10)  # N(75, 10²)

# 成绩高于 85 分
prob_above_85 = 1 - exam_dist.cdf(85)
print(f"1. P(X > 85) = {prob_above_85:.4f}")

# 成绩在 65-85 分之间
prob_65_85 = exam_dist.cdf(85) - exam_dist.cdf(65)
print(f"2. P(65 ≤ X ≤ 85) = {prob_65_85:.4f}")

# 前 10% 的最低分数
top_10_threshold = exam_dist.ppf(0.9)
print(f"3. 前 10% 最低分数 = {top_10_threshold:.2f} 分")

print("\n练习 3：假设检验")
print(f"t 检验结果：t = {t_stat:.4f}, p = {p_value:.4f}")
if p_value < 0.05:
    print(f"在 α=0.05 水平下拒绝 H0，声称不可信")
else:
    print(f"在 α=0.05 水平下不拒绝 H0")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)

# ============================================================
# 可选：绘制分布图（取消注释以显示图形）
# ============================================================
# plt.figure(figsize=(12, 8))
# 
# # 正态分布
# plt.subplot(2, 2, 1)
# x = np.linspace(-4, 4, 100)
# plt.plot(x, stats.norm.pdf(x), 'b-', label='N(0,1)')
# plt.fill_between(x, 0, stats.norm.pdf(x), where=(x>=-1)&(x<=1), alpha=0.3)
# plt.title('标准正态分布')
# plt.legend()
# 
# # 二项分布
# plt.subplot(2, 2, 2)
# x = np.arange(0, 11)
# plt.bar(x, binom_dist.pmf(x))
# plt.title(f'二项分布 B({n},{p})')
# plt.xlabel('k')
# plt.ylabel('P(X=k)')
# 
# # 样本均值分布（中心极限定理）
# plt.subplot(2, 2, 3)
# plt.hist(sample_means, bins=50, density=True, alpha=0.7)
# plt.title('样本均值的分布 (CLT)')
# plt.xlabel('样本均值')
# plt.ylabel('密度')
# 
# plt.tight_layout()
# plt.savefig('probability_distributions.png', dpi=150)
# print("\n图表已保存为 probability_distributions.png")
# plt.show()
