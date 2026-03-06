# 数据科学家统计学 Statistics for Data Science 📊

本模块专门针对数据科学家所需的统计学知识，涵盖从基础到高级应用的完整内容。

## 📚 目录

1. [为什么数据科学家需要统计学](#为什么数据科学家需要统计学)
2. [描述统计与探索性数据分析](#描述统计与探索性数据分析)
3. [概率分布与抽样](#概率分布与抽样)
4. [假设检验与 A/B 测试](#假设检验与 A/B 测试)
5. [回归分析](#回归分析)
6. [贝叶斯统计](#贝叶斯统计)
7. [统计学习方法](#统计学习方法)
8. [实战案例](#实战案例)

---

## 为什么数据科学家需要统计学

### 统计学在数据科学中的角色

```
数据 → 描述统计 → 理解数据
     → 推断统计 → 做出决策
     → 预测模型 → 预测未来
```

### 核心应用场景

| 领域 | 统计方法 | 应用 |
|------|----------|------|
| **数据分析** | 描述统计、可视化 | 理解数据分布、发现模式 |
| **机器学习** | 回归、分类、聚类 | 构建预测模型 |
| **实验设计** | A/B 测试、假设检验 | 产品决策、功能评估 |
| **因果推断** | 倾向得分匹配、工具变量 | 评估干预效果 |
| **时间序列** | ARIMA、指数平滑 | 销售预测、需求规划 |
| **质量控制** | 控制图、过程能力 | 监控模型性能 |

### 统计学思维

1. **变异性思维**：数据有波动，结论有不确定性
2. **样本思维**：用样本推断总体
3. **概率思维**：用概率表达不确定性
4. **相关≠因果**：警惕虚假相关

---

## 描述统计与探索性数据分析

### EDA 流程

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 数据概览
df.info()          # 数据类型、缺失值
df.describe()      # 描述统计
df.head()          # 前几行

# 2. 缺失值分析
df.isnull().sum()
sns.heatmap(df.isnull())

# 3. 单变量分析
sns.histplot(df['column'])      # 分布
sns.boxplot(df['column'])       # 箱线图

# 4. 双变量分析
sns.scatterplot(x='col1', y='col2')  # 散点图
sns.heatmap(df.corr())               # 相关性

# 5. 多变量分析
sns.pairplot(df, hue='target')
```

### 关键统计量

```python
# 集中趋势
df.mean()      # 均值
df.median()    # 中位数
df.mode()      # 众数

# 离散程度
df.var()       # 方差
df.std()       # 标准差
df.quantile([0.25, 0.5, 0.75])  # 分位数

# 分布形状
df.skew()      # 偏度 (>0 右偏，<0 左偏)
df.kurtosis()  # 峰度 (>0 尖峰，<0 平峰)
```

### 异常值检测

```python
# Z-score 方法
from scipy import stats
z_scores = np.abs(stats.zscore(df['column']))
outliers_z = df[z_scores > 3]

# IQR 方法
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
outliers_iqr = df[(df['column'] < Q1 - 1.5*IQR) | 
                  (df['column'] > Q3 + 1.5*IQR)]

# 可视化
sns.boxplot(df['column'])
```

---

## 概率分布与抽样

### 数据科学常用分布

#### 1. 正态分布（高斯分布）

**应用：** 模型残差假设、特征标准化、置信区间

```python
from scipy import stats

# 生成正态分布数据
data = np.random.normal(loc=0, scale=1, size=1000)

# 检验正态性
stats.shapiro(data)           # Shapiro-Wilk 检验
stats.normaltest(data)        # D'Agostino-Pearson 检验

# Q-Q 图
stats.probplot(data, dist="norm", plot=plt)
```

#### 2. 二项分布

**应用：** 转化率、点击率、A/B 测试

```python
# n 次试验，成功概率 p
n, p = 100, 0.3
data = np.random.binomial(n, p, 1000)

# 计算概率
stats.binom.pmf(30, n, p)     # P(X = 30)
stats.binom.cdf(30, n, p)     # P(X ≤ 30)
```

#### 3. 泊松分布

**应用：** 单位时间事件数（访问、购买、故障）

```python
# 平均发生率 λ
lambda_ = 5
data = np.random.poisson(lambda_, 1000)

# 计算概率
stats.poisson.pmf(5, lambda_)  # P(X = 5)
```

#### 4. 指数分布

**应用：** 等待时间、用户留存、生存分析

```python
# 平均等待时间 1/λ
scale = 1/0.5  # λ = 0.5
data = np.random.exponential(scale, 1000)
```

### 抽样方法

```python
# 简单随机抽样
sample = df.sample(n=1000, random_state=42)

# 分层抽样（保持类别比例）
sample = df.groupby('category', group_keys=False).apply(
    lambda x: x.sample(n=min(len(x), 100))
)

# 系统抽样
sample = df.iloc[::10]  # 每 10 个抽 1 个

# Bootstrap 重抽样（用于置信区间）
bootstrap_means = [df.sample(frac=1, replace=True).mean() 
                   for _ in range(1000)]
ci = np.percentile(bootstrap_means, [2.5, 97.5])
```

### 中心极限定理应用

```python
# 无论原始分布如何，样本均值近似正态分布
def clt_demo():
    sample_means = []
    for _ in range(10000):
        # 从均匀分布抽样
        sample = np.random.uniform(0, 1, 30)
        sample_means.append(sample.mean())
    
    # 样本均值的分布
    plt.hist(sample_means, bins=50, density=True)
    # 近似 N(0.5, 1/12/30)
```

---

## 假设检验与 A/B 测试

### A/B 测试完整流程

```python
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.power import TTestIndPower

# 1. 确定样本量（功效分析）
effect_size = 0.5  # 期望检测的效应大小
alpha = 0.05       # 显著性水平
power = 0.8        # 统计功效

analysis = TTestIndPower()
sample_size = analysis.solve_power(effect_size=effect_size, 
                                    alpha=alpha, power=power)
print(f"每组需要 {sample_size:.0f} 个样本")

# 2. 收集数据
# A 组：对照组，B 组：实验组
group_a = [...]  # 转化率、点击率等
group_b = [...]

# 3. 检查假设
# 正态性检验
stats.shapiro(group_a)
stats.shapiro(group_b)

# 方差齐性检验
stats.levene(group_a, group_b)

# 4. 选择检验方法
if 正态且方差齐:
    t_stat, p_value = stats.ttest_ind(group_a, group_b)
elif 正态但方差不齐:
    t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)
else:
    # 非参数检验
    u_stat, p_value = stats.mannwhitneyu(group_a, group_b)

# 5. 计算效应量
from statsmodels.stats.proportion import proportion_effectsize
effect_size = proportion_effectsize(conv_a, conv_b)

# 6. 置信区间
from statsmodels.stats.weightstats import CompareMeans
cm = CompareMeans(sm.stats.DescrStatsW(group_a), 
                  sm.stats.DescrStatsW(group_b))
ci = cm.tconfint_diff(alpha=0.05)

# 7. 得出结论
if p_value < alpha:
    print(f"统计显著！B 组优于 A 组 (p={p_value:.4f})")
    print(f"效应量：{effect_size}")
    print(f"差异 95% CI: {ci}")
else:
    print(f"无统计显著差异 (p={p_value:.4f})")
```

### 多重检验校正

```python
from statsmodels.stats.multitest import multipletests

# 当进行多次检验时，需要校正 p 值
p_values = [0.01, 0.03, 0.04, 0.05, 0.10]

# Bonferroni 校正（保守）
reject_bonf, pvals_bonf, _, _ = multipletests(p_values, method='bonferroni')

# Benjamini-Hochberg 校正（控制 FDR，推荐）
reject_bh, pvals_bh, _, _ = multipletests(p_values, method='fdr_bh')
```

### 常见检验方法速查

| 场景 | 检验方法 | Python 函数 |
|------|----------|-------------|
| 单样本均值 | 单样本 t 检验 | `stats.ttest_1samp()` |
| 两独立样本均值 | 独立样本 t 检验 | `stats.ttest_ind()` |
| 配对样本均值 | 配对 t 检验 | `stats.ttest_rel()` |
| 多组均值 | ANOVA | `stats.f_oneway()` |
| 比例比较 | 卡方检验 | `stats.chi2_contingency()` |
| 相关性 | 皮尔逊相关 | `stats.pearsonr()` |
| 非参数两样本 | Mann-Whitney U | `stats.mannwhitneyu()` |
| 正态性 | Shapiro-Wilk | `stats.shapiro()` |
| 方差齐性 | Levene 检验 | `stats.levene()` |

---

## 回归分析

### 线性回归

```python
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

# 方法 1：statsmodels（统计推断）
X = df[['feature1', 'feature2']]
y = df['target']
X = sm.add_constant(X)  # 添加截距

model = sm.OLS(y, X).fit()
print(model.summary())  # 完整统计报告

# 解读：
# - coef: 回归系数
# - P>|t|: p 值（显著性）
# - R-squared: 决定系数
# - Adj. R-squared: 调整 R²
# - F-statistic: 整体显著性

# 方法 2：sklearn（预测）
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

model = LinearRegression()
model.fit(X, y)
print(f"系数：{model.coef_}")
print(f"截距：{model.intercept_}")
print(f"R²: {model.score(X, y)}")

# 交叉验证
cv_scores = cross_val_score(model, X, y, cv=5, scoring='r2')
print(f"CV R²: {cv_scores.mean():.3f} (+/- {cv_scores.std()*2:.3f})")
```

### 回归假设检验

```python
import statsmodels.api as sm

# 1. 线性关系
# 残差图
plt.scatter(model.fittedvalues, model.resid)
plt.axhline(y=0, color='r', linestyle='--')

# 2. 正态性（残差）
sm.qqplot(model.resid, line='s')

# 3. 同方差性
# Breusch-Pagan 检验
from statsmodels.stats.diagnostic import het_breuschpagan
bp_test = het_breuschpagan(model.resid, model.model.exog)
print(f"BP 检验 p 值：{bp_test[1]}")  # >0.05 满足同方差

# 4. 无自相关
# Durbin-Watson 检验
dw = sm.stats.durbin_watson(model.resid)
print(f"DW 统计量：{dw}")  # 接近 2 无自相关

# 5. 无多重共线性
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif_data = pd.DataFrame()
vif_data['feature'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i) 
                   for i in range(X.shape[1])]
print(vif_data)  # VIF < 5 可接受
```

### 正则化回归

```python
from sklearn.linear_model import Ridge, Lasso, ElasticNet

# 岭回归（L2 正则化）
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

# Lasso 回归（L1 正则化，可做特征选择）
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
print(f"非零系数：{np.sum(lasso.coef_ != 0)}")

# 弹性网络（L1 + L2）
enet = ElasticNet(alpha=0.1, l1_ratio=0.5)
enet.fit(X_train, y_train)

# 交叉验证选择 alpha
from sklearn.linear_model import RidgeCV
ridge_cv = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0], cv=5)
ridge_cv.fit(X_train, y_train)
print(f"最佳 alpha: {ridge_cv.alpha_}")
```

### 逻辑回归

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, roc_curve

# 训练
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

# 预测概率
y_prob = clf.predict_proba(X_test)[:, 1]
y_pred = clf.predict(X_test)

# 评估
print(classification_report(y_test, y_pred))
print(f"AUC: {roc_auc_score(y_test, y_prob):.3f}")

# ROC 曲线
fpr, tpr, _ = roc_curve(y_test, y_prob)
plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1], 'k--')

# 特征重要性（系数）
coef_df = pd.DataFrame({
    'feature': X.columns,
    'coef': clf.coef_[0],
    'odds_ratio': np.exp(clf.coef_[0])
})
print(coef_df.sort_values('coef', ascending=False))
```

---

## 贝叶斯统计

### 贝叶斯 vs 频率学派

| 方面 | 频率学派 | 贝叶斯学派 |
|------|----------|------------|
| 参数 | 固定未知 | 随机变量，有分布 |
| 概率 | 长期频率 | 主观信念程度 |
| 结果 | 点估计 + 置信区间 | 后验分布 + 可信区间 |
| 先验信息 | 不使用 | 明确使用 |

### PyMC3 贝叶斯建模

```python
import pymc3 as pm
import arviz as az

# 示例：贝叶斯线性回归
with pm.Model() as model:
    # 先验分布
    beta = pm.Normal('beta', mu=0, sigma=10, shape=X.shape[1])
    alpha = pm.Normal('alpha', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=1)
    
    # 似然
    mu = alpha + pm.math.dot(X, beta)
    y_obs = pm.Normal('y_obs', mu=mu, sigma=sigma, observed=y)
    
    # 采样
    trace = pm.sample(2000, tune=1000, return_inferencedata=True)

# 后验分析
az.summary(trace)
az.plot_trace(trace)
az.plot_posterior(trace)

# 预测
posterior_predictive = pm.sample_posterior_predictive(trace, model=model)
```

### 贝叶斯 A/B 测试

```python
# A 组：1000 次展示，50 次转化
# B 组：1000 次展示，70 次转化

with pm.Model() as ab_model:
    # 先验：Beta(1, 1) = Uniform(0, 1)
    p_a = pm.Beta('p_a', alpha=1, beta=1)
    p_b = pm.Beta('p_b', alpha=1, beta=1)
    
    # 似然
    obs_a = pm.Binomial('obs_a', n=1000, p=p_a, observed=50)
    obs_b = pm.Binomial('obs_b', n=1000, p=p_b, observed=70)
    
    # 感兴趣的数量
    diff = pm.Deterministic('diff', p_b - p_a)
    
    # 采样
    trace_ab = pm.sample(2000, tune=1000)

# 后验概率
prob_b_better = (trace_ab['p_b'] > trace_ab['p_a']).mean()
print(f"P(B > A | 数据) = {prob_b_better:.3f}")

# 可信区间
ci = np.percentile(trace_ab['diff'], [2.5, 97.5])
print(f"差异 95% 可信区间：{ci}")
```

---

## 统计学习方法

### 偏差 - 方差权衡

```
总误差 = 偏差² + 方差 + 不可约误差
```

- **高偏差**：欠拟合，模型太简单
- **高方差**：过拟合，模型太复杂

### 交叉验证

```python
from sklearn.model_selection import (
    cross_val_score, 
    cross_validate,
    KFold,
    StratifiedKFold,
    LeaveOneOut
)

# K 折交叉验证
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"CV 得分：{scores.mean():.3f} (+/- {scores.std()*2:.3f})")

# 多指标评估
scoring = ['accuracy', 'precision', 'recall', 'f1']
scores = cross_validate(model, X, y, cv=5, scoring=scoring)

# 分层 K 折（保持类别比例）
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for train_idx, test_idx in skf.split(X, y):
    # 训练和评估
    pass

# 留一法（小数据集）
loo = LeaveOneOut()
```

### 学习曲线与验证曲线

```python
from sklearn.model_selection import learning_curve, validation_curve

# 学习曲线（诊断偏差/方差）
train_sizes, train_scores, test_scores = learning_curve(
    model, X, y, cv=5, train_sizes=np.linspace(0.1, 1.0, 10)
)

# 验证曲线（选择超参数）
param_range = [0.001, 0.01, 0.1, 1.0, 10.0]
train_scores, test_scores = validation_curve(
    model, X, y, param_name='C', param_range=param_range, cv=5
)
```

### 特征选择

```python
from sklearn.feature_selection import (
    SelectKBest, 
    f_classif,
    RFE,
    SelectFromModel
)

# 1. 单变量选择（基于统计检验）
selector = SelectKBest(score_func=f_classif, k=10)
X_selected = selector.fit_transform(X, y)

# 2. 递归特征消除
from sklearn.feature_selection import RFE
rfe = RFE(estimator=RandomForestClassifier(), n_features_to_select=10)
X_selected = rfe.fit_transform(X, y)

# 3. 基于模型的选择
from sklearn.feature_selection import SelectFromModel
sfm = SelectFromModel(RandomForestClassifier())
X_selected = sfm.fit_transform(X, y)
```

---

## 实战案例

### 案例 1：电商转化率分析

```python
# 问题：新页面设计是否提高转化率？

# 1. 数据准备
control = pd.read_csv('control_group.csv')  # 旧页面
treatment = pd.read_csv('treatment_group.csv')  # 新页面

# 2. 描述统计
conv_rate_control = control['converted'].mean()
conv_rate_treatment = treatment['converted'].mean()
print(f"对照组转化率：{conv_rate_control:.3f}")
print(f"实验组转化率：{conv_rate_treatment:.3f}")
print(f"相对提升：{(conv_rate_treatment/conv_rate_control - 1)*100:.1f}%")

# 3. 假设检验
from statsmodels.stats.proportion import proportions_ztest

count = [treatment['converted'].sum(), control['converted'].sum()]
nobs = [len(treatment), len(control)]

stat, p_value = proportions_ztest(count, nobs, alternative='larger')
print(f"Z 检验 p 值：{p_value:.4f}")

# 4. 效应量
from statsmodels.stats.proportion import proportion_effectsize
effect_size = proportion_effectsize(conv_rate_treatment, conv_rate_control)
print(f"效应量 (Cohen's h): {effect_size:.3f}")

# 5. 结论
if p_value < 0.05 and effect_size > 0.2:
    print("✓ 新页面显著提升转化率，建议上线")
else:
    print("✗ 无显著提升或效应太小")
```

### 案例 2：用户流失预测

```python
# 1. 探索性分析
sns.boxplot(x='churn', y='tenure', data=df)
sns.boxplot(x='churn', y='monthly_charges', data=df)

# 2. 相关性分析
corr = df.corr()
sns.heatmap(corr[['churn']], annot=True)

# 3. 建立模型
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

X = df.drop('churn', axis=1)
y = df['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. 评估
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred))
print(f"AUC: {roc_auc_score(y_test, y_prob):.3f}")

# 5. 特征重要性
importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("Top 10 重要特征:")
print(importance.head(10))

# 6. 统计检验：流失用户 vs 非流失用户
for col in ['tenure', 'monthly_charges', 'total_charges']:
    t_stat, p_val = stats.ttest_ind(
        df[df['churn']==1][col],
        df[df['churn']==0][col]
    )
    print(f"{col}: t={t_stat:.3f}, p={p_val:.4f}")
```

### 案例 3：时间序列预测

```python
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima

# 1. 平稳性检验（ADF 检验）
result = adfuller(df['sales'])
print(f"ADF 统计量：{result[0]:.3f}, p 值：{result[1]:.4f}")
# p < 0.05 表示平稳

# 2. 差分使序列平稳
df['sales_diff'] = df['sales'].diff().dropna()

# 3. 自动选择 ARIMA 参数
model = auto_arima(df['sales'], seasonal=True, m=12,
                   start_p=1, start_q=1,
                   max_p=3, max_q=3)
print(model.summary())

# 4. 拟合模型
arima = ARIMA(df['sales'], order=(1,1,1), seasonal_order=(1,1,1,12))
arima_fit = arima.fit()

# 5. 预测
forecast = arima_fit.forecast(steps=30)
plt.plot(df['sales'][-100:])
plt.plot(range(len(df)-100, len(df)+30), 
         np.concatenate([df['sales'][-100:].values, forecast]))
```

---

## 📖 参考资料

### 书籍
- 《统计学习方法》- 李航 ⭐⭐⭐
- 《应用回归分析》- 何晓群
- 《贝叶斯思维》- Allen Downey
- 《Practical Statistics for Data Scientists》- Peter Bruce

### 在线资源
- [StatQuest](https://www.youtube.com/c/joshstarmer) ⭐ 视频讲解
- [Kaggle Learn - Statistics](https://www.kaggle.com/learn/statistics)
- [Towards Data Science - Statistics](https://towardsdatascience.com/tagged/statistics)

### Python 库
- `scipy.stats` - 基础统计
- `statsmodels` - 统计建模
- `scikit-learn` - 机器学习
- `pymc3` / `pymc` - 贝叶斯统计
- `arviz` - 贝叶斯诊断

---

## 🔗 相关代码

- `statistics_examples.py` - 完整示例代码
- `../notebooks/02_probability_stats.ipynb` - 概率统计实践
- `../notebooks/03_optimization_ml.ipynb` - 机器学习实践
