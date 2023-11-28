---
layout: post
title: Spatial Filtering
date: 2023-10-10 01:00:00-0400
description: An introduction to spatial filtering in image processing.
tags: spatial-filtering
categories: image-processing
related_posts: false
giscus_comments: true
thumbnail: 
toc:
  sidebar: left
---

## What is Spatial Filtering?

The spatial domain enhancement is based on pixels in a small range (neighbor). This means the transformed intensity is determined by the gray values of those points within the neighborhood, and thus the spatial domain enhancement is also called neighborhood operation or neighborhood processing.

A digital image can be viewed as a two-dimensional function, $$f(x, y)$$, where $$x$$ and $$y$$ are spatial coordinates. The value of $$f$$ at any point $$(x, y)$$ is called the intensity or gray level of the image at that point. The filtering operation based on the values of $$f(x, y)$$ in the neighborhood of $$(x, y)$$ is called spatial filtering.

Spatial filtering can be divided into linear and non-linear filtering. If we regard the filtering as a two-dimensional operation, it can be used to conduct the convolution or correlation operation between the image and the filter. 

Let $$g(x, y)$$ be the output image obtained by filtering $$f(x, y)$$ with a filter $$h(x, y)$$, then the convolution operation is defined as:

$$
g(x, y) = (f \ast h)(x, y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} f(x-s, y-t) h(s, t)
$$

where $$a$$ and $$b$$ are the half-widths of the filter. Similarly, the correlation operation is defined as:

$$
g(x, y) = (f \ast h)(x, y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} f(x+s, y+t) h(s, t)
$$

## Convolution

Convolution is a mathematical operation on two signals, $$f$$ and $$h$$, to produce a third signal, $$g$$. It is defined as the integral of the product of the two functions after one is reversed and shifted. The integral is evaluated for all values of shift, producing the convolution function $$g$$.

$$
g(x) = (f \ast h)(x) = \int_{-\infty}^{\infty} f(\tau) h(x - \tau) d\tau
$$

### Properties of Convolution

#### Commutative

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

#### Distributive over Addition

$$
\begin{aligned}
g(x) &= (f \ast (h_1 + h_2))(x) \\
&= \int_{-\infty}^{\infty} f(\tau) (h_1 + h_2)(x - \tau) d\tau \\
&= \int_{-\infty}^{\infty} f(\tau) (h_1(x - \tau) + h_2(x - \tau)) d\tau \\
&= \int_{-\infty}^{\infty} f(\tau) h_1(x - \tau) d\tau + \int_{-\infty}^{\infty} f(\tau) h_2(x - \tau) d\tau \\
&= (f \ast h_1)(x) + (f \ast h_2)(x) \\
\end{aligned}
$$

#### Bilinear

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

#### Linear

$$
\begin{aligned}
(f\ast (\alpha h_1 + \beta h_2))(x) &= (f \ast (\alpha h_1))(x) + (f \ast (\beta h_2))(x) \\
&= \alpha (f \ast h_1)(x) + \beta (f \ast h_2)(x) \\
\end{aligned}
$$

#### Associative

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

#### Shift Invariant

$$
\begin{aligned}
g(x)&=S\left\{f(x)\right\} \\
S\left\{f(x-x_0)\right\}&=f(x-x_0)\ast h(x)\\
&=g(x-x_0)\\
\end{aligned}
$$

#### Impulse Response

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

### Separable Convolution

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

## Smoothing (Low-Pass) Filters

$$
\begin{aligned}
m &= 2a + 1 \\
n &= 2b + 1 \\
\end{aligned}
$$

### Mean Filter

The mean filter is a simple sliding-window spatial filter that replaces the center value in the window with the average (mean) of all the pixel values in the window.

$$
\begin{aligned}
h(x, y) &= \frac{1}{mn}\\
g(x, y) &= \frac{\sum_{s=-a}^{a} \sum_{t=-b}^{b} f(x+s, y+t)}{mn}
\end{aligned}
$$

#### Geometric Mean Filter

$$
g(x, y) = \sqrt[mn]{\prod_{s=-a}^{a} \prod_{t=-b}^{b} f(x+s, y+t)}
$$

#### Harmonic Mean Filter

$$
g(x, y) = \frac{mn}{\sum_{s=-a}^{a} \sum_{t=-b}^{b} \frac{1}{f(x+s, y+t)}}
$$

#### Contra-Harmonic Mean Filter

$$
g(x, y) = \frac{\sum_{s=-a}^{a} \sum_{t=-b}^{b} f(x+s, y+t)^{Q+1}}{\sum_{s=-a}^{a} \sum_{t=-b}^{b} f(x+s, y+t)^{Q}}
$$

