---
layout: post
title: Probability Distribution
date: 2023-09-01 03:00:00-0400
description: An introduction to probability distribution in Probability and Statistics.
tags: math
categories: statistics
related_posts: false
giscus_comments: false
toc:
  sidebar: left
---

## What is Probability Distribution?

Probability distribution is a function that describes the probability of a random variable taking certain values.

## Types of Probability Distribution

### Discrete Probability Distribution

### Continuous Probability Distribution

## Probability Distribution Functions

### Uniform Distribution

$$
f(x;a,b) = \left\{
\begin{array}{ll}
\frac{1}{b-a} & a \leq x \leq b \\
0 & \text{otherwise}
\end{array}
\right.
$$

### Normal Distribution

$$
f(x;\mu,\sigma) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

### Bernoulli Distribution

$$
f(x;p) = \left\{
\begin{array}{ll}
p & x = 1 \\
1-p & x = 0
\end{array}
\right.
$$

### Binomial Distribution

$$
\binom{n}{x} = \frac{n!}{x!(n-x)!}
$$

$$
f(x;n,p) = \binom{n}{x} p^x (1-p)^{n-x}
$$


### Poisson Distribution

$$
f(x;\lambda) = \frac{\lambda^x e^{-\lambda}}{x!}
$$

### Exponential Distribution

$$
f(x;\lambda) = \left\{
\begin{array}{ll}
\lambda e^{-\lambda x} & x \geq 0 \\
0 & x < 0
\end{array}
\right.
$$

$$
F(x) = \left\{
\begin{array}{ll}
1 - e^{-\lambda x} & x \geq 0 \\
0 & x < 0
\end{array}
\right.
$$

### Gamma Distribution

$$
\begin{aligned}
\Gamma(\alpha) &= \int_0^\infty x^{\alpha-1} e^{-x} dx\\
\Gamma(\alpha + 1) &= \int_0^\infty x^{\alpha} e^{-x} dx\\
&= \int_0^\infty x^{\alpha} d(-e^{-x})\\
&= \left. x^{\alpha} (-e^{-x}) \right|_0^\infty - \int_0^\infty \alpha x^{\alpha-1} (-e^{-x}) dx\\
&= 0 + \alpha \int_0^\infty x^{\alpha-1} e^{-x} dx\\
&= \alpha \Gamma(\alpha)\\
\Gamma(n+1) &= n!\\
\end{aligned}
$$

$$
f(x;\alpha,\beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}
$$

### Beta Distribution

$$
f(x;\alpha,\beta) = \frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha)\Gamma(\beta)} x^{\alpha-1} (1-x)^{\beta-1}
$$

### Rayleigh Distribution

$$
f(x;\sigma) = \frac{x}{\sigma^2} e^{-\frac{x^2}{2\sigma^2}}
$$

$$
F(x) = 1 - e^{-\frac{x^2}{2\sigma^2}}
$$

### Weibull Distribution

$$
f(x;\lambda,k) = \left\{
\begin{array}{ll}
\frac{k}{\lambda} (\frac{x}{\lambda})^{k-1} e^{-(\frac{x}{\lambda})^k} & x \geq 0 \\
0 & x < 0
\end{array}
\right.
$$

$$
F(x) = 1 - e^{-(\frac{x}{\lambda})^k}
$$
