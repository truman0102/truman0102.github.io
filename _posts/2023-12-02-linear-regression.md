---
layout: post
title: Linear Regression
date: 2023-12-18 00:00:00-0400
description: An introduction to linear regression.
tags: ML math
categories: data-science
related_posts: false
giscus_comments: false
disqus_comments: false
thumbnail: /assets/img/ml/LR.png
toc:
  beginning: true
---

## Introduction

Linear regression is a supervised learning algorithm that is used to predict a continuous variable. It is one of the simplest machine learning algorithms and is often used as a baseline for other algorithms. It is also used to determine the relationship between two variables and how one variable affects the other. For example, it can be used to determine how the price of a house is affected by its size, number of bedrooms, etc.

Given a set of training data $$D=\{x_i,y_i\}_{i=1}^N$$, where $$x_i$$ is the input and $$y_i$$ is the target, the goal of linear regression is to find a function $$f(x)$$ that minimizes the error between the predicted value $$f(x_i)$$ and the actual value $$y_i$$. The function $$f(x)$$ is called the hypothesis function and is defined as:

$$f(x) = w_0 + w_1x_1 + w_2x_2 + ... + w_nx_n$$

where $$w_0$$ is the bias term and $$w_1, w_2, \dots, w_n$$ are the weights. The bias term is a constant that is added to the output of the linear regression model. The weights are the coefficients of the input variables. The hypothesis function can also be written in vector form as:

$$\hat{y} = f(x) = w^Tx$$

where $$w$$ is the weight vector and $$x$$ is the input vector. The weight vector is defined as:

$$w = \begin{bmatrix}w_0 \\ w_1 \\ w_2 \\ \vdots \\ w_n\end{bmatrix}$$

and the input vector is defined as:

$$x = \begin{bmatrix}1 \\ x_1 \\ x_2 \\ \vdots \\ x_n\end{bmatrix}$$

## Cost Function

The cost function is the residual sum of squares (RSS), used to measure the error between the predicted value $$f(x_i)$$ and the actual value $$y_i$$:

$$\text{RSS} = \sum_{i=1}^N (y_i - f(x_i))^2 = \sum_{i=1}^N r_i^2$$

where $$r_i$$ is the residual. Minimizing the RSS is equivalent to the MLE of white Gaussian noise. The proof is shown below:

Let $$\epsilon_i = y_i - f(x_i)$$ be the error term. The probability density function of white Gaussian noise is:

$$p(\epsilon_i) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{\epsilon_i^2}{2\sigma^2}}$$

In other words,

$$p(y_i|x_i) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y_i - f(x_i))^2}{2\sigma^2}}$$

where $$f(x_i)$$ is a constant, $$y_i$$ is a random variable, whose distribution is given by the above equation. The likelihood function is:

$$L = \prod_{i=1}^N p(y_i|x_i) = \prod_{i=1}^N \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y_i - f(x_i))^2}{2\sigma^2}}$$

Taking the log of the likelihood function:

$$\ln L = \sum_{i=1}^N \ln \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y_i - f(x_i))^2}{2\sigma^2}} = -\frac{N}{2}\ln 2\pi\sigma^2 - \frac{1}{2\sigma^2}\sum_{i=1}^N (y_i - f(x_i))^2$$

To maximize the likelihood function, we need to minimize the negative log likelihood function, equivalent to minimizing $$\frac{1}{2\sigma^2}\sum_{i=1}^N (y_i - f(x_i))^2$$, which is a constant times the RSS.

The distribution of the residuals is also used to determine whether the linear regression model is a good fit for the data. If the residuals are normally distributed with a mean of 0, then the linear regression model is a good fit for the data.

Other cost functions can also be used, such as the mean absolute error (MAE, L1 loss):

$$\text{MAE} = \sum_{i=1}^N |y_i - f(x_i)|$$

and the Huber loss:

