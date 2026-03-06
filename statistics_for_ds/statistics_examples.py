#!/usr/bin/env python3
"""
数据科学家统计学示例
Statistics Examples for Data Science

涵盖：描述统计、假设检验、A/B 测试、回归分析、贝叶斯统计
"""

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("数据科学家统计学示例")
print("=" * 70)

# ============================================================
# 1. 描述统计与探索性数据分析
# ============================================================
print("\n【1. 描述统计与 EDA】")

# 生成示例数据
np.random.seed(42)
n = 1000
data = pd.DataFrame({
    'age': np.random.normal(35, 10, n),
    'income': np.random.lognormal(10, 1, n),
    'score': np.random.uniform(0, 100, n),
    'category': np.random.choice(['A', 'B', 'C'], n),
    'target': np.random.randint(0, 2, n)
})

print(f"数据形状：{data.shape}")
print(f"\n描述统计:")
print(data.describe())

print(f"\n偏度:")
print(data[['age', 'income', 'score']].skew())

print(f"\n峰度:")
print(data[['age', 'income', 'score']].kurtosis())

# 异常值检测
print(f"\n异常值检测 (Z-score > 3):")
z_scores = np.abs(stats.zscore(data['age'].dropna()))
outliers = np.sum(z_scores > 3)
print(f"  age 列异常值数量：{outliers}")

# ============================================================
# 2. 概率分布
# ============================================================
print("\n【2. 概率分布】")

# 正态分布
print("\n正态分布 N(0, 1):")
print(f"  P(-1 < Z < 1) = {stats.norm.cdf(1) - stats.norm.cdf(-1):.4f}")
print(f"  P(-2 < Z < 2) = {stats.norm.cdf(2) - stats.norm.cdf(-2):.4f}")
print(f"  P(-3 < Z < 3) = {stats.norm.cdf(3) - stats.norm.cdf(-3):.4f}")

# 二项分布（转化率场景）
print("\n二项分布（转化率 30%，100 次试验）:")
n_trials, p_success = 100, 0.3
print(f"  期望成功次数：{n_trials * p_success}")
print(f"  P(恰好 30 次成功) = {stats.binom.pmf(30, n_trials, p_success):.4f}")
print(f"  P(30 次或更少成功) = {stats.binom.cdf(30, n_trials, p_success):.4f}")

# 泊松分布（单位时间事件数）
print("\n泊松分布（平均每小时 5 个事件）:")
lambda_ = 5
print(f"  期望：{lambda_}")
print(f"  P(恰好 5 个事件) = {stats.poisson.pmf(5, lambda_):.4f}")
print(f"  P(超过 7 个事件) = {1 - stats.poisson.cdf(7, lambda_):.4f}")

# ============================================================
# 3. 假设检验
# ============================================================
print("\n【3. 假设检验】")

# 单样本 t 检验
print("\n单样本 t 检验:")
sample = np.random.normal(100, 15, 50)
t_stat, p_value = stats.ttest_1samp(sample, 100)
print(f"  检验均值是否等于 100")
print(f"  t = {t_stat:.4f}, p = {p_value:.4f}")
if p_value > 0.05:
    print("  结论：不拒绝 H0，均值可能为 100")
else:
    print("  结论：拒绝 H0，均值不等于 100")

# 双样本 t 检验
print("\n双样本 t 检验:")
group_a = np.random.normal(100, 15, 100)
group_b = np.random.normal(105, 15, 100)
t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"  比较两组均值")
print(f"  Group A 均值：{group_a.mean():.2f}")
print(f"  Group B 均值：{group_b.mean():.2f}")
print(f"  t = {t_stat:.4f}, p = {p_value:.4f}")
if p_value < 0.05:
    print("  结论：两组均值有显著差异")
else:
    print("  结论：两组均值无显著差异")

# 卡方检验（独立性）
print("\n卡方检验（独立性）:")
contingency = np.array([
    [50, 30, 20],  # 类别 A
    [40, 35, 25],  # 类别 B
    [30, 40, 30]   # 类别 C
])
chi2, p_value, dof, expected = stats.chi2_contingency(contingency)
print(f"  列联表:\n{contingency}")
print(f"  χ² = {chi2:.4f}, p = {p_value:.4f}")
print(f"  自由度：{dof}")
if p_value < 0.05:
    print("  结论：行列变量相关")
else:
    print("  结论：行列变量独立")

# ============================================================
# 4. A/B 测试
# ============================================================
print("\n【4. A/B 测试】")

# 模拟 A/B 测试数据
np.random.seed(42)
n_a, n_b = 1000, 1000
conv_a = np.random.binomial(1, 0.10, n_a)  # A 组转化率 10%
conv_b = np.random.binomial(1, 0.13, n_b)  # B 组转化率 13%

