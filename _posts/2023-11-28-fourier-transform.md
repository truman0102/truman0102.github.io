---
layout: post
title: Fourier Transform
date: 2023-10-12 02:00:00-0400
description: An introduction to fourier transform in image processing.
tags: fourier-transform
categories: image-processing
related_posts: false
giscus_comments: true
thumbnail: 
toc:
  sidebar: left
---

## What is Fourier Transform?

A periodic function $$f(t)$$ can be represented as a sum of sine and cosine functions. This is called Fourier series.

$$
\begin{aligned}
f(t) &= \sum_{n=-\infty}^{\infty} c_n e^{j\frac{2\pi n}{T}t}\\
&= \sum_{n=-\infty}^{\infty} c_n\cos(\frac{2\pi n}{T}t) + j\sum_{n=-\infty}^{\infty} c_n\sin(\frac{2\pi n}{T}t)\\
c_n &= \frac{1}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}} f(t) e^{-j\frac{2\pi n}{T}t} dt\\
&= \frac{1}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}} f(t) \cos(\frac{2\pi n}{T}t) dt - j\frac{1}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}} f(t) \sin(\frac{2\pi n}{T}t) dt\\
\end{aligned}
$$

where $$c_n$$ is the coefficient of the $$n^{th}$$ harmonic, $$T$$ is the period of the function, and $$j$$ is the imaginary unit. The frequency of the $$n^{th}$$ harmonic is $$\frac{n}{T}$$. The fundamental frequency is $$\frac{1}{T}$$, and the fundamental period is $$T$$, the greater $$n$$ is, the higher the frequency.

Fourier transform is an extension of Fourier series to non-periodic functions, used to represent a function in terms of its frequency components. The Fourier transform of a function $$f(t)$$ is defined as:

$$
\begin{aligned}
F(\mu) &= \int_{-\infty}^{\infty} f(t) e^{-j2\pi\mu t} dt\\
&= \int_{-\infty}^{\infty} f(t) \cos(2\pi\mu t) dt - j\int_{-\infty}^{\infty} f(t) \sin(2\pi\mu t) dt\\
F^*(\mu) &= \int_{-\infty}^{\infty} f(t) e^{j2\pi\mu t} dt\\
&= \int_{-\infty}^{\infty} f(t) \cos(2\pi\mu t) dt + j\int_{-\infty}^{\infty} f(t) \sin(2\pi\mu t) dt\\
f(t) &= \int_{-\infty}^{\infty} F(\mu) e^{j2\pi\mu t} d\mu\\
&= \int_{-\infty}^{\infty} F(\mu) \cos(2\pi\mu t) d\mu + j\int_{-\infty}^{\infty} F(\mu) \sin(2\pi\mu t) d\mu\\
\end{aligned}
$$

where $$F(\mu)$$ is the Fourier transform of $$f(t)$$, and $$\mu$$ is the frequency. The inverse Fourier transform is the Fourier transform of $$F(\mu)$$. If $$f(t)$$ is a real function, then $$F(\mu)$$ is a complex function, and $$F(-\mu) = F^*(\mu)$$, where $$F^*(\mu)$$ is the complex conjugate of $$F(\mu)$$.

## Fourier Transform of Impulse Function

An impulse function is a function that is zero everywhere except at one point, where it is infinite.

$$
\begin{aligned}
\delta(t) &= \begin{cases}
\infty, & t = 0\\
0, & t \neq 0
\end{cases}\\
\end{aligned}
$$

The impulse function is also called the Dirac delta function, it can be used to sample a function at a point.

$$
\begin{aligned}
\int_{-\infty}^{\infty} \delta(t) dt &= 1\\
\int_{-\infty}^{\infty}f(t)\delta(t) dt &= f(0)\\
\int_{-\infty}^{\infty}f(t)\delta(t-t_0) dt &= f(t_0)\\
\end{aligned}
$$

If $$x$$ is a discrete function, then $$\delta(x)$$ is a discrete impulse function.

$$
\begin{aligned}
\delta(x) &= \begin{cases}
1, & x = 0\\
0, & x \neq 0
\end{cases}\\
\end{aligned}
$$

$$
\begin{aligned}
\sum_{x=-\infty}^{\infty} \delta(x) &= 1\\
\sum_{x=-\infty}^{\infty}f(x)\delta(x) &= f(0)\\
\sum_{x=-\infty}^{\infty}f(x)\delta(x-x_0) &= f(x_0)\\
\end{aligned}
$$

The fourier transform of the impulse function is

$$
\begin{aligned}
\mathfrak{J}\{\delta(t-t_0)\} &= \int_{-\infty}^{\infty} \delta(t-t_0) e^{-j2\pi\mu t} dt\\
&=e^{-j2\pi\mu t_0}\\
\end{aligned}
$$

