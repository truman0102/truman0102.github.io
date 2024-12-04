---
layout: post
title: Parameter Estimation
date: 2023-12-01 00:00:00-0400
description: An introduction to parameter estimation in data science.
tags: math
categories: statistics
related_posts: false
giscus_comments: false
toc:
  beginning: true
---

## Parameters

Given a model, parameters are the numbers that yield the actual distribution. For example, in a normal distribution, the mean and standard deviation are the parameters. In a binomial distribution, the number of trials and the probability of success are the parameters, and so on.

Parameter of common distributions are detailed in [Probability Distribution](/blog/2023/probability-distribution/).

Let $$X$$ be a random variable with a probability distribution $$f(x;\theta)$$, where $$\theta$$ is the parameter. The goal of parameter estimation is to find the value of $$\theta$$ that best describes the distribution of $$X$$ based on samples $$x_1, x_2, \dots, x_n$$.

## Maximum Likelihood Estimation (MLE)

### Likelihood Function

The likelihood function is the probability of observing the samples $$x_1, x_2, \dots, x_n$$ given the parameter $$\theta$$. Assuming that the samples are independent and identically distributed (iid), the likelihood function is the product of the probability of each sample.

$$
\begin{aligned}
L(\theta) &= P(x_1, x_2, \dots, x_n | \theta) \\
&= \prod_{i=1}^n P(x_i | \theta) \\
&= \prod_{i=1}^n f(x_i; \theta)\\
LL(\theta) &= \log L(\theta) \\
&= \sum_{i=1}^n \log f(x_i; \theta)
\end{aligned}
$$

### Maximization

In MLE, the parameter $$\theta$$ is estimated by maximizing the likelihood function $$L(\theta)$$.

$$
\hat{\theta} = \underset{\theta}{\operatorname{argmax}} L(\theta)
$$

Since the likelihood function is a product of probabilities, it is often more convenient to maximize the log-likelihood function instead.

$$
\begin{aligned}
\hat{\theta} &= \underset{\theta}{\operatorname{argmax}} \log L(\theta) \\
&= \underset{\theta}{\operatorname{argmax}} \sum_{i=1}^n \log f(x_i; \theta)
\end{aligned}
$$

Usually, differentiation is set to zero to find the maximum.

$$
\begin{aligned}
\frac{\partial}{\partial \theta} \log L(\theta) &= 0 \\
\frac{\partial}{\partial \theta} \sum_{i=1}^n \log f(x_i; \theta) &= 0 \\
\sum_{i=1}^n \frac{\partial}{\partial \theta} \log f(x_i; \theta) &= 0 \\
\sum_{i=1}^n \frac{1}{f(x_i; \theta)} \frac{\partial}{\partial \theta} f(x_i; \theta) &= 0 \\
\end{aligned}
$$

## MLE for different ML models

### Linear Regression

$$
f(x_i; \omega) = \omega_0 + \sum_{j=1}^d \omega_j x_{ij} 
$$

$$
y_i = f(x_i; \omega) + \epsilon_i\sim N(f(x_i; \omega), \sigma^2)
$$

$$
\begin{aligned}
\mathcal{L}(\omega) &= \prod_{i=1}^n p(y_i | x_i; \omega) \\
&= \prod_{i=1}^n \frac{1}{\sqrt{2\pi\sigma^2}} \exp(-\frac{(y_i - f(x_i; \omega))^2}{2\sigma^2}) \\
\log \mathcal{L}(\omega) &= \sum_{i=1}^n \log \frac{1}{\sqrt{2\pi\sigma^2}} \exp(-\frac{(y_i - f(x_i; \omega))^2}{2\sigma^2}) \\
&= \sum_{i=1}^n [-\frac{1}{2}\log 2\pi\sigma^2 - \frac{(y_i - f(x_i; \omega))^2}{2\sigma^2}] \\
&= -\frac{n}{2}\log 2\pi\sigma^2 - \frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - f(x_i; \omega))^2 \\
\end{aligned}
$$

### Logistic Regression

$$
f(x_i; \omega,b) = \frac{\exp(\omega^T x_i+b)}{1 + \exp(\omega^T x_i+b)} = p(y_i=1|x_i; \omega, b)
$$

$$
\begin{aligned}
\mathcal{L}(\omega, b) &= \prod_{i=1}^n p(y_i | x_i; \omega, b)\\
&= \prod_{i=1}^n p(y_i=1 | x_i; \omega, b)^{y_i} p(y_i=0 | x_i; \omega, b)^{1-y_i} \\
\log\mathcal{L}(\omega, b) &= \sum_{i=1}^n [y_i \log p(y_i=1 | x_i; \omega, b) + (1-y_i) \log p(y_i=0 | x_i; \omega, b)] \\
&= \sum_{i=1}^n [y_i \log\frac{\exp(\omega^T x_i+b)}{1 + \exp(\omega^T x_i+b)} + (1-y_i) \log\frac{1}{1 + \exp(\omega^T x_i+b)}] \\
&= \sum_{i=1}^n [y_i (\omega^T x_i+b) - \log(1 + \exp(\omega^T x_i+b))]
\end{aligned}
$$