$$\text{Huber} = \sum_{i=1}^N \begin{cases} \frac{1}{2}(y_i - f(x_i))^2 & \text{if } |y_i - f(x_i)| \leq \delta \\ \delta|y_i - f(x_i)| - \frac{1}{2}\delta^2 & \text{otherwise} \end{cases}$$

where $$\delta$$ is a hyperparameter that determines the threshold for the Huber loss. The Huber loss is a combination of the MAE and the RSS. When the residual is small, the Huber loss is equivalent to the RSS. When the residual is large, the Huber loss is equivalent to the MAE.

The residual of MAE obeys the laplace distribution,

$$p(\epsilon_i) = \frac{1}{2b}e^{-\frac{|\epsilon_i|}{b}}$$

where $$b$$ is the scale parameter. And the likelihood function is:

$$L = \prod_{i=1}^N p(y_i|x_i) = \prod_{i=1}^N \frac{1}{2b}e^{-\frac{|y_i - f(x_i)|}{b}}$$

Taking the log of the likelihood function:

$$\ln L = \sum_{i=1}^N \ln \frac{1}{2b}e^{-\frac{|y_i - f(x_i)|}{b}} = -N\ln 2b - \frac{1}{b}\sum_{i=1}^N |y_i - f(x_i)|$$

To maximize the likelihood function, we need to minimize the negative log likelihood function, equivalent to minimizing $$\frac{1}{b}\sum_{i=1}^N \vert y_i - f(x_i)\vert$$, which is a constant times the MAE, similar to the RSS.

## Regularization

Regularization is used to prevent overfitting. It is a technique that adds a penalty term to the cost function. The penalty term is a function of the weights and is used to penalize large weights. The cost function with regularization is:

$$J = RSS + \lambda R(w) = \sum_{i=1}^N (y_i - f(x_i))^2 + \lambda R(w)$$

where $$\lambda$$ is the regularization parameter and $$R(w)$$ is the regularization term. The regularization term can be L1 regularization:

$$R(w) = \sum_{i=1}^N |w_i|$$

or L2 regularization:

$$R(w) = \sum_{i=1}^N w_i^2$$

L1 regularization is also known as Lasso regression and L2 regularization is also known as Ridge regression. It the training data and the weights are represented as matrices, $$X_{N \times D}$$, $$Y_{N \times 1}$$, and $$W_{D \times 1}$$, then the cost function of L1 regularization is:

$$J = RSS + \lambda R(w) = (Y - XW)^T(Y - XW) + \lambda |W|$$

and the cost function of L2 regularization is:

$$
\begin{aligned}
J &= RSS + \lambda R(w) \\
&= (Y - XW)^T(Y - XW) + \lambda W^TW \\
&= (Y^T - W^TX^T)(Y - XW) + \lambda W^TW \\
\end{aligned}
$$

The bayesian interpretation of L2 regularization is that it is equivalent to a Gaussian prior on the weights. The proof is shown below:

The likelihood function is:

$$L = \prod_{i=1}^N p(y_i|x_i) = \prod_{i=1}^N \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y_i - f(x_i))^2}{2\sigma^2}}$$

Taking the log of the likelihood function:

$$\ln L = \sum_{i=1}^N \ln \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y_i - f(x_i))^2}{2\sigma^2}} = -\frac{N}{2}\ln 2\pi\sigma^2 - \frac{1}{2\sigma^2}\sum_{i=1}^N (y_i - f(x_i))^2$$

The prior distribution of the weights is:

$$
\begin{aligned}
p(w_i) &= \frac{1}{\sqrt{2\pi\tau^2}}e^{-\frac{w_i^2}{2\tau^2}} \\
p(W) &= \prod_{i=1}^N \frac{1}{\sqrt{2\pi\tau^2}}e^{-\frac{w_i^2}{2\tau^2}} \\
\ln p(W) &= \sum_{i=1}^N \ln \frac{1}{\sqrt{2\pi\tau^2}}e^{-\frac{w_i^2}{2\tau^2}} = -\frac{N}{2}\ln 2\pi\tau^2 - \frac{1}{2\tau^2}\sum_{i=1}^N w_i^2 \\
\end{aligned}
$$

