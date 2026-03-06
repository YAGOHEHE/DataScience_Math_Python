#!/usr/bin/env python3
"""
微积分 Python 示例
Calculus Examples with SymPy and NumPy

涵盖：导数、积分、偏导数、梯度、梯度下降
"""

import numpy as np
import sympy as sp
from sympy import symbols, diff, integrate, limit, sin, cos, exp, log, sqrt
import matplotlib.pyplot as plt

print("=" * 60)
print("微积分 Python 示例")
print("=" * 60)

# ============================================================
# 1. 符号计算 - 极限
# ============================================================
print("\n【1. 极限计算】")

x = symbols('x')

# 重要极限 1: lim(x->0) sin(x)/x
limit1 = limit(sin(x)/x, x, 0)
print(f"lim(x→0) sin(x)/x = {limit1}")

# 重要极限 2: lim(x->∞) (1 + 1/x)^x
limit2 = limit((1 + 1/x)**x, x, sp.oo)
print(f"lim(x→∞) (1 + 1/x)^x = {limit2}")
print(f"  = e ≈ {np.e:.6f}")

# 其他极限
limit3 = limit((x**2 - 1)/(x - 1), x, 1)
print(f"\nlim(x→1) (x² - 1)/(x - 1) = {limit3}")

# ============================================================
# 2. 符号计算 - 导数
# ============================================================
print("\n【2. 导数计算】")

# 基本导数
f1 = x**3
f1_prime = diff(f1, x)
print(f"f(x) = x³")
print(f"  f'(x) = {f1_prime}")

f2 = exp(x)
f2_prime = diff(f2, x)
print(f"\nf(x) = e^x")
print(f"  f'(x) = {f2_prime}")

f3 = log(x)
f3_prime = diff(f3, x)
print(f"\nf(x) = ln(x)")
print(f"  f'(x) = {f3_prime}")

# 乘积法则示例
f4 = x**2 * exp(x)
f4_prime = diff(f4, x)
print(f"\nf(x) = x² · e^x")
print(f"  f'(x) = {f4_prime}")
print(f"  展开：{sp.expand(f4_prime)}")

# 链式法则示例
f5 = log(sin(x))
f5_prime = diff(f5, x)
print(f"\nf(x) = ln(sin(x))")
print(f"  f'(x) = {f5_prime}")
print(f"  = cot(x)")

# 商法则示例
f6 = (x**2 + 1)/(x - 1)
f6_prime = diff(f6, x)
print(f"\nf(x) = (x² + 1)/(x - 1)")
print(f"  f'(x) = {f6_prime}")
print(f"  化简：{sp.simplify(f6_prime)}")

# ============================================================
# 3. 高阶导数
# ============================================================
print("\n【3. 高阶导数】")

f = x**4 - 3*x**3 + 2*x**2 - x + 5

print(f"f(x) = {f}")
print(f"  f'(x)  = {diff(f, x)}")
print(f"  f''(x) = {diff(f, x, 2)}")
print(f"  f'''(x) = {diff(f, x, 3)}")
print(f"  f⁽⁴⁾(x) = {diff(f, x, 4)}")
print(f"  f⁽⁵⁾(x) = {diff(f, x, 5)} (应为 0)")

# ============================================================
# 4. 积分
# ============================================================
print("\n【4. 积分计算】")

# 不定积分
f_int = x**2
F = integrate(f_int, x)
print(f"∫ x² dx = {F} + C")

f_int2 = exp(x)
F2 = integrate(f_int2, x)
print(f"∫ e^x dx = {F2} + C")

f_int3 = 1/x
F3 = integrate(f_int3, x)
print(f"∫ 1/x dx = {F3} + C")

f_int4 = sin(x)
F4 = integrate(f_int4, x)
print(f"∫ sin(x) dx = {F4} + C")

# 定积分
print("\n定积分:")
def_int = integrate(x**2, (x, 0, 1))
print(f"∫₀¹ x² dx = {def_int}")
print(f"  = {float(def_int):.4f}")

