---
layout: post
title: Linear Regression
date: 2023-12-18 00:00:00-0400
description: An introduction to linear regression.
tags: ML math linear-regression
categories: data-science
related_posts: false
giscus_comments: true
disqus_comments: true
thumbnail: /assets/img/data_science/LR.png
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

$$RSS = \sum_{i=1}^N (y_i - f(x_i))^2 = \sum_{i=1}^N r_i^2$$

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

To maximize the likelihood function, we need to minimize the negative log likelihood function, equivalent to minimizing $$\frac{1}{b}\sum_{i=1}^N |y_i - f(x_i)|$$, which is a constant times the MAE.