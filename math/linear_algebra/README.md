# 线性代数 Linear Algebra 📐

线性代数是数据科学的核心数学基础，广泛应用于机器学习、深度学习和数据分析。

## 📚 目录

1. [向量与矩阵](#向量与矩阵)
2. [矩阵运算](#矩阵运算)
3. [行列式与逆矩阵](#行列式与逆矩阵)
4. [特征值与特征向量](#特征值与特征向量)
5. [向量空间与基](#向量空间与基)
6. [奇异值分解 (SVD)](#奇异值分解-svd)
7. [数据科学应用](#数据科学应用)
8. [练习题](#练习题)

---

## 向量与矩阵

### 向量 (Vector)

**定义：** 向量是有序的数值集合，可以表示空间中的一个点或方向。

$$\vec{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n$$

**几何意义：**
- 在 2D 空间中，向量 $(x, y)$ 表示从原点到点 $(x, y)$ 的箭头
- 在 3D 空间中，向量 $(x, y, z)$ 表示空间中的一个方向
- 在高维空间中，向量表示数据的特征（如用户画像、商品特征等）

**向量的模（长度/范数）：**

$$\|\vec{v}\| = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2} = \sqrt{\sum_{i=1}^{n} v_i^2}$$

**数据科学意义：** 向量的模表示"大小"或"强度"，在推荐系统中可表示用户偏好强度。

### 矩阵 (Matrix)

**定义：** 矩阵是二维数组，由行和列组成。

$$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} \in \mathbb{R}^{m \times n}$$

**数据科学中的矩阵：**
- **数据集**：每行是一个样本，每列是一个特征（$m$ 个样本，$n$ 个特征）
- **权重矩阵**：神经网络中的连接权重
- **协方差矩阵**：描述特征间的相关性
- **图像**：灰度图像是 $H \times W$ 矩阵，彩色图像是 $H \times W \times 3$ 张量

---

## 矩阵运算

### 矩阵加法

$$A + B = \begin{bmatrix} a_{11}+b_{11} & a_{12}+b_{12} \\ a_{21}+b_{21} & a_{22}+b_{22} \end{bmatrix}$$

**要求：** 两个矩阵维度必须相同

**数据科学应用：** 批量数据处理的并行计算

### 矩阵乘法

$$C = AB, \quad c_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}$$

**详细解释：**
- $A$ 是 $m \times n$ 矩阵，$B$ 是 $n \times p$ 矩阵
- 结果 $C$ 是 $m \times p$ 矩阵
- $C$ 的第 $i$ 行第 $j$ 列元素 = $A$ 的第 $i$ 行 与 $B$ 的第 $j$ 列 的点积

**重要性质：**
- ❌ 不满足交换律：$AB \neq BA$（一般情况下）
- ✅ 满足结合律：$(AB)C = A(BC)$
- ✅ 满足分配律：$A(B+C) = AB + AC$

**数据科学应用：**
- **神经网络前向传播**：输入 × 权重 = 输出
- **推荐系统**：用户矩阵 × 物品矩阵 = 评分预测
- **数据变换**：原始数据 × 变换矩阵 = 新特征空间

### 转置 (Transpose)

$$A^T = \begin{bmatrix} a_{11} & a_{21} \\ a_{12} & a_{22} \end{bmatrix}$$

**性质：**
- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(AB)^T = B^T A^T$ （注意顺序反转！）

**数据科学应用：** 特征与样本的转换，如将行样本转为列样本

---

## 行列式与逆矩阵

### 行列式 (Determinant)

**几何意义：** 行列式表示线性变换对空间"体积"的缩放比例。

对于 $2 \times 2$ 矩阵：

$$\det(A) = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$$

**解释：**
- $\det(A) = 0$：矩阵不可逆，变换将空间"压扁"（降维）
- $|\det(A)| > 1$：变换扩大空间
- $|\det(A)| < 1$：变换缩小空间
- $\det(A) < 0$：变换包含"翻转"

对于 $3 \times 3$ 矩阵（按第一行展开）：

$$\det(A) = a_{11}\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} - a_{12}\begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} + a_{13}\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}$$

### 逆矩阵 (Inverse Matrix)

**定义：** 如果 $\det(A) \neq 0$，则 $A$ 可逆，存在 $A^{-1}$ 使得：

$$AA^{-1} = A^{-1}A = I$$

**计算公式：**

$$A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)$$

**性质：**
- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^T)^{-1} = (A^{-1})^T$

**数据科学应用：**
- **线性回归**：$\hat{\beta} = (X^TX)^{-1}X^Ty$（正规方程）
- **解线性方程组**：$Ax = b \Rightarrow x = A^{-1}b$
- **协方差矩阵求逆**：马氏距离计算

---

## 特征值与特征向量

### 定义

对于方阵 $A$，如果存在非零向量 $\vec{v}$ 和标量 $\lambda$ 满足：

$$A\vec{v} = \lambda\vec{v}$$

则：
- $\lambda$ 称为**特征值**（eigenvalue）
- $\vec{v}$ 称为对应的**特征向量**（eigenvector）

### 直观理解

**特征向量**是线性变换中的"不变方向"——变换后方向不变，只改变长度。

**特征值**表示在该方向上的"缩放倍数"：
- $\lambda > 1$：在该方向上拉伸
- $0 < \lambda < 1$：在该方向上压缩
- $\lambda < 0$：在该方向上反向

### 特征方程

$$\det(A - \lambda I) = 0$$

求解此方程得到特征值，再代入 $(A - \lambda I)\vec{v} = 0$ 得到特征向量。

### 数据科学应用

**1. 主成分分析 (PCA)**
- 协方差矩阵的特征向量 = 主成分方向
- 特征值 = 各主成分解释的方差
- 用于降维和特征提取

**2. 谱聚类**
- 利用拉普拉斯矩阵的特征向量进行聚类

**3. PageRank 算法**
- 网页重要性 = 转移矩阵的主特征向量

**4. 稳定性分析**
- 系统稳定 ⇔ 所有特征值的实部 < 0

---

## 向量空间与基

### 线性组合

$$\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k$$

### 线性无关

向量组 $\{\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k\}$ **线性无关**，当且仅当：

$$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k = \vec{0} \implies c_1 = c_2 = \cdots = c_k = 0$$

**直观理解：** 没有任何一个向量可以由其他向量线性表示。

### 基与维度

- **基 (Basis)**：线性无关且能张成整个空间的向量组
- **维度 (Dimension)**：基中向量的个数

**数据科学意义：**
- 特征选择：找到数据的"基"，去除冗余特征
- 维度灾难：高维空间中数据稀疏，需要降维

### 秩 (Rank)

**定义：** 矩阵的秩 = 线性无关的行（或列）的最大数量

**重要性质：**
- $\text{rank}(A) \leq \min(m, n)$
- 满秩矩阵可逆
- $\text{rank}(A) = \text{rank}(A^T)$

**数据科学应用：**
- 检测特征共线性
- 判断方程组解的存在性

---

## 奇异值分解 (SVD)

### 定义

任意 $m \times n$ 矩阵 $A$ 可以分解为：

$$A = U\Sigma V^T$$

其中：
- $U$ 是 $m \times m$ 正交矩阵（左奇异向量）
- $\Sigma$ 是 $m \times n$ 对角矩阵（奇异值，按降序排列）
- $V$ 是 $n \times n$ 正交矩阵（右奇异向量）

### 几何解释

SVD 将任意线性变换分解为三步：
1. **旋转**（$V^T$）：在输入空间旋转
2. **缩放**（$\Sigma$）：沿坐标轴缩放（奇异值）
3. **旋转**（$U$）：在输出空间旋转

### 数据科学应用

**1. 数据降维（截断 SVD）**
- 保留前 $k$ 个最大奇异值
- 近似原矩阵，但维度更低
- 比 PCA 更通用（可处理非方阵）

**2. 推荐系统（矩阵分解）**
- 用户 - 物品评分矩阵分解
- $R \approx UV^T$
- 预测缺失评分

**3. 图像压缩**
- 保留主要奇异值
- 大幅减少存储空间

**4. 潜在语义分析 (LSA)**
- 文档 - 词项矩阵的 SVD
- 发现潜在主题

**5. 去噪**
- 小奇异值通常对应噪声
- 截断后可去除噪声

---

## 数据科学应用

### 1. 线性回归

$$\hat{\beta} = (X^TX)^{-1}X^Ty$$

- $X$：设计矩阵（样本×特征）
- $y$：目标向量
- $\hat{\beta}$：回归系数

### 2. 主成分分析 (PCA)

1. 计算协方差矩阵：$\Sigma = \frac{1}{n-1}X^TX$
2. 求特征值和特征向量
3. 选择前 $k$ 个主成分
4. 投影：$Z = XV_k$

### 3. 神经网络

前向传播：
$$z^{(l)} = W^{(l)}a^{(l-1)} + b^{(l)}$$
$$a^{(l)} = \sigma(z^{(l)})$$

- $W^{(l)}$：权重矩阵
- $b^{(l)}$：偏置向量
- $\sigma$：激活函数

### 4. 相似度计算

**余弦相似度：**
$$\cos(\theta) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$$

用于推荐系统、文本相似度等。

---

## 练习题

### 练习 1：矩阵乘法

计算以下矩阵乘法：

$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$$

求 $AB$ 和 $BA$，验证是否满足交换律。

<details>
<summary>点击查看答案</summary>

$$AB = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}, \quad BA = \begin{bmatrix} 23 & 34 \\ 31 & 46 \end{bmatrix}$$

$AB \neq BA$，矩阵乘法不满足交换律。
</details>

### 练习 2：特征值计算

求矩阵 $A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$ 的特征值和特征向量。

<details>
<summary>点击查看答案</summary>

特征方程：$\det(A - \lambda I) = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10 = 0$

特征值：$\lambda_1 = 5, \lambda_2 = 2$

对应特征向量：$\vec{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$
</details>

### 练习 3：SVD 应用

使用 Python 对以下矩阵进行 SVD 分解，并用前 2 个奇异值重构：

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$$

---

## 📖 参考资料

- [3Blue1Brown - 线性代数的本质](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_abr) ⭐ 强烈推荐
- [MIT OpenCourseWare - Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/)
- 《线性代数及其应用》- Gilbert Strang
- 《深度学习》- 第 2 章 线性代数
- [线性代数 - 维基百科](https://zh.wikipedia.org/wiki/线性代数)

---

## 🔗 相关代码

- `linear_algebra.py` - Python 实现示例
- `../notebooks/01_linear_algebra.ipynb` - Jupyter Notebook 实践
