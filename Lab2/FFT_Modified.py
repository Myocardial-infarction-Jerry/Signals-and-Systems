import numpy as np
import matplotlib.pyplot as plt
from math import floor


def f(x):
    return (-1)**(np.floor(x + 0.5) + 1)


def g(t):
    return np.abs(t - np.floor(t) - 0.5) * 4 - 1


def FourierSeriesApproximation(func, M):
    # 计算信号的傅里叶系数
    t = np.linspace(-M, M + 1)
    signal = func(t) * t
    N = len(signal)
    c = np.zeros(2 * M + 1, dtype=complex)
    for k in range(-M, M + 1):
        c[k] = np.sum(signal * np.exp(-2j * np.pi * k / N)) / N
    # 使用傅里叶级数逼近原始信号
    approx_signal = np.zeros(N, dtype=complex)
    for k in range(-M, M + 1):
        approx_signal += c[k] * np.exp(2j * np.pi * k / N)
    return approx_signal


# 定义初始函数
N = 1000
L = 3
M = 9
t = np.linspace(-L, L, N)
func = f
func = g

# 使用复指数傅里叶级数展开逼近原始信号
approx_signal = FourierSeriesApproximation(func, M)

# 绘制原始信号和逼近信号的图像
plt.plot(t, func(t), label='Original Signal')
plt.plot(t, approx_signal.real, label=f'Approximation (M = {M})')
plt.legend()
plt.show()
