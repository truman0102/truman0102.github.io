---
layout: post
title: Image Restoration
date: 2023-10-12 03:00:00-0400
description: An introduction to image restoration in image processing.
tags: image-restoration
categories: image-processing
related_posts: false
giscus_comments: true
thumbnail: 
toc:
  sidebar: left
---

## What is Image Restoration?

General image restoration model consists of two parts: degradation model and restoration model. The degradation model describes the degradation process of the image, and the restoration model is used to restore the image. 

Degradation model can be described as follows:

$$
g(x,y) = f(x,y) \star h(x,y) + \eta(x,y)
$$

where $$g(x,y)$$ is the degraded image, $$f(x,y)$$ is the original image, $$h(x,y)$$ is the degradation function, and $$\eta(x,y)$$ is the noise.

In the frequency domain, the degradation model can be described as follows:

$$
G(u,v) = H(u,v)F(u,v) + N(u,v)
$$

where $$G(u,v)$$ is the degraded image in the frequency domain, $$H(u,v)$$ is the degradation function in the frequency domain, $$F(u,v)$$ is the original image in the frequency domain, and $$N(u,v)$$ is the noise in the frequency domain.

Since the degraded image is known, the degradation function and noise should be estimated to restore the image.

## Types of Noise

## Types of Degradation

## Restoration Methods

### Spatial Domain Methods

### Frequency Domain Methods