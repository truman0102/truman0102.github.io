---
layout: post
title: Generative Classifier
date: 2023-12-16 12:00:00-0400
description: An introduction to generative classifiers and their use in machine learning.
tags: ML bayes
categories: data-science
related_posts: false
toc:
  beginning: true
---

## Introduction

Given a set of data points $$X$$ and their corresponding labels $$Y$$, a generative classifier attempts to model the distribution $$P(X,Y)$$ and then uses Bayes' rule or the chain rule to calculate $$P(Y\vert X)$$.

$$
X_{D \times N} = \begin{bmatrix}
x_{1,1} & x_{1,2} & \dots & x_{1,N} \\
x_{2,1} & x_{2,2} & \dots & x_{2,N} \\
\vdots & \vdots & \ddots & \vdots \\
x_{D,1} & x_{D,2} & \dots & x_{D,N}
\end{bmatrix} = \begin{bmatrix}
x_1 & x_2 & \dots & x_N
\end{bmatrix}
$$

where $$D$$ is the number of features and $$N$$ is the number of data points. The label of each data point $$y_i$$ is a discrete random variable that can take on one of $$K$$ values.

$$
y_i \in \{1, 2, \dots, K\}
$$

Sometimes, $$y_i$$ is a binary random variable belonging to one of two classes, $$y_i \in \{0, 1\}$$. We can see that the form of the label is not important, as long as it is discrete. It is the goal of the generative classifier to predict the label of a new data point $$x_{new}$$ given the training data $$X$$ and $$Y$$. The generative classifier does this by maximizing the posterior probability (equivalent to minimizing the wrong classification rate) $$P(Y\vert X)$$ or minimizing the expected risk $$R$$.

### Maximizing the Posterior Probability

Given a new data point $$x$$, the wrong classification rate when predicting $$x$$ as $$c$$ is

$$
P(y \neq c | x) = 1 - P(y = c | x)
$$

Using Bayes' rule, we can rewrite this as

$$
P(y \neq c | x) = 1 - \frac{P(x | y = c) P(y = c)}{P(x)}
$$

To minimize the wrong classification rate, we want to maximize the posterior probability $$P(y = c \vert x)$$. Since $$P(x)$$ is constant, and $$P(y = c)$$ is the prior probability of $$y = c$$, we just need to maximize $$P(x \vert y = c)$$, the posterior probability of $$x$$ given $$y = c$$. And the prediction $$\hat{y}$$ is

$$
\hat{y} = \arg\min_c P(y \neq c | x) = \arg\max_c P(x | y = c) P(y = c)
$$

### Minimizing the Expected Risk

The cost of different types of misclassifications can be different. For example, the cost of misclassifying a tumor as benign is much higher than the cost of misclassifying a benign tumor as malignant. In this case, we should define a loss function $$L(y, \hat{y})$$ that captures the cost of misclassifying $$y$$ as $$\hat{y}$$. The expected risk is then

$$
R(\hat{y}|x) = \sum_{y=1}^K L(y, \hat{y}) P(y|x)
$$

where $$P(y\vert x)$$ is the posterior probability of $$y$$ given $$x$$. The prediction $$\hat{y}$$ is

$$
\hat{y} = \arg\min_c R(c|x) = \arg\min_c \sum_{y=1}^K L(y, c) P(y|x)
$$

Actually, the expected risk is the weighted sum of the wrong classification rate, where the weights are the costs of misclassifications, since $$L(y,y) = 0$$. A simple example of a loss function is the 0-1 loss function, where

$$
L(y, \hat{y}) = \begin{cases}
0 & \text{if } y = \hat{y} \\
1 & \text{if } y \neq \hat{y}
\end{cases}
$$

In this case, the expected risk happens to be the wrong classification rate.

$$
R(\hat{y}|x) = \sum_{y=1}^K L(y, \hat{y}) P(y|x) = P(y \neq \hat{y} | x)
$$

The short form of the loss function is $$L_{\hat{y}, y}$$, where $$\hat{y}$$ is the predicted label and $$y$$ is the true label.

## [Parameter Estimation](/blog/2023/parameter-estimation)

In the following we give common distributions and their corresponding parameter estimates.

### [Bernoulli Distribution](/blog/2023/probability-distributions#bernoulli-distribution)

