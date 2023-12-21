---
layout: post
title: Fourier Transform
description: An introduction to fourier transform in image processing.
tags: fourier-transform
categories: image-processing
related_posts: false
giscus_comments: true
thumbnail: 
toc:
    enable: true
    number: false
    auto: true
---
# 傅里叶变换

## 基本公式

### 欧拉公式

$$
\begin{aligned}
e^{j\theta} &= \cos\theta + j\sin\theta \\
e^{-j\theta} &= \cos(-\theta) + j\sin(-\theta)\\
&= \cos\theta - j\sin\theta \\
e^{j\pi} &= \cos\pi + j\sin\pi = -1 \\
e^{j\pi x} &= \cos\pi x + j\sin\pi x = (-1)^x \\
\end{aligned}
$$

### 连续傅里叶变换

一维连续傅里叶变换公式及其反变换公式：

$$
\begin{aligned}
\mathfrak{J}\{f(t)\}  = \int_{-\infty}^{\infty} f(t) e^{-j2\pi ut} dt &= F(u) \\
\mathfrak{J}^{-1}\{F(u)\} = \int_{-\infty}^{\infty} F(u) e^{j2\pi ut} du &= f(t) 
\end{aligned}
$$

二维连续傅里叶变换公式及其反变换公式：

$$
\begin{aligned}
F(u,v) &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j2\pi(ux+vy)} dx dy \\
f(x,y) &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} F(u,v) e^{j2\pi(ux+vy)} du dv
\end{aligned}
$$

### 离散傅里叶变换

一维离散傅里叶变换公式及其反变换公式：

$$
\begin{aligned}
F(u) &= \frac{1}{N}\sum_{x=0}^{N-1} f(x) e^{-j2\pi ux/N} \\
f(x) &= \sum_{u=0}^{N-1} F(u) e^{j2\pi ux/N}
\end{aligned}
$$

可以看出$x$和$u$的取值范围都是$0,1,2,\cdots,N-1$，$x$是空间域的坐标，$u$是频率域的坐标。

二维离散傅里叶变换公式及其反变换公式：

$$
\begin{aligned}
F(u,v) &= \frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j2\pi(ux/M+vy/N)} \\
f(x,y) &= \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) e^{j2\pi(ux/M+vy/N)}
\end{aligned}
$$

易得：

$$
F(0,0) = \frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) = \bar{f}
$$

### 极坐标形式

令$\Re(u,v)$表示实部，$\Im(u,v)$表示虚部，那么有:

$$
\begin{aligned}
F(u,v) &= |F(u,v)|e^{j\phi(u,v)} &\text{极坐标形式} \\
|F(u,v)| &= \sqrt{\Re^2(u,v)+\Im^2(u,v)} &\text{幅度谱或频率谱} \\
\phi(u,v) &= \arctan\frac{\Im(u,v)}{\Re(u,v)} &\text{相角或相位谱} \\
P(u,v) &= |F(u,v)|^2 = \Re^2(u,v)+\Im^2(u,v) &\text{功率谱}
\end{aligned}
$$

## 基本性质



### 平移性

平移是针对离散傅里叶变换而言的，对连续时域的讨论见[时移](#时移)。

$$
\begin{aligned}
F(u-u_0,v-v_0) &= \frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j2\pi((u-u_0)x/M+(v-v_0)y/N)} \\
&= \frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j2\pi(ux/M+vy/N)} e^{j2\pi(u_0x/M+v_0y/N)} \\
&= \frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} [f(x,y)e^{j2\pi(u_0x/M+v_0y/N)}] e^{-j2\pi(ux/M+vy/N)} \\
&\Leftrightarrow f(x,y)e^{j2\pi(u_0x/M+v_0y/N)} \\
f(x-x_0,y-y_0) &= \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) e^{j2\pi(u(x-x_0)/M+v(y-y_0)/N)} \\
&= \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) e^{j2\pi(ux/M+vy/N)} e^{-j2\pi(ux_0/M+vy_0/N)} \\
&= \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} [F(u,v)e^{-j2\pi(ux_0/M+vy_0/N)}] e^{j2\pi(ux/M+vy/N)} \\
&\Leftrightarrow F(u,v)e^{-j2\pi(ux_0/M+vy_0/N)}
\end{aligned}
$$

