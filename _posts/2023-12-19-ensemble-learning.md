---
layout: post
title: Ensemble Learning
date: 2023-12-19 00:00:00-0400
description: An introduction to ensemble learning.
tags: ML
categories: data-science
related_posts: false
thumbnail:
toc:
  beginning: true
---

# Ensemble Learning

Ensemble learning is a technique that combines multiple machine learning models to produce a single model with better predictive performance. The idea is that by combining multiple models, we can reduce the variance of the model, and thus improve the predictive performance.

# Boosting

## AdaBoost

Given a set of base classifiers $$\phi_1, \phi_2, \ldots, \phi_M$$, AdaBoost combines them into a single classifier. The base classifiers are trained sequentially, with each subsequent classifier trained on the misclassified examples of the previous classifier. The final classifier is a weighted sum of the base classifiers.

The most important part of AdaBoost is the weighting of the base classifiers, and the weight of each training example. The weight of each training example is updated after each iteration, and the weight of each base classifier is updated after each iteration. The weight of each training example is updated based on the error of the previous classifier, and the weight of each base classifier is updated based on the error of the current classifier.

The $$m$$-th base classifier is trained on the training examples $$\mathcal{D_m}$$, where the weight of each training example is $$w_{m, i}$$, and the weight of each base classifier is $$\alpha_m$$. We can train the base classifier by minimizing the weighted error:

$$
\mathcal{J}(\phi_m,\lambda) = \sum_{i=1}^N w_{m, i} \mathcal{L}(\phi_m(x_i), y_i) + \lambda \mathcal{R}(\phi_m)
$$

Usually, $$w_{m,i}$$ is initialized to $$\frac{1}{N}$$, where $$N$$ is the number of training examples.

The weight of each base classifier is updated based on the error of the current classifier:

$$
\begin{aligned}
w_{m+1,i} &= \left\{
\begin{array}{ll}
\frac{w_{m,i}d_m}{z_{m}} & \text{if } \phi_m(x_i) \neq y_i \\
\frac{w_{m,i}}{z_m d_m} & \text{if } \phi_m(x_i) = y_i \\
\end{array}
\right. \\
\end{aligned}
$$

To make sure that the weights sum to 1, we normalize the weights:

$$
\begin{aligned}
\epsilon_m &= \sum_{i=1}^N w_{m,i}\mathbb{I}(\phi_m(x_i) \neq y_i) \\
z_{m} &= \sum_{i=1}^N w_{m,i}d_m\mathbb{I}(y_i \neq \phi_m(x_i)) + \sum_{i=1}^N \frac{w_{m,i}}{d_m}\mathbb{I}(y_i = \phi_m(x_i)) \\
&= d_m\epsilon_m + \frac{1}{d_m}(1 - \epsilon_m) \\
\end{aligned}
$$

It is expected that the sum of new weights of misclassified examples is always equal to the sum of new weights of correctly classified examples.

$$
\begin{aligned}
d_m\epsilon_m &= \frac{1-\epsilon_m}{d_m} \\
d_m^2\epsilon_m &= 1 - \epsilon_m \\
d_m &= \sqrt{\frac{1-\epsilon_m}{\epsilon_m}} \\
\alpha_m &= \log d_m \\
&= \frac{1}{2}\log\frac{1-\epsilon_m}{\epsilon_m} \\
z_{m} &= 2\sqrt{\epsilon_m(1-\epsilon_m)}
\end{aligned}
$$

where $$\alpha_m$$ is the weight of the $$m$$-th base classifier, and $$z_{m+1}$$ is the normalization factor. The final classifier is a weighted sum of the base classifiers:

$$
\Phi(x) = \mathrm{sgn}(\sum_{m=1}^M \alpha_m \phi_m(x))
$$

# Appendix

## Mathematical Notation

The dataset is denoted as $$\mathcal{D} = \{(x_1, y_1), (x_2, y_2), \ldots, (x_N, y_N)\}$$, where $$x_i \in \mathbb{R}^d$$ is the $$i$$th training example, and $$y_i \in \{-1, 1\}$$ is the corresponding label. The base classifiers are denoted as $$\phi_1, \phi_2, \ldots, \phi_M$$, and the final classifier is denoted as $$\Phi$$.