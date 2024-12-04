---
layout: post
title: Convolution
date: 2023-10-12 02:00:00-0400
description: An introduction to convolution in image processing.
tags: convolution
categories: image-processing
related_posts: false
giscus_comments: false
thumbnail: 
toc:
  sidebar: left
---

## What is Convolution?

Convolution is a mathematical operation that is used to express the relation between input and output of an LTI system. It is a mathematical way of combining two signals to form a third signal. 

It is the single most important technique in Digital Signal Processing, used to filter images, perform edge detection, perform blurring, and much more.

Convolution is a mathematical operation on two signals, $$f$$ and $$h$$, to produce a third signal, $$g$$. It is defined as the integral of the product of the two functions after one is reversed and shifted. The integral is evaluated for all values of shift, producing the convolution function $$g$$.

$$
g(x) = (f \ast h)(x) = \int_{-\infty}^{\infty} f(\tau) h(x - \tau) d\tau = \int_{-\infty}^{\infty} f(x - \tau) h(\tau) d\tau
$$

Convolution between an image and a kernel is performed by sliding the kernel over the image, multiplying the kernel's values with the overlapping image pixel values, and summing them up.

$$
(w \star f)(x, y) = \sum_{i=-a}^{a} \sum_{j=-b}^{b} w(i, j) f(x-i, y-j)
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

## Convolution in Image Processing

In image processing, convolution is performed by sliding a kernel over the image, multiplying the kernel's values with the overlapping image pixel values, and summing them up.

$$
(w \star f)(x, y) = \sum_{i=-a}^{a} \sum_{j=-b}^{b} w(i, j) f(x-i, y-j)
$$

where $$w$$ is the kernel, $$f$$ is the image, and $$a$$ and $$b$$ are the kernel's half-width and half-height, respectively.

### Kernel

A kernel is a small matrix used in image processing to perform operations such as blurring, sharpening, edge detection, and more. The kernel is usually a square matrix with odd dimensions. The kernel is also known as a filter.

### Padding

The output of the convolution operation is a matrix that is smaller than the input image. This is because the kernel cannot be centered on pixels at the edges of the image. To solve this problem, the image is padded with some pixels around the edges. The common padding methods are:

- **Zero Padding**: The image is padded with zeros around the edges.
- **Replicate Padding**: The pixels at the edges of the image are replicated to pad the image.
- **Symmetric Padding**: The pixels at the edges of the image are mirrored to pad the image.

### Stride

The stride is the number of pixels by which the kernel is shifted when it is moved over the image. The stride is usually set to 1, but it can be set to any value. A larger stride will result in a smaller output image.

### Implementation

```python
import numpy as np

# gaussian kernel
def gaussian_kernel(size, sigma=1):
    """
    Generates a Gaussian kernel of size size x size and standard deviation sigma.
    """
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g

# convolution
def convolution(image, kernel, stride=1, padding=None):
  """
  Performs convolution between an image and a kernel.
  : param image: input image, a 2D numpy array
  : param kernel: kernel, a 2D numpy array
  : param stride: stride, default 1
  : param padding: padding method, default None, options: "zero", "replicate", "symmetric", "circular"
  : return: convolved image, a 2D numpy array
  """
  m, n = kernel.shape # kernel dimensions
  M, N = image.shape # image dimensions
  image_copy = image.copy() # copy of image
  assert m % 2 == 1 and n % 2 == 1, "Kernel dimensions must be odd"
  assert padding in ["zero", "replicate", "symmetric", "Circular", None], "Invalid padding"


  a = (m - 1) // 2 # half-width
  b = (n - 1) // 2 # half-height

  kernel = kernel[::-1, ::-1] # flip kernel

  if padding is None: # no padding
    res = image.copy()
    for i in range(a, M-a, stride): # loop over rows
      for j in range(b, N-b, stride): # loop over columns
        image_copy[i, j] = np.sum(res[i-a:i+a+1, j-b:j+b+1] * kernel) # convolution
    return image_copy[a:-a, b:-b] # return image without padding
  else:
    res = np.zeros((M + 2*a, N + 2*b)) # padded image
    res[a:-a, b:-b] = image # copy image to padded image
    if padding == "zero":
      pass
    elif padding == "replicate": # replicate padding
      res[:a, b:-b] = image[0]
      res[-a:, b:-b] = image[-1]
      res[:, :b] = res[:, b:2*b][:, ::-1]
      res[:, -b:] = res[:, -2*b:-b][:, ::-1]
    elif padding == "symmetric": # symmetric padding
      res[:a, b:-b] = image[a:0:-1]
      res[-a:, b:-b] = image[-2:-a-2:-1]
      res[:, :b] = res[:, b:2*b][:, ::-1]
      res[:, -b:] = res[:, -2*b:-b][:, ::-1]
    elif padding == "circular": # circular padding
      res[:a, b:-b] = image[-a:]
      res[-a:, b:-b] = image[:a]
      res[:, :b] = image[:, -b:]
      res[:, -b:] = image[:, :b]
    else:
      raise ValueError("Invalid padding")

  for i in range(a, M+a, stride): # loop over rows
    for j in range(b, N+b, stride): # loop over columns
      image_copy[i-a, j-b] = np.sum(res[i-a:i+a+1, j-b:j+b+1] * kernel) # convolution

  return image_copy
```