### 周期性

二维傅里叶变换在$u$方向和$v$方向都是无限周期的，即：

$$
\begin{aligned}
F(u,v) &= F(u+k_1M,v+k_2N) \\
f(x,y) &= f(x+k_1M,y+k_2N) \\
\text{where } & k_1\in \mathbb{Z}, k_2\in \mathbb{Z}
\end{aligned}
$$

假设我们将$F(u,v)$平移，令$u_0=\frac{M}{2}$，$v_0=\frac{N}{2}$，那么：

$$
F(u-\frac{M}{2},v-\frac{N}{2}) \Leftrightarrow f(x,y)e^{j\pi(x+y)} \\
$$

因为$e^{j\pi x}=(-1)^x$，所以：

$$
F(u-\frac{M}{2},v-\frac{N}{2}) \Leftrightarrow f(x,y)(-1)^{x+y}
$$

所以频率域滤波的第一步就是用$(-1)^{x+y}$乘以空间域的图像，来进行中心变换，这样就可以将频率域的原点移动到空间域的中心，然后再进行图像的傅里叶变换。

### 对称性

对于二维离散傅里叶变换，$f(x,y)\in \mathbb{R}$，且$x,y,u,v\in \mathbb{Z}$，那么：

$$
\begin{aligned}
F(u,v) &= \frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j2\pi(ux/M+vy/N)} \\
&= \underbrace{\frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y)\cos(2\pi(ux/M+vy/N))}_{\mathbb{R}} - j\underbrace{\frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y)\sin(2\pi(ux/M+vy/N))}_{\mathbb{R}} \\
F(-u, -v) &= \frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j2\pi(-ux/M-vy/N)} \\
&= \frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{j2\pi(ux/M+vy/N)} \\
&= \frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y)\cos(2\pi(ux/M+vy/N)) + j\frac{1}{MN}\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y)\sin(2\pi(ux/M+vy/N)) \\
&= F^*(u,v)
\end{aligned}
$$

同样

$$
|F(-u,-v)| = |F(u,v)| \\
$$

### 奇偶性

先前讨论的二维离散傅里叶变换都是在实数域上的，而奇偶性是针对连续复数域上的函数$f(x,y)$而言的，这里我们对一维连续傅里叶变换进行讨论，二维的情况类似。

$$
\begin{aligned}
F(u) &= \int_{-\infty}^{\infty} f(x) e^{-j2\pi ux} dx \\
&= \int_{-\infty}^{\infty} f(x) \cos(2\pi ux) dx - j\int_{-\infty}^{\infty} f(x) \sin(2\pi ux) dx \\
\end{aligned}
$$

我们首先讨论$f(x)$是实函数或虚函数的情况：

1. 若$f(x)$是实函数，那么：

$$
\begin{aligned}
F(-u) &= \int_{-\infty}^{\infty} f(x) \cos(-2\pi ux) dx - j\int_{-\infty}^{\infty} f(x) \sin(-2\pi ux) dx \\
&= \underbrace{\int_{-\infty}^{\infty} f(x) \cos(2\pi ux) dx}_{\mathbb{\Re}} + \underbrace{j\int_{-\infty}^{\infty} f(x) \sin(2\pi ux) dx}_{\mathbb{\Im}} \\
&= [\int_{-\infty}^{\infty} f(x) \cos(2\pi ux) dx - j\int_{-\infty}^{\infty} f(x) \sin(2\pi ux) dx]^* \\
&= F^*(u)
\end{aligned}
$$

2. 若$f(x)$是虚函数，那么：

$$
\begin{aligned}
F(-u) &= \int_{-\infty}^{\infty} f(x) \cos(-2\pi ux) dx - j\int_{-\infty}^{\infty} f(x) \sin(-2\pi ux) dx \\
&= \underbrace{\int_{-\infty}^{\infty} f(x) \cos(2\pi ux) dx}_{\mathbb{\Im}} + \underbrace{j\int_{-\infty}^{\infty} f(x) \sin(2\pi ux) dx}_{\mathbb{\Re}} \\
&= -[\int_{-\infty}^{\infty} f(x) \cos(2\pi ux) dx - j\int_{-\infty}^{\infty} f(x) \sin(2\pi ux) dx]^* \\
&= -F^*(u)
\end{aligned}
$$

