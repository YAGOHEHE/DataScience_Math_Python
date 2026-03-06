#!/usr/bin/env python3
"""
优化方法 Python 示例
Optimization Examples

涵盖：梯度下降、牛顿法、约束优化、线性规划
"""

import numpy as np
from scipy.optimize import minimize, linprog
import sympy as sp

print("=" * 60)
print("优化方法 Python 示例")
print("=" * 60)

# ============================================================
# 1. 无约束优化 - 梯度下降
# ============================================================
print("\n【1. 梯度下降法】")

def gradient_descent(f, grad_f, x0, alpha=0.01, max_iter=100, tol=1e-6):
    """梯度下降法"""
    x = np.array(x0, dtype=float)
    history = [x.copy()]
    
    for i in range(max_iter):
        g = grad_f(x)
        if np.linalg.norm(g) < tol:
            print(f"  在迭代 {i} 收敛")
            break
        x = x - alpha * g
        history.append(x.copy())
    
    return x, f(x), history

# 测试函数：f(x) = x^4 - 4x^2
def f1(x):
    return x[0]**4 - 4*x[0]**2

def grad_f1(x):
    return np.array([4*x[0]**3 - 8*x[0]])

x0 = [3.0]
result, fval, history = gradient_descent(f1, grad_f1, x0, alpha=0.05, max_iter=50)

print(f"目标函数：f(x) = x⁴ - 4x²")
print(f"初始点：x₀ = {x0[0]}")
print(f"优化结果：x* = {result[0]:.6f}")
print(f"最小值：f(x*) = {fval:.6f}")
print(f"理论最小值：x = ±√2 ≈ ±1.414, f = -4")

# ============================================================
# 2. 牛顿法
# ============================================================
print("\n【2. 牛顿法】")

def newton_method(f, grad_f, hess_f, x0, max_iter=20, tol=1e-8):
    """牛顿法"""
    x = np.array(x0, dtype=float)
    
    print(f"初始点：x₀ = {x}")
    
    for i in range(max_iter):
        g = grad_f(x)
        H = hess_f(x)
        
        if np.linalg.norm(g) < tol:
            print(f"  在迭代 {i} 收敛")
            break
        
        # 牛顿步
        try:
            delta = np.linalg.solve(H, g)
            x = x - delta
            print(f"  迭代 {i+1}: x = {x}, f(x) = {f(x):.6f}")
        except np.linalg.LinAlgError:
            print("  黑塞矩阵奇异，无法继续")
            break
    
    return x, f(x)

# 测试函数：f(x) = x^4 - 4x^2
def hess_f1(x):
    return np.array([[12*x[0]**2 - 8]])

x0_newton = [3.0]
result_n, fval_n = newton_method(f1, grad_f1, hess_f1, x0_newton)

print(f"\n牛顿法结果：x* = {result_n[0]:.6f}, f(x*) = {fval_n:.6f}")

# ============================================================
# 3. 使用 scipy.optimize
# ============================================================
print("\n【3. 使用 SciPy 优化】")

# 多元函数优化
def rosenbrock(x):
    """Rosenbrock 函数"""
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

x0_rosen = [0, 0]
result_rosen = minimize(rosenbrock, x0_rosen, method='BFGS')

print(f"Rosenbrock 函数：f(x,y) = (1-x)² + 100(y-x²)²")
print(f"初始点：{x0_rosen}")
print(f"优化结果：{result_rosen.x}")
print(f"最小值：{result_rosen.fun:.6f}")
print(f"理论最小值：(1, 1), f = 0")
print(f"成功：{result_rosen.success}")

# ============================================================
# 4. 约束优化 - 拉格朗日乘数法
# ============================================================
print("\n【4. 约束优化】")

# 符号计算拉格朗日乘数法
x, y, lam = sp.symbols('x y lambda')

# 问题：min x² + y² s.t. x + y = 1
f_obj = x**2 + y**2
g_constraint = x + y - 1

