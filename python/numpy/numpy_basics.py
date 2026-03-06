#!/usr/bin/env python3
"""
NumPy 基础示例
NumPy Basics Examples

涵盖：数组创建、操作、索引、广播、数学函数
"""

import numpy as np

print("=" * 60)
print("NumPy 基础示例")
print("=" * 60)

# ============================================================
# 1. 数组创建
# ============================================================
print("\n【1. 数组创建】")

# 从列表创建
arr = np.array([1, 2, 3, 4, 5])
print(f"从列表：{arr}, 类型：{type(arr)}")

# 多维数组
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n二维数组:\n{arr_2d}")

# 特殊数组
print(f"\n特殊数组:")
print(f"zeros(3,3):\n{np.zeros((3, 3))}")
print(f"ones(2,4):\n{np.ones((2, 4))}")
print(f"eye(3):\n{np.eye(3)}")
print(f"arange(0,10,2): {np.arange(0, 10, 2)}")
print(f"linspace(0,1,5): {np.linspace(0, 1, 5)}")

# 随机数组
print(f"\n随机数组:")
print(f"rand(2,3):\n{np.random.rand(2, 3)}")
print(f"randn(2,3):\n{np.random.randn(2, 3)}")
print(f"randint(0,10,(2,3)):\n{np.random.randint(0, 10, (2, 3))}")

# 固定随机种子
np.random.seed(42)
print(f"\n固定种子 rand(3): {np.random.rand(3)}")

# ============================================================
# 2. 数组属性
# ============================================================
print("\n【2. 数组属性】")

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"数组:\n{arr}")
print(f"shape: {arr.shape}")
print(f"ndim: {arr.ndim}")
print(f"size: {arr.size}")
print(f"dtype: {arr.dtype}")
print(f"itemsize: {arr.itemsize} bytes")

# ============================================================
# 3. 索引与切片
# ============================================================
print("\n【3. 索引与切片】")

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"数组:\n{arr}")

print(f"\n索引:")
print(f"arr[0, 1] = {arr[0, 1]}")
print(f"arr[2, 2] = {arr[2, 2]}")

print(f"\n切片:")
print(f"arr[:, 1] (第二列) = {arr[:, 1]}")
print(f"arr[1, :] (第二行) = {arr[1, :]}")
print(f"arr[:2, :2]:\n{arr[:2, :2]}")

# 布尔索引
print(f"\n布尔索引:")
print(f"arr > 5: {arr[arr > 5]}")
print(f"arr[arr % 2 == 0]: {arr[arr % 2 == 0]}")

# 花式索引
print(f"\n花式索引:")
print(f"arr[[0, 2], [1, 2]] = {arr[[0, 2], [1, 2]]}")

# ============================================================
# 4. 数组操作
# ============================================================
print("\n【4. 数组操作】")

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"原数组:\n{arr}")

# 重塑
print(f"\nreshape(3,2):\n{arr.reshape(3, 2)}")

# 转置
print(f"\n转置 arr.T:\n{arr.T}")

# 展平
print(f"\nflatten(): {arr.flatten()}")
print(f"ravel(): {arr.ravel()}")

# 拼接
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(f"\n拼接:")
print(f"arr1:\n{arr1}")
print(f"arr2:\n{arr2}")
print(f"concatenate axis=0:\n{np.concatenate([arr1, arr2], axis=0)}")
print(f"vstack:\n{np.vstack([arr1, arr2])}")
print(f"hstack:\n{np.hstack([arr1, arr2])}")

# 分割
arr_big = np.arange(12).reshape(3, 4)
print(f"\n分割 3x4 数组:")
print(f"split axis=0:\n{np.split(arr_big, 3, axis=0)}")

# ============================================================
# 5. 广播机制
# ============================================================
print("\n【5. 广播机制】")

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"数组:\n{arr}")

# 标量广播
print(f"\narr + 10:\n{arr + 10}")
print(f"arr * 2:\n{arr * 2}")

# 数组广播
row = np.array([10, 20, 30])
print(f"\nrow = {row}")
print(f"arr + row:\n{arr + row}")

col = np.array([[10], [20]])
print(f"\ncol = {col.T}")
print(f"arr + col:\n{arr + col}")