接着讨论$f(x)$是偶函数或奇函数的情况：

1. 若$f(x)$是偶函数，那么：

$$
\begin{aligned}
\int_{-\infty}^{\infty} f(x) \cos(2\pi ux) dx &= 2\int_{0}^{\infty} f(x) \cos(2\pi ux) dx \\
\int_{-\infty}^{\infty} f(x) \sin(2\pi ux) dx &= 0 \\
F(u) &= \int_{-\infty}^{\infty} f(x) \cos(2\pi ux) dx\\
F(-u) &= \int_{-\infty}^{\infty} f(x) \cos(2\pi ux) dx + j\int_{-\infty}^{\infty} f(x) \sin(2\pi ux) dx \\
&= \int_{-\infty}^{\infty} f(x) \cos(2\pi ux) dx \\
&= F(u)
\end{aligned}
$$

2. 若$f(x)$是奇函数，那么：

$$
\begin{aligned}
\int_{-\infty}^{\infty} f(x) \cos(2\pi ux) dx &= 0 \\
\int_{-\infty}^{\infty} f(x) \sin(2\pi ux) dx &= 2\int_{0}^{\infty} f(x) \sin(2\pi ux) dx \\
F(u) &= -j\int_{-\infty}^{\infty} f(x) \sin(2\pi ux) dx\\
F(-u) &= \int_{-\infty}^{\infty} f(x) \cos(2\pi ux) dx + j\int_{-\infty}^{\infty} f(x) \sin(2\pi ux) dx \\
&= j\int_{-\infty}^{\infty} f(x) \sin(2\pi ux) dx \\
&= -F(u)
\end{aligned}
$$

说明$F(u)$的奇偶性取决于$f(x)$的奇偶性

### 线性

$$
\mathfrak{J} \{\alpha f(x,y) + \beta g(x,y)\} = \alpha \mathfrak{J}\{f(x,y)\} + \beta \mathfrak{J}\{g(x,y)\}
$$

### 卷积

以一维连续卷积为例：

$$
(f\star h)(t) = \int_{-\infty}^{\infty} f(\tau)h(t-\tau) d\tau \\
$$

对其进行傅里叶变换：

$$
\begin{aligned}
\mathfrak{J}\{(f\star h)(t)\} &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(\tau)h(t-\tau) d\tau e^{-j2\pi ut} dt \\
&= \int_{-\infty}^{\infty}f(\tau)[\int_{-\infty}^{\infty}h(t-\tau) e^{-j2\pi ut} dt] d\tau \\
\text{令 }t-\tau = m & \text{ 则 } t = m+\tau\text{ ,} dt = dm \\
&= \int_{-\infty}^{\infty}f(\tau)[\int_{-\infty}^{\infty}h(m) e^{-j2\pi u(m+\tau)} dm] d\tau \\
&= \int_{-\infty}^{\infty}f(\tau)[\int_{-\infty}^{\infty}h(m) e^{-j2\pi um} dm] e^{-j2\pi u\tau} d\tau \\
&= \int_{-\infty}^{\infty}f(\tau)H(u) e^{-j2\pi u\tau} d\tau \\
&= H(u)\int_{-\infty}^{\infty}f(\tau) e^{-j2\pi u\tau} d\tau \\
&= H(u)F(u)
\end{aligned}
$$

所以空间域上的卷积在频率域上就是乘积。此外，频率域的卷积类似于空间域的乘积。

$$
\begin{aligned}
(f\star h)(t) &\Leftrightarrow F(u)H(u) \\
(f\cdot h)(t) &\Leftrightarrow (F\star H)(u)
\end{aligned}
$$

### 相关

复习一下空域上的二维卷积：

$$
(f\star h)(x,y) = \frac{1}{MN} \sum_{m=0}^{M-1} \sum_{n=0}^{N-1} f(m,n)h(x-m,y-n)
$$

空域上的离散相关与内积类似，定义为：