In turn, the inverse fourier transform of the impulse function is

$$
\begin{aligned}
\mathfrak{J}^{-1}\{e^{-j2\pi\mu t_0}\} &= \int_{-\infty}^{\infty} e^{-j2\pi\mu t_0} e^{j2\pi\mu t} d\mu\\
&=\int_{-\infty}^{\infty} e^{j2\pi\mu (t-t_0)} d\mu\\
&=\delta(t-t_0)\\
\end{aligned}
$$


The series of impulse functions is

$$
\begin{aligned}
s_{\triangle T}(t) &= \sum_{n=-\infty}^{\infty} \delta(t-n\triangle T)\\
&=\sum_{n=-\infty}^{\infty} c_n e^{j\frac{2\pi n}{\triangle T}t}\\
c_n &= \frac{1}{\triangle T} \int_{-\frac{\triangle T}{2}}^{\frac{\triangle T}{2}} s_{\triangle T}(t) e^{-j\frac{2\pi n}{\triangle T}t} dt\\
&=\frac{1}{\triangle T} \int_{-\frac{\triangle T}{2}}^{\frac{\triangle T}{2}} \delta(t) e^{-j\frac{2\pi n}{\triangle T}t} dt\\
&=\frac{1}{\triangle T} e^0\\
&=\frac{1}{\triangle T}\\
s_{\triangle T}(t) &= \frac{1}{\triangle T} \sum_{n=-\infty}^{\infty} e^{j\frac{2\pi n}{\triangle T}t}\\
S(\mu)&=\mathfrak{J}\{s_{\triangle T}(t)\}\\
&=\frac{1}{\triangle T} \sum_{n=-\infty}^{\infty} \mathfrak{J}\{e^{j\frac{2\pi n}{\triangle T}t}\}\\
&=\frac{1}{\triangle T} \sum_{n=-\infty}^{\infty} \int_{-\infty}^{\infty} e^{j\frac{2\pi n}{\triangle T}t} e^{-j2\pi\mu t} dt\\
&=\frac{1}{\triangle T} \sum_{n=-\infty}^{\infty} \int_{-\infty}^{\infty} e^{j2\pi(\frac{n}{\triangle T}-\mu)t} dt\\
&=\frac{1}{\triangle T} \sum_{n=-\infty}^{\infty} \delta(\frac{n}{\triangle T}-\mu)\\
&=\frac{1}{\triangle T} \sum_{n=-\infty}^{\infty} \delta(\mu-\frac{n}{\triangle T})\\
\end{aligned}
$$

which means that the fourier transform of the series of impulse functions in time domain with period $$\triangle T$$ is the series of impulse functions in frequency domain with period $$\frac{1}{\triangle T}$$.


## Convolution and Fourier Transform

The [convolution](/blog/2023/convolution/) of two functions $$f(t)$$ and $$h(t)$$ is defined as

$$
(f\star h)(t) = \int_{-\infty}^{\infty} f(\tau)h(t-\tau) d\tau
$$

The fourier transform of the convolution is

$$
\begin{aligned}
\mathfrak{J}\{(f \star h)(t)\} &= \int_{-\infty}^{\infty} (f\star h)(t) e^{-j2\pi\mu t} dt\\
&=\int_{-\infty}^{\infty} \left [ \int_{-\infty}^{\infty} f(\tau)h(t-\tau) d\tau\right ] e^{-j2\pi\mu t} dt\\
&=\int_{-\infty}^{\infty} f(\tau) \left [ \int_{-\infty}^{\infty} h(t-\tau) e^{-j2\pi\mu t} dt\right ] d\tau\\
&=\int_{-\infty}^{\infty} f(\tau) \left [ \int_{-\infty}^{\infty} h(t-\tau) e^{-j2\pi\mu (t-\tau)} e^{-j2\pi\mu \tau} dt\right ] d\tau\\
&=\int_{-\infty}^{\infty} f(\tau) \left [ \int_{-\infty}^{\infty} h(t-\tau) e^{-j2\pi\mu (t-\tau)} dt\right ] e^{-j2\pi\mu \tau} d\tau\\
&=\int_{-\infty}^{\infty} f(\tau) H(\mu) e^{-j2\pi\mu \tau} d\tau\\
&=H(\mu) \int_{-\infty}^{\infty} f(\tau) e^{-j2\pi\mu \tau} d\tau\\
&=H(\mu) F(\mu)\\
\end{aligned}
$$

If the domain of $$t$$ is spatial domain, and the domain of $$\mu$$ is frequency domain, then the convolution in spatial domain is equivalent to multiplication in frequency domain. In turn, the convolution in frequency domain is equivalent to multiplication in spatial domain.