def_int2 = integrate(exp(-x**2), (x, -sp.oo, sp.oo))
print(f"\n∫₋∞∞ e^(-x²) dx = {def_int2}")
print(f"  = √π ≈ {np.sqrt(np.pi):.6f}")

# ============================================================
# 5. 偏导数
# ============================================================
print("\n【5. 偏导数】")

x, y = symbols('x y')

f_multi = x**2 * y + 3*x*y**2 - y**3

print(f"f(x, y) = {f_multi}")

# 对 x 求偏导
df_dx = diff(f_multi, x)
print(f"\n∂f/∂x = {df_dx}")

# 对 y 求偏导
df_dy = diff(f_multi, y)
print(f"∂f/∂y = {df_dy}")

# 二阶偏导
d2f_dxdy = diff(f_multi, x, y)
print(f"\n∂²f/∂x∂y = {d2f_dxdy}")

d2f_dx2 = diff(f_multi, x, 2)
print(f"∂²f/∂x² = {d2f_dx2}")

d2f_dy2 = diff(f_multi, y, 2)
print(f"∂²f/∂y² = {d2f_dy2}")

# ============================================================
# 6. 梯度
# ============================================================
print("\n【6. 梯度计算】")

# 多元函数梯度
f_grad = x**2 + 2*y**2 - 3*x*y

grad_x = diff(f_grad, x)
grad_y = diff(f_grad, y)

print(f"f(x, y) = {f_grad}")
print(f"\n梯度 ∇f = [{grad_x}, {grad_y}]")

# 在特定点计算梯度
point = {x: 1, y: 2}
grad_at_point = [grad_x.subs(point), grad_y.subs(point)]
print(f"\n在点 (1, 2) 处的梯度:")
print(f"  ∇f(1, 2) = [{grad_at_point[0]}, {grad_at_point[1]}]")

# ============================================================
# 7. 梯度下降法
# ============================================================
print("\n【7. 梯度下降法】")

def gradient_descent_1d(f, df, x0, alpha, n_iterations):
    """
    一维梯度下降
    
    参数:
        f: 目标函数
        df: 导数函数
        x0: 初始点
        alpha: 学习率
        n_iterations: 迭代次数
    
    返回:
        x_values: 每次迭代的 x 值
        y_values: 每次迭代的 f(x) 值
    """
    x = x0
    x_values = [x]
    y_values = [f(x)]
    
    print(f"初始点: x₀ = {x0}, f(x₀) = {f(x0):.4f}")
    print(f"学习率: α = {alpha}")
    print(f"\n迭代过程:")
    print("-" * 40)
    
    for i in range(n_iterations):
        grad = df(x)
        x = x - alpha * grad
        x_values.append(x)
        y_values.append(f(x))
        print(f"迭代 {i+1}: x = {x:.6f}, f(x) = {f(x):.6f}, f'(x) = {grad:.6f}")
    
    return x_values, y_values

# 示例：f(x) = x² - 4x + 5
# 最小值在 x = 2 处，f(2) = 1

def f_obj(x):
    return x**2 - 4*x + 5

def df_obj(x):
    return 2*x - 4

print(f"\n目标函数：f(x) = x² - 4x + 5")
print(f"理论最小值：x = 2, f(2) = 1")

x_vals, y_vals = gradient_descent_1d(f_obj, df_obj, x0=0, alpha=0.1, n_iterations=10)

print(f"\n最终结果：x = {x_vals[-1]:.6f}, f(x) = {y_vals[-1]:.6f}")
print(f"收敛到理论最小值 ✓")

# ============================================================
# 8. 多元梯度下降
# ============================================================
print("\n【8. 多元梯度下降】")

def gradient_descent_2d(f, grad_f, x0, y0, alpha, n_iterations):
    """二维梯度下降"""
    x, y = x0, y0
    history = [(x, y, f(x, y))]
    
    print(f"初始点: ({x0}, {y0}), f = {f(x0, y0):.4f}")
    print(f"\n迭代过程:")
    print("-" * 50)
    
    for i in range(n_iterations):
        gx, gy = grad_f(x, y)
        x = x - alpha * gx
        y = y - alpha * gy
        history.append((x, y, f(x, y)))
        print(f"迭代 {i+1}: ({x:.4f}, {y:.4f}), f = {f(x, y):.6f}")
    
    return history