$$
f(x;p) = \left\{
\begin{array}{ll}
p & x = 1 \\
1-p & x = 0
\end{array}
\right.
$$

MLE of $$p$$:

$$
\hat{p} = \frac{N_1}{N}
$$

MAP of $$p$$:

$$
\hat{p} = \frac{N_1 + \alpha - 1}{N + \alpha + \beta - 2}
$$

The laplace smoothing is 

$$
\hat{p} = \frac{N_1 + 1}{N + 2}
$$

### [Multinoulli Distribution](/blog/2023/probability-distributions#multinoulli-distribution)

$$
f(x;p) = \left\{
\begin{array}{ll}
p_1 & x = 1 \\
p_2 & x = 2 \\
\vdots & \vdots \\
p_K & x = K
\end{array}
\right.
$$

MLE of $$p$$:

$$
\hat{p}_k = \frac{N_k}{N}
$$

MAP of $$p$$:

$$
\hat{p}_k = \frac{N_k + \alpha_k - 1}{N + \sum_{k=1}^K \alpha_k - K}
$$

When $$\alpha_k = 1$$, the MAP estimate is the same as the MLE estimate. The laplace smoothing is

$$
\hat{p}_k = \frac{N_k + 1}{N + K}
$$

### [Gaussian Distribution](/blog/2023/probability-distributions#gaussian-distribution)

$$
f(x;\mu,\sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

MLE of $$\mu$$:

$$
\hat{\mu} = \frac{1}{N} \sum_{i=1}^N x_i
$$

MLE of $$\sigma^2$$:

$$
\hat{\sigma}^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \hat{\mu})^2
$$

### [Multivariate Gaussian Distribution](/blog/2023/probability-distributions#multivariate-gaussian-distribution)

$$
f(x;\mu,\Sigma) = \frac{1}{\sqrt{(2\pi)^D|\Sigma|}} e^{-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)}
$$

MLE of $$\mu$$:

$$
\hat{\mu} = \frac{1}{N} \sum_{i=1}^N x_i
$$

MLE of $$\Sigma$$:

$$
\hat{\Sigma} = \frac{1}{N} \sum_{i=1}^N (x_i - \hat{\mu})(x_i - \hat{\mu})^T
$$

## Gaussian Discriminant Analysis

The Gaussian Discriminant Analysis (GDA) model assumes that the data points $$x$$ are generated from a multivariate Gaussian distribution $$\mathcal{N}(\mu, \Sigma)$$, where $$\mu$$ is the mean vector and $$\Sigma$$ is the covariance matrix. The model also assumes that the labels $$y$$ are generated from a multinoulli distribution $$\text{Multinoulli}(\phi)$$, the prior probability of each class.

$$
\begin{aligned}
P(y|x) &= \frac{P(x|y)P(y)}{P(x)} \\
&\propto P(x|y)P(y)\\
&= \mathcal{N}(x|\mu_y, \Sigma_y) \phi_y\\
\ln P(y|x) &= \ln \mathcal{N}(x|\mu_y, \Sigma_y) + \ln \phi_y\\
&= -\frac{D}{2}\ln2\pi -\frac{1}{2} \ln |\Sigma_y| - \frac{1}{2} (x - \mu_y)^T \Sigma_y^{-1} (x - \mu_y) + \ln \phi_y\\
\ln \frac{P(y=i|x)}{P(y=j|x)} &= -\frac{1}{2} \ln \frac{|\Sigma_i|}{|\Sigma_j|} - \frac{1}{2} (x - \mu_i)^T \Sigma_i^{-1} (x - \mu_i) + \frac{1}{2} (x - \mu_j)^T \Sigma_j^{-1} (x - \mu_j) + \ln \frac{\phi_i}{\phi_j}\\
\end{aligned}
$$

Linear discriminant analysis (LDA) is a special case of GDA where the covariance matrix $$\Sigma$$ is the same for all classes. In this case, the decision boundary is linear.

$$
\begin{aligned}
\ln \frac{P(y=i|x)}{P(y=j|x)} &= - \frac{1}{2} (x - \mu_i)^T \Sigma^{-1} (x - \mu_i) + \frac{1}{2} (x - \mu_j)^T \Sigma^{-1} (x - \mu_j) + \ln \frac{\phi_i}{\phi_j}\\
&= - \frac{1}{2} x^T \Sigma^{-1} x + x^T \Sigma^{-1}\mu_i - \frac{1}{2} \mu_i^T \Sigma^{-1} \mu_i + \frac{1}{2} x^T \Sigma^{-1} x - x^T \Sigma^{-1}\mu_j + \frac{1}{2} \mu_j^T \Sigma^{-1} \mu_j + \ln \frac{\phi_i}{\phi_j}\\
&= x^T \Sigma^{-1} (\mu_i - \mu_j) - \frac{1}{2} \mu_i^T \Sigma^{-1} \mu_i + \frac{1}{2} \mu_j^T \Sigma^{-1} \mu_j + \ln \frac{\phi_i}{\phi_j}\\
\end{aligned}
$$

where $$\Sigma^{-1}$$ is symmetric and $$\phi_i$$ is the prior probability of class $$i$$.

