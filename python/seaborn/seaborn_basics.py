#!/usr/bin/env python3
"""
Seaborn 基础示例
Seaborn Basics Examples

涵盖：分布图、关系图、分类图、热力图、回归图
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置样式
sns.set_style("whitegrid")
sns.set_palette("husl")

print("=" * 60)
print("Seaborn 基础示例")
print("=" * 60)

# 加载示例数据集
print("\n加载示例数据集...")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")

print(f"tips 数据集：{tips.shape}")
print(f"iris 数据集：{iris.shape}")
print(f"titanic 数据集：{titanic.shape}")

# ============================================================
# 1. 分布图
# ============================================================
print("\n【1. 分布图】")

# 直方图 + KDE
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x='total_bill', kde=True, bins=20, color='skyblue')
plt.title('小费金额分布')
plt.xlabel('账单金额')
plt.ylabel('频数')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/dist_plot.png', dpi=150)
print("已保存：dist_plot.png")
plt.close()

# KDE 图
plt.figure(figsize=(10, 6))
sns.kdeplot(data=tips, x='total_bill', hue='sex', fill=True, alpha=0.5)
plt.title('不同性别的小费分布')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/kde_plot.png', dpi=150)
print("已保存：kde_plot.png")
plt.close()

# 联合分布
plt.figure(figsize=(8, 8))
sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter', hue='time')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/joint_plot.png', dpi=150)
print("已保存：joint_plot.png")
plt.close()

# ============================================================
# 2. 分类图
# ============================================================
print("\n【2. 分类图】")

# 条形图
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x='day', y='total_bill', hue='sex', errorbar='sd')
plt.title('每日平均账单金额')
plt.xlabel('星期')
plt.ylabel('平均账单')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/bar_plot.png', dpi=150)
print("已保存：bar_plot.png")
plt.close()

# 箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill', hue='smoker')
plt.title('每日账单分布（按吸烟者）')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/box_plot.png', dpi=150)
print("已保存：box_plot.png")
plt.close()

# 小提琴图
plt.figure(figsize=(10, 6))
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True)
plt.title('每日账单分布（小提琴图）')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/violin_plot.png', dpi=150)
print("已保存：violin_plot.png")
plt.close()

# 计数图
plt.figure(figsize=(10, 6))
sns.countplot(data=titanic, x='class', hue='survived')
plt.title('泰坦尼克号乘客等级与生存情况')
plt.xlabel('舱位等级')
plt.ylabel('人数')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/count_plot.png', dpi=150)
print("已保存：count_plot.png")
plt.close()

# ============================================================
# 3. 关系图
# ============================================================
print("\n【3. 关系图】")

# 散点图
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', size='petal_length', alpha=0.7)
plt.title('鸢尾花萼片长度与宽度')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/scatter_plot.png', dpi=150)
print("已保存：scatter_plot.png")
plt.close()

# 线图
plt.figure(figsize=(10, 6))
fmri = sns.load_dataset("fmri")
sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event", style="event")
plt.title('fMRI 信号随时间变化')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/line_plot.png', dpi=150)
print("已保存：line_plot.png")
plt.close()

# ============================================================
# 4. 热力图
# ============================================================
print("\n【4. 热力图】")

# 相关性热力图
plt.figure(figsize=(10, 8))
corr_matrix = iris.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, fmt='.2f')
plt.title('鸢尾花特征相关性热力图')
plt.tight_layout()
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/heatmap.png', dpi=150)
print("已保存：heatmap.png")
plt.close()

# 矩阵热力图
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

plt.figure(figsize=(12, 8))
sns.heatmap(flights_pivot, annot=True, fmt='d', cmap='YlGnBu', linewidths=0.5)
plt.title('航班乘客数量热力图')
plt.tight_layout()
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/matrix_heatmap.png', dpi=150)
print("已保存：matrix_heatmap.png")
plt.close()

# ============================================================
# 5. 回归图
# ============================================================
print("\n【5. 回归图】")

# 线性回归
plt.figure(figsize=(10, 6))
sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('账单与小费的回归关系')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/reg_plot.png', dpi=150)
print("已保存：reg_plot.png")
plt.close()

# LM 图（带置信区间）
plt.figure(figsize=(10, 6))
sns.lmplot(data=tips, x='total_bill', y='tip', hue='smoker', col='time', height=5)
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/lm_plot.png', dpi=150)
print("已保存：lm_plot.png")
plt.close()

# ============================================================
# 6. 多变量关系
# ============================================================
print("\n【6. 多变量关系】")

# 成对关系图
plt.figure(figsize=(10, 10))
sns.pairplot(iris, hue='species', corner=True, plot_kws={'alpha': 0.7})
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/pairplot.png', dpi=150)
print("已保存：pairplot.png")
plt.close()

# 分类成对图
plt.figure(figsize=(10, 10))
sns.pairplot(tips, hue='sex', vars=['total_bill', 'tip', 'size'], kind='reg')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/pairplot_tips.png', dpi=150)
print("已保存：pairplot_tips.png")
plt.close()

# ============================================================
# 7.  FacetGrid
# ============================================================
print("\n【7. FacetGrid 分面图】")

g = sns.FacetGrid(tips, col="time", row="smoker", height=4, aspect=1.2)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip", alpha=0.7)
g.add_legend()
g.set_titles("{col_name} | {row_name}")
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/facetgrid.png', dpi=150)
print("已保存：facetgrid.png")
plt.close()

# ============================================================
# 8. 自定义样式
# ============================================================
print("\n【8. 自定义样式】")

# 设置不同的样式
styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

fig, axes = plt.subplots(1, len(styles), figsize=(20, 4))
fig.suptitle('Seaborn 样式比较', fontsize=16)

x = np.linspace(0, 10, 50)
y = np.sin(x)

for ax, style in zip(axes, styles):
    with sns.axes_style(style):
        ax.plot(x, y, marker='o', linewidth=2, markersize=6)
        ax.set_title(style)

plt.tight_layout()
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/seaborn/styles.png', dpi=150)
print("已保存：styles.png")
plt.close()

print("\n" + "=" * 60)
print("Seaborn 示例运行完成！所有图表已保存到 seaborn 文件夹")
print("=" * 60)
