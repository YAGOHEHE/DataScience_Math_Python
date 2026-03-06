#!/usr/bin/env python3
"""
离散数学 Python 示例
Discrete Mathematics Examples

涵盖：集合运算、组合计数、图论、递推关系
"""

import numpy as np
from itertools import combinations, permutations, product
from math import factorial, comb, perm
import networkx as nx

print("=" * 60)
print("离散数学 Python 示例")
print("=" * 60)

# ============================================================
# 1. 集合运算
# ============================================================
print("\n【1. 集合运算】")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}")
print(f"\nA ∪ B (并集) = {A | B}")
print(f"A ∩ B (交集) = {A & B}")
print(f"A - B (差集) = {A - B}")
print(f"B - A (差集) = {B - A}")
print(f"A Δ B (对称差) = {A ^ B}")

# 笛卡尔积
cartesian = list(product(A, B))
print(f"\n|A × B| = {len(cartesian)}")
print(f"示例元素：{cartesian[:5]}...")

# ============================================================
# 2. 组合计数
# ============================================================
print("\n【2. 组合计数】")

n, k = 10, 3

# 排列
perm_count = perm(n, k)
print(f"从 {n} 个元素中选 {k} 个排列：P({n},{k}) = {perm_count}")
print(f"  公式：{n}!/({n}-{k})! = {factorial(n)}//{factorial(n-k)} = {perm_count}")

# 组合
comb_count = comb(n, k)
print(f"\n从 {n} 个元素中选 {k} 个组合：C({n},{k}) = {comb_count}")
print(f"  公式：{n}!/({k}!×({n}-{k})!) = {comb_count}")

# 验证：列举所有组合
all_combs = list(combinations(range(1, n+1), k))
print(f"  验证：共 {len(all_combs)} 种组合")

# 二项式系数
print(f"\n二项式系数 (n=5):")
for k in range(6):
    print(f"  C(5,{k}) = {comb(5, k)}")

# 二项式展开验证
print(f"\n验证二项式定理：(x+y)⁴")
print(f"  系数：{[comb(4, k) for k in range(5)]}")
print(f"  展开：x⁴ + 4x³y + 6x²y² + 4xy³ + y⁴")

# ============================================================
# 3. 递推关系 - 斐波那契
# ============================================================
print("\n【3. 递推关系 - 斐波那契数列】")

def fibonacci_recursive(n):
    """递归计算（低效，仅用于小 n）"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    """迭代计算"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def fibonacci_formula(n):
    """Binet 公式"""
    phi = (1 + np.sqrt(5)) / 2
    psi = (1 - np.sqrt(5)) / 2
    return round((phi**n - psi**n) / np.sqrt(5))

print("前 15 个斐波那契数:")
for i in range(15):
    f_iter = fibonacci_iterative(i)
    f_formula = fibonacci_formula(i)
    print(f"  F({i:2d}) = {f_iter:6d} (公式验证：{f_formula}, 匹配：{f_iter == f_formula})")

# ============================================================
# 4. 图论基础
# ============================================================
print("\n【4. 图论基础】")

# 创建图
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])

print(f"图 G 的边：{list(G.edges())}")
print(f"顶点数：{G.number_of_nodes()}")
print(f"边数：{G.number_of_edges()}")

# 度数
print(f"\n各顶点的度:")
for node in G.nodes():
    print(f"  deg({node}) = {G.degree(node)}")

# 验证：奇数度顶点个数为偶数
odd_degree_nodes = [n for n in G.nodes() if G.degree(n) % 2 == 1]
print(f"\n度数为奇数的顶点：{odd_degree_nodes}")
print(f"个数：{len(odd_degree_nodes)} (必为偶数 ✓)")

# 路径
path = nx.shortest_path(G, source=1, target=3)
print(f"\n从 1 到 3 的最短路径：{path}")

# 连通性
print(f"图是否连通：{nx.is_connected(G)}")

# 完全图
K5 = nx.complete_graph(5)
print(f"\n完全图 K₅:")
print(f"  边数：{K5.number_of_edges()} (公式：n(n-1)/2 = {5*4//2})")

# ============================================================
# 5. 鸽巢原理应用
# ============================================================
print("\n【5. 鸽巢原理】")

# 问题：在 13 个人中，至少有几个人在同一个月出生？
people = 13
months = 12
min_in_same_month = (people - 1) // months + 1

print(f"问题：{people} 个人，{months} 个月")
print(f"至少有 {min_in_same_month} 个人在同一个月出生")
print(f"原理：⌈{people}/{months}⌉ = {min_in_same_month}")

# ============================================================
# 6. 排列生成
# ============================================================
print("\n【6. 排列生成】")

items = ['A', 'B', 'C']
all_perms = list(permutations(items))

print(f"集合 {items} 的所有排列:")
for i, p in enumerate(all_perms, 1):
    print(f"  {i}. {p}")
print(f"共 {len(all_perms)} = {factorial(len(items))}! 种")

# ============================================================
# 7. 练习解答
# ============================================================
print("\n【7. 练习题解答】")

print("\n练习 1：集合运算")
A_ex = {1, 2, 3, 4}
B_ex = {3, 4, 5, 6}
print(f"A = {A_ex}, B = {B_ex}")
print(f"  A ∪ B = {A_ex | B_ex}")
print(f"  A ∩ B = {A_ex & B_ex}")
print(f"  A - B = {A_ex - B_ex}")

print("\n练习 2：组合计数")
print(f"从 10 人选 3 人：C(10,3) = {comb(10, 3)} 种")

print("\n练习 3：图论证明")
print("定理：任何图中，度数为奇数的顶点个数必为偶数")
print("证明：所有顶点度数之和 = 2×边数（偶数）")
print("      偶数度顶点的度数和为偶数")
print("      因此奇数度顶点的度数和也必须为偶数")
print("      故奇数度顶点个数必为偶数 ✓")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)
