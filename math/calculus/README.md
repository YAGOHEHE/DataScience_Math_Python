# 微积分 Calculus 📐

微积分是研究变化和累积的数学分支，是机器学习和优化算法的基础。

## 📚 目录

1. [极限与连续](#极限与连续)
2. [导数与微分](#导数与微分)
3. [积分](#积分)
4. [多元函数微积分](#多元函数微积分)
5. [梯度与优化](#梯度与优化)
6. [练习题](#练习题)

---

## 极限与连续

### 极限定义

$$\lim_{x \to a} f(x) = L$$

表示当 $x$ 趋近于 $a$ 时，$f(x)$ 趋近于 $L$。

### 重要极限

$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

$$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$$

### 连续性

函数 $f(x)$ 在 $x = a$ 处连续，当且仅当：

1. $f(a)$ 存在
2. $\lim_{x \to a} f(x)$ 存在
3. $\lim_{x \to a} f(x) = f(a)$

---

## 导数与微分

### 导数定义

$$f'(x) = \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

### 基本导数公式

| 函数 | 导数 |
|------|------|
| $c$ | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $a^x$ | $a^x \ln a$ |

### 求导法则

**乘积法则：**
$$(uv)' = u'v + uv'$$

**商法则：**
$$\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$$

**链式法则：**
$$\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$$

### 高阶导数

$$f''(x) = \frac{d^2f}{dx^2}, \quad f^{(n)}(x) = \frac{d^nf}{dx^n}$$

---

## 积分

### 不定积分

$$\int f(x) dx = F(x) + C, \quad \text{其中 } F'(x) = f(x)$$

### 基本积分公式

| 函数 | 积分 |
|------|------|
| $x^n$ ($n \neq -1$) | $\frac{x^{n+1}}{n+1} + C$ |
| $\frac{1}{x}$ | $\ln|x| + C$ |
| $e^x$ | $e^x + C$ |
| $\frac{1}{1+x^2}$ | $\arctan x + C$ |
| $\frac{1}{\sqrt{1-x^2}}$ | $\arcsin x + C$ |

### 定积分

$$\int_a^b f(x) dx = F(b) - F(a)$$

**几何意义：** 曲线 $f(x)$ 与 $x$ 轴在 $[a,b]$ 区间围成的面积

### 积分性质

1. $\int_a^b f(x) dx = -\int_b^a f(x) dx$
2. $\int_a^a f(x) dx = 0$
3. $\int_a^b [f(x) + g(x)] dx = \int_a^b f(x) dx + \int_a^b g(x) dx$

---

## 多元函数微积分

### 偏导数

对于 $f(x, y)$：

$$\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}$$

$$\frac{\partial f}{\partial y} = \lim_{h \to 0} \frac{f(x, y+h) - f(x, y)}{h}$$

### 全微分

$$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$$

### 链式法则（多元）

若 $z = f(x, y)$，且 $x = g(t), y = h(t)$：

$$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$$

---

## 梯度与优化

### 梯度 (Gradient)

$$\nabla f = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}$$

梯度指向函数增长最快的方向。

### 黑塞矩阵 (Hessian)

$$H = \begin{bmatrix} 
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots \\
\vdots & \vdots & \ddots
\end{bmatrix}$$

### 泰勒展开

**一维：**
$$f(x) \approx f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots$$

**多维：**
$$f(\mathbf{x}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a})^T(\mathbf{x}-\mathbf{a}) + \frac{1}{2}(\mathbf{x}-\mathbf{a})^T H(\mathbf{a}) (\mathbf{x}-\mathbf{a})$$

### 梯度下降

$$\mathbf{x}_{n+1} = \mathbf{x}_n - \alpha \nabla f(\mathbf{x}_n)$$

其中 $\alpha$ 是学习率。

---

## 练习题

### 练习 1：求导

求以下函数的导数：
1. $f(x) = x^3 e^x$
2. $f(x) = \ln(\sin x)$
3. $f(x) = \frac{x^2 + 1}{x - 1}$

### 练习 2：偏导数

求 $f(x, y) = x^2y + 3xy^2 - y^3$ 的偏导数 $\frac{\partial f}{\partial x}$ 和 $\frac{\partial f}{\partial y}$。

### 练习 3：梯度下降

使用梯度下降法求 $f(x) = x^2 - 4x + 5$ 的最小值，初始点 $x_0 = 0$，学习率 $\alpha = 0.1$，迭代 5 次。

---

## 📖 参考资料

- [3Blue1Brown - 微积分的本质](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
- [MIT OpenCourseWare - Single Variable Calculus](https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/)
- 《微积分学教程》- 菲赫金哥尔茨
- [梯度下降可视化](https://www.desmos.com/3d)

---

## 🔗 相关代码

- `calculus.py` - Python 实现示例
