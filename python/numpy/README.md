# NumPy 基础 NumPy Basics 🔢

NumPy 是 Python 科学计算的基础库，提供高效的多维数组操作。

## 📚 目录

1. [数组创建](#数组创建)
2. [数组操作](#数组操作)
3. [索引与切片](#索引与切片)
4. [广播机制](#广播机制)
5. [数学函数](#数学函数)
6. [练习题](#练习题)

---

## 数组创建

```python
import numpy as np

# 从列表创建
arr = np.array([1, 2, 3, 4, 5])

# 特殊数组
np.zeros((3, 3))      # 全零数组
np.ones((2, 4))       # 全一数组
np.eye(3)             # 单位矩阵
np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]

# 随机数组
np.random.rand(3, 3)           # [0,1) 均匀分布
np.random.randn(3, 3)          # 标准正态分布
np.random.randint(0, 10, (3,3)) # 随机整数
```

---

## 数组操作

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.shape      # (2, 3)
arr.ndim       # 2
arr.size       # 6
arr.dtype      # int64

# 重塑
arr.reshape(3, 2)

# 转置
arr.T

# 展平
arr.flatten()
arr.ravel()

# 拼接
np.concatenate([arr1, arr2], axis=0)
np.vstack([arr1, arr2])
np.hstack([arr1, arr2])
```

---

## 索引与切片

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr[0, 1]      # 2
arr[:, 1]      # [2, 5, 8] - 第二列
arr[1, :]      # [4, 5, 6] - 第二行
arr[:2, :2]    # [[1, 2], [4, 5]]

# 布尔索引
arr[arr > 5]   # [6, 7, 8, 9]

# 花式索引
arr[[0, 2], [1, 2]]  # [2, 9]
```

---

## 广播机制

```python
# 标量广播
arr + 10

# 数组广播
arr = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
arr + row  # [[11, 22, 33], [14, 25, 36]]
```

---

## 数学函数

```python
arr = np.array([1, 4, 9, 16])

np.sqrt(arr)      # [1, 2, 3, 4]
np.exp(arr)       # e^x
np.log(arr)       # ln(x)
np.sin(arr)       # sin(x)

# 统计函数
arr.mean()
arr.std()
arr.sum()
arr.min()
arr.max()
np.median(arr)
np.percentile(arr, 75)
```

---

## 练习题

### 练习 1：数组操作

创建一个 5x5 的数组，值为 1-25，计算每行、每列的和。

### 练习 2：布尔索引

创建一个 10x10 的随机整数数组 (0-100)，找出所有大于 50 的元素位置。

### 练习 3：矩阵运算

实现矩阵乘法（不使用 `np.dot`），验证结果。

---

## 📖 参考资料

- [NumPy 官方文档](https://numpy.org/doc/)
- [NumPy 快速入门](https://numpy.org/doc/stable/user/quickstart.html)
- 《Python 数据科学手册》- Jake VanderPlas

## 🔗 相关代码

- `numpy_basics.py` - 示例代码
