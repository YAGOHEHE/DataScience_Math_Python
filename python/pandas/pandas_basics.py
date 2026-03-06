#!/usr/bin/env python3
"""
Pandas 基础示例
Pandas Basics Examples

涵盖：Series、DataFrame、数据操作、分组聚合、合并
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("Pandas 基础示例")
print("=" * 60)

# ============================================================
# 1. Series 创建与操作
# ============================================================
print("\n【1. Series 基础】")

# 创建 Series
s = pd.Series([1, 3, 5, 7, 9])
print(f"从列表创建:\n{s}")

s_labeled = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
print(f"\n带标签:\n{s_labeled}")
print(f"s_labeled['c'] = {s_labeled['c']}")

# Series 运算
print(f"\nSeries 运算:")
print(f"s * 2:\n{s * 2}")
print(f"s + 10:\n{s + 10}")

# ============================================================
# 2. DataFrame 创建
# ============================================================
print("\n【2. DataFrame 创建】")

# 从字典创建
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28],
    'city': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen'],
    'salary': [8000, 12000, 15000, 9000]
}
df = pd.DataFrame(data)
print(f"从字典创建:\n{df}")

# 从 CSV 读取（示例）
# df = pd.read_csv('data.csv')

# 查看信息
print(f"\nDataFrame 信息:")
print(f"shape: {df.shape}")
print(f"columns: {list(df.columns)}")
print(f"dtypes:\n{df.dtypes}")

# ============================================================
# 3. 数据查看
# ============================================================
print("\n【3. 数据查看】")

print(f"head(2):\n{df.head(2)}")
print(f"\ntail(2):\n{df.tail(2)}")
print(f"\ndescribe():\n{df.describe()}")
print(f"\ninfo():")
df.info()

# ============================================================
# 4. 数据选择
# ============================================================
print("\n【4. 数据选择】")

# 列选择
print(f"单列 df['name']:\n{df['name']}")
print(f"\n多列:\n{df[['name', 'salary']]}")

# 行选择
print(f"\niloc[0] (第一行):\n{df.iloc[0]}")
print(f"\niloc[0:2] (前两行):\n{df.iloc[0:2]}")

# loc - 标签索引
print(f"\nloc[0, 'name']: {df.loc[0, 'name']}")
print(f"\nloc[0:1, ['name', 'age']]:\n{df.loc[0:1, ['name', 'age']]}")

# 布尔索引
print(f"\n布尔索引 - age > 28:\n{df[df['age'] > 28]}")
print(f"\n多条件 - age > 28 & salary > 10000:\n{df[(df['age'] > 28) & (df['salary'] > 10000)]}")

# ============================================================
# 5. 数据修改
# ============================================================
print("\n【5. 数据修改】")

df_copy = df.copy()

# 添加列
df_copy['bonus'] = df_copy['salary'] * 0.1
print(f"添加 bonus 列:\n{df_copy}")

# 修改值
df_copy.loc[0, 'age'] = 26
print(f"\n修改后:\n{df_copy}")

# 删除列
df_copy = df_copy.drop('bonus', axis=1)
print(f"\n删除 bonus 列:\n{df_copy}")

# 删除行
df_copy = df_copy.drop(0)
print(f"\n删除第一行:\n{df_copy}")

# ============================================================
# 6. 处理缺失值
# ============================================================
print("\n【6. 处理缺失值】")

df_na = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [10, 11, 12, 13]
})
print(f"含缺失值:\n{df_na}")

print(f"\nisna():\n{df_na.isna()}")
print(f"\n每列缺失数:\n{df_na.isna().sum()}")

# 删除缺失值
print(f"\ndropna():\n{df_na.dropna()}")
print(f"\ndropna(thresh=2):\n{df_na.dropna(thresh=2)}")

# 填充缺失值
print(f"\nfillna(0):\n{df_na.fillna(0)}")
print(f"\nfillna(method='ffill'):\n{df_na.fillna(method='ffill')}")
print(f"\nfillna(df.mean()):\n{df_na.fillna(df_na.mean())}")

# ============================================================
# 7. 分组聚合
# ============================================================
print("\n【7. 分组聚合】")

df_group = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'value': [10, 20, 30, 40, 50, 60],
    'count': [1, 2, 3, 4, 5, 6]
})
print(f"数据:\n{df_group}")

print(f"\n按 category 分组求和:\n{df_group.groupby('category').sum()}")
print(f"\n分组统计:\n{df_group.groupby('category').agg(['mean', 'sum', 'count'])}")

# 多列分组
df_group['subcat'] = ['X', 'X', 'Y', 'Y', 'X', 'Y']
print(f"\n多列分组:\n{df_group.groupby(['category', 'subcat'])['value'].sum()}")

# ============================================================
# 8. 数据合并
# ============================================================
print("\n【8. 数据合并】")

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value1': [1, 2, 3, 4]
})
df2 = pd.DataFrame({
    'key': ['B', 'D', 'E', 'F'],
    'value2': [10, 20, 30, 40]
})

print(f"df1:\n{df1}")
print(f"\ndf2:\n{df2}")

print(f"\ninner merge:\n{pd.merge(df1, df2, on='key', how='inner')}")
print(f"\nleft merge:\n{pd.merge(df1, df2, on='key', how='left')}")
print(f"\nright merge:\n{pd.merge(df1, df2, on='key', how='right')}")
print(f"\nouter merge:\n{pd.merge(df1, df2, on='key', how='outer')}")

# 拼接
df_concat = pd.concat([df1, df2], ignore_index=True)
print(f"\nconcat:\n{df_concat}")

# ============================================================
# 9. 字符串与日期
# ============================================================
print("\n【9. 字符串与日期】")

# 字符串操作
df_str = pd.DataFrame({'text': ['Hello World', 'Python Data', 'Pandas Easy']})
print(f"原文本:\n{df_str}")
print(f"\n转小写:\n{df_str['text'].str.lower()}")
print(f"\n分割:\n{df_str['text'].str.split()}")
print(f"\n包含 'o':\n{df_str['text'].str.contains('o')}")

# 日期操作
df_date = pd.DataFrame({
    'date': ['2024-01-01', '2024-02-15', '2024-03-20'],
    'value': [100, 200, 300]
})
df_date['date'] = pd.to_datetime(df_date['date'])
print(f"\n日期数据:\n{df_date}")
print(f"\n日期 dtypes: {df_date['date'].dtype}")
print(f"\n提取年份:\n{df_date['date'].dt.year}")
print(f"\n提取月份:\n{df_date['date'].dt.month}")

# ============================================================
# 10. 练习
# ============================================================
print("\n【10. 练习】")

# 创建示例数据集
np.random.seed(42)
n = 100
sales_data = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=n, freq='D'),
    'product': np.random.choice(['A', 'B', 'C'], n),
    'sales': np.random.randint(100, 1000, n),
    'region': np.random.choice(['North', 'South', 'East', 'West'], n)
})

print(f"销售数据 (前 5 行):\n{sales_data.head()}")

# 练习 1：按产品分组统计
print(f"\n练习 1：按产品分组统计")
print(sales_data.groupby('product')['sales'].agg(['sum', 'mean', 'count']))

# 练习 2：按地区和产品的交叉统计
print(f"\n练习 2：地区 - 产品交叉统计")
print(pd.pivot_table(sales_data, values='sales', index='region', 
                     columns='product', aggfunc='sum', fill_value=0))

# 练习 3：添加日期特征
sales_data['month'] = sales_data['date'].dt.month
sales_data['weekday'] = sales_data['date'].dt.day_name()
print(f"\n练习 3：添加日期特征后:\n{sales_data[['date', 'month', 'weekday']].head()}")

# 练习 4：计算累计销售额
sales_data['cumulative_sales'] = sales_data['sales'].cumsum()
print(f"\n练习 4：累计销售额 (最后 5 行):")
print(sales_data[['date', 'sales', 'cumulative_sales']].tail())

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)