$$
\begin{aligned}
(f \star h)(t) &\Leftrightarrow F(\mu)H(\mu)\\
f(t)h(t) &\Leftrightarrow \frac{1}{2\pi}F(\mu)\star H(\mu)\\
\end{aligned}
$$

## Discrete Fourier Transform

The discrete Fourier transform (DFT) is the discrete version of the Fourier transform. The DFT of a discrete function $$f(x)$$ is defined as

$$
\begin{aligned}
\tilde{F(u)} &= \int_{-\infty}^{\infty} \tilde{f(t)} e^{-j2\pi\mu t} dt\\
&=\int_{-\infty}^{\infty}\sum_{t=-\infty}^{\infty} f(t)\delta(t-n\triangledown T) e^{-j2\pi\mu t} dt\\
&=\sum_{t=-\infty}^{\infty} \int_{-\infty}^{\infty} f(t)\delta(t-n\triangledown T) e^{-j2\pi\mu t} dt\\
&=\sum_{t=-\infty}^{\infty} f(n\triangledown T) e^{-j2\pi\mu n\triangledown T}\\
\end{aligned}
$$

where $$\tilde{f(t)}$$ is the discrete function of $$f(t)$$, and $$\triangledown T$$ is the sampling period. 

To achieve the sampling of a continuous function, we need to sample the function in one period. 



$$
\mu = \frac{m}{M\triangledown T}
$$

$$
\begin{aligned}
F_m &= \sum_{n=0}^{M-1} f_n e^{-j2\pi\frac{mn}{M}}\\
f_n &= \frac{1}{M} \sum_{m=0}^{M-1} F_m e^{j2\pi\frac{mn}{M}}\\
\end{aligned}
$$

## Two-Dimensional Fourier Transform

The impulse function in two-dimensional space is

$$
\delta(x, y) = \begin{cases}
1, & x = 0 \wedge y = 0\\
0, & x \neq 0 \vee y \neq 0
\end{cases}\\
$$

$$
\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \delta(x, y) dx dy = 1
$$

$$
\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y)\delta(x, y) dx dy = f(0, 0)
$$

$$
\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y)\delta(x-x_0, y-y_0) dx dy = f(x_0, y_0)\\
$$

The two-dimensional Fourier transform in continuous space is

$$
\begin{aligned}
F(\mu, \nu) &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(t,z) e^{-j2\pi(\mu t + \nu z)} dt dz\\
f(t, z) &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} F(\mu, \nu) e^{j2\pi(\mu t + \nu z)} d\mu d\nu\\
\end{aligned}
$$

The form of discrete two-dimensional Fourier transform is

$$
\begin{aligned}
F(\mu, \nu) &= \sum_{t=0}^{M-1} \sum_{z=0}^{N-1} f(x,y) e^{-j2\pi(\frac{\mu x}{M} + \frac{\nu y}{N})}\\
f(x, y) &= \frac{1}{MN} \sum_{\mu=0}^{M-1} \sum_{\nu=0}^{N-1} F(\mu, \nu) e^{j2\pi(\frac{\mu x}{M} + \frac{\nu y}{N})}\\
\end{aligned}
$$

## Properties of Fourier Transform

### Relation between interval and frequency

If an image $$f(x,y)$$ is sampled from continuous function $$f(t,z)$$, $$M$$ and $$N$$ are the number of pixels in $$t$$ and $$z$$ direction, respectively, then the sampling interval is $$\triangle t = \frac{1}{M}$$ and $$\triangle z = \frac{1}{N}$$. The frequency interval is $$\triangle \mu = \frac{1}{M\triangle t} = M$$ and $$\triangle \nu = \frac{1}{N\triangle z} = N$$. The frequency range is $$\mu \in [-\frac{M}{2}, \frac{M}{2}]$$ and $$\nu \in [-\frac{N}{2}, \frac{N}{2}]$$.

### Linearity

### Scaling

### Shifting

$$
\begin{aligned}
f(x,y)e^{j2\pi(\mu_0 \frac{x}{M} + \nu_0 \frac{y}{N})} &\Leftrightarrow F(\mu-\mu_0, \nu-\nu_0)\\
f(x-x_0,y-y_0) &\Leftrightarrow F(\mu, \nu)e^{-j2\pi(\mu \frac{x_0}{M} + \nu \frac{y_0}{N})}\\
\end{aligned}
$$

### Periodicity

$$
\begin{aligned}
F(\mu,\nu) &= F(\mu+k_1M, \nu+k_2N)\\
f(x,y)&=f(x+k_1M, y+k_2N)\\
\end{aligned}
$$

$$
f(x,y)(-1)^{x+y} \Leftrightarrow F(\mu+\frac{M}{2}, \nu+\frac{N}{2}) \Leftrightarrow F(\mu-\frac{M}{2}, \nu-\frac{N}{2})
$$

