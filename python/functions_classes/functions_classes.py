#!/usr/bin/env python3
"""
函数与类示例
Functions and Classes Examples

涵盖：函数定义、装饰器、类、继承、特殊方法
"""

print("=" * 60)
print("函数与类示例")
print("=" * 60)

# ============================================================
# 1. 函数基础
# ============================================================
print("\n【1. 函数基础】")

def greet(name, greeting="Hello"):
    """简单的问候函数"""
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# 文档字符串
print(f"\n函数文档：{greet.__doc__}")

# ============================================================
# 2. 可变参数
# ============================================================
print("\n【2. 可变参数】")

def sum_all(*args):
    """可变位置参数"""
    return sum(args)

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

def print_info(**kwargs):
    """可变关键字参数"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nprint_info 示例:")
print_info(name="Alice", age=30, city="Beijing")

# 混合使用
def mixed_func(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

print("\n混合参数:")
mixed_func(1, 2, 3, 4, 5, x=10, y=20)

# ============================================================
# 3. Lambda 函数
# ============================================================
print("\n【3. Lambda 函数】")

add = lambda x, y: x + y
print(f"add(3, 5) = {add(3, 5)}")

# 与 map/filter 配合使用
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"\n平方：{squared}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数：{evens}")

# 排序 key
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(f"\n按第二个元素排序：{sorted_pairs}")

# ============================================================
# 4. 装饰器
# ============================================================
print("\n【4. 装饰器】")

def timer_decorator(func):
    """计时装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} 耗时：{end-start:.6f} 秒")
        return result
    return wrapper

def log_decorator(func):
    """日志装饰器"""
    def wrapper(*args, **kwargs):
        print(f"  调用 {func.__name__}, 参数：{args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"  返回：{result}")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b

print("装饰器示例:")
add_numbers(3, 5)

@timer_decorator
def slow_function():
    import time
    time.sleep(0.1)
    return "完成"

print("\n计时装饰器:")
slow_function()

# ============================================================
# 5. 生成器
# ============================================================
print("\n【5. 生成器】")

def fibonacci_generator(n):
    """生成斐波那契数列"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("斐波那契生成器 (前 10 个):")
print(list(fibonacci_generator(10)))

# 生成器表达式
squares_gen = (x**2 for x in range(10))
print(f"\n平方生成器：{list(squares_gen)}")

# ============================================================
# 6. 类基础
# ============================================================
print("\n【6. 类基础】")

class Person:
    """人类"""
    
    # 类变量
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """初始化"""
        self.name = name  # 实例变量
        self.age = age
    
    def greet(self):
        """问候方法"""
        return f"Hello, I'm {self.name}, {self.age} years old."
    
    def birthday(self):
        """过生日"""
        self.age += 1
        return f"Happy birthday! Now {self.age} years old."
    
    @classmethod
    def get_species(cls):
        """类方法"""
        return cls.species
    
    @staticmethod
    def is_adult(age):
        """静态方法"""
        return age >= 18
    
    def __str__(self):
        """字符串表示"""
        return f"Person({self.name}, {self.age})"
    
    def __repr__(self):
        """开发者表示"""
        return f"Person('{self.name}', {self.age})"

# 创建实例
alice = Person("Alice", 30)
bob = Person("Bob", 25)

print(alice.greet())
print(bob.greet())

print(f"\n{alice.name} 过生日：{alice.birthday()}")

print(f"\n类方法 - 物种：{Person.get_species()}")
print(f"静态方法 - 18 岁是成人？{Person.is_adult(18)}")

print(f"\n__str__: {alice}")
print(f"__repr__: {repr(alice)}")

# ============================================================
# 7. 继承
# ============================================================
print("\n【7. 继承】")

class Student(Person):
    """学生类，继承 Person"""
    
    def __init__(self, name, age, major):
        super().__init__(name, age)  # 调用父类初始化
        self.major = major
        self.grades = []
    
    def add_grade(self, grade):
        """添加成绩"""
        self.grades.append(grade)
    
    def get_average(self):
        """计算平均分"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def greet(self):
        """重写父类方法"""
        base_greeting = super().greet()
        return f"{base_greeting} I study {self.major}."

student = Student("Charlie", 20, "Computer Science")
print(student.greet())

student.add_grade(85)
student.add_grade(90)
student.add_grade(78)
print(f"平均成绩：{student.get_average():.2f}")

# ============================================================
# 8. 特殊方法
# ============================================================
print("\n【8. 特殊方法】")

class Vector:
    """向量类"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """向量加法"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        """标量乘法"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __abs__(self):
        """向量模长"""
        import math
        return math.sqrt(self.x**2 + self.y**2)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"|v1| = {abs(v1):.2f}")

# ============================================================
# 9. 数据类 (Python 3.7+)
# ============================================================
print("\n【9. 数据类】")

from dataclasses import dataclass

@dataclass
class Point:
    """数据类示例"""
    x: float
    y: float
    label: str = "unnamed"
    
    def distance_from_origin(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

p1 = Point(3.0, 4.0, "A")
p2 = Point(1.0, 1.0)

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1 到原点距离：{p1.distance_from_origin():.2f}")

# ============================================================
# 10. 练习
# ============================================================
print("\n【10. 练习】")

# 练习：实现一个简单的栈
class Stack:
    """栈实现"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)
    
    def __repr__(self):
        return f"Stack({self.items})"

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"栈：{stack}")
print(f"pop: {stack.pop()}")
print(f"peek: {stack.peek()}")
print(f"当前栈：{stack}")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)
