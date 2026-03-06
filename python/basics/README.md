# Python 基础 Python Basics 🐍

Python 是数据科学的首选编程语言，语法简洁、功能强大。

## 📚 目录

1. [变量与数据类型](#变量与数据类型)
2. [控制流](#控制流)
3. [字符串操作](#字符串操作)
4. [列表推导式](#列表推导式)
5. [练习题](#练习题)

---

## 变量与数据类型

### 基本类型

```python
# 整数
x = 42

# 浮点数
y = 3.14159

# 布尔值
is_valid = True

# 字符串
name = "Data Science"

# None (空值)
result = None
```

### 类型检查

```python
type(x)      # <class 'int'>
isinstance(x, int)  # True
```

---

## 控制流

### 条件语句

```python
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'
```

### 循环

```python
# for 循环
for i in range(5):
    print(i)

# while 循环
count = 0
while count < 10:
    count += 1

# 带 else 的循环
for i in range(5):
    if i == 3:
        break
else:
    print("循环正常结束")  # 不会执行
```

---

## 字符串操作

### 常用方法

```python
s = "  Hello, World!  "

s.strip()           # "Hello, World!"
s.lower()           # "  hello, world!  "
s.upper()           # "  HELLO, WORLD!  "
s.split(",")        # ["  Hello", " World!  "]
s.replace("!", "?") # "  Hello, World?  "
s.startswith("He")  # False (因为有前导空格)
```

### f-string 格式化

```python
name = "Alice"
age = 30
print(f"{name} is {age} years old")

# 格式化数字
pi = 3.1415926
print(f"π ≈ {pi:.2f}")  # π ≈ 3.14
```

---

## 列表推导式

```python
# 基本语法
squares = [x**2 for x in range(10)]

# 带条件
evens = [x for x in range(20) if x % 2 == 0]

# 嵌套
matrix = [[i*j for j in range(3)] for i in range(3)]

# 字典推导式
square_dict = {x: x**2 for x in range(5)}

# 集合推导式
unique_squares = {x**2 for x in [-2, -1, 1, 2]}
```

---

## 练习题

### 练习 1：列表操作

创建一个列表，包含 1-100 中所有能被 3 或 5 整除的数。

### 练习 2：字符串处理

编写函数，统计字符串中每个单词出现的次数。

### 练习 3：斐波那契

用循环和列表推导式分别生成前 20 个斐波那契数。

---

## 📖 参考资料

- [Python 官方教程](https://docs.python.org/3/tutorial/)
- 《Python 编程：从入门到实践》
- [Real Python](https://realpython.com/)

## 🔗 相关代码

- `python_basics.py` - 示例代码