- If $$Q > 0$$, the filter removes pepper noise.
- If $$Q < 0$$, the filter removes salt noise.
- When $$Q = 0$$, the filter becomes the arithmetic mean filter.
- When $$Q = -1$$, the filter becomes the harmonic mean filter.

#### Alpha-Trimmed Mean Filter

$$
g(x, y) = \frac{1}{mn-d} \sum_{s=-a}^{a} \sum_{t=-b}^{b} f_r(x+s, y+t)
$$

where $$f_r$$ is the sorted sequence of the pixel values in the window, and $$d$$ is the number of pixels to be trimmed from the beginning and end of the sorted sequence.

### Gaussian Filter

The average smoothing treats the same to all the pixels in the neighborhood. In order to reduce the blur in the smoothing process and obtain a more natural smoothing effect, it is natural to think to increase the weight of the template center point and reduce the weight of distant points. So that the new center point intensity is closer to its nearest neighbors. The Gaussian template is based on such consideration.

$$
\begin{aligned}
w(s,t)&=Ke^{-\frac{s^2+t^2}{2\sigma^2}}\\
r=\sqrt{s^2+t^2}&\Rightarrow w(r)=Ke^{-\frac{r^2}{2\sigma^2}}\\
\end{aligned}
$$

where $$r$$ is the distance from the center point. For a n*n (n is odd) square template, the distance between the center point and the farthest point is $$\frac{n-1}{2}\sqrt{2}$$. The greater the distance, the smaller the weight. The weight of the center point is the largest, and the weight of the farthest point is the smallest.

$$
\begin{bmatrix}
\frac{n-1}{2}\sqrt{2}&\dotsb&\dotsb&\dotsb&\dotsb&\dotsb&\frac{n-1}{2}\sqrt{2}\\

\vdots&2\sqrt{2}&\sqrt{5}&2&\sqrt{5}&2\sqrt{2}&\vdots\\
\vdots&\sqrt{5}&\sqrt{2}&1&\sqrt{2}&\sqrt{5}&\vdots\\
\vdots&2&1&0&1&2&\vdots\\
\vdots&\sqrt{5}&\sqrt{2}&1&\sqrt{2}&\sqrt{5}&\vdots\\
\vdots&2\sqrt{2}&\sqrt{5}&2&\sqrt{5}&2\sqrt{2}&\vdots\\
\frac{n-1}{2}\sqrt{2}&\dotsb&\dotsb&\dotsb&\dotsb&\dotsb&\frac{n-1}{2}\sqrt{2}\\
\end{bmatrix}
$$

The filter is normalized by dividing the sum of all the elements by the sum of the weights.

$$
h(x,y)=\frac{1}{\sum_{x=-a}^{a}\sum_{y=-b}^{b}w(x,y)}w(x,y)
$$

It is worth noting that the weight of the point outside $$3\sigma$$ is very small, so the usual size of the Gaussian template is $$6\sigma+1$$.

The gaussian filter is also separable:

$$
\begin{aligned}
w(s,t)&=Ke^{-\frac{s^2+t^2}{2\sigma^2}}\\
&=Ke^{-\frac{s^2}{2\sigma^2}}e^{-\frac{t^2}{2\sigma^2}}\\
&=w(s)w(t)\\
\end{aligned}
$$

### Median Filter

The median filter is a nonlinear filter that replaces the center value in the window with the median of all the pixel values in the window. The median filter is more effective than the mean filter in removing salt-and-pepper noise.

$$
g(x, y) = \text{median}\{f(x+s, y+t)\}
$$

#### Order Filter

Generally, the median filter belongs to the order/rank filter, replacing the center value with the $$k$$-th order statistic of the window. The median filter is a special case of the order filter, where $$k$$ is the median of the window. If $$k=1$$ or $$k=mn$$, the order filter becomes the minimum filter or the maximum filter.

#### Adaptive Median Filter

Given a initial window size $$S_{min}$$, the adaptive median filter is defined as:

1. For each pixel $$f(x, y)$$, increase the window size $$S$$ from $$S_{min}$$ until $$z_{min} < z_{med} < z_{max}$$.
1. If $$S > S_{max}$$, then $$g(x, y) = z_{med}$$, otherwise:

$$
g(x, y) = \left\{
\begin{aligned}
f(x, y) &\quad \text{if } z_{min} < f(x, y) < z_{max} \\
z_{med} &\quad \text{otherwise}
\end{aligned}
\right.
$$

## Sharpening (High-Pass) Filters