$$
(f\circ h)(x,y) = \frac{1}{MN}\sum_{m=0}^{M-1} \sum_{n=0}^{N-1} f^*(m,n)h(x+m,y+n)
$$

$$
\begin{aligned}
(f\circ h)(x,y) &\Leftrightarrow F^*(u,v)H(u,v) \\
f^*(x,y)h(x,y) &\Leftrightarrow (F\circ H)(u,v) \\
(f\circ f)(x,y) &\Leftrightarrow |F(u,v)|^2 \\ 
|f(x,y)|^2 &\Leftrightarrow (F\circ F)(u,v)
\end{aligned}
$$

### 尺度变换

$$
\begin{aligned}
\mathfrak{J} \{f(at)\} &= \int_{-\infty}^{\infty} f(at) e^{-j2\pi ut} dt \\
\text{令 }at = \tau & \text{ 则 } t = \frac{\tau}{a}\text{ ,} dt = \frac{d\tau}{a} \\
&= \int_{-\infty}^{\infty} f(\tau) e^{-j2\pi \frac{u}{a} \tau} \frac{d\tau}{a} \\
&= \frac{1}{a}\int_{-\infty}^{\infty} f(\tau) e^{-j2\pi \frac{u}{a} \tau} d\tau \\
&= \frac{1}{a}F(\frac{u}{a})
\end{aligned}
$$

### 时移

与[空域](#平移性)类似，时域上的平移也满足类似的性质，即：

$$
\begin{aligned}
\mathfrak{J} \{f(t-t_0)\} &= \int_{-\infty}^{\infty} f(t-t_0) e^{-j2\pi ut} dt \\
\text{令 }t-t_0 = \tau & \text{ 则 } t = \tau+t_0\text{ ,} dt = d\tau \\
&= \int_{-\infty}^{\infty} f(\tau+t_0) e^{-j2\pi u(\tau+t_0)} d\tau \\
&= e^{-j2\pi ut_0}\int_{-\infty}^{\infty} f(\tau+t_0) e^{-j2\pi u\tau} d\tau \\
&= e^{-j2\pi ut_0}F(u)
\end{aligned}
$$

### 冲激函数

$$
\begin{aligned}
\mathfrak{J} \{\delta(t)\} &= \int_{-\infty}^{\infty} \delta(t) e^{-j2\pi ut} dt \\
&= e^{-j2\pi u0} = 1 \\
\mathfrak{J} \{\delta(t-t_0)\} &= \int_{-\infty}^{\infty} \delta(t-t_0) e^{-j2\pi ut} dt \\
&= e^{-j2\pi ut_0} \\
\end{aligned}
$$

## 基本步骤

频率域滤波的基本步骤如下：

1. 用$(-1)^{x+y}$乘以空间域的图像，来进行中心变换，这样就可以将频率域的原点移动到空间域的中心，然后再进行图像的傅里叶变换。
2. 计算图像的傅里叶变换$F(u,v)$。
3. 用滤波器$H(u,v)$乘以$F(u,v)$，得到$G(u,v)$。
4. 计算$G(u,v)$的反傅里叶变换$g(x,y)$。
5. 保留$g(x,y)$的实部。
6. 用$(-1)^{x+y}$乘以$g(x,y)$，得到$g'(x,y)$。

更完整地，我们一般先对图像进行填充使其大小为$P\times Q$，其中$P=2M$，$Q=2N$，然后再乘上$(-1)^{x+y}$；同样，反变换处理后的图像最终也要裁剪，我们保留左上角的$M\times N$部分。

# 频率域滤波

频率域滤波是指在频率域上将滤波器$H(u,v)$乘以图像的傅里叶变换$F(u,v)$，得到$G(u,v)$，然后再将$G(u,v)$进行反傅里叶变换，得到滤波后的图像$g(x,y)$。

$$
g(x,y) = \Re\{\mathfrak{J}^{-1}\{H(u,v)F(u,v)\}\}(-1)^{x+y}
$$

## 低通滤波器

### 理想低通滤波器

$$
H(u,v) = \begin{cases}
1 & \text{if } D(u,v) \leq D_0 \\
0 & \text{if } D(u,v) > D_0
\end{cases}
$$

其中$D(u,v)$表示频率域上的距离，$D_0$表示截止频率。

$$
D(u,v) = \sqrt{(u-\frac{P}{2})^2+(v-\frac{Q}{2})^2}
$$

理想低通滤波器包含的功率比例为：

$$
p_{D_0} = \frac{\sum_{D(u,v)\leq D_0} |F(u,v)|^2}{\sum_{u=0}^{P-1} \sum_{v=0}^{Q-1} |F(u,v)|^2}
$$

### 高斯低通滤波器

二维频域上截止频率为$D_0$的高斯低通滤波器：

$$
H(u,v) = e^{-D^2(u,v)/2D_0^2}
$$

一维频域上的标准差为$\sigma$的高斯低通滤波器：

$$
H(u) = A e^{-\frac{u^2}{2\sigma^2}}
$$

反求空间域的滤波器：

$$
\begin{aligned}
h(x) &= \mathfrak{J}^{-1}\{H(u)\} \\
&= \mathfrak{J}^{-1}\{A e^{-\frac{u^2}{2\sigma^2}}\} \\
&= \int_{-\infty}^{\infty} A e^{-\frac{u^2}{2\sigma^2}} e^{j2\pi ux} du \\
&= \int_{-\infty}^{\infty} A e^{-\frac{u^2}{2\sigma^2}+j2\pi ux} du \\
&= \int_{-\infty}^{\infty} A e^{-(\frac{u}{\sqrt{2}\sigma}-j\sqrt{2}\pi\sigma x)^2} e^{-2\pi^2\sigma^2x^2} du \\
&= Ae^{-2\pi^2\sigma^2x^2}\int_{-\infty}^{\infty} e^{-(\frac{u}{\sqrt{2}\sigma}-j\sqrt{2}\pi\sigma x)^2} du \\
&= Ae^{-2\pi^2\sigma^2x^2}\int_{-\infty}^{\infty} e^{-\frac{1}{2\sigma^2}(u-j2\pi\sigma^2x)^2} du \\
\text{令 }r=u-j2\pi\sigma^2x & \text{ 则 } u = r+j2\pi\sigma^2x\text{ ,} du = dr \\
&= A\sigma\sqrt{2\pi}e^{-2\pi^2\sigma^2x^2}\int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{r^2}{2\sigma^2}} dr \\
&= A\sigma\sqrt{2\pi}e^{-2\pi^2\sigma^2x^2} \\
\end{aligned}
$$