### Parity

$$
\begin{aligned}
F(\mu,\nu)&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j2\pi(\mu x + \nu y)} dx dy\\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \cos(2\pi(\mu x + \nu y)) dx dy - j\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \sin(2\pi(\mu x + \nu y)) dx dy\\
\end{aligned}
$$

where $$\mathfrak{Re}\{F(\mu,\nu)\}$$ is the real part of $$F(\mu,\nu)$$, and $$\mathfrak{Im}\{F(\mu,\nu)\}$$ is the imaginary part of $$F(\mu,\nu)$$.

If $$f(x,y)$$ is a real function, then $$F(\mu,\nu)$$ is a complex function, and $$F(-\mu, -\nu) = F^*(\mu, \nu)$$, where $$F^*(\mu, \nu)$$ is the complex conjugate of $$F(\mu, \nu)$$.

$$
\begin{aligned}
F(-\mu, -\nu) &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j2\pi(-\mu x -\nu y)} dx dy\\
&=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{j2\pi(\mu x + \nu y)} dx dy\\
&=\underbrace{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \cos(2\pi(\mu x + \nu y)) dx dy}_{\mathfrak{Real}} + j\underbrace{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \sin(2\pi(\mu x + \nu y)) dx dy}_{Real}\\
&=(\underbrace{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \cos(2\pi(\mu x + \nu y)) dx dy}_{\mathfrak{Real}} - j\underbrace{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \sin(2\pi(\mu x + \nu y)) dx dy}_{Real})^*\\
&=(\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j2\pi(\mu x + \nu y)} dx dy)^*\\
&=F^*(\mu, \nu)\\
\end{aligned}
$$

If $$f(x,y)$$ is an imaginary function, then $$F(-\mu, -\nu) = -F^*(\mu, \nu)$$.

$$
\begin{aligned}
F(-\mu, -\nu) &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j2\pi(-\mu x -\nu y)} dx dy\\
&=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{j2\pi(\mu x + \nu y)} dx dy\\
&=\underbrace{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \cos(2\pi(\mu x + \nu y)) dx dy}_{\mathfrak{Imaginary}} + \underbrace{j\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \sin(2\pi(\mu x + \nu y)) dx dy}_{Real}\\
&=-(\underbrace{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \cos(2\pi(\mu x + \nu y)) dx dy}_{\mathfrak{Imaginary}} - j\underbrace{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \sin(2\pi(\mu x + \nu y)) dx dy}_{Real})^*\\
&=-(\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j2\pi(\mu x + \nu y)} dx dy)^*\\
&=-F^*(\mu, \nu)\\
\end{aligned}
$$

If $$f(x,y)$$ is an odd function, then the fourier transform of $$f(x,y)$$ is an imaginary function and also an odd function.

$$
\begin{aligned}
F(-\mu, -\nu) &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{j2\pi(\mu x + \nu y)} dx dy\\
&= \underbrace{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y)\cos(2\pi(\mu x + \nu y)) dx dy}_{0} + j\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y)\sin(2\pi(\mu x + \nu y)) dx dy\\
&=j\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y)\sin(2\pi(\mu x + \nu y)) dx dy\\
&=-\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j2\pi(\mu x + \nu y)} dx dy\\
&=-F(\mu, \nu)\\
\end{aligned}
$$

If $$f(x,y)$$ is an even function, then the fourier transform is a real function and also an even function.

$$
\begin{aligned}
F(-\mu, -\nu) &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{j2\pi(\mu x + \nu y)} dx dy\\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y)\cos(2\pi(\mu x + \nu y)) dx dy + j\underbrace{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y)\sin(2\pi(\mu x + \nu y)) dx dy}_{0}\\
&=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j2\pi(\mu x + \nu y)} dx dy\\
&=F(\mu, \nu)\\
\end{aligned}
$$

### Amplitude and Phase

$$
\begin{aligned}
F(\mu,\nu) &= \mathfrak{Re}\{F(\mu,\nu)\} + j\mathfrak{Im}\{F(\mu,\nu)\}\\
A(\mu,\nu) &= \sqrt{\mathfrak{Re}\{F(\mu,\nu)\}^2 + \mathfrak{Im}\{F(\mu,\nu)\}^2}\\
\phi(\mu,\nu) &= \arctan\left(\frac{\mathfrak{Im}\{F(\mu,\nu)\}}{\mathfrak{Re}\{F(\mu,\nu)\}}\right)\\
\end{aligned}
$$

## Examples of Fourier Transform

### Gaussian Function

$$
\begin{aligned}
f(x) &= ae^{-\frac{x^2}{2\sigma^2}}\\
\end{aligned}
$$