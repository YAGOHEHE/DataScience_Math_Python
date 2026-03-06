#!/usr/bin/env python3
"""
Python 数据结构示例
Data Structures Examples

涵盖：列表、元组、字典、集合、deque
"""

from collections import deque, Counter, defaultdict
import time

print("=" * 60)
print("Python 数据结构示例")
print("=" * 60)

# ============================================================
# 1. 列表 (List)
# ============================================================
print("\n【1. 列表 List】")

lst = [1, 2, 3, 4, 5]
print(f"列表：{lst}")

# 常用操作
lst.append(6)
print(f"append(6): {lst}")

lst.extend([7, 8])
print(f"extend([7,8]): {lst}")

lst.insert(0, 0)
print(f"insert(0, 0): {lst}")

lst.remove(0)
print(f"remove(0): {lst}")

popped = lst.pop()
print(f"pop(): {popped}, 列表：{lst}")

# 列表切片
print(f"\n切片 lst[2:5]: {lst[2:5]}")
print(f"切片 lst[::-1]: {lst[::-1]}")

# 列表排序
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n排序前：{unsorted}")
print(f"sorted(): {sorted(unsorted)}")
unsorted.sort(reverse=True)
print(f"sort(reverse=True): {unsorted}")

# ============================================================
# 2. 元组 (Tuple)
# ============================================================
print("\n【2. 元组 Tuple】")

tup = (1, 2, 3, 4, 5)
print(f"元组：{tup}")
print(f"tup[2]: {tup[2]}")
print(f"tup.count(3): {tup.count(3)}")
print(f"tup.index(4): {tup.index(4)}")

# 元组解包
a, b, c, d, e = tup
print(f"\n解包：a={a}, b={b}, c={c}")

# 交换变量
x, y = 10, 20
x, y = y, x
print(f"交换后：x={x}, y={y}")

# ============================================================
# 3. 字典 (Dictionary)
# ============================================================
print("\n【3. 字典 Dictionary】")

dct = {'name': 'Alice', 'age': 30, 'city': 'Beijing'}
print(f"字典：{dct}")

# 访问
print(f"dct['name']: {dct['name']}")
print(f"dct.get('age'): {dct.get('age')}")
print(f"dct.get('job', 'Unknown'): {dct.get('job', 'Unknown')}")

# 修改
dct['age'] = 31
dct['job'] = 'Data Scientist'
print(f"\n修改后：{dct}")

# 遍历
print("\n遍历字典:")
for key, value in dct.items():
    print(f"  {key}: {value}")

# 字典推导式
squares = {x: x**2 for x in range(6)}
print(f"\n平方字典：{squares}")

# ============================================================
# 4. 集合 (Set)
# ============================================================
print("\n【4. 集合 Set】")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"并集 set1 | set2: {set1 | set2}")
print(f"交集 set1 & set2: {set1 & set2}")
print(f"差集 set1 - set2: {set1 - set2}")
print(f"对称差 set1 ^ set2: {set1 ^ set2}")

# 集合操作
set1.add(6)
print(f"\nadd(6): {set1}")
set1.discard(6)
print(f"discard(6): {set1}")

# 集合推导式
unique_squares = {x**2 for x in [-3, -2, -1, 1, 2, 3]}
print(f"\n唯一平方值：{unique_squares}")

# ============================================================
# 5. 双端队列 (deque)
# ============================================================
print("\n【5. 双端队列 deque】")

dq = deque([1, 2, 3, 4, 5])
print(f"deque: {dq}")

dq.append(6)
print(f"append(6): {dq}")

dq.appendleft(0)
print(f"appendleft(0): {dq}")

dq.pop()
print(f"pop(): {dq}")

dq.popleft()
print(f"popleft(): {dq}")

# 旋转
dq.rotate(2)
print(f"rotate(2): {dq}")

# 限制最大长度
dq_limited = deque(maxlen=5)
for i in range(10):
    dq_limited.append(i)
print(f"\n限制长度 5 的 deque: {dq_limited}")

# ============================================================
# 6. Counter
# ============================================================
print("\n【6. Counter 计数器】")

text = "mississippi"
counter = Counter(text)
print(f"统计 '{text}': {counter}")

print(f"\n最常见的 3 个字符: {counter.most_common(3)}")

# 计数器运算
c1 = Counter(['a', 'b', 'b', 'c'])
c2 = Counter(['b', 'c', 'c', 'd'])
print(f"\nc1: {c1}")
print(f"c2: {c2}")
print(f"c1 + c2: {c1 + c2}")
print(f"c1 - c2: {c1 - c2}")

# ============================================================
# 7. defaultdict
# ============================================================
print("\n【7. defaultdict】")

# 普通字典
word_count = {}
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"普通字典统计：{word_count}")

# defaultdict
dd = defaultdict(int)
for word in words:
    dd[word] += 1
print(f"defaultdict 统计：{dict(dd)}")

# 分组
dd_list = defaultdict(list)
items = [('fruit', 'apple'), ('fruit', 'banana'), ('veg', 'carrot')]
for category, item in items:
    dd_list[category].append(item)
print(f"\n分组结果：{dict(dd_list)}")

# ============================================================
# 8. 性能比较
# ============================================================
print("\n【8. 性能比较】")

# 列表 vs deque (作为队列)
n = 10000

# 列表
start = time.time()
lst = []
for i in range(n):
    lst.insert(0, i)
list_time = time.time() - start

# deque
start = time.time()
dq = deque()
for i in range(n):
    dq.appendleft(i)
deque_time = time.time() - start

print(f"在头部插入 {n} 个元素:")
print(f"  列表耗时：{list_time:.4f} 秒")
print(f"  deque 耗时：{deque_time:.4f} 秒")
print(f"  deque 快 {list_time/deque_time:.1f} 倍")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)