conv_rate_a = conv_a.mean()
conv_rate_b = conv_b.mean()

print(f"A 组（对照）: {n_a} 人，转化 {conv_a.sum()} 人，转化率 {conv_rate_a:.2%}")
print(f"B 组（实验）: {n_b} 人，转化 {conv_b.sum()} 人，转化率 {conv_rate_b:.2%}")
print(f"相对提升：{(conv_rate_b / conv_rate_a - 1) * 100:.1f}%")

# 比例 Z 检验
from statsmodels.stats.proportion import proportions_ztest

count = [conv_b.sum(), conv_a.sum()]
nobs = [n_b, n_a]

z_stat, p_value = proportions_ztest(count, nobs, alternative='larger')
print(f"\n比例 Z 检验:")
print(f"  z = {z_stat:.4f}, p = {p_value:.4f}")

if p_value < 0.05:
    print("  结论：B 组转化率显著高于 A 组 ✓")
else:
    print("  结论：无显著差异")

# 效应量
from statsmodels.stats.proportion import proportion_effectsize
effect_size = proportion_effectsize(conv_rate_b, conv_rate_a)
print(f"\n效应量 (Cohen's h): {effect_size:.3f}")
print(f"  解释：0.2=小，0.5=中，0.8=大")

# 置信区间
from statsmodels.stats.weightstats import CompareMeans
import statsmodels.api as sm
cm = CompareMeans(sm.stats.DescrStatsW(conv_b), sm.stats.DescrStatsW(conv_a))
ci = cm.tconfint_diff(alpha=0.05)
print(f"\n差异 95% 置信区间：[{ci[0]:.4f}, {ci[1]:.4f}]")

# ============================================================
# 5. 相关性分析
# ============================================================
print("\n【5. 相关性分析】")

# 皮尔逊相关系数
x = np.random.normal(0, 1, 100)
y = 2 * x + np.random.normal(0, 0.5, 100)

corr, p_value = stats.pearsonr(x, y)
print(f"皮尔逊相关系数：r = {corr:.4f}, p = {p_value:.4f}")

# 斯皮尔曼相关系数（非参数）
corr_s, p_value_s = stats.spearmanr(x, y)
print(f"斯皮尔曼相关系数：ρ = {corr_s:.4f}, p = {p_value_s:.4f}")

# 相关系数解释
print(f"\n相关系数解释:")
print(f"  |r| > 0.7: 强相关")
print(f"  0.4 < |r| < 0.7: 中等相关")
print(f"  |r| < 0.4: 弱相关")

# ============================================================
# 6. 线性回归
# ============================================================
print("\n【6. 线性回归】")

# 生成数据
np.random.seed(42)
X = np.random.randn(200, 3)  # 3 个特征
true_coef = [2.5, -1.5, 0.8]
y = X @ true_coef + np.random.randn(200) * 0.5 + 5

# 训练模型
model = LinearRegression()
model.fit(X, y)

print(f"真实系数：{true_coef}")
print(f"拟合系数：{model.coef_}")
print(f"真实截距：5, 拟合截距：{model.intercept_:.2f}")
print(f"R² = {model.score(X, y):.4f}")

# 交叉验证
cv_scores = cross_val_score(model, X, y, cv=5, scoring='r2')
print(f"\n5 折交叉验证 R²: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")

# ============================================================
# 7. 逻辑回归
# ============================================================
print("\n【7. 逻辑回归】")

# 生成分类数据
np.random.seed(42)
X_clf = np.random.randn(300, 2)
y_clf = (X_clf[:, 0] + X_clf[:, 1] + np.random.randn(300) * 0.5 > 0).astype(int)

# 训练模型
clf = LogisticRegression()
clf.fit(X_clf, y_clf)

# 预测
y_pred = clf.predict(X_clf)
y_prob = clf.predict_proba(X_clf)[:, 1]

# 评估
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score

print(f"准确率：{accuracy_score(y_clf, y_pred):.4f}")
print(f"精确率：{precision_score(y_clf, y_pred):.4f}")
print(f"召回率：{recall_score(y_clf, y_pred):.4f}")
print(f"AUC: {roc_auc_score(y_clf, y_prob):.4f}")

# 优势比
odds_ratio = np.exp(clf.coef_)
print(f"\n优势比:")
print(f"  特征 1: OR = {odds_ratio[0][0]:.3f}")
print(f"  特征 2: OR = {odds_ratio[0][1]:.3f}")
print(f"  解释：OR > 1 表示正相关，OR < 1 表示负相关")

