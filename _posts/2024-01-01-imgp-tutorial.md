---
layout: post
title: An tutorial on image processing
date: 2024-01-01 00:00:00-0400
description: An introduction to image processing aligned with the course of Image Processing at the University of Chinese Academy of Sciences.
tags: tutorial
categories: image-processing
related_posts: false
giscus_comments: false
thumbnail: 
---

This is an introduction to how my image processing posts are organized, aligned with the [Digital Image Processing](https://amazon.com/Digital-Image-Processing-Rafael-Gonzalez/dp/0133356728) book by Gonzalez and Woods.

***

[Point operations](/blog/2023/point-operation/) are operations that are applied to each pixel in an image. They are the simplest operations that can be performed on an image.

A more complex operation is [spatial filtering](/blog/2023/spatial-filtering/), which is a way to apply a filter to the neighborhood of each pixel in an image. This is a very powerful operation that can be used to perform a wide variety of tasks, such as edge detection, noise removal, and image sharpening.

[Convolution](/blog/2023/convolution/) is a mathematical operation that is used to perform spatial filtering. And Fourier transform is a mathematical operation that is used to transform an image from the spatial domain to the frequency domain, and vice versa. By performing operations in the frequency domain, we can replace convolution in the spatial domain with multiplication in the frequency domain, which is much faster. You are expected to visit the [Fourier transform page](/assets/html/imgp/fourier-transform.html).

Filters are as important as the operations that are performed on images, which can also be classified into [filtering in spatial domain](/blog/2023/spatial-filtering/) and [filtering in frequency domain](/assets/html/imgp/frequency-filter.html), see also some special filters used in [image restoration](/blog/2023/image-restoration/#restoration-in-the-frequency-domain).

Wavelets are introduced in the [Chinese version](/assets/pdf/wavelet-analysis.pdf). And so is the [image compression](/assets/pdf/imgp/image-compression.pdf), including entropy, Hamming code, Huffman code, and arithmetic code.