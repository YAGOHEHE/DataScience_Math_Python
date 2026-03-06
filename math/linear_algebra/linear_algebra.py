#!/usr/bin/env python3
"""
线性代数 Python 示例
Linear Algebra Examples with NumPy

涵盖：向量运算、矩阵运算、行列式、特征值、SVD
"""

import numpy as np
from numpy.linalg import det, inv, eig, svd, norm

print("=" * 60)
print("线性代数 Python 示例")
print("=" * 60)

# ============================================================
# 1. 向量运算
# ============================================================
print("\n【1. 向量运算】")

# 创建向量
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(f"向量 v1 = {v1}")
print(f"向量 v2 = {v2}")

# 向量加法
print(f"\nv1 + v2 = {v1 + v2}")

# 向量点积（内积）
dot_product = np.dot(v1, v2)
print(f"v1 · v2 (点积) = {dot_product}")
# 公式：v1·v2 = 1*4 + 2*5 + 3*6 = 32

# 向量的模（长度）
v1_norm = norm(v1)
print(f"||v1|| (模) = {v1_norm:.4f}")
# 公式：sqrt(1² + 2² + 3²) = sqrt(14)

# 单位向量
v1_unit = v1 / v1_norm
print(f"v1 的单位向量 = {v1_unit}")
print(f"验证单位向量模长：{norm(v1_unit):.4f}")

# ============================================================
# 2. 矩阵运算
# ============================================================
print("\n【2. 矩阵运算】")

# 创建矩阵
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print(f"矩阵 A:\n{A}")
print(f"\n矩阵 B:\n{B}")

# 矩阵加法
print(f"\nA + B:\n{A + B}")

# 矩阵乘法
AB = np.dot(A, B)
BA = np.dot(B, A)
print(f"\nA × B:\n{AB}")
print(f"\nB × A:\n{BA}")
print(f"AB == BA? {np.array_equal(AB, BA)} (矩阵乘法不满足交换律)")

# 矩阵转置
print(f"\nA 的转置 A^T:\n{A.T}")

# 标量乘法
print(f"\n2 × A:\n{2 * A}")

# ============================================================
# 3. 行列式与逆矩阵
# ============================================================
print("\n【3. 行列式与逆矩阵】")

# 行列式
det_A = det(A)
print(f"det(A) = {det_A}")
# 公式：det(A) = 1*4 - 2*3 = -2

# 逆矩阵
if det_A != 0:
    A_inv = inv(A)
    print(f"\nA 的逆矩阵 A⁻¹:\n{A_inv}")
    
    # 验证：A × A⁻¹ = I
    identity = np.dot(A, A_inv)
    print(f"\n验证 A × A⁻¹:\n{identity}")
    print(f"是否等于单位矩阵？\n{np.allclose(identity, np.eye(2))}")

# ============================================================
# 4. 特征值与特征向量
# ============================================================
print("\n【4. 特征值与特征向量】")

# 计算特征值和特征向量
eigenvalues, eigenvectors = eig(A)

print(f"矩阵 A 的特征值：{eigenvalues}")
print(f"\n矩阵 A 的特征向量:\n{eigenvectors}")

# 验证：Av = λv
print("\n验证特征值方程 Av = λv:")
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lam = eigenvalues[i]
    Av = np.dot(A, v)
    lam_v = lam * v
    print(f"\n特征值 λ{i+1} = {lam:.4f}")
    print(f"A·v{i+1} = {Av}")
    print(f"λ{i+1}·v{i+1} = {lam_v}")
    print(f"验证：{np.allclose(Av, lam_v)}")

# ============================================================
# 5. 奇异值分解 (SVD)
# ============================================================
print("\n【5. 奇异值分解 (SVD)】")

# 创建示例矩阵
C = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(f"矩阵 C:\n{C}")

# SVD 分解
U, S, Vt = svd(C)

print(f"\nU 矩阵 (左奇异向量):\n{U}")
print(f"\n奇异值 Σ: {S}")
print(f"\nV^T 矩阵 (右奇异向量的转置):\n{Vt}")

# 重构矩阵
Sigma = np.zeros_like(C, dtype=float)
np.fill_diagonal(Sigma, S)
C_reconstructed = np.dot(U, np.dot(Sigma, Vt))

print(f"\n重构矩阵 C' = U·Σ·V^T:\n{C_reconstructed}")
print(f"重构误差：{np.max(np.abs(C - C_reconstructed)):.10f}")

# ============================================================
# 6. 线性方程组求解
# ============================================================
print("\n【6. 线性方程组求解】")

# Ax = b
# 2x + 3y = 8
# 5x + 4y = 13

A_sys = np.array([[2, 3],
                  [5, 4]])
b = np.array([8, 13])

print(f"求解方程组 Ax = b")
print(f"A = \n{A_sys}")
print(f"b = {b}")

# 方法 1：使用逆矩阵
x1 = np.dot(inv(A_sys), b)
print(f"\n方法 1 - 使用逆矩阵：x = {x1}")

# 方法 2：使用 solve (推荐)
x2 = np.linalg.solve(A_sys, b)
print(f"方法 2 - 使用 solve: x = {x2}")

# 验证
print(f"验证：A·x = {np.dot(A_sys, x2)}")

# ============================================================
# 7. 练习解答
# ============================================================
print("\n【7. 练习题解答】")

print("\n练习 1：矩阵乘法验证")
print(f"AB = \n{AB}")
print(f"BA = \n{BA}")
print(f"AB ≠ BA，矩阵乘法不满足交换律 ✓")

print("\n练习 2：特征值计算")
A_ex = np.array([[4, 1],
                 [2, 3]])
eigvals, eigvecs = eig(A_ex)
print(f"矩阵 [[4,1],[2,3]] 的特征值：{eigvals}")
print(f"特征向量:\n{eigvecs}")

print("\n练习 3：SVD 分解")
A_svd = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
U_ex, S_ex, Vt_ex = svd(A_svd)
print(f"奇异值：{S_ex}")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)