# 拉格朗日函数
L = f_obj + lam * g_constraint

# KKT 条件
eq1 = sp.diff(L, x)
eq2 = sp.diff(L, y)
eq3 = sp.diff(L, lam)

print(f"问题：min f(x,y) = x² + y², s.t. x + y = 1")
print(f"\n拉格朗日函数：L = {L}")
print(f"\nKKT 方程组:")
print(f"  ∂L/∂x = {eq1} = 0")
print(f"  ∂L/∂y = {eq2} = 0")
print(f"  ∂L/∂λ = {eq3} = 0")

# 求解
solution = sp.solve([eq1, eq2, eq3], [x, y, lam])
print(f"\n解：{solution}")

# 使用 scipy 求解约束优化
def f_constr(x):
    return x[0]**2 + x[1]**2

def constraint_eq(x):
    return x[0] + x[1] - 1

cons = {'type': 'eq', 'fun': constraint_eq}
result_constr = minimize(f_constr, [0, 0], method='SLSQP', constraints=cons)

print(f"\nSciPy 数值解：x = {result_constr.x}")
print(f"最小值：f(x) = {result_constr.fun:.6f}")

# ============================================================
# 5. 线性规划
# ============================================================
print("\n【5. 线性规划】")

# 问题：max 3x + 2y
# s.t. 2x + y ≤ 100
#      x + y ≤ 80
#      x ≤ 40
#      x, y ≥ 0

# scipy.linprog 求解最小化问题，所以目标函数取负
c = [-3, -2]  # 最大化 3x + 2y

A = [
    [2, 1],   # 2x + y ≤ 100
    [1, 1],   # x + y ≤ 80
    [1, 0]    # x ≤ 40
]
b = [100, 80, 40]

# 变量边界
x_bounds = (0, None)
y_bounds = (0, None)

result_lp = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

print(f"问题：max 3x + 2y")
print(f"约束:")
print(f"  2x + y ≤ 100")
print(f"  x + y ≤ 80")
print(f"  x ≤ 40")
print(f"  x, y ≥ 0")
print(f"\n最优解：x = {result_lp.x[0]:.2f}, y = {result_lp.x[1]:.2f}")
print(f"最大值：{-result_lp.fun:.2f}")

# ============================================================
# 6. 凸优化示例
# ============================================================
print("\n【6. 凸优化示例】")

# 最小二乘问题是凸优化
# min ||Ax - b||²

np.random.seed(42)
A = np.random.randn(10, 5)
b = np.random.randn(10)

def least_squares(x):
    return np.sum((A @ x - b)**2)

def grad_ls(x):
    return 2 * A.T @ (A @ x - b)

x0_ls = np.zeros(5)
result_ls, fval_ls, _ = gradient_descent(least_squares, grad_ls, x0_ls, alpha=0.01, max_iter=500)

# 解析解：x = (A^T A)^(-1) A^T b
x_analytic = np.linalg.lstsq(A, b, rcond=None)[0]

print(f"最小二乘问题：min ||Ax - b||²")
print(f"A: {A.shape}, b: {b.shape}")
print(f"\n梯度下降解：{result_ls}")
print(f"解析解：    {x_analytic}")
print(f"误差：{np.linalg.norm(result_ls - x_analytic):.10f}")

# ============================================================
# 7. 练习解答
# ============================================================
print("\n【7. 练习题解答】")

print("\n练习 1：梯度下降求 f(x) = x⁴ - 4x² 最小值")
print(f"结果：x* ≈ {result[0]:.4f}, f(x*) ≈ {fval:.4f}")
print(f"理论值：x = ±√2 ≈ ±1.414, f = -4")

print("\n练习 2：拉格朗日乘数法")
print(f"min x² + y² s.t. x + y = 1")
print(f"解：x = y = 0.5, 最小值 = 0.5")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)
