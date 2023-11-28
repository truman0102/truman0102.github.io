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

The series of impulse functions is

$$
s_{\triangledown T}(t) = \sum_{n=-\infty}^{\infty} \delta(t-nT)
$$

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

where $$\tilde{f(t)}$$ is the discrete function of $$f(t)$$, and $$\triangledown T$$ is the sampling period. The inverse DFT is
