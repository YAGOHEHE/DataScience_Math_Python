# 概率统计 Probability & Statistics 📈

概率论与统计学是数据科学的核心，用于理解数据、建立模型和做出推断。

## 📚 目录

1. [概率基础](#概率基础)
2. [随机变量](#随机变量)
3. [常见分布](#常见分布)
4. [描述统计](#描述统计)
5. [推断统计](#推断统计)
6. [贝叶斯定理](#贝叶斯定理)
7. [练习题](#练习题)

---

## 概率基础

### 基本定义

**样本空间 (Sample Space)**：所有可能结果的集合，记为 $\Omega$

**事件 (Event)**：样本空间的子集

**概率公理：**
1. $0 \leq P(A) \leq 1$
2. $P(\Omega) = 1$
3. 若 $A_1, A_2, \ldots$ 互斥，则 $P(\bigcup_i A_i) = \sum_i P(A_i)$

### 条件概率

$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

### 独立性

事件 $A$ 和 $B$ 独立，当且仅当：

$$P(A \cap B) = P(A) \cdot P(B)$$

---

## 随机变量

### 离散随机变量

取有限或可数无限个值的随机变量。

**概率质量函数 (PMF)**：$P(X = x)$

**期望值：**
$$E[X] = \sum_x x \cdot P(X = x)$$

**方差：**
$$\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$$

### 连续随机变量

取连续值的随机变量。

**概率密度函数 (PDF)**：$f(x)$，满足 $\int_{-\infty}^{\infty} f(x) dx = 1$

$$P(a \leq X \leq b) = \int_a^b f(x) dx$$

**期望值：**
$$E[X] = \int_{-\infty}^{\infty} x \cdot f(x) dx$$

---

## 常见分布

### 离散分布

| 分布 | PMF | 期望 | 方差 |
|------|-----|------|------|
| 伯努利 $Bern(p)$ | $P(X=k) = p^k(1-p)^{1-k}$ | $p$ | $p(1-p)$ |
| 二项 $Bin(n,p)$ | $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| 泊松 $Poi(\lambda)$ | $P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$ | $\lambda$ | $\lambda$ |

### 连续分布

| 分布 | PDF | 期望 | 方差 |
|------|-----|------|------|
| 均匀 $U(a,b)$ | $f(x) = \frac{1}{b-a}$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| 正态 $N(\mu,\sigma^2)$ | $f(x) = \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |
| 指数 $Exp(\lambda)$ | $f(x) = \lambda e^{-\lambda x}$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |

### 标准正态分布

$$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$

**68-95-99.7 规则：**
- 约 68% 的数据在 $\mu \pm \sigma$ 内
- 约 95% 的数据在 $\mu \pm 2\sigma$ 内
- 约 99.7% 的数据在 $\mu \pm 3\sigma$ 内

---

## 描述统计

### 集中趋势

**均值 (Mean)：**
$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$

**中位数 (Median)：** 排序后中间的值

**众数 (Mode)：** 出现最频繁的值

### 离散程度

**方差 (Variance)：**
$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2$$

**标准差 (Standard Deviation)：**
$$s = \sqrt{s^2}$$

**四分位距 (IQR)：**
$$IQR = Q_3 - Q_1$$

---

## 推断统计

### 中心极限定理

当样本量 $n$ 足够大时，样本均值的分布近似正态分布：

$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

### 置信区间

总体均值的 $100(1-\alpha)\%$ 置信区间：

$$\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

### 假设检验

**零假设 $H_0$** vs **备择假设 $H_1$**

**p 值**：在 $H_0$ 为真时，观察到当前或更极端结果的概率

**决策规则：**
- 若 $p < \alpha$，拒绝 $H_0$
- 若 $p \geq \alpha$，不拒绝 $H_0$

---

## 贝叶斯定理

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

其中：
- $P(A)$：先验概率
- $P(B|A)$：似然
- $P(A|B)$：后验概率
- $P(B)$：证据

### 贝叶斯更新

$$\text{后验} \propto \text{似然} \times \text{先验}$$

---

## 练习题

### 练习 1：条件概率

一个疾病检测的准确率为 99%，即：
- $P(\text{阳性}|\text{患病}) = 0.99$
- $P(\text{阴性}|\text{健康}) = 0.99$

疾病患病率为 0.1%。如果某人检测结果为阳性，他实际患病的概率是多少？

### 练习 2：正态分布应用

某考试成绩服从 $N(75, 100)$ 分布。求：
1. 成绩高于 85 分的概率
2. 成绩在 65-85 分之间的概率
3. 前 10% 学生的最低分数

### 练习 3：假设检验

某公司声称其产品的平均寿命为 1000 小时。随机抽取 25 个产品，测得平均寿命为 980 小时，标准差为 50 小时。在 $\alpha = 0.05$ 水平下，检验该声称是否可信。

---

## 📖 参考资料

- [可汗学院 - 概率与统计](https://zh.khanacademy.org/math/statistics-probability)
- [MIT OpenCourseWare - Introduction to Probability](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-spring-2014/)
- 《概率论与数理统计》- 陈希孺
- [StatQuest 统计学系列](https://www.youtube.com/c/joshstarmer)

---

## 🔗 相关代码

- `probability.py` - Python 实现示例
