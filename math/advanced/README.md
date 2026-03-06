# 高级数学主题 Advanced Topics 🎓

数据科学中的高级数学主题，包括信息论、傅里叶分析、随机过程等。

## 📚 目录

1. [信息论基础](#信息论基础)
2. [傅里叶分析](#傅里叶分析)
3. [随机过程](#随机过程)
4. [马尔可夫链](#马尔可夫链)
5. [练习题](#练习题)

---

## 信息论基础

### 信息量

事件 $x$ 的信息量：
$$I(x) = -\log_2 P(x)$$

### 熵 (Entropy)

随机变量 $X$ 的熵：
$$H(X) = -\sum_x P(x) \log_2 P(x)$$

熵衡量不确定性，单位：比特 (bits)

### 交叉熵

$$H(p, q) = -\sum_x p(x) \log_2 q(x)$$

### KL 散度

$$D_{KL}(p || q) = \sum_x p(x) \log_2 \frac{p(x)}{q(x)}$$

### 互信息

$$I(X; Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)$$

---

## 傅里叶分析

### 傅里叶级数

周期函数可表示为：
$$f(x) = a_0 + \sum_{n=1}^{\infty} [a_n \cos(nx) + b_n \sin(nx)]$$

### 傅里叶变换

$$\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x) e^{-2\pi i \xi x} dx$$

### 离散傅里叶变换 (DFT)

$$X_k = \sum_{n=0}^{N-1} x_n e^{-2\pi i kn/N}$$

### 快速傅里叶变换 (FFT)

高效计算 DFT 的算法，复杂度 $O(N \log N)$

---

## 随机过程

### 定义

随机过程是随时间演化的随机变量族 $\{X_t\}_{t \in T}$

### 泊松过程

计数过程 $N(t)$ 满足：
- $N(0) = 0$
- 独立增量
- $N(t) - N(s) \sim \text{Poi}(\lambda(t-s))$

### 布朗运动

标准布朗运动 $B_t$ 满足：
- $B_0 = 0$
- 连续路径
- 独立增量
- $B_t - B_s \sim N(0, t-s)$

---

## 马尔可夫链

### 定义

马尔可夫性：$P(X_{n+1} | X_n, X_{n-1}, \ldots) = P(X_{n+1} | X_n)$

### 转移矩阵

$$P = \begin{bmatrix} p_{11} & p_{12} & \cdots \\ p_{21} & p_{22} & \cdots \\ \vdots & \vdots & \ddots \end{bmatrix}$$

其中 $p_{ij} = P(X_{n+1} = j | X_n = i)$

### 平稳分布

$\pi$ 是平稳分布，如果：
$$\pi P = \pi, \quad \sum_i \pi_i = 1$$

---

## 练习题

### 练习 1：熵计算

计算公平硬币和偏置硬币 ($P(H)=0.9$) 的熵。

### 练习 2：马尔可夫链

给定转移矩阵 $P = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}$，求平稳分布。

---

## 📖 参考资料

- 《信息论、推理与学习算法》- MacKay
- 《随机过程》- Sheldon Ross
- [FFT 可视化](https://www.johndcook.com/blog/fft/)

## 🔗 相关代码

- `advanced_math.py` - Python 实现示例