# ============================================================
# 6. 数学函数
# ============================================================
print("\n【6. 数学函数】")

arr = np.array([1, 4, 9, 16, 25])
print(f"数组：{arr}")

print(f"\n数学函数:")
print(f"sqrt: {np.sqrt(arr)}")
print(f"exp: {np.exp(arr/10)}")
print(f"log: {np.log(arr)}")
print(f"sin: {np.sin(arr * np.pi / 180)}")  # 角度转弧度

# 舍入
arr_float = np.array([1.234, 2.567, 3.891])
print(f"\n舍入 {arr_float}:")
print(f"round(2): {np.round(arr_float, 2)}")
print(f"floor: {np.floor(arr_float)}")
print(f"ceil: {np.ceil(arr_float)}")

# ============================================================
# 7. 统计函数
# ============================================================
print("\n【7. 统计函数】")

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"数组:\n{arr}")

print(f"\n整体统计:")
print(f"mean: {arr.mean()}")
print(f"std: {arr.std():.4f}")
print(f"var: {arr.var()}")
print(f"sum: {arr.sum()}")
print(f"min: {arr.min()}")
print(f"max: {arr.max()}")
print(f"median: {np.median(arr)}")

print(f"\n按轴统计:")
print(f"mean axis=0 (列): {arr.mean(axis=0)}")
print(f"mean axis=1 (行): {arr.mean(axis=1)}")
print(f"sum axis=0: {arr.sum(axis=0)}")

# 百分位数
print(f"\npercentile 75%: {np.percentile(arr, 75)}")

# ============================================================
# 8. 线性代数
# ============================================================
print("\n【8. 线性代数】")

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"A:\n{A}")
print(f"B:\n{B}")

print(f"\n矩阵运算:")
print(f"A @ B:\n{A @ B}")
print(f"np.dot(A, B):\n{np.dot(A, B)}")
print(f"A.T:\n{A.T}")

# 逆矩阵
print(f"\n逆矩阵 A⁻¹:\n{np.linalg.inv(A)}")

# 行列式
print(f"det(A) = {np.linalg.det(A):.4f}")

# 特征值
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"\n特征值：{eigenvalues}")
print(f"特征向量:\n{eigenvectors}")

# 解线性方程组
# 2x + 3y = 8
# 5x + 4y = 13
A_sys = np.array([[2, 3], [5, 4]])
b = np.array([8, 13])
x = np.linalg.solve(A_sys, b)
print(f"\n解方程组 2x+3y=8, 5x+4y=13:")
print(f"x = {x}")
print(f"验证：A·x = {A_sys @ x}")

# ============================================================
# 9. 练习解答
# ============================================================
print("\n【9. 练习解答】")

# 练习 1：5x5 数组，值为 1-25
arr_5x5 = np.arange(1, 26).reshape(5, 5)
print(f"\n练习 1：5x5 数组 (1-25)")
print(arr_5x5)
print(f"每行的和：{arr_5x5.sum(axis=1)}")
print(f"每列的和：{arr_5x5.sum(axis=0)}")

# 练习 2：10x10 随机整数，找大于 50 的元素位置
np.random.seed(42)
arr_10x10 = np.random.randint(0, 101, (10, 10))
positions = np.where(arr_10x10 > 50)
print(f"\n练习 2：10x10 随机数组中 >50 的元素位置")
print(f"共 {len(positions[0])} 个元素")
print(f"位置 (行，列): {list(zip(positions[0][:10], positions[1][:10]))}...")

# 练习 3：矩阵乘法（不使用 np.dot）
def matrix_multiply(A, B):
    """手动实现矩阵乘法"""
    m, n = A.shape
    n2, p = B.shape
    if n != n2:
        raise ValueError("维度不匹配")
    
    result = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i, j] += A[i, k] * B[k, j]
    return result

A_test = np.array([[1, 2], [3, 4]])
B_test = np.array([[5, 6], [7, 8]])
manual_result = matrix_multiply(A_test, B_test)
numpy_result = A_test @ B_test

print(f"\n练习 3：矩阵乘法验证")
print(f"手动实现:\n{manual_result}")
print(f"NumPy 实现:\n{numpy_result}")
print(f"结果一致：{np.allclose(manual_result, numpy_result)}")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)
