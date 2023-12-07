---
layout: post
title: Wavelet Analysis
date: 2023-12-06 10:40:00-0400
description: An introduction to wavelet analysis and other image transforms.
tags: wavelet-analysis image-transforms
categories: image-processing
related_posts: false
giscus_comments: true
thumbnail: 
toc:
  sidebar: left
---

## Image Pyramid (图像金字塔)

尺度 (scale) 是图像金字塔的一个重要概念。尺度是指图像的尺寸和分辨率，对图像进行缩放就是改变图像的尺度。图像金字塔是一种多尺度的图像表示，可以用来检测图像中的不同尺度的特征。

图像金字塔第$n$级[^1]的图像大小为$2^{n}\times 2^{n}$，顶点一般为第0级，大小为$1\times 1$，依次向下为$2\times 2\text{，}\dots\text{，}2^{n}\times 2^{n}$。

[^1]: 一般从上往下称为级，第0级为顶点，第1级为第0级的下一级，以此类推；从下往上称为层，第0层为底层，第1层为第0层的上一层，以此类推。

采样 (sampling) 是图像金字塔的另一个重要概念。采样分为上采样 (upsampling) 和下采样[^2] (downsampling)。上采样是指将图像的尺度变大，比如插入零值像素并使用插值算法对其重构，上采样可以得到图像金字塔中尺度更大的图像；下采样是指将图像的尺度变小，比如将图像的每个像素替换为其邻域像素的平均值，下采样可以得到图像金字塔中尺度更小的图像。

[^2]: 对一张图像进行2倍下采样就可以得到下一层/上一级的图像。

## Z Transform (Z变换)

Z变换用于分析离散信号，以复数平面的单位圆为基础，将离散信号的时域/空域转换为复数平面的频域。Z变换的定义如下：

$$
X(z)=\sum_{n=-\infty}^{\infty}x(n)z^{-n}\quad z\in\mathbb{C} \tag{1}
$$

Z变换的性质如下：

$$
\begin{aligned}
X(z^{-1}) &= \sum_{n=-\infty}^{\infty}x(n)z^{n}\\
&= \sum_{m=\infty}^{-\infty}x(-m)z^{-m}\\
&= \sum_{m=-\infty}^{\infty}x(-m)z^{-m}\\
&\Leftrightarrow x(-n) \tag{2}\\
\end{aligned}
$$

$$
\begin{aligned}
z^{-k}X(z) &= \sum_{n=-\infty}^{\infty}x(n)z^{-(n+k)}\\
&= \sum_{m=-\infty}^{\infty}x(m-k)z^{-m}\\
&\Leftrightarrow x(n-k) \tag{3}\\
\end{aligned}
$$

$$
\begin{aligned}
X(-z) &= \sum_{n=-\infty}^{\infty}x(n)(-z)^{-n}\\
&= \sum_{n=-\infty}^{\infty}x(n)(-1)^{-n}z^{-n}\\
&= \sum_{k=-\infty}^{\infty}x(2k)z^{-2k} - \sum_{k=-\infty}^{\infty}x(2k+1)z^{-(2k+1)}\\
\end{aligned}
$$

对于下采样:

$$
\begin{aligned}
x_{down}(n) &= x(2n)\\
&\Leftrightarrow \frac{1}{2}[X(z^{\frac{1}{2}})+X(-z^{\frac{1}{2}})] \tag{4}\\
\end{aligned}
$$

证明如下:

$$
\begin{aligned}
\frac{1}{2}[X(z^{\frac{1}{2}})+X(-z^{\frac{1}{2}})] &= \frac{1}{2}\sum_{n=-\infty}^{\infty}x(n)z^{-\frac{n}{2}}+\frac{1}{2}\sum_{n=-\infty}^{\infty}x(n)(-z)^{-\frac{n}{2}}\\
\end{aligned}
$$

对于上采样:

