# 线性代数 Linear Algebra 📐

线性代数是数据科学的核心数学基础，广泛应用于机器学习、深度学习和数据分析。

## 📚 目录

1. [向量与矩阵](#向量与矩阵)
2. [矩阵运算](#矩阵运算)
3. [行列式与逆矩阵](#行列式与逆矩阵)
4. [特征值与特征向量](#特征值与特征向量)
5. [向量空间与基](#向量空间与基)
6. [奇异值分解 (SVD)](#奇异值分解-svd)
7. [练习题](#练习题)

---

## 向量与矩阵

### 向量 (Vector)

向量是有序的数值集合，可以表示为：

$$\vec{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n$$

**向量的模（长度）：**

$$\|\vec{v}\| = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2} = \sqrt{\sum_{i=1}^{n} v_i^2}$$

### 矩阵 (Matrix)

矩阵是二维数组，表示为：

$$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} \in \mathbb{R}^{m \times n}$$

---

## 矩阵运算

### 矩阵加法

$$A + B = \begin{bmatrix} a_{11}+b_{11} & a_{12}+b_{12} \\ a_{21}+b_{21} & a_{22}+b_{22} \end{bmatrix}$$

### 矩阵乘法

$$C = AB, \quad c_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}$$

**重要性质：**
- 不满足交换律：$AB \neq BA$（一般情况下）
- 满足结合律：$(AB)C = A(BC)$
- 满足分配律：$A(B+C) = AB + AC$

### 转置 (Transpose)

$$A^T = \begin{bmatrix} a_{11} & a_{21} \\ a_{12} & a_{22} \end{bmatrix}$$

**性质：** $(AB)^T = B^T A^T$

---

## 行列式与逆矩阵

### 行列式 (Determinant)

对于 $2 \times 2$ 矩阵：

$$\det(A) = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$$

对于 $3 \times 3$ 矩阵：

$$\det(A) = a_{11}\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} - a_{12}\begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} + a_{13}\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}$$

### 逆矩阵 (Inverse Matrix)

如果 $\det(A) \neq 0$，则 $A$ 可逆：

$$A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)$$

**性质：**
- $AA^{-1} = A^{-1}A = I$
- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^T)^{-1} = (A^{-1})^T$

---

## 特征值与特征向量

### 定义

对于方阵 $A$，如果存在非零向量 $\vec{v}$ 和标量 $\lambda$ 满足：

$$A\vec{v} = \lambda\vec{v}$$

则 $\lambda$ 称为**特征值**，$\vec{v}$ 称为对应的**特征向量**。

### 特征方程

$$\det(A - \lambda I) = 0$$

### 应用

- 主成分分析 (PCA)
- 矩阵对角化
- 稳定性分析

---

## 向量空间与基

### 线性组合

$$\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k$$

### 线性无关

向量组 $\{\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k\}$ 线性无关，当且仅当：

$$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k = \vec{0} \implies c_1 = c_2 = \cdots = c_k = 0$$

### 基与维度

- **基 (Basis)**：线性无关且能张成整个空间的向量组
- **维度 (Dimension)**：基中向量的个数

---

## 奇异值分解 (SVD)

任意 $m \times n$ 矩阵 $A$ 可以分解为：

$$A = U\Sigma V^T$$

其中：
- $U$ 是 $m \times m$ 正交矩阵
- $\Sigma$ 是 $m \times n$ 对角矩阵（奇异值）
- $V$ 是 $n \times n$ 正交矩阵

### 应用

- 数据降维
- 图像压缩
- 推荐系统

---

## 练习题

### 练习 1：矩阵乘法

计算以下矩阵乘法：

$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$$

求 $AB$ 和 $BA$，验证是否满足交换律。

### 练习 2：特征值计算

求矩阵 $A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$ 的特征值和特征向量。

### 练习 3：SVD 应用

使用 Python 对以下矩阵进行 SVD 分解：

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$$

---

## 📖 参考资料

- [3Blue1Brown - 线性代数的本质](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_abr)
- [MIT OpenCourseWare - Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/)
- [线性代数 - 维基百科](https://zh.wikipedia.org/wiki/线性代数)
- 《线性代数及其应用》- Gilbert Strang

---

## 🔗 相关代码

- `linear_algebra.py` - Python 实现示例
