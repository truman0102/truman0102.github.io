---
layout: post
title: Linear Discriminant Classifier
date: 2023-12-16 00:00:00-0400
description: An introduction to the Linear Discriminant Classifier in Machine Learning.
tags: ML
categories: data-science
related_posts: false
giscus_comments: false
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
1 \\
x_1 \\
x_2 \\
\vdots \\
x_D
\end{bmatrix}
$$

and $$w$$ can be written as:

$$
w = \begin{bmatrix}
w_0 \\
w_1 \\
w_2 \\
\vdots \\
w_D
\end{bmatrix}
$$

So $$f(x)$$ can be written as:

$$
f(x) = w^Tx = \sum_{i=0}^{D}w_ix_i
$$

where $$x_0 = 1$$.

### One vs. Rest

There are $$C$$ discriminant functions for `One vs. Rest` method. A sample $$x$$ is classified as $$y = c$$ if $$f_c(x) > 0$$ and $$f_k(x) \leq 0$$ for all $$k \neq c$$.

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

If there are $$C$$ classes, the `One vs. One` method matters in two cases:

1. For all $$k\neq c$$, $$f_{c, k}(x) > 0$$, then $$y = c$$. There are $$\frac{C(C-1)}{2}$$ discriminant functions, as $$f_{c,k}(x) = - f_{k,c}(x)$$.
2. In this case, there are $$C$$ discriminant functions $$f_i(x)$$ for $$i=1,2,\dots,C$$. $$f_{c,k}(x) = f_c(x) - f_k(x)$$, then $$y=\arg\max_{c}f_c(x)$$. 

## Linear Discriminant Classifier

Let the data matrix $$X$$ be $$D \times N$$, where $$D$$ is the number of features and $$N$$ is the number of samples. The weight vector $$w$$ is $$D \times 1$$ and the bias $$w_0$$ is a scalar. The transformed data matrix $$Z_{1 \times N}$$ is defined as:

$$
Z = w^TX
$$
<!-- 
Similarly, $$X$$ can also be written as a $$(D+1) \times N$$ matrix, where the first row is all $$1$$s. $$w$$ is a $$(D+1) \times 1$$ vector. The transformed data matrix $$Z_{1 \times N}=w^TX$$. -->

### Fisher's Linear Discriminant

Consider a binary classification problem with two classes $$c_1$$ and $$c_2$$. The mean vectors of the two classes are $$\mu_1$$ and $$\mu_2$$, respectively. The within-class scatter matrix $$S_c$$ is defined as:

$$
S_c = \sum_{n \in c}(x_n - \mu_c)(x_n - \mu_c)^T
$$

The sum of the within-class scatter matrices $$S_W$$ is defined as:

$$
S_W = S_{c_1} + S_{c_2}
$$

And the between-class scatter matrix $$S_B$$ is defined as:

$$
S_B = (\mu_1 - \mu_2)(\mu_1 - \mu_2)^T
$$

Once the data is projected onto the line $$w$$, the within-class scatter matrix $$S_W$$ and the between-class scatter matrix $$S_B$$ can be written as:

$$
\begin{aligned}
\tilde{S}_c &= \sum_{n \in c}(w^Tx_n - w^T\mu_c)(w^Tx_n - w^T\mu_c)^T = w^TS_cw\\
\tilde{S}_W &= \tilde{S}_{c_1} + \tilde{S}_{c_2} = w^TS_Ww\\
\tilde{S}_B &= (w^T\mu_1 - w^T\mu_2)(w^T\mu_1 - w^T\mu_2)^T = w^TS_Bw
\end{aligned}
$$

The fisher's linear discriminant tries to maximize the ratio of the between-class scatter matrix and the within-class scatter matrix:

$$
\max_w \frac{\tilde{S}_B}{\tilde{S}_W} = \max_w \frac{w^TS_Bw}{w^TS_Ww}
$$

which can be regarded as a rayleigh quotient. The solution is the eigenvector of $$S_W^{-1}S_B$$ with the largest eigenvalue, satisfying the constraint $$S_Bw = \lambda S_Ww$$.

