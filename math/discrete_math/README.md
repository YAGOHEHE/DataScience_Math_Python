# 离散数学 Discrete Mathematics 🔢

离散数学是计算机科学和算法的基础，对数据科学同样重要。

## 📚 目录

1. [集合论](#集合论)
2. [逻辑与证明](#逻辑与证明)
3. [图论](#图论)
4. [组合数学](#组合数学)
5. [递推关系](#递推关系)
6. [练习题](#练习题)

---

## 集合论

### 基本概念

- **集合**：元素的无序集合，如 $A = \{1, 2, 3\}$
- **子集**：$A \subseteq B$ 表示 $A$ 的所有元素都在 $B$ 中
- **并集**：$A \cup B = \{x | x \in A \text{ 或 } x \in B\}$
- **交集**：$A \cap B = \{x | x \in A \text{ 且 } x \in B\}$
- **补集**：$A^c = \{x | x \notin A\}$

### 笛卡尔积

$$A \times B = \{(a, b) | a \in A, b \in B\}$$

---

## 逻辑与证明

### 命题逻辑

| 符号 | 含义 |
|------|------|
| $\neg p$ | 非 p |
| $p \land q$ | p 且 q |
| $p \lor q$ | p 或 q |
| $p \to q$ | 若 p 则 q |
| $p \leftrightarrow q$ | p 当且仅当 q |

### 量词

- **全称量词**：$\forall x, P(x)$ 表示"对所有 x，P(x) 成立"
- **存在量词**：$\exists x, P(x)$ 表示"存在 x 使 P(x) 成立"

---

## 图论

### 基本定义

- **图**：$G = (V, E)$，$V$ 是顶点集，$E$ 是边集
- **度**：顶点的边数
- **路径**：顶点的序列
- **环**：起点和终点相同的路径

### 特殊图

- **完全图** $K_n$：每对顶点都有边
- **二分图**：顶点可分为两个集合，边只在集合间
- **树**：无环连通图

### 欧拉公式

对于连通平面图：
$$V - E + F = 2$$

---

## 组合数学

### 排列

从 $n$ 个元素中选 $k$ 个排列：
$$P(n, k) = \frac{n!}{(n-k)!}$$

### 组合

从 $n$ 个元素中选 $k$ 个组合：
$$C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$

### 二项式定理

$$(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k$$

### 鸽巢原理

如果 $n$ 个物品放入 $m$ 个盒子，且 $n > m$，则至少有一个盒子包含多于一个物品。

---

## 递推关系

### 斐波那契数列

$$F_n = F_{n-1} + F_{n-2}, \quad F_0 = 0, F_1 = 1$$

通项公式（Binet 公式）：
$$F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}$$

其中 $\phi = \frac{1+\sqrt{5}}{2}$, $\psi = \frac{1-\sqrt{5}}{2}$

### 线性递推

$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \cdots + c_k a_{n-k}$$

---

## 练习题

### 练习 1：集合运算

设 $A = \{1, 2, 3, 4\}$, $B = \{3, 4, 5, 6\}$，求 $A \cup B$, $A \cap B$, $A - B$。

### 练习 2：组合计数

从 10 个人中选 3 个人组成委员会，有多少种选法？

### 练习 3：图论

证明：任何图中，度数为奇数的顶点个数必为偶数。

---

## 📖 参考资料

- 《离散数学及其应用》- Kenneth Rosen
- [MIT OpenCourseWare - Mathematics for Computer Science](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/)
- [图论可视化](https://graphonline.ru/en/)

## 🔗 相关代码

- `discrete_math.py` - Python 实现示例
