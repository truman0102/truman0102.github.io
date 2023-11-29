---
layout: post
title: Image Enhancement
date: 2023-10-12 00:00:00-0400
description: An introduction to image enhancement in image processing.
tags: image-enhancement
categories: image-processing
related_posts: false
giscus_comments: true
thumbnail: 
toc:
  sidebar: left
---

## What is Image Enhancement?

Image enhancement is the process of emphasizing specific details within an image, while simultaneously reducing or removing any superfluous elements. This can include removing noise, revealing obscured details, and adjusting image levels to bring attention to particular features.

There are two primary categories of image enhancement techniques:

- **Spatial domain** techniques operate directly on pixels in an image.
- **Frequency domain** techniques operate on the frequency domain representation of an image, usually applying a Fourier transform to the image.

## Spatial Domain Techniques

Spatial domain techniques can be subdivided into:

- **[Point operations](/blog/2023/point-operation/)** that operate on individual pixels.
- **[Spatial filtering](/blog/2023/spatial-filtering)** that operates on a neighborhood of pixels.

## Frequency Domain Techniques

### Filtering in Frequency Domain

1. Given an image $$f(x,y)$$ of size $$M \times N$$, pad the image with zeros to size $$P \times Q$$, where $$P=2M$$ and $$Q=2N$$.
2. Use the zero/replicated/symmetric padding method to pad the image.
3. Multiply the image by $$(-1)^{x+y}$$ to center the fourier transform.
4. Calculate the fourier transform $$F(u,v)$$ of the new image.
5. Create a filter function $$H(u,v)$$ of size $$P \times Q$$, whose center is at $$\left(\frac{P}{2}, \frac{Q}{2}\right)$$.
6. Multiply $$F(u,v)$$ by $$H(u,v)$$ to get $$G(u,v)$$.
7. Compute the inverse fourier transform $$g(x,y)$$ of $$G(u,v)$$, keep the real part of $$g(x,y)$$ and multiply it by $$(-1)^{x+y}$$, to get the filtered image.
8. Crop the filtered image to size $$M \times N$$.