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

### [Gaussian](/blog/2023/probability-distribution/#normal-distribution) Noise

### Salt and Pepper Noise

Salt noise is the pixel with maximum value, since salt is white. And pepper noise is the pixel with minimum value, since pepper is black.

$$
p(z)=\left\{
\begin{aligned}
&P_s, &\; &z=2^L-1\\
&P_p, &\; &z=0\\
&1-(P_s+P_p), &\; &otherwise
\end{aligned}
\right.
$$

### [Rayleigh](/blog/2023/probability-distribution/#rayleigh-distribution) Noise

### [Exponential](/blog/2023/probability-distribution/#exponential-distribution) Noise

### [Uniform](/blog/2023/probability-distribution/#uniform-distribution) Noise

### [Gamma](/blog/2023/probability-distribution/#gamma-distribution) Noise

### Periodic Noise

### Estimation of Noise

$$
\begin{aligned}
\bar{z} &= \sum_{i=0}^{L-1}z_ip(z_i) \\ 
\sigma^2 &= \sum_{i=0}^{L-1}(z_i-\bar{z})^2p(z_i)\\
\end{aligned}
$$

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

#### Adaptive, local noise reduction filter

#### Adaptive median filter

## Restoration in the Frequency Domain

The origin in the frequency domain is usually located at the center of the image $$(\frac{M}{2},\frac{N}{2})$$, where $$M$$ and $$N$$ are the width and height of the transformed image respectively. The distance from the origin to the point $$(u,v)$$ is defined as follows:

$$
D(u,v) = \sqrt{(u-\frac{M}{2})^2+(v-\frac{N}{2})^2}
$$

### Bandreject Filter

Let $$D_0$$ be the center of the rejection band, and $$W$$ be the width of the rejection band. The ideal bandreject filter is defined as follows:

$$
H_{BR}(u,v) = \left\{
\begin{aligned}
&0, &\; &D_0-\frac{W}{2} \leq D(u,v) \leq D_0+\frac{W}{2}\\
&1, &\; &\text{otherwise}
\end{aligned}
\right.
$$

where $$D(u,v)$$ is the distance from the point $$(u,v)$$ to the center of the frequency plane.

A practical bandreject filter is a $$n$$-order butterworth filter, which is defined as follows:

$$
H_{BR}(u,v) = \frac{1}{1+\left(\frac{D(u,v)W}{D^2(u,v)-D_0^2}\right)^{2n}}
$$

And the gaussian bandreject filter is defined as follows:

$$
H_{BR}(u,v) = 1-e^{-\frac{1}{2}\left(\frac{D^2(u,v)-D_0^2}{D(u,v)W}\right)^2}
$$

Since the bandreject filter is the difference between the constant $$1$$ and the bandpass filter $$H_{BP}(u,v)$$. The exponent of the gaussian bandreject filter is similar to the high-order component of the denominator of the butterworth bandpass filter. The closer the frequency is to the center of the frequency plane, the smaller the value of the bandreject filter.

### Bandpass Filter

The ideal bandpass filter is defined as follows:

$$
H_{BP}(u,v) = \left\{
\begin{aligned}
&1, &\; &D_0-\frac{W}{2} \leq D(u,v) \leq D_0+\frac{W}{2}\\
&0, &\; &\text{otherwise}
\end{aligned}
\right.
$$

So a bandpass filter can be obtained by subtracting a bandreject filter from a constant $$1$$.

$$
H_{BP}(u,v) = 1-H_{BR}(u,v)
$$

A practical example of a gaussian bandpass filter is similar to the gaussian bandreject filter.

$$
H_{BP}(u,v) = e^{-\frac{1}{2}\left(\frac{D^2(u,v)-D_0^2}{D(u,v)W}\right)^2}
$$

### Notch Filter

The most important feature of the notch filter is that the bandstop centre is symmetric ($$(\frac{M}{2} + u_0, \frac{N}{2} + v_0)$$ and $$(\frac{M}{2} - u_0, \frac{N}{2} - v_0)$$), so there are two corresponding distances $$D_1$$ and $$D_2$$.

$$
\begin{aligned}
D_1 &= \sqrt{(u-\frac{M}{2}-u_0)^2+(v-\frac{N}{2}-v_0)^2}\\
D_2 &= \sqrt{(u-\frac{M}{2}+u_0)^2+(v-\frac{N}{2}+v_0)^2}\\
\end{aligned}
$$

The ideal notch filter is defined as follows:

$$
H_{NR}(u,v) = \left\{
\begin{aligned}
&0, &\; &D_1 \leq \frac{W}{2} \; \text{or} \; D_2 \leq \frac{W}{2}\\
&1, &\; &\text{otherwise}
\end{aligned}
\right.
$$

A practical example of a $$n$$-order butterworth notch filter is defined as follows:

$$
H_{NR}(u,v) = \frac{1}{1+\left(\frac{W^2}{4D_1D_2}\right)^{n}}
$$

And the gaussian notch reject filter is defined as follows:

$$
H_{NR}(u,v) = 1-e^{-\frac{1}{2}\left(\frac{4D_1D_2}{W^2}\right)}
$$

The notch pass filter is the difference between the constant $$1$$ and the notch reject filter $$H_{NR}(u,v)$$.

$$
H_{NP}(u,v) = 1-H_{NR}(u,v)
$$

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

- Degradation function $$H(u,v)$$ is a complex function, and $$H^*(u,v)$$ is the complex conjugate of $$H(u,v)$$.

$$
|H(u,v)|^2 =\left\langle H(u,v), H(u,v) \right\rangle = H^*(u,v)H(u,v)
$$

- $$\hat{F}(u,v)$$ is the fourier transform of the estimation of the original image.
- Power spectrum is the quadratic power of the fourier transform.
- - $$S_f(u,v)$$ is the power spectrum of the original image.

$$
S_f(u,v) = |F(u,v)|^2
$$

- - $$S_\eta(u,v)$$ is the power spectrum of the noise.

$$
S_\eta(u,v) = |N(u,v)|^2
$$

- $$G(u,v)$$ is the fourier transform of the degraded image. 

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

The constrained least squares filter is used to estimate the original image when the degradation function is known.

$$
C = \sum_{x=0}^{M-1}\sum_{y=0}^{N-1}[\triangledown^2f(x,y)]^2\\
$$

$$
\begin{aligned}
\triangledown^2f(x,y) &= f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)-4f(x,y)\\
&=(f\star h)(x,y)
\end{aligned}
$$

where $$h$$ is the laplacian filter.

The constrain is

$$
\lVert g-H\hat{f} \rVert^2 = \lVert \eta \rVert^2
$$

The fourier transform of $$C$$ is $$P\hat{F}$$, where $$P$$ is the fourier transform of the laplacian filter. So the lagrangian function is

$$
L(\hat{F},\lambda) = \lVert P\hat{F} \rVert^2 + \lambda(\lVert G-H\hat{F} \rVert^2 - \lVert N \rVert^2)
$$

The partial derivative of $$L$$ with respect to $$\hat{F}$$ is

$$
\begin{aligned}
\frac{\partial L}{\partial \hat{F}} &= \frac{\partial}{\partial \hat{F}}(\lVert P\hat{F} \rVert^2 + \lambda(\lVert G-H\hat{F} \rVert^2 - \lVert N \rVert^2))\\
&= 2P^*P\hat{F}+2\lambda H^*H\hat{F}-2\lambda H^*G\\
&= 2(P^*P+\lambda H^*H)\hat{F}-2\lambda H^*G\\
\end{aligned}
$$

If $$\frac{\partial L}{\partial \hat{F}}=0$$, then

$$
\begin{aligned}
\hat{F} &= \frac{\lambda H^*G}{P^*P+\lambda H^*H}\\
&= \frac{H^*G}{\frac{P^*P}{\lambda}+H^*H}\\
&= \frac{H^*G}{|H|^2+\gamma|P|^2}\\
\end{aligned}
$$

Therefore, the estimation of the original image is

$$
\hat{F}(u,v) = \left [ \frac{H^*(u,v)}{|H(u,v)|^2+\gamma|P(u,v)|^2} \right ]G(u,v)
$$

where $$P(u,v)$$ is the fourier transform of the laplacian filter.

To estimate $$\gamma$$, we need to define a residual $$r=g-H\hat{f}$$, and adjust $$r$$ until $$\lVert r \rVert^2 = \lVert \eta \rVert^2 \pm \epsilon$$.

$$
R(u,v) = G(u,v)-H(u,v)\hat{F}(u,v)
$$

$$
r = \mathcal{F}^{-1}\{R(u,v)\}
$$

The larger the $$\gamma$$, the smaller the $$\hat{F}$$, and the larger the $$r$$. So we can adjust $$\gamma$$ until $$\lVert r \rVert^2 = \lVert \eta \rVert^2 \pm \epsilon$$.

$$
\begin{aligned}
\phi(\gamma) &= \lVert r \rVert^2\\
&= r^Tr\\
&= \sum_{x=0}^{M-1}\sum_{y=0}^{N-1}r^2(x,y)\\
\end{aligned}
$$

To estimate $$\lVert\eta\rVert^2$$, it is known that $$D(x)=E(x^2)-[E(x)]^2$$, where $$D(x)$$ is the variance of $$x$$, $$E(x)$$ is the mean of $$x$$. So $$E(x^2)=D(x)+[E(x)]^2$$.

$$
\begin{aligned}
\lVert\eta\rVert^2 &= MN(\sigma_{\eta}^2+\bar{\eta}^2)\\
\bar{\eta} &= \frac{1}{MN}\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}\eta(x,y)\\
\sigma_{\eta}^2 &= \frac{1}{MN}\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}[\eta(x,y)-\bar{\eta}]^2\\
\end{aligned}
$$

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