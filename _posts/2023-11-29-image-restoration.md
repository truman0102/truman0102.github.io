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

### Wiener Filter

$$
\begin{aligned}
\hat{F}(u,v) &= \left [ \frac{H^*(u,v)S_f(u,v)}{|H(u,v)|^2S_f(u,v)+S_\eta(u,v)} \right ]G(u,v)\\
&= \left [ \frac{H^*(u,v)}{|H(u,v)|^2+\frac{S_\eta(u,v)}{S_f(u,v)}} \right ]G(u,v)\\
&= \left [ \frac{1}{H(u,v)}\frac{|H(u,v)|^2}{|H(u,v)|^2+\frac{S_\eta(u,v)}{S_f(u,v)}} \right ]G(u,v)\\
\end{aligned}
$$

- Degradation function $$H(u,v)$$ is a complex function, $$H^2(u,v)=H(u,v)H^*(u,v)$$.
- $$H^*(u,v)$$ is the complex conjugate of $$H(u,v)$$.
- $$\hat{F}(u,v)$$ is the fourier transform of the estimation of the original image.
- $$S_f(u,v)$$ is the power spectrum of the original image.
- $$S_\eta(u,v)$$ is the power spectrum of the noise.
- $$G(u,v)$$ is the fourier transform of the degraded image. 
- Power spectrum is the quadratic power of the fourier transform.

Sometimes the power spectrum of the noise is unknown, so it can be replaced by a constant $$K$$.

$$
\hat{F}(u,v) = \left [ \frac{1}{H(u,v)}\frac{|H(u,v)|^2}{|H(u,v)|^2+K} \right ]G(u,v)
$$

### Geometric Mean Filter

$$
\hat{F}(u,v) = \left [ \frac{H^*(u,v)}{|H(u,v)|^2} \right ]^{\alpha}\left [ \frac{H^*(u,v)}{|H(u,v)|^2+\beta\frac{S_\eta(u,v)}{S_f(u,v)}} \right ]^{1-\alpha}G(u,v)
$$

where $$\alpha$$ and $$\beta$$ are the non-negative parameters.

### Constrained Least Squares Filter

The constrain is

$$
\lVert g-Hf \rVert^2 = \lVert \eta \rVert^2
$$

$$
\hat{F}(u,v) = \left [ \frac{H^*(u,v)}{|H(u,v)|^2+\gamma|P(u,v)|^2} \right ]G(u,v)
$$

where $$P(u,v)$$ is the fourier transform of the laplacian filter.

To estimate $$\gamma$$, we need to define a residual $$r=g-H\hat{f}$$, and adjust $$r$$ until $$\lVert r \rVert^2 = \lVert \eta \rVert^2 \pm \epsilon$$.

## Estimation of Degradation Function

Blind convolution is used to estimate the degradation function.

### Observations

If the noise in the frequency domain is ignored and the estimation of the original image is known,

$$
\hat{H}(u,v) = \frac{G(u,v)}{\hat{F}(u,v)}
$$

In turn, if the degradation function is known, the estimation of the original image can be obtained as follows:

$$
\begin{aligned}
\hat{F}(u,v) &= \frac{G(u,v)}{H(u,v)}\\
&= F(u,v) + \frac{N(u,v)}{H(u,v)}
\end{aligned}
$$

This is called the inverse filtering. The inverse filtering is very sensitive the degradation function. If the degradation function is very small, the noise will be amplified.

### Experiment

Let $$A$$ be the fourier transform of an impulse function, and $$H(u,v)$$ be the degradation function in the frequency domain, $$G(u,v)$$ be the degradation of the impulse function in the frequency domain.

$$
H(u,v) = \frac{G(u,v)}{A}
$$

It is worth noting that the fourier transform of an impulse function is a constant function.

### Modelization

Assuming that the image moves with uniform velocity in both x and y directions, the exposure time is T. And the displacement of the image in the x and y directions is $$x_0(t)$$ and $$y_0(t)$$ respectively.

$$
g(x,y) = \int_{0}^{T}f(x-x_0(t),y-y_0(t))dt
$$

The fourier transform of the degradation function can be obtained as follows:

$$
\begin{aligned}
G(u,v) &= \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}g(x,y)e^{-j2\pi(ux+vy)}dxdy\\
&= \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\int_{0}^{T}f(x-x_0(t),y-y_0(t))e^{-j2\pi(ux+vy)}dtdxdy\\
&= \int_{0}^{T}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(x-x_0(t),y-y_0(t))e^{-j2\pi(ux+vy)}dxdydt\\
&= \int_{0}^{T}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(x,y)e^{-j2\pi(ux+vy)}e^{-j2\pi(ux_0(t)+vy_0(t))}dxdydt\\
&= \int_{0}^{T}(\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(x,y)e^{-j2\pi(ux+vy)}dxdy) e^{-j2\pi(ux_0(t)+vy_0(t))}dt\\
&= \int_{0}^{T}F(u,v)e^{-j2\pi(ux_0(t)+vy_0(t))}dt\\
&= F(u,v)\int_{0}^{T}e^{-j2\pi(ux_0(t)+vy_0(t))}dt\\
H(u,v) &= \frac{G(u,v)}{F(u,v)}\\
&= \int_{0}^{T}e^{-j2\pi(ux_0(t)+vy_0(t))}dt
\end{aligned}
$$

## Metrics for Image Restoration

### Mean Square Error (MSE)

$$
MSE = \frac{1}{MN}\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}[f(x,y)-\hat{f}(x,y)]^2
$$

### Signal-to-Noise Ratio (SNR)

$$
SNR = \frac{\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}[\hat{f}(x,y)]^2}{\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}[f(x,y)-\hat{f}(x,y)]^2}
$$

$$
SNR= \frac{\sum_{u=0}^{M-1}\sum_{v=0}^{N-1}[F(u,v)]^2}{\sum_{u=0}^{M-1}\sum_{v=0}^{N-1}[N(u,v)]^2}
$$