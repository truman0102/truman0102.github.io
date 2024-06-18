---
layout: post
title: Covariance
date: 2023-09-20 00:00:00-0400
description: An introduction to covariance.
tags: math
categories:
related_posts: false
giscus_comments: false
disqus_comments: false
thumbnail:
toc:
  beginning: true
---

## What is Covariance?

Covariance is a measure of how two variables change together. It is a measure of the linear relationship between two variables. It is given by:

$$
\text{Cov}(X,Y) = \frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{x})(y_i - \bar{y}) = E[(X-E(X))(Y-E(Y))]
$$

where $$\bar{x}$$ and $$\bar{y}$$ are the means of $$X$$ and $$Y$$ respectively. The covariance is positive if $$X$$ and $$Y$$ are positively correlated, negative if $$X$$ and $$Y$$ are negatively correlated, and zero if $$X$$ and $$Y$$ are uncorrelated.

For sample covariance, the denominator is $$N-1$$ instead of $$N$$. This is because the sample mean is used instead of the population mean, and the sample mean is calculated using $$N-1$$ instead of $$N$$.

$$
\text{Cov}(X,Y) = \frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})(y_i - \bar{y})
$$

The covariance between a variable and itself is the variance of that variable.

$$
\text{Cov}(X,X) = \frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{x})^2 = \sigma_X^2 = E[(X-E(X))^2] = E(X^2) - E^2(X) = \text{Var}(X)
$$

## Correlation

Correlation is a measure of the strength of the linear relationship between two variables. It is given by:

$$
\text{Corr}(X,Y) = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{\text{Cov}(X,Y)}{\sqrt{\text{Cov}(X,X)} \sqrt{\text{Cov}(Y,Y)}}
$$

where $$\sigma_X$$ and $$\sigma_Y$$ are the standard deviations of $$X$$ and $$Y$$ respectively. The correlation is positive if $$X$$ and $$Y$$ are positively correlated, negative if $$X$$ and $$Y$$ are negatively correlated, and zero if $$X$$ and $$Y$$ are uncorrelated.

## Covariance Matrix

Sometimes the variables $$X$$ is not a single value but a vector of values $$X = (X_1, X_2, \dots, X_n)$$. In this case, the covariance matrix is used to describe the covariance between the different dimensions of $$X$$. The covariance matrix is given by:

$$
\text{Cov}(X) = \begin{bmatrix}
\text{Cov}(X_1, X_1) & \text{Cov}(X_1, X_2) & \dots & \text{Cov}(X_1, X_n) \\
\text{Cov}(X_2, X_1) & \text{Cov}(X_2, X_2) & \dots & \text{Cov}(X_2, X_n) \\
\vdots & \vdots & \ddots & \vdots \\
\text{Cov}(X_n, X_1) & \text{Cov}(X_n, X_2) & \dots & \text{Cov}(X_n, X_n)
\end{bmatrix}
$$

The covariance matrix is symmetric, and the diagonal elements are the variances of the corresponding dimensions of $$X$$. Let $$\mu$$ be the mean vector of $$X$$, then the covariance matrix can be written as:

$$
\text{Cov}(X) = \frac{1}{N} \sum_{i=1}^{N} (X_i - \mu)(X_i - \mu)^T
$$


## Properties of Covariance

### Linearity

$$
\begin{aligned}
\text{Cov}(X+Y,Z) &= \frac{1}{N} \sum_{i=1}^{N} [(x_i + y_i) - (\bar{x} + \bar{y})] (z_i - \bar{z}) \\
&= \frac{1}{N} \sum_{i=1}^{N} [(x_i - \bar{x}) + (y_i - \bar{y})] (z_i - \bar{z}) \\
&= \frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{x})(z_i - \bar{z}) + \frac{1}{N} \sum_{i=1}^{N} (y_i - \bar{y})(z_i - \bar{z}) \\
&= \text{Cov}(X,Z) + \text{Cov}(Y,Z)
\end{aligned}
$$

$$
\begin{aligned}
\text{Cov}(aX,Y) &= \frac{1}{N} \sum_{i=1}^{N} [a(x_i - \bar{x})] (y_i - \bar{y}) \\
&= a \frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{x})(y_i - \bar{y}) \\
&= a \text{Cov}(X,Y)
\end{aligned}
$$

### semi-definite positive

The covariance matrix $$\Sigma$$ is semi-definite positive. This means that for any vector $$v$$, the following inequality holds:

$$
v^T \Sigma v \geq 0
$$

This can be shown as follows:

$$
\begin{aligned}
v^T \Sigma v &= v^T \mathbb{E}[(X-\mu)(X-\mu)^T] v \\
&= \mathbb{E}[v^T(X-\mu)(X-\mu)^T v] \\
&= \mathbb{E}[((X-\mu)^T v)^T ((X-\mu)^T v)] \\
&= \mathbb{E}[\vert\vert (X-\mu)^T v \vert\vert^2] \geq 0
\end{aligned}
$$

### diagonality

Since the covariance matrix is symmetric, it can be diagonalized. This means that there exists a matrix $$P$$ such that:

$$
P^T \Sigma P = D
$$

where $$D$$ is a diagonal matrix. The diagonal elements of $$D$$ are the eigenvalues of $$\Sigma$$, and the columns of $$P$$ are the corresponding eigenvectors.