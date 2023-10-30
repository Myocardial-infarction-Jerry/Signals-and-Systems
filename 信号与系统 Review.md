# 信号与系统 Review

## Chap.1 信号与系统

#### 1.1.3 信号能量与功率

瞬时功率: $p(t)=v(t)i(t)=\frac1Rv^2(t)$

时间间隔内消耗总能量: 

- $\int_{t_1}^{t_2}p(t)\text dt=\int_{t_1}^{t_2}\frac1Rv^2(t)\text dt$
- $\int_{t_1}^{t_2}|x(t)|^2\text dt \qquad复数意义下$
- $\sum_{n=n_1}^{n_2}|x[n]|^2$

平均功率: $\frac1{t_2-t_1}\int_{t_1}^{t_2}p(t)\text dt=\frac1{t_2-t_1}\int_{t_1}^{t_2}\frac1Rv^2(t)\text dt$

#### 1.2.2 周期信号

基波周期: 使得 $x(t)=x(t+T)$ 的最小正值 $T$

#### 1.2.3 偶信号与奇信号

任何信号都能分解为两个信号之和, 其中之一为偶信号, 另一个为奇信号.

$$
\begin{align}
\mathcal{Ev}\{x(t)\}&=\frac12[x(t)+x(-t)]\\
\mathcal{Od}\{x(t)\}&=\frac12[x(t)-x(-t)]
\end{align}
$$

#### 1.3.1 连续时间复指数信号与正弦信号

正弦信号: $x(t)=A\cos(\omega_0t+\phi)$

- 基波频率: $\omega_0$

**欧拉关系: $e^{j\omega_0t}=\cos\omega_0t+j\sin\omega_0t$**

复指数信号表示: 

- $A\cos(\omega_0t+\phi)=\frac A2e^{j(\omega_0t+\phi)}+\frac A2e^{-j(\omega_0t+\phi)}$
- $A\cos(\omega_0t+\phi)=A\mathcal{Re}\{e^{j(\omega_0t+\phi)}\}$
- $A\sin(\omega_0t+\phi)=A\mathcal{Im}\{e^{j(\omega_0t+\phi)}\}$

**谐波关系:**

集合内全部信号具有公共周期 $T_0$, 即 
$$
e^{j\omega T_0}=1\Longrightarrow\omega T_0=2\pi k,\quad k=0,\pm1,\pm2,\cdots
$$
由此, 若定义
$$
\omega_0=\frac{2\pi}{T_0}
$$
易得, $\omega$ 必须是 $\omega_0$ 的整倍数.

##### **一般复指数信号:**

- $a=r+j\omega_0$

- $Ce^{at}=|C|e^{rt}\cos(\omega_0+\theta)+j|C|e^{rt}\sin(\omega_0+\theta)$
  ![image-20230517172000457](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230517172000457.png)
  
  ![image-20230517173739222](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230517173739222.png)

#### 1.3.3 离散时间复指数序列的周期性质

- 我们注意到, 
  $$
  e^{j(\omega_0+2\pi)n}=e^{j\omega_0n}e^{j2\pi n}=e^{j\omega_0n}
  $$

  即离散时间复指数信号在 $\omega_0, \omega_0+2\pi,\omega_0+4\pi,\cdots$ 等情况下复指数信号相同. 故考虑离散时间复指数信号时, 仅从某一个 $2\pi$ 区间内选择 $\omega_0$ 即可.

- 为了使信号 $e^{j\omega_0n}$ 是周期的, 周期为 $N>0$ , 则必须有
  $$
  e^{j\omega_0(n+N)}=e^{j\omega_0n}
  $$
  等效于
  $$
  e^{j\omega_0N}=1\\
  \frac{\omega_0}{2\pi}=\frac mN
  $$
  其中 $m$ 为整数.

  即 $\omega_0/2\pi$ 为一个有理数, 则 $e^{j\omega_0n}$ 是周期的, 否则就不是周期的.

  同时可有,
  $$
  \omega_0/m=2\pi/N,\quad m=\pm1,\pm2,\cdots
  $$
  

#### 1.4.1 离散时间单位脉冲和单位阶跃序列