$$
x_{up}(n) =
\left\{
    \begin{aligned}
&x(\frac{n}{2})&n\text{为偶数}\\
&0&n\text{为奇数}\\
\end{aligned}\right.
$$

$$
\begin{aligned}
X(z^2)&= \sum_{n=-\infty}^{\infty}x(n)z^{-2n}\\
&= \sum_{m=-\infty}^{\infty}x(\frac{m}{2})z^{-m}\quad m\text{为偶数}\\
&\Leftrightarrow x_{up}(n) \tag{5}\\
\end{aligned}
$$

一个信号经过上采样和下采样后，其对应的Z变换为：

$$
\hat{X}(z) = \frac{1}{2}[X(z)+X(-z)] \tag{6}
$$

$$
\begin{aligned}
\hat{x}(n) &= Z^{-1}[\hat{X}(z)]\\
Z^{-1}[\hat{X}(-z)] &= (-1)^n\hat{x}(n)\\
\end{aligned}
$$

### Subband Coding (子带编码)

$$
\begin{aligned}
\hat{X}(z)&= \frac{1}{2}G_0(z)[H_0(z)X(z)+H_0(-z)X(-z)]+\frac{1}{2}G_1(z)[H_1(z)X(z)+H_1(-z)X(-z)]\\
&=\frac{1}{2}[G_0(z)H_0(z)+G_1(z)H_1(z)]X(z)+\frac{1}{2}[G_0(z)H_0(-z)+G_1(z)H_1(-z)]X(-z)\\
\end{aligned}
$$

### Error-Free Reconstruction (无误差重构)

$$
\begin{aligned}
G_0(z)H_0(z)+G_1(z)H_1(z) &= 2\\
G_0(z)H_0(-z)+G_1(z)H_1(-z) &= 0\\
\end{aligned}
$$

$$
\begin{aligned}
\begin{bmatrix}
G_0(z) & G_1(z)\\
\end{bmatrix}
H_m
&=
\begin{bmatrix}
2 & 0\\
\end{bmatrix}\\
H_m&=\begin{bmatrix}
H_0(z) & H_0(-z)\\
H_1(z) & H_1(-z)\\
\end{bmatrix}
\end{aligned}
$$

如果$H_m$是可逆的，那么存在

$$
H_m^* = \begin{bmatrix}
H_1(-z) & -H_0(-z)\\
-H_1(z) & H_0(z)\\
\end{bmatrix}=|H_m|H_m^{-1}
$$

$$
\begin{aligned}
\begin{bmatrix}
G_0(z) & G_1(z)\\
\end{bmatrix}
H_mH_m^*&=
\begin{bmatrix}
2 & 0\\
\end{bmatrix}H_m^*\\
\begin{bmatrix}
G_0(z) & G_1(z)\\
\end{bmatrix}
&=
\begin{bmatrix}
2 & 0\\
\end{bmatrix}H_m^*|H_m|^{-1}\\
&=2\begin{bmatrix}
H_1(-z) & -H_0(-z)\\
\end{bmatrix}|H_m|^{-1}\\
\end{aligned}
$$

伴随矩阵是代数余子式矩阵的转置，是逆矩阵$A^{-1}$的$|A|$倍，

因此，$G_0(z)$和$G_1(z)$是$H_1(-z)$和$-H_0(-z)$的线性变换，倍数为$\frac{2}{|H_m|}=\frac{2}{|H_0(z)H_1(-z)-H_1(z)H_0(-z)|}$。

### Finite Impulse Response (有限脉冲响应)

$$
|H_m|=\alpha z^{-(2k+1)}
$$

- $\alpha=2$

$$
\begin{aligned}
g_0(n)&=(-1)^n h_1(n)\\
g_1(n)&=(-1)^{n+1} h_0(n)\\
\end{aligned}
$$

- $\alpha=-2$

$$
\begin{aligned}
g_0(n)&=(-1)^{n+1} h_1(n)\\
g_1(n)&=(-1)^n h_0(n)\\
\end{aligned}
$$

### Biorthogonality (双正交性)

$$
\begin{aligned}
P(z)=&G_0(z)H_0(z)\\&=\frac{2}{|H_m(z)|}H_1(-z)H_0(z)\\
G_1(z)H_1(z)&=\frac{-2}{|H_m(z)|}H_0(-z)H_1(z)\\
&=\frac{2}{|H_m(-z)|}H_1(z)H_0(-z)\\
&=P(-z)\\
&=G_0(-z)H_0(-z)\\
\end{aligned}
$$

代入无误差重构的条件：

$$
G_0(z)H_0(z)+G_0(-z)H_0(-z)=2
$$

## 哈尔变换 (Haar Transform)

给定大小为$N=2^n$，$k=0,1,\dots,N-1$，可分解为$k=2^p+q-1$，其中$p\in [0,n-1]$，$q\in [1,2^p]$，$p\in \mathbb{Z}$，$q\in \mathbb{Z}$。

$$
h_k(z)=h_{pq}(z) = \frac{1}{\sqrt{N}}\left\{
    \begin{aligned}
    0&\quad p=0\text{且} q=0\\
    2^{p/2}&\quad (q-1)/2^p\leq z<(q-0.5)/2^p\\
    -2^{p/2}&\quad (q-0.5)/2^p\leq z<q/2^p\\
    0&\quad otherwise\\
\end{aligned}\right.
$$

对于$i\in [0,N-1]$，$j\in [0,N-1]$，$h_{i,j}=h_i(\frac{j}{N})$
