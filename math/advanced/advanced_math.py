#!/usr/bin/env python3
"""
高级数学 Python 示例
Advanced Mathematics Examples

涵盖：信息论、傅里叶变换、马尔可夫链
"""

import numpy as np
from scipy import fft
import matplotlib.pyplot as plt

print("=" * 60)
print("高级数学 Python 示例")
print("=" * 60)

# ============================================================
# 1. 信息论 - 熵计算
# ============================================================
print("\n【1. 信息论 - 熵计算】")

def entropy(p):
    """计算熵 H(X) = -Σ p(x) log₂ p(x)"""
    p = np.array(p)
    p = p[p > 0]  # 排除零概率
    return -np.sum(p * np.log2(p))

def kl_divergence(p, q):
    """计算 KL 散度 D_KL(p || q)"""
    p, q = np.array(p), np.array(q)
    return np.sum(p * np.log2(p / q))

def mutual_information(p_xy):
    """计算互信息 I(X;Y)"""
    p_xy = np.array(p_xy)
    p_x = np.sum(p_xy, axis=1)
    p_y = np.sum(p_xy, axis=0)
    
    mi = 0
    for i in range(p_xy.shape[0]):
        for j in range(p_xy.shape[1]):
            if p_xy[i, j] > 0:
                mi += p_xy[i, j] * np.log2(p_xy[i, j] / (p_x[i] * p_y[j]))
    return mi

# 公平硬币
fair_coin = [0.5, 0.5]
H_fair = entropy(fair_coin)
print(f"公平硬币的熵：H = {H_fair:.4f} bits (最大值)")

# 偏置硬币 P(H) = 0.9
biased_coin = [0.9, 0.1]
H_biased = entropy(biased_coin)
print(f"偏置硬币 P(H)=0.9 的熵：H = {H_biased:.4f} bits")

# 均匀分布 vs 偏置分布
uniform = [0.25, 0.25, 0.25, 0.25]
biased_dist = [0.7, 0.1, 0.1, 0.1]

print(f"\n四结果均匀分布熵：H = {entropy(uniform):.4f} bits")
print(f"四结果偏置分布熵：H = {entropy(biased_dist):.4f} bits")

# KL 散度
kl = kl_divergence(uniform, biased_dist)
print(f"\nKL 散度 D_KL(uniform || biased) = {kl:.4f} bits")

# ============================================================
# 2. 傅里叶变换
# ============================================================
print("\n【2. 傅里叶变换】")

# 创建信号：正弦波叠加
fs = 1000  # 采样频率
t = np.linspace(0, 1, fs, endpoint=False)

# 50Hz 和 120Hz 正弦波
f1, f2 = 50, 120
signal = 0.7 * np.sin(2 * np.pi * f1 * t) + 0.3 * np.sin(2 * np.pi * f2 * t)

print(f"信号组成：")
print(f"  50Hz 正弦波 (振幅 0.7)")
print(f"  120Hz 正弦波 (振幅 0.3)")
print(f"  采样率：{fs} Hz")
print(f"  采样点数：{len(t)}")

# FFT
fft_result = fft.fft(signal)
freqs = fft.fftfreq(len(t), 1/fs)

# 取正频率部分
positive_mask = freqs >= 0
freqs_pos = freqs[positive_mask]
magnitude = np.abs(fft_result[positive_mask]) / len(t) * 2

# 找到主要频率
top_indices = np.argsort(magnitude)[-5:][::-1]
print(f"\nFFT 检测到的主要频率:")
for idx in top_indices[:3]:
    if magnitude[idx] > 0.01:
        print(f"  {freqs_pos[idx]:.1f} Hz (振幅：{magnitude[idx]:.4f})")

print(f"\n✓ 成功检测到 50Hz 和 120Hz 成分")

# ============================================================
# 3. 马尔可夫链
# ============================================================
print("\n【3. 马尔可夫链】")

def markov_chain_simulate(P, initial, n_steps):
    """模拟马尔可夫链"""
    n_states = len(P)
    state = initial
    history = [state]
    
    for _ in range(n_steps):
        state = np.random.choice(n_states, p=P[state])
        history.append(state)
    
    return history

def stationary_distribution(P):
    """计算平稳分布"""
    n = len(P)
    # 求解 πP = π, Σπ = 1
    A = np.vstack([np.array(P).T - np.eye(n), np.ones(n)])
    b = np.zeros(n + 1)
    b[-1] = 1
    
    # 最小二乘解
    pi, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    return pi / np.sum(pi)  # 归一化