- 单位脉冲
  $$
  \delta[n]=\left\{
  \begin{align}
  0,&\quad n\neq0\\
  1,&\quad n=0
  \end{align}
  \right.
  $$

- 单位阶跃
  $$
  u[n]=\left\{
  \begin{align}
  0,&\quad n<0\\
  1,&\quad n\geq0
  \end{align}
  \right.
  $$

- 其中有
  $$
  \delta[n]=u[n]-u[n-1],&\qquad 一次差分\\
  u[n]=\sum_{m=-\infty}^n\delta[m],&\qquad 求和函数
  $$

#### 1.4.2 连续时间单位阶跃和单位冲激函数

- 单位阶跃
  $$
  u(t)=\left\{
  \begin{align}
  0,&\quad t<0\\
  1,&\quad t>0
  \end{align}
  \right.
  $$

- 单位冲激
  $$
  \delta(t)=\left\{
  \begin{align}
  0,&\quad t\neq0\\
  1,&\quad t=0
  \end{align}
  \right.
  $$

- 其中有
  $$
  u(t)=\int_{-\infty}^t\delta(\tau)\text d\tau,&\qquad 积分函数\\
  \delta(t)=\frac{\text du(t)}{\text dt},&\qquad 一次微分
  $$

#### 1.6.1 记忆系统与无记忆系统

若对自变量的每一个值, 一个系统的输出仅仅取决于该时刻的输入, 则将这个系统称为**无记忆系统**, 如**恒等系统** $y(t)=x(t)$.

相对的, **记忆系统**有:

- 累加器: $y[n]=\sum_{k=-\infty}^nx[k]$
- 延迟单元: $y[n]=x[n-1]$
- 电容器: $y(t)\frac1C\int_{-\infty}^tx(\tau)\text d\tau$

#### 1.6.2 可逆性与可逆系统

若一个系统在不同的输入下, 导致不同的输出, 则称该系统是**可逆的**. 若一个系统是可逆的, 则就会存在一个**逆系统**.

可逆系统的例子如下:
$$
y(t)=2x(t),&\qquad 原系统\\
w(t)=\frac12y(t),&\qquad 逆系统
$$
不可逆系统的例子如下:
$$
y[n]=0\\
y(t)=x^2(t)
$$

#### 1.6.3 因果性

若一个系统在任一时刻的输出仅取决于现在的输入以及过去的输入, 则称该系统为**因果系统**. 往往也称为**不可预测的系统**, 因为系统的输入值无法预测未来的输入值.

所有的无记忆系统都是因果的.

#### 1.6.4 稳定性

若一个系统的输入有界, 其输出也有界 (不发散), 则该系统是**稳定系统**.

#### 1.6.5 时不变性

若一个系统的特性和行为不随时间而变, 则该系统是**时不变系统**.

*具体来说, 如果在输入信号上有一个时移, 而在输出信号中产生同样的时移, 则该系统是时不变的.*

#### 1.6.6 线性

**线性系统的叠加性质:**

- 可加性: $x_1(t)+x_2(t)\rightarrow y_1(t)+y_2(t)$ 

- 比例性/齐次性: $ax_1(t)\rightarrow ay_2(t),\qquad a为任意复常数$

- $$
  x[n]=\sum_ka_kx_k[n]\\
  y[n]=\sum_ka_ky_k[n]\\
  x[n]\rightarrow y[n]
  $$

## Chap.2 线性时不变系统

#### 2.1.1 用脉冲表示离散时间信号

$$
x[n]=\sum_{k=-\infty}^{+\infty}x[k]\delta[n-k]
$$

#### 2.1.2 离散时间线性时不变系统的单位脉冲响应及卷积和表示

- 单位脉冲序列响应: $h[n]=h_0[n]$, 即为线性系统对 $\delta[n]$ 的响应

- $$
  y[n]=\sum_{k=-\infty}^{+\infty}x[k]h[n-k]
  $$
  该结果称为**卷积和**.

#### 2.2.1 用冲激表示连续时间信号

若定义
$$
\delta_\Delta(t)=
\left\{
\begin{align}
\frac1\Delta,&\qquad 0\leq t<\Delta\\
0,&\qquad 其他
\end{align}
\right.
$$
由于 $\Delta\delta_\Delta(t)=1$, 则 $\hat x(t)$ 可表示为
$$
\hat x(t)=\sum_{k=-\infty}^\infty x(k\Delta)\delta_\Delta(t-k\Delta)\Delta\\
$$
所以
$$
\begin{align}
x(t)&=\lim_{\Delta\rightarrow0}\sum_{k=-\infty}^\infty x(k\Delta)\delta_\Delta(t-k\Delta)\Delta\\
x(t)&=\int_{-\infty}^\infty x(\tau)\delta(t-\tau)\text d\tau
\end{align}
$$
上式称为连续时间冲激函数的**筛选性质**.

#### 2.2.2 连续时间线性时不变系统的单位冲激响应及卷积积分表示

对于连续时间线性系统而言, 令 $h_\tau(t)$ 表示系统在时间 $t$ 对于单位冲激 $\delta(t-\tau)$ 的响应, 
$$
\begin{align}
\hat y(t)&=\sum_{k=-\infty}^\infty x(k\Delta)\hat h_{k\Delta}(t)\Delta\\
y(t)&=\lim_{\Delta\rightarrow0}\sum_{k=-\infty}^\infty x(k\Delta)\hat h_{k\Delta}(t)\Delta\\
y(t)&=\int_{-\infty}^\infty x(\tau)h_\tau(t)\text d\tau\\
    &=\int_{-\infty}^\infty x(\tau)h(t-\tau) \text d\tau
\end{align}
$$
上式称为**卷积积分**.

### 2.3 线性时不变系统的性质

$$
y[n]=\sum_{k=-\infty}^\infty x[k]h[n-k]=x[n]*h[n]\\
y(t)=\int_{-\infty}^\infty x(\tau)h(t-\tau)\text d\tau=x(t)*h(t)
$$

该性质一般仅对线性时不变系统成立.

- **交换律:**
  $$
  x[n]*h[n]=h[n]*x[n]\\
  x(t)*h(t)=h(t)*x(t)
  $$

- **分配律:**
  $$
  x[n]*(h_1[n]+h_2[n])=x[n]*h_1[n]+x[n]*h_2[n]\\
  x(t)*(h_1(t)+h_2(t))=x(t)*h_1(t)+x(t)*h_2(t)
  $$

- **结合律:**
  $$
  (x[n]*h_1[n])*h_2[n]=x[n]*(h_1[n]*h_2[n])\\
  (x(t)*h_1(t))*h_2(t)=x(t)*(h_1(t)*h_2(t))
  $$

#### 2.3.4 有记忆和无记忆线性时不变系统

若一个系统是无记忆的, 则必定有
$$
h[n]=K\delta[n]
$$
其中 $K=h[0]$ 是一个常数, 卷积和退化为
$$
y(t)=Kx(t)
$$

#### 2.3.5 线性时不变系统的可逆性

给定一个系统, 其冲激响应为 $h(t)$, 逆系统的冲激响应为 $h_1(t)$, 则有
$$
h(t)*h_1(t)=\delta(t)
$$

#### 2.3.6 线性时不变系统的因果性

若一个线性时不变系统是因果的, 则有
$$
h[n]=0,&\qquad n<0\\
h(t)=0,&\qquad t<0
$$
等效于**初始松弛**: 若一个因果系统的输入在某个时刻点以前为零,则其输出在那个时刻以前也必须为零

##### 2.3.7 线性时不变系统的稳定性

若一个线性时不变系统是稳定的, 则有
$$
\sum_{k=-\infty}^\infty|h[k]|<\infty,&\qquad 绝对可和\\
\int_{-\infty}^\infty|h(\tau)|\text d\tau<\infty,&\qquad 绝对可积\quad等价于平方可积
$$

#### 2.3.8 线性时不变系统的单位阶跃响应

$$
s[n]=u[n]*h[n]\\
s(t)=\int_{-\infty}^th(\tau)\text d\tau
$$

显然有
$$
h[n]=s[n]-s[n-1]\\
h(t)=\frac{\text ds(t)}{\text dt}=s'(t)
$$

#### 2.4.1 线性常系数微分方程

如一阶微分方程
$$
\frac{\text dy(t)}{\text dt}+2y(t)=x(t)
$$
*微分方程求解*

#### 2.4.2 线性常系数差分方程

如 $N$ 阶差分方程
$$
\sum_{k=0}^Na_ky[n-k]=\sum_{k=0}^Mb_kx[n-k]
$$
上式可重写为
$$
y[n]=\frac1{a_0}\left\{
\sum_{k=0}^Mb_kx[n-k]-\sum_{k=1}^Ma_ky[n-k]
\right\}
$$
上两式可称为**递归方程**, 当 $N=0$ 时, 方程退化为**非递归方程**
$$
y[n]=\sum_{k=0}^M\left(\frac{b_k}{a_0}\right)x[n-k]
$$
上式表征的系统称为**有限脉冲响应系统**.

**无限脉冲响应系统**见课本 P77 例 2.15.

#### 2.4.3 用微分和差分方程描述的一阶系统的方框图表示

$$
y[n]+ay[n-1]=bx[n]
$$

![image-20230522103950417](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230522103950417.png)
$$
\frac{\text dy(t)}{\text dt}+ay(t)=bx(t)
$$
![image-20230522104002771](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230522104002771.png)

## Chap.3 周期信号的傅立叶级数表示

### 3.2 线性时不变系统对复指数信号的响应

若一个线性时不变系统对复指数信号的响应仍为复指数信号, 且只有幅度上的变化, 即
$$
e^{st}\rightarrow H(s)e^{st}\\
z^n\rightarrow H(z)z^n
$$
其中 $H(s), H(z)$ 为复振幅因子, 为 $s,z$ 的函数. 一个信号, 若系统对其输出响应仅为一个复常数成一输入, 则将该信号称为系统的**特征函数**, 幅度因子称为系统的**特征值**.

现考虑一个单位冲激响应为 $h(t)$ 的线性时不变系统, 若 $x(t)=e^{st}$ , 则有
$$
\begin{align}
y(t)
&=\int_{-\infty}^\infty h(\tau)x(t-\tau)\text d\tau\\
&=\int_{-\infty}^\infty h(\tau)e^{s(t-\tau)}\text d\tau\\
&=e^{st}\int_{-\infty}^\infty h(\tau)e^{-s\tau}\text d\tau\\
&=H(s)e^{st}\\
\end{align}
$$
其中
$$
H(s)=\int_{-\infty}^\infty h(\tau)e^{-s\tau}\text d\tau
$$
同理有离散形式,
$$
\begin{align}
y[n]
&=\sum_{k=-\infty}^\infty h[k]x[n-k]\\
&=\sum_{k=-\infty}^\infty h[k]z^{n-k}\\
&=z^n\sum_{k=-\infty}^\infty h[k]z^{-k}\\
&=H(z)z^n
\end{align}
$$
其中
$$
H(z)=\sum_{k=-\infty}^\infty h[k]z^{-k}
$$

#### 3.3.1 成谐波关系的复指数信号的线性组合

一个由成谐波关系的复指数线性组合形成的信号
$$
x(t)=\sum_{k=-\infty}^\infty a_ke^{jk\omega_0t}=\sum_{k=-\infty}^\infty a_ke^{jk(2\pi/T)t}
$$
上式中, $k=0$ 这项为常数, $k=\pm i$ 合称**基波分量**或者称为 **$i$ 次谐波分量**, 当一个信号表示为上式形式, 就称为**傅立叶级数**表示.

若 $x(t)$ 是一个实信号, 且能够表示成傅立叶级数表示, 由于 $x(t)=x^*(t)$, 故有
$$
\begin{align}
x(t)
&=\sum_{k=-\infty}^\infty a_k^*e^{-jk\omega_0t}\\
&=\sum_{k=-\infty}^\infty a_{-k}^*e^{jk\omega_0t}
\end{align}
$$
即
$$
a^*k=a_{-k}\\
a_k=a_{-k},\quad a_k为实数
$$
现给出傅立叶级数的另一种形式
$$
\begin{align}
x(t)
&=a_0+\sum_{k=1}^\infty \left[a_ke^{jk\omega_0t}+a_{-k}e^{-jk\omega_0t} \right]\\
&=a_0+\sum_{k=1}^\infty \left[a_ke^{jk\omega_0t}+a^*_ke^{-jk\omega_0t} \right]\\
&=a_0+\sum_{k=1}2\mathcal{Re}\{a_ke^{jk\omega_0t} \}
\end{align}
$$
若将 $a_k$ 以极坐标形式给出
$$
a_k=A_ke^{j\theta_k}
$$
则有
$$
\begin{align}
x(t)
&=a_0+\sum_{k=1}^\infty2\mathcal{Re}\{A_ke^{j(k\omega_0t+\theta_k)} \}\\
&=a_0+2\sum_{k=1}^\infty A_k\cos(k\omega_0t+\theta_k)
\end{align}
$$
上式为连续时间情况下, 对实周期信号常常见到的傅立叶级数的表达式.

若将 $a_k$ 以笛卡尔坐标形式表示, 则有
$$
a_k=B_k+jC_k\\
x(t)=a_0+2\sum_{k=1}^\infty[B_k\cos k\omega_0t-C_k\sin k\omega_0t]
$$

#### 3.3.2 连续时间周期信号傅立叶级数表示的确定

假设一个周期信号能表示成傅立叶级数形式, 有以下办法来确定系数

将式两边各乘以 $e^{-jn\omega_0t}$
$$
x(t)e^{-jn\omega_0t}=\sum_{k=-\infty}^\infty a_ke^{jk\omega_0t}e^{jn\omega_0t}
$$
将上式两边从 $0\sim T=2\pi/\omega_0$ 对 $t$ 积分
$$
\begin{align}
\int_0^Tx(t)e^{-jn\omega_0t}\text dt&=\int_0^T\sum_{k=-\infty}^\infty a_ke^{jk\omega_0t}e^{-jn\omega_0t}\text dt\\
&=\sum_{k=-\infty}^\infty a_k\left[\int_0^Te^{j(k-n)\omega_0t}\text dt \right]\\
\end{align}
$$
解积分有
$$
\int_0^Te^{j(k-n)\omega_0t}=\int_0^T\cos(k-n)\omega_0t\text dt+j\int_0^T\sin(k-n)\omega_0t\text dt
$$
分类讨论可得
$$
\int_0^Te^{j(k-n)\omega_0t}\text dt=\left\{
\begin{align}
T,&\quad k=n\\
0,&\quad k\neq n
\end{align}
\right.
$$
因此右边化为 $Ta_n$, 故有
$$
a_n=\frac1T\int_0^Tx(t)e^{-jn\omega_0t}\text dt
$$
其中 $(0,T)$ 可置换为任意一个 $T$ 间隔内区间, 若以 $\int_T$ 表示, 归纳则有:

**对于一个周期连续时间信号的傅立叶级数**
$$
x(t)=\sum_{k=-\infty}^\infty a_ke^{jk\omega_0t}=\sum_{k=-\infty}^\infty a_ke^{jk(2\pi/T)t} \tag{1}
$$
$$
a_k=\frac1T\int_T x(t)e^{-jk\omega_0t}\text dt=\frac1T\int_T x(t)e^{-jk(2\pi/T)t}\text dt \tag{2}
$$

式 (1) 称为**综合公式**, 式 (2) 称为**分析公式**, 系数 $\{a_k\}$ 称为 $x(t)$ 的**傅立叶级数系数**, 或称为**频谱系数**

其中
$$
a_0=\frac1T\int_Tx(t)\text dt
$$

### 3.4 傅立叶级数的收敛

可以用傅立叶级数表示的一类周期信号 $x(t)$ 是它在一个周期内能量有限的信号, 即
$$
\int_T|x(t)|^2\text dt<\infty
$$
**狄里赫利条件**

- 在任何周期内, $x(t)$ 必须绝对可积, 即
  $$
  \int_T|x(t)|\text dt<\infty
  $$
  与平方可积条件相同.

- 在任意有限区间内, $x(t)$ 具有有限个起伏变化; 也就是说, 在任何单个周期内, $x(t)$ 的最大值和最小值数目有限.

- 在任意有限区间内, $x(t)$ 仅有有限个不连续点, 且这些不连续点上函数为有限值

### 3.5 连续时间傅立叶级数性质

#### 3.5.1 线性性质

$$
z(t)=Ax(t)+By(t)\xleftrightarrow{\mathcal{FS}}c_k=Aa_k+Bb_k
$$

#### 3.5.2 时移性质

若周期信号 $x(t)$ 时不变, 故 $y(t)=x(t-t_0)$ 的傅立叶级数可表示为
$$
b_k=\frac1T\int_Tx(t-t_0)e^{-jk\omega_0t}\text dt
$$
令 $\tau=t-t_0$, 有
$$
\begin{align}
\frac1T\int_Tx(\tau)e^{-jk\omega_0(\tau+t_0)}\text d\tau
&=e^{-jk\omega_0t_0}\frac1T\int_Tx(\tau)e^{-jk\omega_0\tau}\text d\tau\\
&=e^{-jk\omega_0t_0}a_k=e^{-jk(2\pi/T)t_0}a_k
\end{align}
$$
也就是说, 若
$$
x(t)\xleftrightarrow{\mathcal{FS}}a_k
$$
则有
$$
x(t-t_0)\xleftrightarrow{\mathcal{FS}}e^{-jk\omega_0t_0}a_k=e^{-jk(2\pi/T)t_0}a_k
$$
即傅立叶级数系数的模保持不变, $|b_k|=|a_k|$

#### 3.5.3 时间反转

$$
x(t)\xleftrightarrow{\mathcal{FS}}a_k\\
x(-t)\xleftrightarrow{\mathcal{FS}}a_{-k}
$$

若 $x(t)$ 为奇/偶函数, 有
$$
a_{-k}=-a_k,&\quad 奇函数\\
a_{-k}=a_k,&\quad 偶函数
$$

#### 3.5.4 时域尺度变换

$$
x(\alpha t)=\sum_{k=-\infty}^\infty a_ke^{jk(\alpha\omega_0)t}
$$

#### 3.5.5 相乘

$$
x(t)y(t)\xleftrightarrow{\mathcal{FS}}h_k=\sum_{l=-\infty}^\infty a_kb_{k-l}
$$

#### 3.5.6 共轭及共轭对称

$$
x(t)\xleftrightarrow{\mathcal{FS}}a_k\\
x^*(t)\xleftrightarrow{\mathcal{FS}}a^*_{-k}
$$

当 $x(t)$ 为实函数时, 其共轭对称, 即
$$
a_k=a^*_{-k}
$$

#### 3.5.7 连续时间周期信号的帕斯瓦尔定理

$$
\frac1T\int_T|x(t)|^2\text dt=\sum_{k=-\infty}^\infty|a_k|^2\\
\frac1T\int_T|a_ke^{jk\omega_0t}|^2\text dt=\frac1T\int_T|a_k|^2\text dt=|a_k|^2
$$

#### 3.5.8 连续时间傅立叶级数性质表

*page 130*

### 3.6 离散时间周期信号的傅立叶级数表示

一个离散时间周期信号的傅立叶级数是有限项级数, 而连续时间周期信号的是无穷级数

#### 3.6.1 成谐波关系的复指数信号的信号组合

由 1.3.3 可知, 对于
$$
\phi_k[n]=e^{jk\omega_0n}=e^{jk(2\pi/N)n}
$$
有
$$
\phi_k[n]=\phi_{k+rN}[n],\quad r\in\mathbb{R}
$$
故可有**离散时间傅立叶级数**
$$
x[n]=\sum_{k=\langle N\rangle}a_k\phi_k[n]=\sum_{k=\langle N\rangle}a_ke^{jk\omega_0n}=\sum_{k=\langle N\rangle}a_ke^{jk(2\pi/N)n}
$$

#### 3.6.2 周期信号傅立叶级数表示的确定

与连续时间周期信号类似, **有离散时间傅立叶级数对**
$$
x[n]=\sum_{k=\langle N\rangle}a_ke^{jk\omega_0n}=\sum_{k=\langle N\rangle}a_ke^{jk(2\pi/N)n}\\
a_k=\frac1N\sum_{n=\langle N\rangle}x[n]e^{-jk\omega_0n}=\frac1N\sum_{n=\langle N\rangle}x[n]e^{-jk(2\pi/N)n}
$$

### 3.7 离散时间傅立叶级数性质

*page 140*

#### 3.7.1 相乘

$$
x[n]y[n]\xleftrightarrow{\mathcal{FS}}d_k=\sum_{l=\langle N\rangle}a_lb_{k-l}
$$

#### 3.7.2 一次差分

$$
x[n]-x[n-1]\xleftrightarrow{\mathcal{FS}}(1-e^{-jk(2\pi/N)})a_k
$$

#### 3.7.3 离散时间周期信号的帕斯瓦尔定理

$$
\frac1N\sum_{n=\langle N\rangle}|x[n]|^2=\sum_{k=\langle N\rangle}|a_k|^2
$$

### 3.9 滤波

改变一个信号中各频率分量的相对大小, 或者消除全部某些频率分量, 这种过程称为**滤波**

用于改变频谱形状的线性时不变系统称为**频率成型滤波器**

基本上无失真地通过某些频率, 而显著的衰减掉或消除掉另一些频率的系统称为**频率选择性滤波器**

## Chap.4 连续时间傅立叶变换

### 4.1 非周期信号的表示: 连续时间傅立叶变换

#### 4.1.1 非周期信号傅立叶变换的导出

建立非周期信号的傅立叶变换时, 可以把非周期信号当成一个周期信号在周期任意大时的极限来对待, 并且研究这个周期信号傅立叶级数表示式的极限特性.

随着 $T\rightarrow\infty$, 对于任意有限时间的 $t$ 而言, $\tilde x(t)=x(t)$
$$
\tilde x(t)=\sum_{k=-\infty}^\infty a_ke^{jk\omega_0t}\\
a_k=\frac1T\int_{-T/2}^{T/2}\tilde x(t)e^{-jk\omega_0t}\text dt
$$
其中 $\omega_0=2\pi/T$, 由于在 $|t|<T/2$ 时 $\tilde x(t)=x(t)$, 而在其它情况下 $x(t)=0$, 故可重写为
$$
a_k=\frac1T\int_{-T/2}^{T/2}x(t)e^{-jk\omega_0t}\text dt=\frac1T\int_{-\infty}^\infty x(t)e^{-jk\omega_0t}\text dt
$$
因此, 定义 $Ta_k$ 的包络 $X(j\omega)$ 为
$$
X(j\omega)=\int_{-\infty}^\infty x(t)e^{-j\omega t}\text dt
$$
故
$$
a_k=\frac1TX(jk\omega_0)
$$
$\tilde x(t)$ 就可以用 $X(j\omega)$ 表示为
$$
\begin{align}
\tilde x(t)&=\sum_{k=-\infty}^\infty\frac1TX(jk\omega_0)e^{jk\omega_0t}\\
&=\frac1{2\pi}\sum_{k=-\infty}^\infty X(jk\omega_0)e^{jk\omega_0t}
\end{align}
$$

$$
x(t)=\lim_{T\rightarrow\infty}\tilde x(t)=\frac1{2\pi}\int_{-\infty}^\infty X(j\omega)e^{j\omega t}\text d\omega
\tag{1}
$$
$$
X(j\omega)=\int_{-\infty}^\infty x(t)e^{-j\omega t}\text dt
\tag{2}
$$
$$
a_k=\left.\frac1TX(j\omega)\right|_{\omega=k\omega_0} \tag{3}
$$

式 (1)(2) 称为**傅立叶变换对**, 函数 $X(j\omega)$ 称为 $x(t)$ 的**傅立叶变换**或**频谱**, 式 (2) 称为**傅立叶逆变换**

#### 4.1.2 傅立叶变换的收敛

**狄里赫利条件:**

- $x(t)$ 绝对可积, 即
  $$
  \int_{-\infty}^\infty|x(t)|\text dt<\infty
  $$

- 在任何有限区间内, $x(t)$ 仅有有限个最大值和最小值

- 在任何有限区间内, $x(t)$ 有有限个不连续点, 并且在每个不连续点都必须是有限值

### 4.2 周期信号的傅立叶变换

$$
x(t)=\sum_{k=-\infty}^\infty a_ke^{jk\omega_0t}\\
X(j\omega)=\sum_{k=-\infty}^\infty2\pi a_k\delta(\omega-k\omega_0)\\
x(t)=\frac1{2\pi}\int_{-\infty}^\infty X(j\omega)e^{j\omega t}\text d\omega\\
X(j\omega)=\int_{-\infty}^\infty x(t)e^{-j\omega t}\text dt
$$

### 4.3 连续时间傅立叶变换性质

- 4.3.1 线性性质
- 4.3.2 时移性质
- 4.3.3 共轭与共轭对称性

#### 4.3.4 微分与积分

$$
\boxed{
\frac{\text dx(t)}{\text dt}\xleftrightarrow{\mathcal{F}}j\omega X(j\omega)
}
$$

$$
\boxed{
\int_{-\infty}^tx(\tau)\text d\tau\xleftrightarrow{\mathcal{F}}\frac1{j\omega}X(j\omega)+\pi X(0)\delta(\omega)
}
$$

##### 4.3.5 时间与频率的尺度变换

$$
\boxed{
x(\alpha t)\xleftrightarrow{\mathcal{F}}\frac1{|\alpha|}X\left(\frac{j\omega}\alpha \right)
}
$$

#### 4.3.6 对偶性

对于傅立叶变换的综合和分析公式
$$
x(t)=\frac1{2\pi}\int_{-\infty}^\infty X(j\omega)e^{j\omega t}\text d\omega\\
X(j\omega)=\int_{-\infty}^\infty x(t)e^{-j\omega t}\text dt
$$
两式形式相似, 但不完全一样. 这一对称性导致了傅立叶变换的一个性质, 称为对偶性.

结合例子说明:

考虑如下信号
$$
g(t)=\frac2{1+t^2}
$$
设信号 $x(t)$ , 其傅立叶变换是
$$
X(j\omega)=\frac2{1+\omega^2}\\
x(t)=e^{-|t|}\xleftrightarrow{\mathcal{F}}X(j\omega)=\frac2{1+\omega^2}
$$
故有综合公式
$$
e^{-|t|}=\frac1{2\pi}\int_{-\infty}^\infty\left(\frac2{1+\omega^2} \right)e^{j\omega t}\text d\omega
$$
$t\rightarrow -t$, 变形可得
$$
2\pi e^{-|t|}=\int_{-\infty}^\infty\left(\frac2{1+\omega^2} \right)e^{-j\omega t}\text d\omega
$$
交换 $t,\omega$ 可得
$$
2\pi e^{-|\omega|}=\int_{-\infty}^\infty\left(\frac2{1+t^2}\right)e^{-j\omega t}\text dt
$$
可得
$$
F\left\{\frac2{1+t^2} \right\}=2\pi e^{-|\omega|}
$$


#### 4.3.7 帕斯瓦尔定理

$$
\int_{-\infty}^\infty|x(t)|^2\text dt=\frac1{2\pi}\int_{-\infty}^\infty |X(j\omega)|^2\text d\omega
$$

### 4.4 卷积性质

$$
y(t)=h(t)*x(t)\xleftrightarrow{\mathcal{F}}Y(j\omega)=H(j\omega)X(j\omega)
$$

### 4.5 相乘性质

$$
r(t)=s(t)p(t)\leftrightarrow R(j\omega)=\frac1{2\pi}\int_{-\infty}^\infty S(j\theta)P(j\omega-j\theta)\text d\theta
$$

两个信号相乘称为**幅度调制**, 上式称为**调制性质**

## Chap.5 离散时间傅立叶变换

### 5.1 非周期信号的表示: 离散时间傅立叶变换

#### 5.1.1 离散时间傅立叶变换的导出

$$
a_k=\frac1N\sum_{n=\langle N\rangle}\tilde x[n]e^{-jk(2\pi/N)n}\\
x[n]=\frac1{2\pi}\int_{2\pi}X(e^{j\omega})e^{j\omega n}\text d\omega\\
X(e^{j\omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\omega n}
$$

### 5.2 周期信号的傅立叶变换

$$
x[n]=\sum_{k=\langle N\rangle}a_ke^{jk(2\pi/N)n}\\
X(e^{j\omega})=\sum_{k=-\infty}^\infty 2\pi a_k\delta(\omega-\frac{2\pi k}N)
$$

### 5.3 离散时间傅立叶变换性质

#### 5.3.1 离散时间傅立叶变换的周期性

$$
X(e^{j(\omega+2\pi)})=X(e^{j\omega})
$$

#### 5.3.2 线性性质

$$
ax_1[n]+bx_2[n]\xleftrightarrow{\mathcal{F}}aX_1(e^{j\omega})+bX_2(e^{j\omega})
$$

#### 5.3.3 时移与频移性质

$$
x[n-n_0]\xleftrightarrow{\mathcal{F}}e^{-j\omega n_0}X(e^{j\omega})\\
e^{j\omega_0n}x[n]\xleftrightarrow{\mathcal{F}}X(e^{j(\omega-\omega_0)})
$$

#### 5.3.4 共轭与共轭对称性

$$
x^*[n]\xleftrightarrow{\mathcal{F}}X^*(e^{-j\omega})\\
X(e^{j\omega})=X^*(e^{-j\omega})\qquad x[n]为实值
$$

同时即有,

- $\mathcal{Re}\{X(e^{j\omega})\}$ 为 $\omega$ 的偶函数
- $\mathcal{Im}\{X(e^{j\omega}) \}$ 为 $\omega$ 的奇函数
- $X(e^{j\omega})$ 的模为 $\omega$ 的偶函数
- $X(e^{j\omega})$ 的相角为 $\omega$ 的奇函数

进一步有
$$
\mathcal{Ev}\{x[n] \}\xleftrightarrow{\mathcal{F}}\mathcal{Re}\{X(e^{j\omega}) \}\\
\mathcal{Od}\{x[n]\}\xleftrightarrow{\mathcal{F}}j\mathcal{Im}\{X(e^{j\omega}) \}
$$

#### 5.3.5 差分与累加

$$
x[n]-x[n-1]\xleftrightarrow{\mathcal F}(1-e^{-j\omega})X(e^{j\omega})\\
\sum_{m=-\infty}^n x[m]\xleftrightarrow{\mathcal F}\frac1{1-e^{-j\omega}}X(e^{j\omega})+\pi X(e^{j0})\sum_{k=-\infty}^\infty\delta(\omega-2\pi k)
$$

#### 5.3.6 时间反转

$$
x[-n]\xleftrightarrow{\mathcal F}X(e^{-j\omega})
$$

#### 5.3.7 时域扩展

若令 $k$ 为正整数, 并定义
$$
x_{(k)}[n]=\left\{
\begin{align}
x[n/k],&\qquad n为k的整倍数\\
0,&\qquad n不为k的整倍数
\end{align}
\right.
$$
由于 $x_{(k)}[rk]=x[r]$, 故有
$$
\begin{align}
X_{(k)}(e^{j\omega})
&=\sum_{n=-\infty}^\infty x_{(k)}[n]e^{-j\omega n}=\sum_{r=-\infty}^\infty x_{(k)}[rk]e^{-j\omega rk}\\
&=\sum_{r=-\infty}^\infty x[r]e^{-j(k\omega)r}=X(e^{jk\omega})
\end{align}
$$
即有
$$
x_{(k)}[n]\xleftrightarrow{\mathcal F}X(e^{jk\omega})
$$

#### 5.3.8 频域微分

$$
nx[n]\xleftrightarrow{\mathcal F}j\frac{\text dX(e^{j\omega})}{\text d\omega}
$$

#### 5.3.9 帕斯瓦尔定理

$$
\sum_{n=-\infty}^\infty|x[n]|^2=\frac1{2\pi}\int_{2\pi}|X(e^{j\omega})|^2\text d\omega
$$

### 5.4 卷积性质

若有
$$
y[n]=x[n]*h[n]
$$
则有
$$
Y(e^{j\omega})=X(e^{j\omega})H(e^{j\omega})
$$

### 5.5 相乘性质

若有
$$
y[n]=x_1[n]x_2[n]
$$
则有
$$
Y(e^{j\omega})=\frac1{2\pi}\int_{2\pi}X_1(e^{j\theta})X_2(e^{j(\omega-\theta)})\text d\theta
$$

### 5.7 对偶性

#### 5.7.1 离散时间傅立叶级数的对偶性

对于
$$
x[n]\xleftrightarrow{\mathcal{FS}}a_k
$$
由于离散时间周期信号的傅立叶级数系数本身就是一个周期序列
$$
g[n]\xleftrightarrow{\mathcal{FS}}f[k]
$$
若令 $m=n,r=-k$ 则有
$$
f[n]=\sum_{k=\langle N\rangle}\frac1Ng[-k]e^{jk(2\pi/N)n}
$$
与下式比较
$$
x[n]=\sum_{k=\langle N\rangle}a_ke^{jk(2\pi/N)n}
$$
可知
$$
f[n]\xleftrightarrow{\mathcal{FS}}\frac1Ng[-k]
$$

#### 5.7.2 离散时间傅立叶变换和连续时间傅立叶级数之间的对偶性

重新写出以下公式
$$
x[n]=\frac1{2\pi}\int_{2\pi}X(e^{j\omega})e^{j\omega n}\text d\omega\tag 1
$$

$$
X(e^{j\omega})=\sum_{n=-\infty}^\infty x[n]e^{-j\omega n}\tag 2
$$

$$
x(t)=\sum_{k=-\infty}^\infty a_ke^{jk\omega_0t}\tag3
$$

$$
a_k=\frac1T\int_Tx(t)e^{-jk\omega_0t}\text dt\tag4
$$

有例子如下:

对于信号
$$
x[n]=\frac{\sin(\pi n/2)}{\pi n}
$$
为了利用对偶性, 可列周期信号如下
$$
g(t)=\left\{
\begin{align}
1,&\qquad |t|\leq T_1\\
0,&\qquad T_1<|t|\leq\pi
\end{align}
\right.
$$
若要令 $a_k=x[k]$, 则有 $T_1=\pi/2$, 即有分析公式 (4)
$$
\frac{\sin(\pi k/2)}{\pi k}=\frac1{2\pi}\int_{-\pi}^\pi g(t)e^{-jkt}\text dt=\frac1{2\pi}\int_{-\pi/2}^{\pi/2}(1)e^{-jkt}\text dt
$$
将 $k\rightarrow n,t\rightarrow \omega$, 则有
$$
\frac{\sin(\pi k/2)}{\pi k}=\frac1{2\pi}\int_{-\pi/2}^{\pi/2}(1)e^{-jn\omega}\text d\omega
$$
$n\rightarrow -n$, 并由于 sinc 函数是偶函数, 有
$$
\frac{\sin(\pi n/2)}{\pi n}=\frac1{2\pi}\int_{-\pi/2}^{\pi/2}(1)e^{jn\omega}\text d\omega
$$
故形似式 (1), 有
$$
X(e^{j\omega})=\left\{
\begin{align}
1,&\qquad |\omega|\leq\pi/2\\
0,&\qquad \pi/2<|\omega|\leq\pi
\end{align}
\right.
$$

### 5.8 由线性常系数差分方程表征的系统

对于一个线性时不变系统, 其输出 $y[n]$ 和输入 $x[n]$ 之间的线性常系数差分方程一般具有如下形式:
$$
\sum_{k=0}^Na_ky[n-k]=\sum_{k=0}^Mb_kx[n-k]
$$
设 $X(e^{j\omega}),Y(e^{j\omega}),H(e^{j\omega})$ 分别为输入 $x[n]$, 输出 $y[n]$, 和单位脉冲响应 $h[n]$ 的傅立叶变换, 那么离散时间傅立叶变换的卷积性质意味着有
$$
H(e^{j\omega})=\frac{Y(e^{j\omega})}{X(e^{j\omega})}
$$
两边应用傅立叶变换, 并利用线性和时移性质, 有
$$
\sum_{k=0}^Na_ke^{-jk\omega}Y(e^{j\omega})=\sum_{k=0}^Mb_ke^{-jk\omega}X(e^{j\omega})
$$
或者等效为
$$
H(e^{j\omega})=\frac{Y(e^{j\omega})}{X(e^{j\omega})}=\frac{\sum_{k=0}^Mb_ke^{-jk\omega}}{\sum_{k=0}^Na_ke^{-jk\omega}}
$$
与连续时间情况下一样, $H(e^{j\omega})$ 是两个多项式的比, 但是在离散时间情况下, 多项式变量为 $e^{-j\omega}$

有如下例子:

考虑一个因果线性时不变系统, 其差分方程为
$$
y[n]-\frac34y[n-1]+\frac18y[n-2]=2x[n]
$$
由 $H(e^{j\omega})=Y(e^{j\omega})/X(e^{j\omega})$ 可知, 频率响应为
$$
\begin{align}
H(e^{j\omega})
&=\frac2{1-\frac34e^{-j\omega}+\frac18e^{-j2\omega}}\\
&=\frac2{(1-\frac12e^{-j\omega})(1-\frac14e^{-j\omega})}\\
&=\frac4{1-\frac12e^{-j\omega}}-\frac2{1-\frac14e^{-j\omega}}
\end{align}
$$
故有
$$
h[n]=4\cdot2^{-n}u[n]-2\cdot4^{-n}u[n]
$$
若输入信号为
$$
x[n]=4^{-n}u[n]
$$
故有
$$
\begin{align}
Y(e^{j\omega})=H(e^{j\omega})X(e^{j\omega})
&=\left[\frac2{(1-\frac12e^{-j\omega})(1-\frac14e^{-j\omega})}\right]\left[\frac1{1-\frac14e^{-j\omega}}\right]\\
&=\frac2{(1-\frac12e^{-j\omega})(1-\frac14e^{-j\omega})^2}
\end{align}
$$
参考附录给出的方法, 展开有
$$
Y(e^{j\omega})=\frac{-4}{1-\frac14e^{-j\omega}}+\frac{-2}{(1-\frac14e^{-j\omega})^2}+\frac8{1-\frac12e^{-j\omega}}
$$
从而求逆变换得出
$$
y[n]=\left\{
-4\cdot4^{-n}-2(n+1)\cdot4^{-n}+8\cdot2^{-n}
\right\}u[n]
$$

## Chap.6 信号与系统的时域和频域特性

### 6.1 傅立叶变换的模和相位表示

$$
X(j\omega)=|X(j\omega)|e^{j\sphericalangle X(j\omega)}\\
X(e^{j\omega})=|X(e^{j\omega})|e^{j\sphericalangle X(e^{j\omega})}
$$

- $X(j\omega)$ 本身可以看成信号 $x(t)$ 的一种分解, 即把信号分解成不同频率的复指数之 “和”
- 由 $\sphericalangle X(j\omega)$ 所代表的相位关系对信号 $x(t)$ 的本质属性有显著影响, 包含了大量信息
- $X(j\omega)$ 的相位函数的变化可能会导致信号 $x(t)$ 时域特性的改变

### 6.2 线性时不变系统频率响应的模和相位表示

根据卷积性质, 有
$$
|Y(j\omega)|=|H(j\omega)||X(j\omega)|\\
\sphericalangle Y(j\omega)=\sphericalangle H(j\omega)+\sphericalangle X(j\omega)
$$
~~P.S. 离散时间下有完全类似的关系~~

$|H(j\omega)|$ 一般称为系统的**增益**, $\sphericalangle H(j\omega)$ 一般称为系统的**相移**, 由上两式产生的影响一般称为幅度和相位**失真**

#### 6.2.1 线性与非线性相位

系统在各个地方都具有单位增益, 这样的系统称为**全通**系统

#### 6.2.2 群时延

若有一个窄带信号 $x(t)$ 作为输入, 即该信号的傅立叶变换在 $\omega=\omega_0$ 为中心的一个很小的频率范围以外都是零或非常小, 就可以将该系统的相位特性用线性关系来近似, 有
$$
\sphericalangle H(j\omega)\simeq=-\phi-\omega\alpha
$$
故有
$$
Y(j\omega)\simeq X(j\omega)|H(j\omega)|e^{-j\phi}e^{-j\omega\alpha}
$$
即为, 对应于 $|H(j\omega)|$ 的幅度成型部分, 乘以一个总的恒定复数因子 $e^{-j\phi}$ 以及对应于延时 $\alpha$ 秒的线性项移项 $e^{-j\omega\alpha}$. 这个时延称为在 $\omega=\omega_0$ 的**群时延**, 若将 $\sphericalangle H(j\omega)$ 的值限制在 $(-\pi,\pi)$ 中, 则称为**主值相位** (即将相位取 $2\pi$ 模)

每个频率上的群时延等于该频率上相位特性斜率的负值, 即**群时延定义**为
$$
\tau(\omega)=-\frac{\text d}{\text d\omega}\{\sphericalangle H(j\omega) \}
$$

#### 6.2.3 对数模和相位图

注意到有
$$
\log|Y(j\omega)|=\log|H(j\omega)|+\log|X(j\omega)|
$$
一般采用的对数标尺是以 $20\log_{10}$ 为单位的, 称为分贝dB. $20\log_{10}|H(j\omega)|$ 和 $\sphericalangle H(j\omega)$ 对于 $\log_{10}(\omega)$ 的图称为**伯德图**

![image-20230609103341585](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230609103341585.png)

### 6.3 理想频率选择性滤波器的时域特性

理想低通滤波器的单位阶跃响应
$$
s(t)=\int_{-\infty}^th(\tau)\text d\tau\\
s[n]=\sum_{m=-\infty}^nh[m]
$$

- 振铃: 滤波器阶跃后的振荡

  ![image-20230612001131087](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230612001131087.png)

- 上升时间: 正比于 $\pi/\omega$

## Chap.7 采样

### 7.1 用信号样本表示连续时间信号: 采样定理

若一个信号是带限的 (即它的傅立叶变换在某一有限频带范围以外均为零), 并且它的样本取得足够密 (相对于信号中最高的频率而言), 那么这些样本值就能**唯一的**用来表征这一信号, 并且能从这些样本中把信号完全恢复出来, 这一结果就是**采样定理**.

#### 7.1.1 冲激串采样

通过一个周期冲激串去乘待采样的连续时间信号, 称为**冲激串采样**

该周期冲激串 $p(t)$ 称为**采样函数**, 周期 $T$ 称为**采样周期**, 而基波频率 $\omega_s=2\pi/T$ 称为**采样频率**
$$
x_p(t)=x(t)p(t)
$$
其中
$$
p(t)=\sum_{n=-\infty}^\infty\delta(t-nT)
$$
分析可得
$$
x_p(t)=\sum_{n=-\infty}^\infty x(nT)\delta(t-nT)\\
X_p(t)=\frac1{2\pi}\int_{-\infty}^\infty X(j\omega)P(j(\omega-\theta))\text d\theta
$$
其中
$$
P(j\omega)=\frac{2\pi}T\sum_{k=-\infty}^\infty\delta(\omega-k\omega_s)
$$
因为信号与一个单位冲激函数的卷积就是该信号的移位
$$
X(j\omega)*\delta(\omega-\omega_0)=X(j(\omega-\omega_0))
$$
故有
$$
X_p(j\omega)=\frac1T\sum_{k=-\infty}^\infty X(j(\omega-k\omega_s))
$$
意味着 $X_p(j\omega)$ 是 $\omega$ 的周期函数, 这一结果称为**采样定理**.

![image-20230612005945439](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230612005945439.png)

**采样定理:**

设 $x(t)$ 是某一个带限信号, 在 $|\omega|>\omega_M$ 时, $X(j\omega)=0$. 如果 $\omega_s>2\omega_M$, 其中 $\omega_s=2\pi/T$, 那么 $x(t)$ 就唯一的由其样本 $x(nT),\quad n=0,\pm1,\pm2,\cdots$ 所确定

已知这些样本值, 我们能用如下办法重建 $x(t)$: 产生一个周期冲激串, 其冲激幅度就是这些依次而来的样本值, 然后将该冲激串通过一个增益为 $T$, 截止频率大于 $\omega_M$ 而小于 $\omega_s-\omega_M$ 的理想低通滤波器, 该滤波器的输出就是 $x(t)$

$2\omega_M$ 一般称为**奈奎斯特率**

#### 7.1.2 零阶保持采样

**零阶保持采样:** 在一个给定的瞬时对 $x(t)$ 采样并保持着一样本值, 直到下一个样本被采为止
$$
H_0(j\omega)=e^{-j\omega T/2}\left[\frac{2\sin(\omega T/2)}{\omega} \right]
$$
若给出 $H_r(j\omega)$ 使得 $r(t)=x(t)$ 则有
$$
H_r(j\omega)=\frac{e^{j\omega T/2}H(j\omega)}{\frac{2\sin(\omega T/2)}\omega}
$$

### 7.2 利用内插由样本重建信号

**内插**

用一连续信号对一组样本值的拟合

**线性内插** 

将相邻的样本点用直线直接连接起来, 若采样足够密, 那么信号就能被完全恢复
$$
x_r(t)=x_p(t)*h(t)
$$
将 $x_p(t)$ 代入可得
$$
x_r(t)=\sum_{n=-\infty}^\infty x(nT)h(t-nT)
$$
上式体现在样本点 $x(nT)$ 之间如何拟合成一条连续曲线, 代表一种内插公式, 对于理想低通滤波器 $H(j\omega)$
$$
h(t)=\frac{\omega_cT\sin(\omega_ct)}{\pi\omega_ct}
$$
故有
$$
x_r(t)=\sum_{n=-\infty}^\infty x(nT)\frac{\omega_cT}\pi\frac{\sin(\omega_c(t-nT))}{\omega_c(t-nT)}
$$
如上式, 利用理想低通滤波器的单位冲激响应的内插通常称为**带限内插**, 该种内插只要 $x(t)$ 是带限的, 而采样频率满足条件, 就能真正重建信号.

若由零阶保持给出的粗糙内插令人不够满意, 则能使用**高阶保持**, 线性内插 (有时称为一阶保持), 其传输函数为
$$
H(j\omega)=\frac1T\left[\frac{\sin(\omega T/2)}{\omega/2} \right]^2
$$

### 7.3 欠采样的效果: 混叠现象

$\omega_s<2\omega_M$ 时, $x(t)$ 的频谱 $X(j\omega)$ 不再在 $X_p(j\omega)$ 中重复, 一次利用低通滤波也不再能恢复原信号, 这一现象称为**混叠**.

## Chap.8 通信系统

- 调制: 讲一个载有信息的信号嵌入另一个信号
- 解调: 将载有信息的信号提取出来
- 复用: 将多个频谱重叠的信号在同一信道上同时传输

### 8.1 复指数与正弦幅度调制

信号 $x(t)$ 称为**调制信号**, 信号 $c(t)$ 称为**载波信号**, 信号 $y(t)$ 称为已调信号
$$
y(t)=x(t)c(t)
$$

#### 8.1.1 复指数载波的幅度调制

正弦幅度调制有两种常用形式
$$
c(t)=e^{j(\omega_ct+\theta_c)}\\
c(t)=\cos(\omega_ct+\theta_c)
$$
$\omega_c$ 称为**载波频率**, 先考虑复指数载波的情况, 选 $\theta_c=0$
$$
y(t)=x(t)e^{j\omega_ct}\\
y(t)=x(t)\cos\omega_ct+jx(t)\sin\omega_ct
$$
根据相乘性质有
$$
Y(j\omega)=\frac1{2\pi}\int_{-\infty}^\infty X(j\theta)C(j(\omega-\theta))\text d\theta
$$
若 $c(t)$ 为第一种形式给出
$$
C(j\omega)=2\pi\delta(\omega-\omega_c)
$$
故有
$$
Y(j\omega)=X(j\omega-j\omega_c)
$$

#### 8.1.2 正弦载波的幅度调制

考虑正弦载波的情况, $\theta_c=0$
$$
C(j\omega)=\pi[\delta(\omega-\omega_c)+\delta(\omega+\omega_c)]
$$
故有
$$
Y(j\omega)=\frac12[X(j\omega-j\omega_c)+X(j\omega+j\omega_c)]
$$

### 8.2 正弦幅度调制的解调

同步/不同步 解调: 发射接收相位 同步/不同步

#### 8.2.1 同步解调

假设 $\omega_c>\omega_M$, 将一个一条信号进行解调考虑如下进程:

由于
$$
y(t)=x(t)\cos\omega_ct
$$
设
$$
w(t)=y(t)\cos\omega_ct=x(t)\cos^2\omega_ct
$$
利用三角恒等式有
$$
\cos^2\omega_ct=\frac12+\frac12\cos2\omega_ct
$$
就可重写为
$$
w(t)=\frac12x(t)+\frac12x(t)\cos2\omega_ct
$$
![image-20230612162559619](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230612162559619.png)

对 $w(t)$ 应用低通滤波器就相当于保留第一项, 去除第二项

![image-20230612164440124](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230612164440124.png)

上述两种系统, 都假设解调器载波在相位上与调制器载波是同相的, 因为这一过程称为**同步解调**.

### 8.3 频分多路复用

如果有频谱互相重叠的单个声音信号, 利用正弦幅度调制把他们的频谱在频率上进行搬移, 使这些已调信号的频谱不在重叠, 就能够在同一个宽带信道上同时传输这些信号, 称为**频分多路复用**.

​	![image-20230612170208410](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230612170208410.png)

### 8.4 单边带正弦幅度调制

**单/双边带调制**

![image-20230612171048074](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230612171048074.png)

利用边带滤波器来得到单边带

![image-20230612174751873](/Users/qiu_nangong/Library/Application Support/typora-user-images/image-20230612174751873.png)

### 8.5 用脉冲串进行载波的幅度调制

若 $x(t)$ 是带限的, 且脉冲重复频率足够高, 那么信号就能从样本中恢复.
$$
y(t)=x(t)c(t)
$$
由相乘性质
$$
Y(j\omega)=\frac1{2\pi}\int_{-\infty}^\infty X(j\theta)C(j(\omega-\theta))\text d\theta
$$
由于 $c(t)$ 周期为 $T$, 故 $C(j\omega)$ 就是由在频域中相隔 $2\pi/T$ 的冲激所组成的, 即
$$
C(j\omega)=2\pi\sum_{k=-\infty}^\infty a_k\delta(\omega-k\omega_c)
$$
其中 $\omega_c=2\pi/T$, 系数 $a_k$ 为 $c(t)$ 的傅立叶级数
$$
a_k=\frac{\sin(k\omega_c\Delta/2)}{\pi k}
$$
$\omega_c=2\pi/T>2\omega_M$ 时, 信号可恢复, 低通滤波器截止频率 $\omega$ 满足 $\omega_M<\omega<\omega_c-\omega_M$

#### 8.5.2 时分多路复用

每一路信号被安排在一组持续期为 $\Delta$ 的时隙内, 每 $T$ 秒重复一次, 并且不与其他路信号的时隙相重合, 这一过程称为**时分多路复用**

### 8.6 脉冲幅度调制

#### 8.6.1 脉冲幅度已调信号

