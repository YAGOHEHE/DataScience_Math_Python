# 优化 Optimization 🎯

优化是数据科学和机器学习的核心，用于找到最佳解决方案。

## 📚 目录

1. [优化问题基础](#优化问题基础)
2. [无约束优化](#无约束优化)
3. [约束优化](#约束优化)
4. [凸优化](#凸优化)
5. [线性规划](#线性规划)
6. [练习题](#练习题)

---

## 优化问题基础

### 标准形式

$$\min_{x} f(x)$$
$$\text{s.t. } g_i(x) \leq 0, \quad i = 1, \ldots, m$$
$$\quad \quad h_j(x) = 0, \quad j = 1, \ldots, p$$

### 局部最优 vs 全局最优

- **局部最优**：在邻域内是最优的
- **全局最优**：在整个定义域内是最优的

---

## 无约束优化

### 梯度下降法

$$x_{k+1} = x_k - \alpha \nabla f(x_k)$$

### 牛顿法

$$x_{k+1} = x_k - [Hf(x_k)]^{-1} \nabla f(x_k)$$

其中 $Hf$ 是黑塞矩阵。

### 最优性条件

**一阶必要条件：**
$$\nabla f(x^*) = 0$$

**二阶充分条件：**
$$\nabla f(x^*) = 0 \text{ 且 } Hf(x^*) \succ 0 \text{ (正定)}$$

---

## 约束优化

### 拉格朗日乘数法

对于等式约束 $\min f(x)$ s.t. $g(x) = 0$：

$$\mathcal{L}(x, \lambda) = f(x) + \lambda g(x)$$

求解：
$$\nabla_x \mathcal{L} = 0, \quad \nabla_\lambda \mathcal{L} = 0$$

### KKT 条件

对于不等式约束，KKT 条件包括：
1. 平稳性：$\nabla f + \sum \lambda_i \nabla g_i = 0$
2. 原始可行性：$g_i(x) \leq 0$
3. 对偶可行性：$\lambda_i \geq 0$
4. 互补松弛：$\lambda_i g_i(x) = 0$

---

## 凸优化

### 凸集

集合 $S$ 是凸集，如果 $\forall x, y \in S, \theta \in [0,1]$：
$$\theta x + (1-\theta)y \in S$$

### 凸函数

函数 $f$ 是凸函数，如果：
$$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$

### 凸优化优势

- 局部最优 = 全局最优
- 高效算法可解

---

## 线性规划

### 标准形式

$$\min c^T x$$
$$\text{s.t. } Ax = b, \quad x \geq 0$$

### 单纯形法

通过顶点迭代寻找最优解。

---

## 练习题

### 练习 1：梯度下降

用梯度下降法求 $f(x) = x^4 - 4x^2$ 的最小值。

### 练习 2：拉格朗日乘数法

在约束 $x + y = 1$ 下，最小化 $f(x,y) = x^2 + y^2$。

---

## 📖 参考资料

- [Convex Optimization - Boyd](https://web.stanford.edu/~boyd/cvxbook/)
- 《凸优化》- 王书宁译
- [scipy.optimize 文档](https://docs.scipy.org/doc/scipy/reference/optimize.html)

## 🔗 相关代码

- `optimization.py` - Python 实现示例
