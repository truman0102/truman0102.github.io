---
layout: post
date: 2023-12-24 11:12:00-0400
title: An introduction to image processing posts
inline: false
related_posts: false
---

This is an introduction to how my image processing posts are organized, aligned with the [Digital Image Processing]() book by Gonzalez and Woods.

***

[Point operations](/blog/2023/point-operation/) are operations that are applied to each pixel in an image. They are the simplest operations that can be performed on an image.

A more complex operation is [spatial filtering](/blog/2023/spatial-filtering/), which is a way to apply a filter to the neighborhood of each pixel in an image. This is a very powerful operation that can be used to perform a wide variety of tasks, such as edge detection, noise removal, and image sharpening.

[Convolution](/blog/2023/convolution/) is a mathematical operation that is used to perform spatial filtering. And [Fourier transform](/blog/2023/fourier-transform/) is a mathematical operation that is used to transform an image from the spatial domain to the frequency domain, and vice versa. By performing operations in the frequency domain, we can replace convolution in the spatial domain with multiplication in the frequency domain, which is much faster. You are expected to visit the [Fourier transform page](/assets/html/imgp/fourier-transform.html).

Filters are as important as the operations that are performed on images, which can also be classified into [filtering in spatial domain](/blog/2023/spatial-filtering/) and [filtering in frequency domain](/blog/2023/image-restoration/#restoration-in-the-frequency-domain) (see also the low-pass and high-pass in [fourier transforms](/assets/html/imgp/fourier-transform.html)), and can also be categorized into low-pass filters and high-pass filters, or [band-pass filters](/blog/2023/image-restoration/#bandpass-filter) and [band-reject filters](/blog/2023/image-restoration/#bandreject-filter).
