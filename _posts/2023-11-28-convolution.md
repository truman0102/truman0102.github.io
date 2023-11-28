---
layout: post
title: Convolution
date: 2023-10-12 02:00:00-0400
description: An introduction to convolution in image processing.
tags: convolution
categories: image-processing
related_posts: false
giscus_comments: true
thumbnail: 
toc:
  sidebar: left
---

## What is Convolution?

Convolution is a mathematical operation that is used to express the relation between input and output of an LTI system. It is a mathematical way of combining two signals to form a third signal. 

It is the single most important technique in Digital Signal Processing, used to filter images, perform edge detection, perform blurring, and much more.

Convolution is a mathematical operation on two signals, $$f$$ and $$h$$, to produce a third signal, $$g$$. It is defined as the integral of the product of the two functions after one is reversed and shifted. The integral is evaluated for all values of shift, producing the convolution function $$g$$.

$$
g(x) = (f \ast h)(x) = \int_{-\infty}^{\infty} f(\tau) h(x - \tau) d\tau
$$

## Properties of Convolution

### Commutative

Replace $$x-\tau$$ with $$t$$, then $$\tau = x - t$$, and $$d\tau = -dt$$.

$$
\begin{aligned}
g(x) &= (f \ast h)(x) \\
&= \int_{-\infty}^{\infty} f(\tau) h(x - \tau) d\tau \\
&= \int_{\infty}^{-\infty} f(x - t) h(t) (-dt) \\
&= \int_{-\infty}^{\infty} f(x - t) h(t) dt \\
&= (h \ast f)(x) \\
\end{aligned}
$$

### Distributive over Addition

$$
\begin{aligned}
g(x) &= (f \ast (h_1 + h_2))(x) \\
&= \int_{-\infty}^{\infty} f(\tau) (h_1 + h_2)(x - \tau) d\tau \\
&= \int_{-\infty}^{\infty} f(\tau) (h_1(x - \tau) + h_2(x - \tau)) d\tau \\
&= \int_{-\infty}^{\infty} f(\tau) h_1(x - \tau) d\tau + \int_{-\infty}^{\infty} f(\tau) h_2(x - \tau) d\tau \\
&= (f \ast h_1)(x) + (f \ast h_2)(x) \\
\end{aligned}
$$

### Bilinear

If $$\alpha \in \mathbb{C}$$, then

$$
\begin{aligned}
\alpha (f \ast h)(x) &= \alpha \int_{-\infty}^{\infty} f(\tau) h(x - \tau) d\tau \\
&= \int_{-\infty}^{\infty} \alpha f(\tau) h(x - \tau) d\tau \\
&= (\alpha f \ast h)(x) \\
&= \int_{-\infty}^{\infty} f(\tau) (\alpha h)(x - \tau) d\tau \\
&= (f \ast (\alpha h))(x)
\end{aligned}
$$

### Linear

$$
\begin{aligned}
(f\ast (\alpha h_1 + \beta h_2))(x) &= (f \ast (\alpha h_1))(x) + (f \ast (\beta h_2))(x) \\
&= \alpha (f \ast h_1)(x) + \beta (f \ast h_2)(x) \\
\end{aligned}
$$

### Associative

Let $$\theta+\tau=t$$, then $$\theta=t-\tau$$, and $$d\theta=dt$$.

$$
\begin{aligned}
(f\ast (h_1 \ast h_2))(x) &= \int_{-\infty}^{\infty} f(\tau) (h_1 \ast h_2)(x - \tau) d\tau \\
&= \int_{-\infty}^{\infty} f(\tau) \int_{-\infty}^{\infty} h_1(\theta) h_2(x - \tau - \theta) d\theta d\tau \\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(\tau) h_1(\theta) h_2(x - \tau - \theta) d\theta d\tau \\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(\tau) h_1(t-\tau) h_2(x - t) dt d\tau \\
&= \int_{-\infty}^{\infty} h_2(x - t) \int_{-\infty}^{\infty} f(\tau) h_1(t-\tau) d\tau dt \\
&= \int_{-\infty}^{\infty} h_2(x - t) (f \ast h_1)(t) dt \\
&= ((f \ast h_1) \ast h_2)(x) \\
\end{aligned}
$$

### Shift Invariant

$$
\begin{aligned}
g(x)&=S\left\{f(x)\right\} \\
S\left\{f(x-x_0)\right\}&=f(x-x_0)\ast h(x)\\
&=g(x-x_0)\\
\end{aligned}
$$

## Impulse Response

$$
\begin{aligned}
f(x) &= (f \ast \delta)(x) \\
&= \int_{-\infty}^{\infty} f(\tau) \delta(x - \tau) d\tau \\
g(x)&= S\left\{f(x)\right\} \\
&= S\left\{\int_{-\infty}^{\infty} f(\tau) \delta(x - \tau) d\tau\right\} \\
&= \int_{-\infty}^{\infty} f(\tau) S\left\{\delta(x - \tau)\right\} d\tau \\
&=(f \ast S\left\{\delta\right\})(x) \\
\end{aligned}
$$

Thus, given the impulse response $$h$$ of a system, the output $$g$$ of the system is the convolution of the input $$f$$ and the impulse response $$h$$.

## Separable Convolution

A separable convolution is a convolution that can be factored into one-dimensional convolutions, kernel $$h$$ can be written as the convolution of two 1D kernels $$h_1$$ and $$h_2$$.

$$
\underbrace{
\begin{bmatrix}
\alpha a&\alpha b&\alpha c\\
\beta a&\beta b&\beta c\\
\gamma a&\gamma b&\gamma c\\
\end{bmatrix}
}_{h}=
\underbrace{
\begin{bmatrix}
\alpha\\
\beta\\
\gamma\\
\end{bmatrix}
}_{h_1}\ast
\underbrace{
\begin{bmatrix}
a&b&c\\
\end{bmatrix}
}_{h_2}
$$

Thus, the convolution between $$f$$ and $$h$$ can be calculated by first convolving $$f$$ with $$h_1$$, and then convolving the result with $$h_2$$.

$$
f \ast h = f \ast (h_1 \ast h_2) = (f \ast h_1) \ast h_2
$$