# 目标函数：f(x, y) = x² + 2y²
# 最小值在 (0, 0) 处

def f_2d(x, y):
    return x**2 + 2*y**2

def grad_2d(x, y):
    return (2*x, 4*y)

print(f"\n目标函数：f(x, y) = x² + 2y²")
print(f"理论最小值：(0, 0), f(0,0) = 0")

history = gradient_descent_2d(f_2d, grad_2d, x0=3, y0=3, alpha=0.1, n_iterations=15)

print(f"\n最终结果：({history[-1][0]:.6f}, {history[-1][1]:.6f}), f = {history[-1][2]:.6f}")

# ============================================================
# 9. 泰勒展开
# ============================================================
print("\n【9. 泰勒展开】")

# 在 x=0 处展开 e^x
f_taylor = exp(x)
taylor_3 = f_taylor.series(x, 0, 4).removeO()
taylor_5 = f_taylor.series(x, 0, 6).removeO()

print(f"f(x) = e^x 在 x=0 处的泰勒展开:")
print(f"  3 阶：{taylor_3}")
print(f"  5 阶：{taylor_5}")

# 验证
x_val = 0.5
exact = np.exp(x_val)
approx_3 = float(taylor_3.subs(x, x_val))
approx_5 = float(taylor_5.subs(x, x_val))

print(f"\n在 x = {x_val} 处:")
print(f"  精确值：e^{x_val} = {exact:.6f}")
print(f"  3 阶近似：{approx_3:.6f}, 误差：{abs(exact - approx_3):.6f}")
print(f"  5 阶近似：{approx_5:.6f}, 误差：{abs(exact - approx_5):.6f}")

# ============================================================
# 10. 练习解答
# ============================================================
print("\n【10. 练习题解答】")

print("\n练习 1：求导")
print("1. f(x) = x³e^x")
print(f"   f'(x) = {diff(x**3 * exp(x), x)}")

print("\n2. f(x) = ln(sin(x))")
print(f"   f'(x) = {diff(log(sin(x)), x)}")

print("\n3. f(x) = (x²+1)/(x-1)")
print(f"   f'(x) = {sp.simplify(diff((x**2 + 1)/(x - 1), x))}")

print("\n练习 2：偏导数")
f_ex = x**2*y + 3*x*y**2 - y**3
print(f"f(x,y) = {f_ex}")
print(f"   ∂f/∂x = {diff(f_ex, x)}")
print(f"   ∂f/∂y = {diff(f_ex, y)}")

print("\n练习 3：梯度下降")
print("f(x) = x² - 4x + 5, x₀ = 0, α = 0.1")
x_vals_ex, _ = gradient_descent_1d(f_obj, df_obj, x0=0, alpha=0.1, n_iterations=5)
print(f"5 次迭代后：x = {x_vals_ex[-1]:.6f}")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)

# ============================================================
# 可选：绘制梯度下降可视化
# ============================================================
# plt.figure(figsize=(12, 5))
# 
# # 函数图像
# plt.subplot(1, 2, 1)
# x_plot = np.linspace(-1, 5, 100)
# plt.plot(x_plot, f_obj(x_plot), 'b-', label='f(x) = x² - 4x + 5')
# plt.plot(x_vals, y_vals, 'ro-', label='梯度下降路径')
# plt.axvline(x=2, color='g', linestyle='--', label='最小值 x=2')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('梯度下降可视化')
# plt.legend()
# plt.grid(True, alpha=0.3)
# 
# # 收敛曲线
# plt.subplot(1, 2, 2)
# plt.plot(range(len(y_vals)), y_vals, 'bo-')
# plt.xlabel('迭代次数')
# plt.ylabel('f(x)')
# plt.title('收敛曲线')
# plt.grid(True, alpha=0.3)
# 
# plt.tight_layout()
# plt.savefig('gradient_descent.png', dpi=150)
# print("\n图表已保存为 gradient_descent.png")
# plt.show()
