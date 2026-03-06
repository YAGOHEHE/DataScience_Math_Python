#!/usr/bin/env python3
"""
Matplotlib 基础示例
Matplotlib Basics Examples

涵盖：基础图表、多子图、样式定制、保存图表
"""

import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体（如果系统支持）
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("Matplotlib 基础示例")
print("=" * 60)

# ============================================================
# 1. 基础折线图
# ============================================================
print("\n【1. 基础折线图】")

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', linewidth=2, color='blue')
plt.plot(x, y2, label='cos(x)', linewidth=2, color='red', linestyle='--')

plt.xlabel('x')
plt.ylabel('y')
plt.title('正弦和余弦函数')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)

plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/matplotlib/line_plot.png', dpi=150)
print("已保存：line_plot.png")
plt.close()

# ============================================================
# 2. 散点图
# ============================================================
print("\n【2. 散点图】")

np.random.seed(42)
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)
colors = np.random.randn(100)
sizes = 100 * np.random.randn(100)**2

plt.figure(figsize=(10, 6))
scatter = plt.scatter(x_scatter, y_scatter, c=colors, s=sizes, 
                      alpha=0.6, cmap='viridis', edgecolors='black')
plt.colorbar(scatter, label='颜色值')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('散点图示例')
plt.grid(True, alpha=0.3)

plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/matplotlib/scatter_plot.png', dpi=150)
print("已保存：scatter_plot.png")
plt.close()

# ============================================================
# 3. 柱状图
# ============================================================
print("\n【3. 柱状图】")

categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
colors_bar = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=colors_bar, edgecolor='black', linewidth=1.5)

# 在柱子上添加数值标签
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
             str(value), ha='center', va='bottom', fontsize=10)

plt.xlabel('类别')
plt.ylabel('数值')
plt.title('柱状图示例')
plt.grid(True, alpha=0.3, axis='y')

plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/matplotlib/bar_plot.png', dpi=150)
print("已保存：bar_plot.png")
plt.close()

# ============================================================
# 4. 直方图
# ============================================================
print("\n【4. 直方图】")

np.random.seed(42)
data = np.random.randn(1000) * 2 + 5

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7, density=True)

# 添加正态分布曲线
x_hist = np.linspace(data.min(), data.max(), 100)
from scipy import stats
y_hist = stats.norm.pdf(x_hist, data.mean(), data.std())
plt.plot(x_hist, y_hist, 'r-', linewidth=2, label='正态分布拟合')

plt.xlabel('值')
plt.ylabel('密度')
plt.title('直方图与正态分布拟合')
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/matplotlib/histogram.png', dpi=150)
print("已保存：histogram.png")
plt.close()

# ============================================================
# 5. 饼图
# ============================================================
print("\n【5. 饼图】")

labels = ['产品 A', '产品 B', '产品 C', '产品 D']
sizes = [30, 25, 25, 20]
colors_pie = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
explode = [0.1, 0, 0, 0]  # 突出显示第一个

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors_pie,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('产品销售占比')
plt.axis('equal')

plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/matplotlib/pie_chart.png', dpi=150)
print("已保存：pie_chart.png")
plt.close()

# ============================================================
# 6. 箱线图
# ============================================================
print("\n【6. 箱线图】")

np.random.seed(42)
data_box = [np.random.randn(100) * std + mean 
            for mean, std in [(10, 2), (15, 3), (8, 1.5), (12, 2.5)]]
labels_box = ['组 A', '组 B', '组 C', '组 D']

plt.figure(figsize=(10, 6))
plt.boxplot(data_box, labels=labels_box, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red', linewidth=2),
            whiskerprops=dict(color='green'),
            capprops=dict(color='purple'))
plt.ylabel('数值')
plt.title('箱线图 - 多组数据比较')
plt.grid(True, alpha=0.3, axis='y')

plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/matplotlib/boxplot.png', dpi=150)
print("已保存：boxplot.png")
plt.close()

# ============================================================
# 7. 多子图
# ============================================================
print("\n【7. 多子图】")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('多子图示例', fontsize=16)

# 子图 1：折线图
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x), 'b-', label='sin(x)')
axes[0, 0].plot(x, np.cos(x), 'r--', label='cos(x)')
axes[0, 0].set_title('三角函数')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 子图 2：散点图
np.random.seed(42)
axes[0, 1].scatter(np.random.randn(50), np.random.randn(50), 
                   alpha=0.6, color='green')
axes[0, 1].set_title('散点图')
axes[0, 1].grid(True, alpha=0.3)

# 子图 3：柱状图
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 33]
axes[1, 0].bar(categories, values, color='orange', edgecolor='black')
axes[1, 0].set_title('柱状图')
axes[1, 0].grid(True, alpha=0.3, axis='y')

# 子图 4：热力图
data_heat = np.random.rand(10, 10)
im = axes[1, 1].imshow(data_heat, cmap='YlOrRd', aspect='auto')
axes[1, 1].set_title('热力图')
plt.colorbar(im, ax=axes[1, 1])

plt.tight_layout()
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/matplotlib/subplots.png', dpi=150)
print("已保存：subplots.png")
plt.close()

# ============================================================
# 8. 3D 图
# ============================================================
print("\n【8. 3D 曲面图】")

from mpl_toolkits.mplot3d import Axes3D

x_3d = np.linspace(-5, 5, 50)
y_3d = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_3d, y_3d)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, 
                       edgecolor='none', antialiased=True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D 曲面图')
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/matplotlib/3d_surface.png', dpi=150)
print("已保存：3d_surface.png")
plt.close()

# ============================================================
# 9. 样式与主题
# ============================================================
print("\n【9. 样式与主题】")

# 使用内置样式
styles = ['default', 'seaborn-v0_8', 'ggplot', 'dark_background', 'bmh']

fig, axes = plt.subplots(1, len(styles), figsize=(20, 4))
fig.suptitle('Matplotlib 样式比较', fontsize=16)

x = np.linspace(0, 10, 100)

for ax, style in zip(axes, styles):
    with plt.style.context(style):
        ax.plot(x, np.sin(x), label='sin(x)')
        ax.plot(x, np.cos(x), label='cos(x)')
        ax.set_title(style)
        ax.legend()

plt.tight_layout()
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/matplotlib/styles.png', dpi=150)
print("已保存：styles.png")
plt.close()

print("\n" + "=" * 60)
print("示例运行完成！所有图表已保存到 matplotlib 文件夹")
print("=" * 60)
