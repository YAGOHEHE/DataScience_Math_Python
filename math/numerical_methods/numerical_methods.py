#!/usr/bin/env python3
"""
数值方法 Python 示例
Numerical Methods Examples

涵盖：方程求根、数值积分、数值微分、线性方程组
"""

import numpy as np
from scipy import integrate, optimize
import matplotlib.pyplot as plt

print("=" * 60)
print("数值方法 Python 示例")
print("=" * 60)

# ============================================================
# 1. 误差分析
# ============================================================
print("\n【1. 误差分析】")

true_value = np.pi
approx_value = 3.14159

abs_error = abs(true_value - approx_value)
rel_error = abs_error / abs(true_value)

print(f"真值：π = {true_value:.15f}")
print(f"近似值：{approx_value}")
print(f"绝对误差：{abs_error:.15f}")
print(f"相对误差：{rel_error:.10f} ({rel_error*100:.6f}%)")

# 浮点数精度问题
print(f"\n浮点数精度示例:")
print(f"  0.1 + 0.2 = {0.1 + 0.2}")
print(f"  0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")
print(f"  使用 np.isclose: {np.isclose(0.1 + 0.2, 0.3)}")

# ============================================================
# 2. 方程求根 - 二分法
# ============================================================
print("\n【2. 方程求根 - 二分法】")

def bisection(f, a, b, tol=1e-8, max_iter=100):
    """二分法求根"""
    if f(a) * f(b) > 0:
        raise ValueError("f(a) 和 f(b) 必须异号")
    
    print(f"初始区间：[{a}, {b}]")
    print(f"f({a}) = {f(a):.6f}, f({b}) = {f(b):.6f}")
    print("\n迭代过程:")
    
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        
        print(f"  迭代 {i+1}: [{a:.6f}, {b:.6f}], c = {c:.8f}, f(c) = {fc:.8f}")
        
        if abs(fc) < tol or (b - a) / 2 < tol:
            print(f"\n  在迭代 {i+1} 收敛")
            return c, i+1
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    return c, max_iter

# 求解 f(x) = x³ - x - 2 = 0
def f_bisect(x):
    return x**3 - x - 2

root, iterations = bisection(f_bisect, 1, 2)
print(f"\n二分法结果：x ≈ {root:.10f}")
print(f"验证：f({root:.6f}) = {f_bisect(root):.10f}")

# 使用 scipy 验证
root_scipy = optimize.brentq(f_bisect, 1, 2)
print(f"SciPy 验证：x = {root_scipy:.10f}")

# ============================================================
# 3. 方程求根 - 牛顿法
# ============================================================
print("\n【3. 方程求根 - 牛顿法】")

def newton_raphson(f, df, x0, tol=1e-10, max_iter=20):
    """牛顿法求根"""
    x = x0
    print(f"初始值：x₀ = {x0}")
    print("\n迭代过程:")
    
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-15:
            print("  导数接近零，停止")
            break
        
        x_new = x - fx / dfx
        print(f"  迭代 {i+1}: x = {x_new:.10f}, f(x) = {f(x_new):.10f}")
        
        if abs(x_new - x) < tol:
            print(f"\n  在迭代 {i+1} 收敛")
            return x_new, i+1
        
        x = x_new
    
    return x, max_iter

def df_bisect(x):
    return 3*x**2 - 1

root_newton, iters_newton = newton_raphson(f_bisect, df_bisect, 1.5)
print(f"\n牛顿法结果：x ≈ {root_newton:.10f} (迭代 {iters_newton} 次)")
print(f"二分法迭代次数对比：{iterations} 次")
print(f"牛顿法收敛更快 ✓")

# ============================================================
# 4. 数值积分
# ============================================================
print("\n【4. 数值积分】")

def trapezoidal(f, a, b, n):
    """复合梯形法则"""
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h * (y[0]/2 + np.sum(y[1:-1]) + y[-1]/2)

