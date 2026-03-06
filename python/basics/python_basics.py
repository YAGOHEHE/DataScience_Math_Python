#!/usr/bin/env python3
"""
Python 基础示例
Python Basics Examples
"""

print("=" * 60)
print("Python 基础示例")
print("=" * 60)

# ============================================================
# 1. 变量与数据类型
# ============================================================
print("\n【1. 变量与数据类型】")

# 基本类型
integer_var = 42
float_var = 3.14159
bool_var = True
string_var = "Data Science"
none_var = None

print(f"整数：{integer_var} (类型：{type(integer_var).__name__})")
print(f"浮点数：{float_var} (类型：{type(float_var).__name__})")
print(f"布尔值：{bool_var} (类型：{type(bool_var).__name__})")
print(f"字符串：{string_var} (类型：{type(string_var).__name__})")
print(f"None: {none_var} (类型：{type(none_var).__name__})")

# 类型转换
print(f"\n类型转换:")
print(f"  int('42') = {int('42')}")
print(f"  float('3.14') = {float('3.14')}")
print(f"  str(100) = '{str(100)}'")
print(f"  bool(1) = {bool(1)}, bool(0) = {bool(0)}")

# ============================================================
# 2. 控制流
# ============================================================
print("\n【2. 控制流】")

# 条件语句
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'D'
print(f"分数 {score} 对应等级：{grade}")

# for 循环
print(f"\nfor 循环 (0-4):")
for i in range(5):
    print(f"  i = {i}", end="")
print()

# 带 enumerate
print(f"\nenumerate 使用:")
fruits = ['apple', 'banana', 'cherry']
for idx, fruit in enumerate(fruits):
    print(f"  {idx}: {fruit}")

# while 循环
print(f"\nwhile 循环 (计算 1+2+...+10):")
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(f"  结果：{total}")

# ============================================================
# 3. 字符串操作
# ============================================================
print("\n【3. 字符串操作】")

s = "  Hello, Data Science!  "
print(f"原字符串：'{s}'")
print(f"  strip(): '{s.strip()}'")
print(f"  lower(): '{s.lower()}'")
print(f"  upper(): '{s.upper()}'")
print(f"  split(','): {s.strip().split(',')}")
print(f"  replace('!', '?'): '{s.replace('!', '?').strip()}'")

# f-string 格式化
name = "Alice"
age = 30
pi = 3.14159265359

print(f"\nf-string 格式化:")
print(f"  {name} is {age} years old")
print(f"  π ≈ {pi:.4f}")
print(f"  二进制：{42:b}, 十六进制：{42:x}")

# 字符串方法
text = "python is awesome"
print(f"\n'{text}' 的方法:")
print(f"  capitalize(): '{text.capitalize()}'")
print(f"  title(): '{text.title()}'")
print(f"  count('e'): {text.count('e')}")
print(f"  find('is'): {text.find('is')}")
print(f"  'python' in text: {'python' in text}")

# ============================================================
# 4. 列表推导式
# ============================================================
print("\n【4. 列表推导式】")

# 基本语法
squares = [x**2 for x in range(10)]
print(f"0-9 的平方：{squares}")

# 带条件
evens = [x for x in range(20) if x % 2 == 0]
print(f"0-19 的偶数：{evens}")

# 嵌套列表推导式
matrix = [[i*j for j in range(4)] for i in range(4)]
print(f"\n4x4 乘法表:")
for row in matrix:
    print(f"  {row}")

# 字典推导式
square_dict = {x: x**2 for x in range(6)}
print(f"\n平方字典：{square_dict}")

# 集合推导式
unique_squares = {x**2 for x in [-3, -2, -1, 0, 1, 2, 3]}
print(f"唯一平方值：{unique_squares}")

# 列表推导式 vs map/filter
numbers = [1, 2, 3, 4, 5]
squares_lc = [x**2 for x in numbers]
squares_map = list(map(lambda x: x**2, numbers))
print(f"\n列表推导式：{squares_lc}")
print(f"map 方式：{squares_map}")

# ============================================================
# 5. 函数基础
# ============================================================
print("\n【5. 函数基础】")

def greet(name, greeting="Hello"):
    """简单的问候函数"""
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# lambda 函数
add = lambda x, y: x + y
print(f"\nlambda 函数：add(3, 5) = {add(3, 5)}")

# 可变参数
def sum_all(*args):
    return sum(args)

print(f"sum_all(1, 2, 3, 4) = {sum_all(1, 2, 3, 4)}")

# ============================================================
# 6. 练习解答
# ============================================================
print("\n【6. 练习解答】")

# 练习 1：1-100 中能被 3 或 5 整除的数
divisible = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0]
print(f"\n练习 1：1-100 中能被 3 或 5 整除的数")
print(f"  共 {len(divisible)} 个")
print(f"  前 10 个：{divisible[:10]}")
print(f"  总和：{sum(divisible)}")

# 练习 2：统计单词出现次数
def count_words(text):
    """统计字符串中每个单词出现的次数"""
    words = text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

sample_text = "python is awesome python is fun python is great"
print(f"\n练习 2：统计单词频率")
print(f"  文本：'{sample_text}'")
print(f"  结果：{count_words(sample_text)}")

# 练习 3：斐波那契数列
def fibonacci_iterative(n):
    """迭代生成斐波那契数列"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

print(f"\n练习 3：前 20 个斐波那契数")
print(f"  {fibonacci_iterative(20)}")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)
