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
- **Spatial filtering** that operates on a neighborhood of pixels.