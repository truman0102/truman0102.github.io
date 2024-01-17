---
layout: post
title: Regularization
date: 2024-01-10 00:00:00-0400
description: An introduction to regularization in machine learning.
tags: regularization ML
categories: data-science
related_posts: false
thumbnail:
toc:
  beginning: true
---

## Introduction

Regularization is a technique used to prevent overfitting in machine learning models. It does this by adding a penalty term to the loss function. The penalty term is a function of the weights of the model. The penalty term is small when the weights are small and large when the weights are large. This encourages the model to learn smaller weights, which in turn reduces overfitting.

$$
\mathcal{L}(\theta) = \mathcal{L}_0(\theta) +  \underbrace{\lambda\mathcal{R}(\theta)}_{\text{regularization}}
$$

where $$\mathcal{L}_0(\theta)$$ is the loss function without regularization, $$\lambda$$ is the regularization strength, and $$\mathcal{R}(\theta)$$ is the regularization term.

## Types of Regularization

### L2 Regularization

L2 regularization is the most common type of regularization. It is also known as ridge regression. The regularization term is the sum of the squares of the weights.

$$
\mathcal{R}(\theta) = \sum_{i=1}^n \theta_i^2
$$

### L1 Regularization

L1 regularization is also known as Lasso regression. The regularization term is the sum of the absolute values of the weights.

$$
\mathcal{R}(\theta) = \sum_{i=1}^n |\theta_i|
$$

## Regularization, Bias, and Variance

Bias and variance are two sources of error in machine learning models. Bias is the difference between the expected value of the model's predictions and the true value. Variance is the variability of the model's predictions. 

The bias-variance tradeoff is a fundamental concept in machine learning. It states that there is a tradeoff between bias and variance. A model with high bias will have low variance and vice versa. The goal is to find a model that has low bias and low variance. Regularization reduces variance at the expense of increasing bias. This is because regularization reduces the complexity of the model, which reduces the model's ability to fit the training data.