$$
\begin{aligned}
S_Bw &= \lambda S_Ww\\
S_W^{-1}S_Bw &= \lambda w \\
S_W^{-1}(\mu_1 - \mu_2)\underbrace{(\mu_1 - \mu_2)^Tw}_{1\times 1} &= \lambda w \\
w &\propto S_W^{-1}(\mu_1 - \mu_2)
\end{aligned}
$$

So all you need to do is to find the mean vectors of the two classes and the inverse of the within-class scatter matrix. We can also use SVD to find the inverse of the within-class scatter matrix:

$$
\begin{aligned}
S_W &= U\Sigma V^T \\
S_W^{-1} &= V\Sigma^{-1}U^T
\end{aligned}
$$

The decision boundary is defined as:

$$
w^Tx = \frac{1}{2}(\tilde{\mu}_1 + \tilde{\mu}_2) = \frac{1}{2}w^T(\mu_1 + \mu_2)
$$

where $$\tilde{\mu}_c = w^T\mu_c$$. Replace $$w$$ with $$S_W^{-1}(\mu_1 - \mu_2)$$, we get:

$$
\begin{aligned}
w^T &= (S_W^{-1}(\mu_1 - \mu_2))^T \\
&= (\mu_1 - \mu_2)^TS_W^{-1} \\
w^Tx &= \frac{1}{2}w^T(\mu_1 + \mu_2) \\
(\mu_1 - \mu_2)^TS_W^{-1}x &= \frac{1}{2}(\mu_1 - \mu_2)^TS_W^{-1}(\mu_1 + \mu_2) \\
0 &= (\mu_1 - \mu_2)^TS_W^{-1}x - \frac{1}{2}\mu_1^TS_W^{-1}\mu_1 + \frac{1}{2}\mu_2^TS_W^{-1}\mu_2 \\
\end{aligned}
$$

equivalent to [gasussian discriminant analysis](/blog/2023/gen-classifier/#gaussian-discriminant-analysis).

### Perceptron

Perceptron is a linear classifier that uses the sign of the discriminant function as the prediction. The prediction $$\hat{y}$$ is defined as:

$$
\hat{y} = \begin{cases}
1 & f(x) > 0 \\
-1 & f(x) \leq 0
\end{cases}
$$

where the class labels are $$y \in \{-1, 1\}$$. The absolute value of the discriminant function $$\vert w^Tx+w_0\vert$$ can be written as $$y(w^Tx+w_0)$$, and the loss function is defined as:

$$
L(w, w_0) = -\sum_{n=1}^{N}y_n(w^Tx_n+w_0)
$$

The gradient of the loss function is:

$$
\begin{aligned}
\nabla_wL(w, w_0) &= -\sum_{n=1}^{N}y_nx_n \\
\nabla_{w_0}L(w, w_0) &= -\sum_{n=1}^{N}y_n
\end{aligned}
$$

The weights are updated when the prediction is wrong (i.e. $$y_n(w^Tx_n+w_0) \leq 0$$):

$$
\begin{aligned}
w &\leftarrow w + \eta y_nx_n \\
w_0 &\leftarrow w_0 + \eta y_n
\end{aligned}
$$

where $$\eta$$ is the learning rate.

### Minimum Squared Error

### [Support Vector Machine](/blog/2023/SVM/)

### [Logistic Regression](/blog/2023/logistic-regression/)

## Generalized Linear Discriminant Classifier

### Polynomial Discriminant

Usually, a single point $$x$$ is represented as a vector $$x = [x_1, x_2, \dots, x_D]$$, where $$D$$ is the number of features. The polynomial discriminant combines the features into a $$r$$-degree polynomial:

$$
\begin{aligned}
f_1(x) &= w_0 + w_1x_1 + w_2x_2 + \dots + w_Dx_D \\
f_2(x) &= \sum_{i=1}^{D}\sum_{j=1}^{D}w_{ij}x_ix_j + f_1(x) \\
f_r(x) &= \sum_{i_1=1}^{D}\sum_{i_2=1}^{D}\dots\sum_{i_r=1}^{D}w_{i_1i_2\dots i_r}x_{i_1}x_{i_2}\dots x_{i_r} + f_{r-1}(x)
\end{aligned}
$$

The number of total terms is $$\frac{(D+r)!}{D!r!}$$:

## Segemented Linear Discriminant Classifier

### [Decision Tree](/blog/2023/decision-tree/)