### 巴特沃斯低通滤波器

$$
H(u,v) = \frac{1}{1+[D(u,v)/D_0]^{2n}}
$$

越接近原点的频率越容易通过滤波器，$n$越大，越接近理想低通滤波器。

## 高通滤波器

频率域上的高通滤波器可以通过频率域上的低通滤波器得到，即：

$$
H_{hp}(u,v) = 1 - H_{lp}(u,v)
$$

### 理想高通滤波器

$$
H(u,v) = \begin{cases}
0 & \text{if } D(u,v) \leq D_0 \\
1 & \text{if } D(u,v) > D_0
\end{cases}
$$

### 高斯高通滤波器
P
$$
H(u,v) = 1 - e^{-\frac{D^2(u,v)}{2D_0^2}}
$$

### 巴特沃斯高通滤波器

$$
H(u,v) = \frac{1}{1+[D_0/D(u,v)]^{2n}}
$$

注意巴特沃斯低通滤波器和高通滤波器的分母不同

## 频率域中的拉普拉斯

$$
H(u,v) = -4\pi^2[(u-\frac{P}{2})^2+(v-\frac{Q}{2})^2] = -4\pi^2D^2(u,v)
$$

给定图像$f(x,y)$的傅里叶变换$F(u,v)$，那么其拉普拉斯算子为：

$$
\nabla^2f(x,y) = \mathfrak{J}^{-1}\{H(u,v)F(u,v)\}
$$

对应的图像增强/锐化方法为：

$$
g(x,y) = f(x,y) + c\nabla^2f(x,y)
$$

如果$H(u,v)$是负数，那么$c=-1$，与拉普拉斯核的中心系数的正负关系类似。

$$
\begin{aligned}
g(x,y) &= \mathfrak{J}^{-1}\{F(u,v)-H(u,v)F(u,v)\} \\
&= \mathfrak{J}^{-1}\{F(u,v)(1+4\pi^2D^2(u,v))\} \\
\end{aligned}
$$