# 转移矩阵：天气模型
# 状态：0=晴，1=阴，2=雨
P_weather = np.array([
    [0.7, 0.2, 0.1],  # 晴 → [晴，阴，雨]
    [0.3, 0.4, 0.3],  # 阴 → [晴，阴，雨]
    [0.2, 0.3, 0.5]   # 雨 → [晴，阴，雨]
])

print("天气马尔可夫链:")
print("状态：0=晴，1=阴，2=雨")
print(f"\n转移矩阵 P = ")
print(P_weather)

# 计算平稳分布
pi = stationary_distribution(P_weather)
print(f"\n平稳分布 π:")
print(f"  晴天：{pi[0]:.4f} ({pi[0]*100:.1f}%)")
print(f"  阴天：{pi[1]:.4f} ({pi[1]*100:.1f}%)")
print(f"  雨天：{pi[2]:.4f} ({pi[2]*100:.1f}%)")

# 模拟
np.random.seed(42)
history = markov_chain_simulate(P_weather, initial=0, n_steps=1000)

# 统计频率
unique, counts = np.unique(history, return_counts=True)
empirical = counts / len(history)

print(f"\n1000 步模拟的经验分布:")
print(f"  晴天：{empirical[0]:.4f}")
print(f"  阴天：{empirical[1]:.4f}")
print(f"  雨天：{empirical[2]:.4f}")
print(f"\n经验分布接近平稳分布 ✓")

# ============================================================
# 4. 简单随机游走
# ============================================================
print("\n【4. 随机游走 (布朗运动模拟)】")

def random_walk(n_steps):
    """一维简单随机游走"""
    steps = np.random.choice([-1, 1], size=n_steps)
    return np.cumsum(steps)

n = 1000
walk = random_walk(n)

print(f"随机游走 {n} 步:")
print(f"  最终位置：{walk[-1]}")
print(f"  最大偏离：{np.max(np.abs(walk))}")
print(f"  返回原点次数：{np.sum(walk == 0)}")

# 理论：E[|X_n|] ≈ √(2n/π)
theoretical_mean = np.sqrt(2 * n / np.pi)
print(f"\n理论平均偏离：√(2n/π) ≈ {theoretical_mean:.2f}")
print(f"实际平均偏离：{np.mean(np.abs(walk)):.2f}")

# ============================================================
# 5. 练习解答
# ============================================================
print("\n【5. 练习题解答】")

print("\n练习 1：熵计算")
print(f"公平硬币熵：H = {entropy([0.5, 0.5]):.4f} bits")
print(f"偏置硬币 P(H)=0.9 熵：H = {entropy([0.9, 0.1]):.4f} bits")
print(f"公平硬币熵更大（不确定性更高）✓")

print("\n练习 2：马尔可夫链平稳分布")
P_ex = np.array([[0.7, 0.3], [0.4, 0.6]])
pi_ex = stationary_distribution(P_ex)
print(f"转移矩阵 P = [[0.7, 0.3], [0.4, 0.6]]")
print(f"平稳分布 π = [{pi_ex[0]:.4f}, {pi_ex[1]:.4f}]")
print(f"验证 πP = π: {np.allclose(pi_ex @ P_ex, pi_ex)}")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)

# ============================================================
# 可选：绘制图形
# ============================================================
# plt.figure(figsize=(15, 5))
# 
# # FFT 频谱
# plt.subplot(1, 3, 1)
# plt.plot(freqs_pos[:200], magnitude[:200])
# plt.xlabel('频率 (Hz)')
# plt.ylabel('振幅')
# plt.title('FFT 频谱分析')
# plt.grid(True, alpha=0.3)
# plt.xlim(0, 200)
# 
# # 随机游走
# plt.subplot(1, 3, 2)
# plt.plot(walk)
# plt.xlabel('步数')
# plt.ylabel('位置')
# plt.title('一维随机游走')
# plt.grid(True, alpha=0.3)
# 
# # 马尔可夫链收敛
# plt.subplot(1, 3, 3)
# plt.bar(['晴', '阴', '雨'], pi, alpha=0.7, label='平稳分布')
# plt.bar(['晴', '阴', '雨'], empirical, alpha=0.7, label='经验分布')
# plt.xlabel('天气状态')
# plt.ylabel('概率')
# plt.title('马尔可夫链分布')
# plt.legend()
# 
# plt.tight_layout()
# plt.savefig('advanced_math.png', dpi=150)
# print("\n图表已保存为 advanced_math.png")
# plt.show()
