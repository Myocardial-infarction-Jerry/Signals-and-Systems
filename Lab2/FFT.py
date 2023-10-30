import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (-1)**(np.floor(x + 0.5) + 1)


def g(t):
    return np.abs(t - np.floor(t) - 0.5) * 4 - 1


def h(x):
    return np.heaviside(x, 1)


def complex_fourier_coefficients(x, M):
    # 计算复指数傅里叶系数
    T = len(x)
    n = np.arange(-M, M + 1)
    c = np.zeros(2 * M + 1, dtype=complex)
    for i in range(2 * M + 1):
        c[i] = np.sum(x * np.exp(-1j * 2 * np.pi / T * n[i] * np.arange(T)))
    return c / T


def complex_fourier_series(x, M):
    # 使用复指数傅里叶级数逼近原始信号
    T = len(x)
    n = np.arange(-M, M + 1)
    c = complex_fourier_coefficients(x, M)
    xs = np.zeros(T, dtype=complex)
    for i in range(2 * M + 1):
        xs += c[i] * np.exp(1j * 2 * np.pi / T * n[i] * np.arange(T))
    return xs.real


# 定义常数
L = np.pi
t = np.linspace(-L, L, 1000)

# 定义参数
funcs = [f(t), g(t), h(t)]
Ms = [1, 7, 29, 99]

fig = plt.figure(figsize=(10, 8))
for x_index in range(len(funcs)):
    x = funcs[x_index]

    for M_index in range(len(Ms)):
        # 逼近原始信号
        M = Ms[M_index]
        x_approx = complex_fourier_series(x, M)

        # 绘图显示
        sub = fig.add_subplot(len(Ms), len(funcs),
                              x_index + M_index * len(funcs) + 1)
        plt.plot(t, x, label='Original signal')
        plt.plot(t, x_approx, label=f'Approximation with {M}')

plt.show()
