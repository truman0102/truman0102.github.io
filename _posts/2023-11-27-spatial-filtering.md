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
g(x, y) = (f \star h)(x, y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} f(x-s, y-t) h(s, t)
$$

where $$a$$ and $$b$$ are the half-widths of the filter. Similarly, the correlation operation is defined as:

$$
g(x, y) = (f \ast h)(x, y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} f(x+s, y+t) h(s, t)
$$

## [Convolution](/blog/2023/convolution/)

The default operation between an image and a filter is convolution.

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

The filter is normalized by dividing the sum of all the elements in the filter.

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

#### [Optimal Notch Filter](/blog/2023/image-restoration/#optimal-notch-filter)

## Sharpening (High-Pass) Filters

Since spatial filtering is discrete, the derivative of the image intensity function is approximated by the difference between the pixel values in the neighborhood:

$$
\begin{aligned}
\frac{\partial f}{\partial x} &\approx f(x+1, y) - f(x, y) \\
\frac{\partial^2 f}{\partial x^2} &\approx f(x+1, y) - 2f(x, y) + f(x-1, y) \\
\frac{\partial f}{\partial y} &\approx f(x, y+1) - f(x, y) \\
\frac{\partial^2 f}{\partial y^2} &\approx f(x, y+1) - 2f(x, y) + f(x, y-1) \\
\end{aligned}
$$

### Laplacian Filter

The Laplacian filter is a second-order derivative filter, which is used to detect edges and is very sensitive to noise. The Laplacian filter is defined as:

$$
\begin{aligned}
\triangledown^2 f &= \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} \\
&= f(x+1, y) + f(x-1, y) + f(x, y+1) + f(x, y-1) - 4f(x, y) \\
&=(f \star h)(x, y) \\
\end{aligned}
$$

Common Laplacian filters are:

$$
\begin{aligned}
&\begin{bmatrix}
0&1&0\\
1&-4&1\\
0&1&0\\
\end{bmatrix}
&\begin{bmatrix}
-1&-1&-1\\
-1&8&-1\\
-1&-1&-1\\
\end{bmatrix}\\
&\begin{bmatrix}
1&1&1\\
1&-8&1\\
1&1&1\\
\end{bmatrix}
&\begin{bmatrix}
0&-1&0\\
-1&4&-1\\
0&-1&0\\
\end{bmatrix}
\end{aligned}
$$

To sharpen the image, the Laplacian filter is convolved with the image, and the result is added to the original image if center pixel of the Laplacian filter is positive (right two filters), or subtracted from the original image if the center pixel is negative (left two filters).

$$
g(x, y) = f(x, y) \pm \alpha \triangledown^2 f(x, y)
$$

It is worth noting that the sum of the coefficients of the Laplacian filter is zero, so the convolution result of a region with same intensity is zero.

### First-Order Derivative Filters

$$\begin{aligned}
G&=\sqrt{G_x^2+G_y^2}\\
&\approx|G_x|+|G_y|\\
\end{aligned}
$$

#### Roberts Cross Operator

$$
\begin{aligned}
\pm\begin{bmatrix}
1&0\\
0&-1\\
\end{bmatrix}\quad
\pm\begin{bmatrix}
0&1\\
-1&0\\
\end{bmatrix}
\end{aligned}
$$

#### Prewitt Operator

$$
\begin{aligned}
h_x &= \begin{bmatrix}
-1 & 0 & 1\\
-1 & 0 & 1\\
-1 & 0 & 1\\
\end{bmatrix}
&=\begin{bmatrix}
1\\
1\\
1\\
\end{bmatrix}
\ast
\begin{bmatrix}
-1&0&1\\
\end{bmatrix} \\
h_y &= \begin{bmatrix}
-1 & -1 & -1\\
0 & 0 & 0\\
1 & 1 & 1\\
\end{bmatrix}
&=\begin{bmatrix}
-1\\
0\\
1\\
\end{bmatrix}
\ast
\begin{bmatrix}
1&1&1\\
\end{bmatrix} \\
\end{aligned}
$$

$$
\begin{aligned}
g_x(x, y) &= (f \ast h_x)(x, y) \\
&= f_7 + f_8 + f_9 - f_1 - f_2 - f_3 \\
g_y(x, y) &= (f \ast h_y)(x, y) \\
&= f_3 + f_6 + f_9 - f_1 - f_4 - f_7 \\
\end{aligned}
$$

#### Sobel Operator

Sobel filter is used to detect edges/calculate the gradient of an image. 

$$
\begin{aligned}
h_x &= \begin{bmatrix}
-1 & 0 & 1\\
-2 & 0 & 2\\
-1 & 0 & 1\\
\end{bmatrix}
&=\begin{bmatrix}
1\\
2\\
1\\
\end{bmatrix}
\ast
\begin{bmatrix}-1&0&1\\
\end{bmatrix} \\
h_y &= \begin{bmatrix}
-1 & -2 & -1\\
0 & 0 & 0\\
1 & 2 & 1\\
\end{bmatrix}
&=\begin{bmatrix}
-1\\
0\\
1\\
\end{bmatrix}
\ast
\begin{bmatrix}
1&2&1\\
\end{bmatrix} \\
\end{aligned}
$$

$$
\begin{aligned}
g_x(x, y) &= (f \ast h_x)(x, y) \\
&= f_7 + 2f_8 + f_9 - f_1 - 2f_2 - f_3 \\
g_y(x, y) &= (f \ast h_y)(x, y) \\
&= f_3 + 2f_6 + f_9 - f_1 - 2f_4 - f_7 \\
\end{aligned}
$$

### Unsharp Masking

In unsharp masking, a blurred image is subtracted from the original image to get its edges only, and the result is added to the original image to get an enhanced version.

$$
h_o = \left [ \begin{matrix}
0 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 0 \\
\end{matrix} \right ]
$$

$$
f(x,y) = (f\star h_o)(x,y)
$$

$$
\begin{aligned}
g(x, y) &= f(x, y) + \alpha (f(x, y) - (f \star h)(x, y)) \\
&= (1 + \alpha) f(x, y) - \alpha (f \star h)(x, y) \\
&= (1 + \alpha)(f\star h_o)(x,y) - \alpha (f \star h)(x, y) \\
&= (f\star((1 + \alpha)h_o - \alpha h))(x,y)
\end{aligned}
$$

where $$h$$ is a low-pass filter to make the image blurred. An example of $$h$$ is an average filter $$h(x, y) = 1$$. Then the sharpening filter is:

$$
h_s = (1 + \alpha)h_o - \alpha h = \begin{bmatrix}
0 & 0 & 0 \\
0 & 1 + \alpha & 0 \\
0 & 0 & 0 \\
\end{bmatrix} - \alpha \begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1 \\
\end{bmatrix} = \begin{bmatrix}
-\alpha & -\alpha & -\alpha \\
-\alpha & 1 & -\alpha \\
-\alpha & -\alpha & -\alpha \\
\end{bmatrix}
$$
