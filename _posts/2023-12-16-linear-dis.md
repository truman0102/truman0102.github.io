---
layout: post
title: Linear Discriminant Classifier
date: 2023-12-16 00:00:00-0400
description: An introduction to the Linear Discriminant Classifier in Machine Learning.
tags: ml linear-discriminant-classifier linear-discriminant-classification
categories: data-science
related_posts: false
giscus_comments: true
thumbnail: /assets/img/data_science/LDA.png
toc:
  beginning: true
---

## Introduction

The Linear Discriminant Classifier is a supervised learning algorithm that is used to classify data into two or more classes. A discriminant function is constructed to separate the classes, including `One vs. Rest` and `One vs. One`.

Let $$x$$ be a $$D$$-dimensional vector and $$C$$ be the number of classes. The discriminant function $$f(x)$$ is defined as:

$$
f(x) = w^Tx + w_0 = \sum_{i=1}^{D}w_ix_i + w_0
$$

where $$w_0$$ is a scalar. $$x$$ can also be written as:

$$
x = \begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_D \\
1
\end{bmatrix}
$$

and $$w$$ can be written as:

$$
w = \begin{bmatrix}
w_1 \\
w_2 \\
\vdots \\
w_D \\
w_0
\end{bmatrix}
$$

So $$f(x)$$ can be written as:

$$
f(x) = w^Tx = \sum_{i=0}^{D}w_ix_i
$$

where $$x_0 = 1$$.

### One vs. Rest

$$
f_c(x) = w_c^Tx \begin{cases}
> 0 & y = c \\
\leq 0 & y \neq c
\end{cases}
$$

### One vs. One

$$
f_{c_1, c_2}(x) = w_{c_1, c_2}^Tx \begin{cases}
> 0 & y = c_1 \\
\leq 0 & y = c_2
\end{cases}
$$

If there are $$C$$ classes, then there are $$\frac{C(C-1)}{2}$$ discriminant functions. The `One vs. One` method matters in two cases:

1. For all $$k\neq c$$, $$f_{c, k}(x) > 0$$, then $$y = c$$.
2. $$f_{c,k}(x) = f_c(x) - f_k(x)$$, then $$y=\arg\max_{c}f_c(x)$$.