# ============================================================
# 8. 贝叶斯统计示例
# ============================================================
print("\n【8. 贝叶斯统计示例】")

# 贝叶斯更新示例：硬币偏置
print("\n贝叶斯更新 - 硬币偏置估计:")

# 先验：Beta(1, 1) = Uniform(0, 1)
alpha_prior, beta_prior = 1, 1
print(f"先验：Beta({alpha_prior}, {beta_prior})")
print(f"  先验期望：{alpha_prior / (alpha_prior + beta_prior):.2f}")

# 数据：抛 10 次，7 次正面
n_heads, n_tails = 7, 3

# 后验：Beta(α + heads, β + tails)
alpha_post = alpha_prior + n_heads
beta_post = beta_prior + n_tails

print(f"\n数据：{n_heads} 次正面，{n_tails} 次反面")
print(f"后验：Beta({alpha_post}, {beta_post})")
print(f"  后验期望：{alpha_post / (alpha_post + beta_post):.3f}")
print(f"  后验 95% 可信区间：{stats.beta.ppf([0.025, 0.975], alpha_post, beta_post)}")

# 共轭先验的优势
print(f"\n共轭先验优势：后验分布与先验同族，解析可解")

# ============================================================
# 9. 功效分析（样本量计算）
# ============================================================
print("\n【9. 功效分析（样本量计算）】")

from statsmodels.stats.power import TTestIndPower, GofChisquarePower

# A/B 测试样本量计算
print("\nA/B 测试样本量计算:")

effect_size = 0.3  # 期望检测的效应大小
alpha = 0.05       # 显著性水平
power = 0.8        # 统计功效

analysis = TTestIndPower()
sample_size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power)

print(f"  效应大小 (Cohen's d): {effect_size}")
print(f"  显著性水平 α: {alpha}")
print(f"  统计功效 1-β: {power}")
print(f"  每组需要样本量：{sample_size:.0f}")
print(f"  总样本量：{sample_size * 2:.0f}")

# 不同效应大小下的样本量
print(f"\n不同效应大小所需样本量:")
for es in [0.2, 0.3, 0.5, 0.8]:
    n = analysis.solve_power(effect_size=es, alpha=alpha, power=power)
    print(f"  d = {es}: 每组 {n:.0f} 个样本")

# ============================================================
# 10. 多重检验校正
# ============================================================
print("\n【10. 多重检验校正】")

from statsmodels.stats.multitest import multipletests

# 模拟多个假设检验
np.random.seed(42)
n_tests = 20
p_values = np.random.uniform(0, 1, n_tests)

print(f"原始 p 值：{p_values[:5]}...")

# Bonferroni 校正
_, p_bonf, _, _ = multipletests(p_values, method='bonferroni')
print(f"\nBonferroni 校正后：{p_bonf[:5]}...")
print(f"  显著数量 (α=0.05): {np.sum(p_bonf < 0.05)}")

# Benjamini-Hochberg 校正（控制 FDR）
_, p_bh, _, _ = multipletests(p_values, method='fdr_bh')
print(f"\nBH 校正后：{p_bh[:5]}...")
print(f"  显著数量 (α=0.05): {np.sum(p_bh < 0.05)}")

print(f"\n校正方法比较:")
print(f"  Bonferroni: 控制 FWER，保守")
print(f"  BH: 控制 FDR，推荐用于探索性分析")

# ============================================================
# 11. 练习
# ============================================================
print("\n【11. 练习】")

# 练习 1：单样本 t 检验
print("\n练习 1：单样本 t 检验")
sample_ex = np.random.normal(98, 12, 40)
t_stat_ex, p_value_ex = stats.ttest_1samp(sample_ex, 100)
print(f"  样本均值：{sample_ex.mean():.2f}")
print(f"  检验 H0: μ = 100")
print(f"  t = {t_stat_ex:.4f}, p = {p_value_ex:.4f}")
print(f"  结论：{'拒绝 H0' if p_value_ex < 0.05 else '不拒绝 H0'}")

# 练习 2：置信区间
print("\n练习 2：置信区间")
sample_mean = sample_ex.mean()
sample_std = sample_ex.std(ddof=1)
n = len(sample_ex)
ci = stats.t.interval(0.95, df=n-1, loc=sample_mean, scale=sample_std/np.sqrt(n))
print(f"  样本均值：{sample_mean:.2f}")
print(f"  95% 置信区间：[{ci[0]:.2f}, {ci[1]:.2f}]")
print(f"  解释：重复抽样 95% 的区间会包含真实均值")

print("\n" + "=" * 70)
print("示例运行完成！")
print("=" * 70)