## 频率域中的钝化掩蔽

空域的钝化掩蔽是从原始图像中减去一个平滑图像，从而得到边缘图像：

$$
g_{mask} = f(x,y) - (f\star h_{lp})(x,y)
$$

再将边缘图像加回到原始图像中，从而得到增强的图像：

$$
g(x,y) = f(x,y) + kg_{mask}
$$

其中$k$是一个常数，$h_{lp}$是一个低通滤波器的空域核。对应的频域表示为：

$$
\begin{aligned}
g_{mask} &\Leftrightarrow F(u,v) - H_{lp}(u,v)F(u,v) \\
g(x,y) &\Leftrightarrow F(u,v) + k[F(u,v) - H_{lp}(u,v)F(u,v)] \\
&\Leftrightarrow (1+k)F(u,v) - kH_{lp}(u,v)F(u,v) \\
&\Leftrightarrow (1+k-kH_{lp}(u,v))F(u,v) \\
\end{aligned}
$$

## 选择性滤波

### 带阻滤波器和带通滤波器

低通滤波器和高通滤波器以截断频率$D_0$为界，分别将低于截断频率和高于截断频率的频率滤除，而带阻滤波器和带通滤波器则是在中心频率$C_0$ 
(频带中心)附近滤除或保留一定带宽的频率。

理想带阻滤波器：

$$
H(u,v) = \begin{cases}
0 & \text{if } C_0-\frac{W}{2} \leq D(u,v) \leq C_0+\frac{W}{2} \\
1 & \text{otherwise}
\end{cases}
$$

高斯带阻滤波器：

$$
H(u,v) = 1 - e^{-\frac{[D(u,v)-C_0]^2}{2\sigma^2}}
$$

这个滤波器的问题是$D(u,v)=0$时$H(u,v)<1$，对低频信号起到了抑制作用，所以我们可以将其改为修正高斯带阻滤波器：

$$
H(u,v) = 1 - e^{-\frac{1}{2}[\frac{D^2(u,v)-C_0^2}{D(u,v)W}]^2}
$$

巴特沃斯带阻滤波器：

$$
H(u,v) = \frac{1}{1+[\frac{D(u,v)W}{D^2(u,v)-C_0^2}]^{2n}}
$$

### 陷波滤波器

陷波滤波器假定两个对称的中心频率$(\frac{M}{2} + u_k, \frac{N}{2} + v_k)$和$(\frac{M}{2} - u_k, \frac{N}{2} - v_k)$，那么对应的距离为：

$$  
\begin{aligned}
D_k(u,v) &= \sqrt{(u- \frac{M}{2} - u_k)^2 + (v- \frac{N}{2} - v_k)^2} \\
D_{-k}(u,v)&= \sqrt{(u- \frac{M}{2} + u_k)^2 + (v- \frac{N}{2} + v_k)^2} \\
\end{aligned}
$$

陷波滤波器的一般形式为：

$$
H(u,v) = \prod_{k=1}^{K} H_k(u,v)H_{-k}(u,v)
$$

陷波带通滤波器可由$1$减去陷波带阻滤波器得到：

$$
H_{NP}(u,v) = 1 - H_{NR}(u,v)
$$

在第二版教材中，作者给出了一个更简单的形式，只考虑两个中心频率，将频率点距离两个中心的距离重写为$D_1(u,v)$和$D_2(u,v)$，将半径重写为$D_0$。

理想陷波带阻滤波器：

$$
H(u,v) = \begin{cases}
0 & \text{if } D_1(u,v) \leq D_{0} \text{ or } D_{2}(u,v) \leq D_{0} \\
1 & \text{otherwise}
\end{cases}
$$

阶数为$n$的巴特沃斯陷波带阻滤波器：

$$
H(u,v)=\frac{1}{1+[\frac{D_0^2}{D_1(u,v)D_2(u,v)}]^n}
$$

高斯陷波带阻滤波器：

$$
H(u,v)=1-e^{-\frac{1}{2}[\frac{D_1(u,v)D_2(u,v)}{D_0^2}]}
$$