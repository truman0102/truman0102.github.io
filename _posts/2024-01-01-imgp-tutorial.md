---
layout: post
title: Digital Image Processing
date: 2024-01-01 00:00:00-0400
description: An introduction to image processing aligned with the course of Image Processing at the University of Chinese Academy of Sciences.
tags: tutorial
categories: image-processing
related_posts: false
giscus_comments: false
thumbnail: 
featured: true
---

## Introduction

This is an introduction to how my image processing posts are organized, aligned with the [Digital Image Processing](https://amazon.com/Digital-Image-Processing-Rafael-Gonzalez/dp/0133356728) book by Gonzalez and Woods.

***

## Point operations

An image is a two-dimensional function $$f(x, y)$$, where $$x$$ and $$y$$ are spatial coordinates, and the amplitude of $$f$$ at any pair of coordinates $$(x, y)$$ is called the intensity or gray level of the image at that point. When $$x$$, $$y$$, and the amplitude values of $$f$$ are all finite, discrete quantities, we call the image a **digital image**.

$$
\begin{bmatrix}
\cdots & \cdots & \cdots & \cdots & \cdots \\
\cdots & f(x-1, y-1) & f(x-1, y) & f(x-1, y+1) & \cdots \\
\cdots & f(x, y-1) & f(x, y) & f(x, y+1) & \cdots \\
\cdots & f(x+1, y-1) & f(x+1, y) & f(x+1, y+1) & \cdots \\
\cdots & \cdots & \cdots & \cdots & \cdots
\end{bmatrix}
$$

The specific representation of the image depends on the [color system](/blog/2023/color-system/) used. For example, a grayscale image is represented by a single intensity value at each spatial coordinate, while a color image is represented by three intensity values at each spatial coordinate, corresponding to the three primary colors.


[Point operations](/blog/2023/point-operation/) are operations that are applied to each pixel in an image. They are the simplest operations that can be performed on an image.

## Image Enhancement

Image enhancement is the process of emphasizing specific details within an image, while simultaneously reducing or removing any superfluous elements. This can include removing noise, revealing obscured details, and adjusting image levels to bring attention to particular features.

There are two primary categories of image enhancement techniques:

- **Spatial domain** techniques operate directly on pixels in an image.
- **Frequency domain** techniques operate on the frequency domain representation of an image, usually applying a Fourier transform to the image.

[Spatial filtering](/blog/2023/spatial-filtering/) is a more complex operation, which is a way to apply a filter to the neighborhood of each pixel in an image. This is a very powerful operation that can be used to perform a wide variety of tasks, such as edge detection, noise removal, and image sharpening. [Convolution](/blog/2023/convolution/) is a mathematical operation that is used to perform spatial filtering. 

And [Fourier transform](/assets/html/imgp/fourier-transform.html) is a mathematical operation that is used to transform an image from the spatial domain to the frequency domain, and vice versa. By performing operations in the frequency domain, we can replace convolution in the spatial domain with multiplication in the frequency domain, which is much faster.

The key to enchance an image is to construct a filter function, which is a function that can be applied to an image to produce an enhanced image. Filters are as important as the operations that are performed on images, which can also be classified into [filtering in spatial domain](/blog/2023/spatial-filtering/) and [filtering in frequency domain](/assets/html/imgp/frequency-filter.html), see also some special filters used in [image restoration](/blog/2023/image-restoration/#restoration-in-the-frequency-domain).

There are four basic types of filters:

1. **Lowpass filter**: allows low frequency components to pass through, while attenuating high frequency components, equivalent to a blurring operation, including [mean filter](/blog/2023/spatial-filtering/#mean-filter), [median filter](/blog/2023/spatial-filtering/#median-filter), [gaussian filter](/blog/2023/spatial-filtering/#gaussian-filter), etc.
2. **Highpass filter**: allows high frequency components to pass through, while attenuating low frequency components, equivalent to a sharpening operation, including [laplacian filter](/blog/2023/spatial-filtering/#laplacian-filter), [sobel filter](/blog/2023/spatial-filtering/#sobel-operator), [unsharp masking](/blog/2023/spatial-filtering/#unsharp-masking), etc.
3. **Bandreject filter**: attenuates components in a specific frequency band, including [notch filter](/blog/2023/image-restoration/#notch-filter), etc. Bandreject filter is a combination of lowpass filter and highpass filter.
4. **Bandpass filter**: allows components in a specific frequency band to pass through. Bandpass filter can be regarded as the difference between a constant and a Bandreject filter.

In the proof of Fourier transform, we have shown that convolution in spatial domain is equivalent to multiplication in frequency domain.

$$
\mathcal{F}\{f(x,y) \star g(x,y)\} = F(u,v)G(u,v)
$$

If the signal of an image $$f(x,y)$$ consists of a low-frequency component $$F_l(u,v)$$ and a high-frequency component $$F_h(u,v)$$, then the image can be with a lowpass filter $$H_l(u,v)$$ and a highpass filter $$H_h(u,v)$$.

$$
\begin{aligned}
\mathcal{F}\{f(x,y)\} &= F_l(u,v) + F_h(u,v) \\
\mathcal{F}\{f(x,y) \star h_l(x,y)\} &= F(u,v)H_l(u,v) \\
\mathcal{F}\{f(x,y) \star h_h(x,y)\} &= F(u,v)H_h(u,v) \\
\mathcal{F}\{f(x,y) \star (h_l(x,y) + h_h(x,y))\} &= F(u,v)(H_l(u,v) + H_h(u,v)) = F(u,v) \\
H_l + H_h &= 1
\end{aligned}
$$

which means that the ideal lowpass filter and the ideal highpass filter are complementary to each other, and the sum of the two filters is a constant $$1$$. Actually, a low-pass filter can be used to construct all other three types of filters.

## Image Restoration

Frequency domain techniques are usually used to restore images that have been degraded or corrupted by noise. They can be subdivided into:

$$
\text{Original Image} f(x,y) \xrightarrow{\text{Fourier Transform}} F(u,v) \xrightarrow{\text{Degradation Function} H} G(u,v)=H(u,v)F(u,v) + N(u,v) \xrightarrow{\text{Restoration Filter}} \hat{F}(u,v) \xrightarrow{\text{Inverse Fourier Transform}} \hat{f}(x,y)
$$

Basic steps of image restoration in frequency domain are:

1. Given an image $$f(x,y)$$ of size $$M \times N$$, pad the image with zeros to size $$P \times Q$$, where $$P=2M$$ and $$Q=2N$$.
2. Use the zero/replicated/symmetric padding method to pad the image.
3. Multiply the image by $$(-1)^{x+y}$$ to center the fourier transform.
4. Calculate the fourier transform $$F(u,v)$$ of the new image.
5. Create a filter function $$H(u,v)$$ of size $$P \times Q$$, whose center is at $$\left(\frac{P}{2}, \frac{Q}{2}\right)$$.
6. Multiply $$F(u,v)$$ by $$H(u,v)$$ to get $$G(u,v)$$.
7. Compute the inverse fourier transform $$g(x,y)$$ of $$G(u,v)$$, keep the real part of $$g(x,y)$$ and multiply it by $$(-1)^{x+y}$$, to get the filtered image.
8. Crop the filtered image to size $$M \times N$$.

## Other Topics

[Wavelets analysis](/assets/pdf/imgp/wavelet-analysis.pdf) are introduced in the Chinese version. And so is the [image compression](/assets/html/imgp/image-compression.html), including entropy, Hamming code, Huffman code, and arithmetic code.