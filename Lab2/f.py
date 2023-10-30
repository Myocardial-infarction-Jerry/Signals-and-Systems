# 导入 需要的 library 库
import numpy as np  # 科学计算
import matplotlib.pyplot as plt  # 画图
import scipy.signal as sg  # 导入 scipy 的 signal 库 命名为 sg
import sympy  # 符号运算
from scipy.integrate import quad  # 用于求解定积分
import warnings

warnings.filterwarnings("ignore")  # 去掉常规警告
import time


def rectangular_pulse(t):
    T = 2
    t = t % T
    if t < 0.5 or t > 1.5:
        return 1.0
    else:
        return -1.0


def triangle_wave(t):
    t = t % 1
    if t < 0.5:
        return 1 - 4 * t
    else:
        return -1 + 4 * (t - 0.5)


#N项插值 方波
def aNt1(N, T):
    an = np.zeros(N + 1)  # 系数an，三角形式
    bn = np.zeros(N + 1)  # 系数bn，三角形式
    FuncA0 = lambda t: rectangular_pulse(t) * 2 / T  # 用于计算a0
    an[0] = quad(FuncA0, -T / 2, T / 2)[0]  # 计算a0
    for n in range(1, N + 1):

        def FuncA(t):
            return rectangular_pulse(t) * np.cos(n * t) * 2 / T

        def FuncB(t):
            return rectangular_pulse(t) * np.sin(n * t) * 2 / T

        an[n] = quad(FuncA, -T / 2, T / 2)[0]
        bn[n] = quad(FuncB, -T / 2, T / 2)[0]
    return an, bn  # 返回傅里叶系数，从0~N


#N项插值 三角波
def aNt2(N, T):
    an = np.zeros(N + 1)  # 系数an，三角形式
    bn = np.zeros(N + 1)  # 系数bn，三角形式
    FuncA0 = lambda t: triangle_wave(t) * 2 / T  # 用于计算a0
    an[0] = quad(FuncA0, -T / 2, T / 2)[0]  # 计算a0
    for n in range(1, N + 1):

        def FuncA(t):
            return triangle_wave(t) * np.cos(n * t) * 2 / T

        def FuncB(t):
            return triangle_wave(t) * np.sin(n * t) * 2 / T

        an[n] = quad(FuncA, -T / 2, T / 2)[0]
        bn[n] = quad(FuncB, -T / 2, T / 2)[0]
    return an, bn  # 返回傅里叶系数，从0~N


def xNt(an, bn, T, N):
    # 周期矩形傅里叶级数有限项级数
    A0 = an[0]
    t = np.arange(-0.5 * T, 0.5 * T, 0.01)  # 时间采样序列
    fnt = A0 / 2  # 直流项，即a0/2
    for n in range(1, N + 1):
        fnt = fnt + an[n] * np.cos(n * t) + bn[n] * np.sin(n * t)  # 傅里叶级数N项逼近值
    return fnt


def plot_xNt1(an, bn, T, N):
    tt = np.arange(-0.5 * T, 0.5 * T, 0.01)  # 时间采样序列
    plt.figure(figsize=(20, 20))  # 通过figsize调整图大小
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.title("trigonometric interpolation polynomial", {'size': 14})
    plt.grid(True)  # 显示网格
    plt.plot(tt,
             np.array([rectangular_pulse(t) for t in tt]),
             label='original function')  # 绘制原始函数信号
    plt.plot(tt, xNt(an, bn, T, N), label='trigonometric polynomial')
    plt.legend()
    plt.show()  # 显示图像


def plot_xNt2(an, bn, T, N):
    tt = np.arange(-0.5 * T, 0.5 * T, 0.01)  # 时间采样序列
    plt.figure(figsize=(10, 10))  # 通过figsize调整图大小
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.title("trigonometric interpolation polynomial", {'size': 7})
    plt.grid(True)  # 显示网格
    plt.plot(tt,
             np.array([triangle_wave(t) for t in tt]),
             label='original function')  # 绘制原始函数信号
    plt.plot(tt, xNt(an, bn, T, N), label='trigonometric polynomial')
    plt.legend()
    plt.show()  # 显示图像


T = 2 * np.pi  # 基波周期
N = [1, 7, 29, 99]  # N项有限项级数逼近，可修改N值显示不同的逼近效果
for i in range(4):
    an, bn = aNt1(N[i], T)  # 0~N傅里叶级数幅度值
    # 有限项级数逼近
    plot_xNt1(an, bn, T, N[i])
    an, bn = aNt2(N[i], T)
    plot_xNt2(an, bn, T, N[i])