The posterior distribution of the weights $$\ln p(W\vert X,Y)\propto \ln p(Y\vert X,W) + \ln p(W)$$:

$$
\begin{aligned}
\ln p(W|X,Y) &\propto \ln p(Y|X,W) + \ln p(W) \\
&= \ln L + \ln p(W) \\
&= -\frac{N}{2}\ln 2\pi\sigma^2 - \frac{1}{2\sigma^2}\sum_{i=1}^N (y_i - f(x_i))^2 -\frac{N}{2}\ln 2\pi\tau^2 - \frac{1}{2\tau^2}\sum_{i=1}^N w_i^2 \\
\end{aligned}
$$

To maximize the posterior distribution, we need to minimize the negative log posterior distribution, equivalent to minimizing $$\frac{1}{2\sigma^2}\sum_{i=1}^N (y_i - f(x_i))^2 + \frac{1}{2\tau^2}\sum_{i=1}^N w_i^2$$, which is a constant times the RSS plus the L2 regularization term. The proof of L1 regularization and laplace prior is similar, and is omitted here.

## Optimization

### Analytical Solution

Omitting regularization, the cost function, named the RSS, is:

$$J = (Y - XW)^T(Y - XW)$$

To minimize the cost function, we take the derivative of the cost function with respect to the weights $$W$$ and set it to 0:

$$
\begin{aligned}
\frac{\partial J}{\partial W} &= \frac{\partial}{\partial W} (Y - XW)^T(Y - XW) \\
&= \frac{\partial}{\partial W} (Y^T - W^TX^T)(Y - XW) \\
&= \frac{\partial}{\partial W} (Y^TY - Y^TXW - W^TX^TY + W^TX^TXW) \\
&= -2X^TY + 2X^TXW = 0 \\
X^TXW &= X^TY \\
W &= (X^TX)^{-1}X^TY \\
\end{aligned}
$$

To get the inverse of $$X^TX$$, SVD is used:

$$X = U\Sigma V^T$$

where $$U$$ is an $$N \times N$$ orthogonal matrix, $$\Sigma$$ is an $$N \times D$$ diagonal matrix, and $$V$$ is a $$D \times D$$ orthogonal matrix. The inverse of $$X^TX$$ is:

$$
\begin{aligned}
X^TX &= (U\Sigma V^T)^T(U\Sigma V^T) \\
&= V\Sigma^T U^TU\Sigma V^T \\
&= V\Sigma^T\Sigma V^T \\
&= V\Sigma^2 V^T \\
V^{-1} &= V^T \\
(X^TX)^{-1} &= (V\Sigma^2 V^T)^{-1} \\
&= V\Sigma^{-2} V^T \\
\end{aligned}
$$

The entries of $$\Sigma^{-2}$$ are the reciprocals of the diagonal entries of $$\Sigma^2$$, and are the reciprocals of the eigenvalues of $$X^TX$$.

### Gradient Descent

Gradient descent is an iterative optimization algorithm that is used to find the minimum of a function. It is used to find the weights that minimize the cost function. The weights are initialized and are updated iteratively:

$$W_{t+1} = W_t - \alpha \frac{\partial J}{\partial W}$$

where $$\alpha$$ is the learning rate. The learning rate determines the step size of the gradient descent algorithm. If the learning rate is too small, the algorithm will take a long time to converge. If the learning rate is too large, the algorithm will not converge. The gradient descent algorithm is:

1. Initialize the weights $$W$$.
2. Calculate the gradient $$\frac{\partial J}{\partial W}$$.
3. Update the weights $$W$$.
4. Repeat steps 2 and 3 until convergence.
5. Return the weights $$W$$.

From the [analytical solution](#analytical-solution), the gradient of the cost function is:

$$\frac{\partial J}{\partial W} = -2X^TY + 2X^TXW$$

If L2 regularization is used, the gradient of the cost function is:

$$\frac{\partial J}{\partial W} = -2X^TY + 2X^TXW + 2\lambda W$$