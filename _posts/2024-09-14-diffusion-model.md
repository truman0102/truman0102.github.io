---
layout: post
title: Diffusion Model
date: 2024-09-14 00:00:00-0400
description: An introduction to the diffusion model.
tags: math
categories: data-science
related_posts: false
giscus_comments: false
toc:
  beginning: true
---

## Introduction

Diffusion model is defined as a Markov chain of diffusion steps to slowly add random noise to data and learn to reverse the process to construct data from the noise.

## Definition

### Forward Process

Given a data $$x_0\sim q(x)$$, a sequence of noisy samples $$x_1, x_2, \ldots, x_T$$ is generated by adding gaussian noise to the data step by step. The step sizes are controlled by a variance schedule $$\{\beta_t\in (0,1)\}_{t=1}^T$$.

$$
\begin{aligned}
q(x_t\vert x_{t-1}) &= \mathcal{N}(x_t\vert \sqrt{1-\beta_t}x_{t-1}, \beta_t I) \\
q(x_{1\colon T}\vert x_0) &= \prod_{t=1}^T q(x_t\vert x_{t-1})
\end{aligned}
$$

As $$T\to\infty$$, the distribution of $$x_T$$ approaches an isotropic gaussian distribution. Let $$\alpha_t = 1-\beta_t$$ and $$\bar{\alpha}_t = \prod_{s=1}^t\alpha_s$$, the above process can be written as a closed-form solution using repameterization trick:

$$
\begin{aligned}
q(x_t\vert x_{t-1}) &= \mathcal{N}(x_t\vert \sqrt{\alpha_t}x_{t-1}, (1-\alpha_t)I)& \\
&= \sqrt{\alpha_t}x_{t-1} + \sqrt{1-\alpha_t}\epsilon_{t-1}& \epsilon_{t-1}\sim\mathcal{N}(0, I) \\
&= \sqrt{\alpha_t\alpha_{t-1}}x_{t-2} + \sqrt{\alpha_t(1-\alpha_{t-1})}\epsilon_{t-2} + \sqrt{1-\alpha_t}\epsilon_{t-1}& \\
&= \sqrt{\alpha_t\alpha_{t-1}}x_{t-2} + \sqrt{1-\alpha_t\alpha_{t-1}}\bar{\epsilon}_{t-2}& \bar{\epsilon}_{t-2}\text{ is a mixture of }\epsilon_{t-1}\text{ and }\epsilon_{t-2} \\
&= \dots & \\
&= \sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon& \\
q(x_t\vert x_0) &= \mathcal{N}(x_t\vert \sqrt{\bar{\alpha}_t}x_0, (1-\bar{\alpha}_t)I)
\end{aligned}
$$

Two gaussians $$\mathcal{N}(0, \sigma_1^2 I)$$ and $$\mathcal{N}(0, \sigma_2^2 I)$$ can be mixed into a gaussian $$\mathcal{N}(0, (\sigma_1^2+\sigma_2^2)I)$$. The variance of the gaussian $$x_t$$ refers to the sum of the variances of the noise at each step, which is $$\sum_{s=1}^t\beta_s$$.

### Reverse Process

A model $$p_{\theta}$$ is trained to reverse the process by learning the conditional distribution $$p_{\theta}(x_{t-1}\vert x_t)$$.

$$
p_{\theta}(x_{t-1}\vert x_t) = \mathcal{N}(x_{t-1}\vert \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))
$$

The conditional probability can be written as conditioned on $$x_0$$:

$$
\begin{aligned}
q(x_{t-1}\vert x_t, x_0) &= \mathcal{N}(x_{t-1}\vert \tilde{\mu}_(x_t, x_0), \tilde{\beta}_t I) \\
\end{aligned}
$$

According bayes' rule,  the mean and variance can be parameterized as follows:

$$
\begin{aligned}
\tilde{\beta}_t &= \frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t}\beta_t \\
\tilde{\mu}_t(x_t, x_0) &= \frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t}x_t + \frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}{1-\bar{\alpha}_t}x_0 \\
x_0 &= \frac{1}{\sqrt{\bar{\alpha}_t}}(x_t - \sqrt{1-\bar{\alpha}_t}\epsilon) \\
\tilde{\mu} &= \frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t}x_t + \frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}{1-\bar{\alpha}_t}\frac{1}{\sqrt{\bar{\alpha}_t}}(x_t - \sqrt{1-\bar{\alpha}_t}\epsilon) \\
&= \frac{1}{\sqrt{\alpha_t}}(x_t-\frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t}}\epsilon)
\end{aligned}
$$

Thus, the reverse process can be written as:

$$
x_{t-1} = \mathcal{N}(x_{t-1}\vert \frac{1}{\sqrt{\alpha_t}}(x_t-\frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t}}\epsilon_\theta(x_t, t)), \frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t}\beta_t I)
$$

It can be shown that all we need to do is to learn the noise $$\epsilon_\theta(x_t, t)$$, equivalent to learning the noise $$\epsilon_\theta(\sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon, t)$$

## Advanced Topics

### Parameterization of $$\beta$$

Usually, we can afford a larger update step when the sample gets noisier, so $$\beta_1< \beta_2< \ldots < \beta_T$$ and therefore $$\bar{\alpha}_1 > \bar{\alpha}_2 > \ldots > \bar{\alpha}_T$$.

### Parameterization of Variance

Since learning a variance leads to unstable training, the variance is usually set to a fixed value $$\frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t}\beta_t$$.

### Denoising Diffusion Implicit Model

DDIM makes it possible to train the diffusion model up to any arbitrary number of forward steps but only sample from a subset of steps in the generative process.

$$
q_{\sigma, s<t}(x_s\vert x_t, x_0) = \mathcal{N}(x_s\vert \sqrt{\bar{\alpha}_s}(\frac{x_t-\sqrt{1-\bar{\alpha}_t}\epsilon_\theta^t(x_t)}{\sqrt{\bar{\alpha}_t}})+\sqrt{1-\bar{\alpha}_s-\sigma_t^2}\epsilon_\theta^t(x_t), \sigma_t^2I)
$$

### Latent Variable Space

Latent diffusion model runs the process in a latent space $$z_t$$ instead of the data space $$x_t$$, which is more efficient and can be used to process multi-modal data.

### Model Architecture

There are two common architectures for diffusion models: U-Net and Transformer.


For more details, please refer to [Lilian Weng's blog](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/).