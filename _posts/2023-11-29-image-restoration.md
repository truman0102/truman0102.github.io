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

### Gaussian Noise

### Salt and Pepper Noise

### Rayleigh Noise

### Exponential Noise

### Uniform Noise

### Gamma Noise

### Periodic Noise

## Types of Degradation

## Restoration in the Spatial Domain

Spatial domain methods are used to restore the image that is only degraded by noise, without degradation function.

$$
\begin{aligned}
g(x,y) &= f(x,y) + \eta(x,y)\\
\hat{f}(x,y) &= g(x,y) - \eta(x,y)
\end{aligned}
$$

### Mean Filter

### Order-Statistic Filter

### Adaptive Filter

### Wiener Filter

## Restoration in the Frequency Domain

### Notch Filter

### Optimal Notch Filter

Let $$H_{NP}(u,v)$$ be the notch filter, and $$G(u,v)$$ be the degraded image in the frequency domain. We can extract the noise from the degraded image by using the notch filter.

$$
N(u,v) = H_{NP}(u,v)G(u,v)
$$

The noise function in the spatial domain can be obtained by using the inverse Fourier transform.

$$
\eta(x,y) = \mathcal{F}^{-1}\{H_{NP}(u,v)G(u,v)\}
$$

The optimal notch filter is based on the assumption that the noise function in the spatial domain is already known.

$$
\hat{f}(x,y) = g(x,y) - \omega(x,y)\eta(x,y)
$$

$$
\omega(x,y) = \frac{\overline{g\eta}-\bar{g}\bar{\eta}}{\overline{\eta^2}-(\bar{\eta})^2}
$$

where $$\bar{g}$$ is the mean of the degraded image, $$\bar{\eta}$$ is the mean of the noise function, $$\overline{g\eta}$$ is the cross-correlation between the degraded image and the noise function, and $$\overline{\eta^2}$$ is the auto-correlation of the noise function in the local area $$S_{xy}$$.