def simpson(f, a, b, n):
    """复合辛普森法则 (n 必须为偶数)"""
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h/3 * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])

# 积分：∫₀¹ e^(-x²) dx
def integrand(x):
    return np.exp(-x**2)

a, b = 0, 1
exact = 0.7468241328124271  # 误差函数值

print(f"计算 ∫₀¹ e^(-x²) dx")
print(f"精确值：{exact:.12f}")

for n in [2, 4, 8, 16, 32]:
    trap = trapezoidal(integrand, a, b, n)
    simp = simpson(integrand, a, b, n)
    print(f"\nn = {n}:")
    print(f"  梯形法则：{trap:.12f}, 误差：{abs(trap - exact):.2e}")
    print(f"  辛普森法：{simp:.12f}, 误差：{abs(simp - exact):.2e}")

# 使用 SciPy
scipy_result, scipy_error = integrate.quad(integrand, 0, 1)
print(f"\nSciPy quad: {scipy_result:.12f} (估计误差：{scipy_error:.2e})")

# ============================================================
# 5. 数值微分
# ============================================================
print("\n【5. 数值微分】")

def forward_diff(f, x, h):
    """前向差分"""
    return (f(x + h) - f(x)) / h

def central_diff(f, x, h):
    """中心差分"""
    return (f(x + h) - f(x - h)) / (2 * h)

# 测试：f(x) = sin(x), f'(x) = cos(x)
def f_diff(x):
    return np.sin(x)

def df_exact(x):
    return np.cos(x)

x0 = np.pi / 4
exact_deriv = df_exact(x0)

print(f"计算 f(x) = sin(x) 在 x = π/4 处的导数")
print(f"精确值：cos(π/4) = {exact_deriv:.12f}")

for h in [0.1, 0.01, 0.001, 0.0001]:
    fwd = forward_diff(f_diff, x0, h)
    ctr = central_diff(f_diff, x0, h)
    print(f"\nh = {h}:")
    print(f"  前向差分：{fwd:.12f}, 误差：{abs(fwd - exact_deriv):.2e}")
    print(f"  中心差分：{ctr:.12f}, 误差：{abs(ctr - exact_deriv):.2e}")

print(f"\n中心差分精度更高（O(h²) vs O(h)）✓")

# ============================================================
# 6. 线性方程组求解
# ============================================================
print("\n【6. 线性方程组求解】")

# 方程组：
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3

A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

b = np.array([8, -11, -3])

print("求解 Ax = b:")
print(f"A = \n{A}")
print(f"b = {b}")

# 方法 1：直接求解
x_direct = np.linalg.solve(A, b)
print(f"\n直接求解：x = {x_direct}")
print(f"验证 Ax = {A @ x_direct}")

# 方法 2：LU 分解
from scipy.linalg import lu
P, L, U = lu(A)
print(f"\nLU 分解:")
print(f"L = \n{L}")
print(f"U = \n{U}")

# 方法 3：迭代法（雅可比）
def jacobi(A, b, x0, max_iter=100, tol=1e-8):
    """雅可比迭代"""
    x = x0.copy()
    n = len(b)
    
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        
        if np.linalg.norm(x_new - x) < tol:
            return x_new, k+1
        x = x_new
    
    return x, max_iter

x0_jac = [0, 0, 0]
x_jac, iters_jac = jacobi(A, b, x0_jac)
print(f"\n雅可比迭代：x = {x_jac} (迭代 {iters_jac} 次)")

# ============================================================
# 7. 练习解答
# ============================================================
print("\n【7. 练习题解答】")

print("\n练习 1：二分法求根")
print(f"f(x) = x³ - x - 2 = 0 在 [1,2] 内的根")
print(f"结果：x ≈ {root:.8f}")

print("\n练习 2：数值积分")
print(f"∫₀¹ e^(-x²) dx ≈ {simpson(integrand, 0, 1, 100):.10f}")
print(f"精确值：{exact:.10f}")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)