### Naive Bayes

$$
p(y_i=k | x_i; \theta) = \frac{p(x_i | y_i=k; \theta) p(y_i=k; \theta)}{p(x_i; \theta)} \propto \underbrace{p(x_i | y_i=k; \theta)}_{\text{likelihood}} \underbrace{p(y_i=k; \theta)}_{\text{prior}}
$$

## Maximum A Posteriori Estimation (MAP)

$$
P(\theta | x_1, x_2, \dots, x_n) = \frac{P(x_1, x_2, \dots, x_n | \theta) P(\theta)}{P(x_1, x_2, \dots, x_n)} \propto P(x_1, x_2, \dots, x_n | \theta) P(\theta)=L(\theta)P(\theta)
$$

Similar to MLE, log function is used to simplify the calculation.

$$
\log P(\theta | x_1, x_2, \dots, x_n) \propto \log L(\theta) + \log P(\theta) = \sum_{i=1}^n \log f(x_i; \theta) + \log P(\theta)
$$

In terms of form, MAP is similar to MLE. The difference is that MAP incorporates prior knowledge of the parameter $$\theta$$ in the form of $$P(\theta)$$.

We also need to find the maximum of the posterior distribution.

$$
\begin{aligned}
\hat{\theta} &= \underset{\theta}{\operatorname{argmax}} P(\theta | x_1, x_2, \dots, x_n) \\
&= \underset{\theta}{\operatorname{argmax}} \log P(\theta | x_1, x_2, \dots, x_n) \\
&= \underset{\theta}{\operatorname{argmax}} [\sum_{i=1}^n \log f(x_i; \theta) + \log P(\theta)]
\end{aligned}
$$

Differentiate the above equation with respect to $$\theta$$ and set it to zero.

$$
\begin{aligned}
\frac{\partial}{\partial \theta} \log P(\theta | x_1, x_2, \dots, x_n) &= 0 \\
\frac{\partial}{\partial \theta} [\sum_{i=1}^n \log f(x_i; \theta) + \log P(\theta)] &= 0 \\
\sum_{i=1}^n \frac{\partial}{\partial \theta} \log f(x_i; \theta) + \frac{\partial}{\partial \theta} \log P(\theta) &= 0 \\
\sum_{i=1}^n \frac{1}{f(x_i; \theta)} \frac{\partial}{\partial \theta} f(x_i; \theta) + \frac{\partial}{\partial \theta} \log P(\theta) &= 0 \\
\end{aligned}
$$

Using Bayesian terminology, MAP estimation is equivalent to MLE estimation with a prior distribution.

## Minimum Mean Square Error (MMSE)

## Least Squares Estimation (LSE)

## Bayes Estimation

In Bayesian estimation, the parameter $$\theta$$ is treated as a random variable with a prior distribution $$P(\theta)$$. The MMSE, LAE and MAP estimators are all special cases of Bayes estimation.

Define the cost function $$C(\theta, \hat{\theta})$$, which measures the cost of estimating $$\theta$$ as $$\hat{\theta}$$. The goal of Bayes estimation is to minimize the expected cost.

$$
\hat{\theta} = \underset{\theta}{\operatorname{argmin}} E[C(\theta, \hat{\theta})] = \underset{\theta}{\operatorname{argmin}} \int C(\theta, \hat{\theta}) P(\theta | x_1, x_2, \dots, x_n) d\theta
$$

After defining the cost function and simplifying the integrand, differentiate the expression, and set it to zero to find the estimator.

### Quadratic Cost Function

$$
C(\theta, \hat{\theta}) = (\theta - \hat{\theta})^2
$$

$$
J(\theta) = \int (\theta - \hat{\theta})^2 P(\theta | x) d\theta = \int (\theta^2 - 2\theta\hat{\theta} + \hat{\theta}^2) P(\theta | x) d\theta
$$

$$
\begin{aligned}
\frac{\partial}{\partial \hat{\theta}} J(\theta) &= 0 \\
\frac{\partial}{\partial \hat{\theta}} \int (\theta^2 - 2\theta\hat{\theta} + \hat{\theta}^2) P(\theta | x) d\theta &= 0 \\
\int \frac{\partial}{\partial \hat{\theta}} (\theta^2 - 2\theta\hat{\theta} + \hat{\theta}^2) P(\theta | x) d\theta &= 0 \\
\int (-2\theta + 2\hat{\theta}) P(\theta | x) d\theta &= 0 \\
-2\int \theta P(\theta | x) d\theta + 2\hat{\theta} \int P(\theta | x) d\theta &= 0 \\
-2E[\theta|x] + 2\hat{\theta} &= 0 \\
\hat{\theta} &= E[\theta|x]
\end{aligned}
$$

### Absolute Cost Function

### Zero-One Cost Function