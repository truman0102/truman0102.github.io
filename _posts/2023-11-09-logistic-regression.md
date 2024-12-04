---
layout: post
title: Logistic Regression
date: 2023-11-09 13:45:00-0400
description: An introduction to logistic regression
tags: LR ML math
categories: data-science
related_posts: false
giscus_comments: false
disqus_comments: false
toc:
  beginning: true
---

## What is Logistic Regression?

Logistic regression is a classification algorithm. It is a linear model that uses a sigmoid function to predict the probability of a binary output. It is a special case of generalized linear model (GLM).

## Bernoulli Distribution

Consider a binary classification task where the output $$y_i\in\{0,1\}$$. Let:

$$
y|x\sim\text{Bernoulli}(\mu(x))
$$

where$$\mu(x)=p(y=1\vert x)$$. We want to find a function $$f(x)$$ that predicts $$\mu(x)$$.

$$
p(y\vert x) = \mu(x)^y(1-\mu(x))^{1-y}
$$

Specifically,

$$
p(1|x)=\mu(x)
$$ 

and

$$
p(0|x)=1-\mu(x)
$$

We can rewrite the above equation as:

$$
p(y|x) = \mu(x)^y(1-\mu(x))^{1-y} = p(1|x)^yp(0|x)^{1-y}
$$

## Sigmoid Function

Assuming a simplest linear model

$$
z=w_{d}^Tx_{d}
$$

$$
\sigma(z)=\frac{1}{1+e^{-z}}=\frac{e^z}{1+e^z}
$$

is a sigmoid function, where

$$
\mu(x)=\sigma(w^Tx)
$$

The derivative of $$\sigma(z)$$ is

$$
\frac{d\sigma(z)}{dz}=\sigma(z)(1-\sigma(z))
$$

## Logistic Regression

Above, we have 

$$
p(y=1|x) = \mu(x) = \sigma(w^Tx)
$$

and

$$
p(y=0|x) = 1-\mu(x) = 1-\sigma(w^Tx)
$$

Therefore, we can rewrite the equation as:

$$
\begin{aligned}
\frac{p(y=1|x)}{p(y=0|x)} &= \frac{\sigma(w^Tx)}{1-\sigma(w^Tx)} \\
&=\frac{\frac{1}{1+e^{-w^Tx}}}{\frac{e^{-w^Tx}}{1+e^{-w^Tx}}} \\
&=e^{w^Tx}
\end{aligned}
$$

Simultaneously taking logarithms on both sides of the equation:

$$
\ln\frac{p(y=1|x)}{p(y=0|x)} = w^Tx
$$

Therefore, we can predict $$y$$ by $$w^Tx$$.

$$
w^Tx>0\Rightarrow p(y=1|x) > p(y=0|x)
$$

and we predict $$y=1$$.

$$
w^Tx<0\Rightarrow p(y=1|x) < p(y=0|x)
$$

and we predict $$y=0$$.

## Loss Function

The log-likelihood function is

$$
\begin{aligned}
\ell(\mu) &= \sum_{i=1}^N\ln p(y_i|x_i) \\
&= \sum_{i=1}^N\ln(\mu_i^{y_i}(1-\mu_i)^{1-y_i}) \\
&= \sum_{i=1}^N[y_i\ln\mu_i+(1-y_i)\ln(1-\mu_i)]\\
\end{aligned}
$$

The negative log-likelihood (NLL, also known as cross-entropy) function is

$$
L(y, \mu(x)) = -y\ln\mu(x)-(1-y)\ln(1-\mu(x))
$$

Here, $$y$$ is the true label and $$\mu(x)$$ is the predicted probability.Then the great likelihood estimate is equivalent to the negative log likelihood loss:

$$
\begin{aligned}
J(\mu) &= \sum_{i=1}^NL(y_i, \mu(x_i)) \\
&= -\sum_{i=1}^N[y_i\ln\mu(x_i)+(1-y_i)\ln(1-\mu(x_i))]\\
&= -\ell(\mu)
\end{aligned}
$$

The loss function for logistic regression is $$L(y, \mu(x))$$. If we also add a regularization ($$L1$$, $$L2$$, or $$L1+L2$$) term $$\Omega(w)$$, the loss function becomes

$$
J(\omega, \lambda) = \sum_{i=1}^NL(y_i, \mu(x_i;\omega))+\lambda\Omega(w)
$$

Regularization is of much more importance in logistic regression than in linear regression. This is because when the training data is fully divisible, in order to minimize the cross-entropy loss to zero, $$L(y_i, \mu(x_i))$$ must be minimized to zero, and $$\mu(x_i)$$ is either 0 or 1 from $$\sigma(w^Tx_i)$$. This means that $$w^Tx_i$$ must be $$\pm\infty$$, meaning that $$|w|=\infty$$, 
which is a sign of overfitting. Regularization can prevent this from happening.

It is worth noting that the regularized coefficients C of the logistic regression in sklearn is actually the coefficients of cross-entropy loss:

$$
J(\omega, C) = C\sum_{i=1}^NL(y_i, \mu(x_i;\omega))+\Omega(w)
$$

where bigger $$C$$ means less regularization.

## Optimization

The gradient of the negative log-likelihood function $$g(\omega)$$ is

$$
\begin{aligned}
\frac{\partial J(\mu)}{\partial \omega} &= \frac{\partial}{\partial \omega}(-\sum_{i=1}^N[y_i\ln\mu(x_i)+(1-y_i)\ln(1-\mu(x_i))]) \\
&=-\sum_{i=1}^N[y_i\frac{\partial}{\partial \omega}\ln\mu(x_i)+(1-y_i)\frac{\partial}{\partial \omega}\ln(1-\mu(x_i))] \\
&=-\sum_{i=1}^N[y_i\frac{1}{\mu(x_i)}\frac{\partial}{\partial \omega}\mu(x_i)+(1-y_i)\frac{1}{1-\mu(x_i)}\frac{\partial}{\partial \omega}(1-\mu(x_i))] \\
&=-\sum_{i=1}^N[y_i\frac{1}{\mu(x_i)}-(1-y_i)\frac{1}{1-\mu(x_i)}]\frac{\partial}{\partial \omega}\mu(x_i) \\
&=-\sum_{i=1}^N[y_i\frac{1}{\mu(x_i)}-(1-y_i)\frac{1}{1-\mu(x_i)}]\frac{\partial}{\partial \omega}(\sigma(\omega^Tx_i)) \\
&=-\sum_{i=1}^N[y_i\frac{1}{\mu(x_i)}-(1-y_i)\frac{1}{1-\mu(x_i)}]\mu(x_i)(1-\mu(x_i))\frac{\partial}{\partial \omega}(\omega^Tx_i) \\
&=-\sum_{i=1}^N[y_i(1-\mu(x_i))-(1-y_i)\mu(x_i)]x_i \\
&=-\sum_{i=1}^N[y_i-\mu(x_i)]x_i \\
&=-\sum_{i=1}^N[y_i-\sigma(\omega^Tx_i)]x_i \\
&=\sum_{i=1}^N[\sigma(\omega^Tx_i)-y_i]x_i \\
&=X[\sigma(X^T\omega)-y]
\end{aligned}
$$

If regularization is not considered, then $$\omega$$ is updated by

$$
\omega^{(t+1)}=\omega^{(t)}-\eta g(\omega^{(t)})
$$

where $$\eta$$ is the learning rate. However, first-order derivative dose not guarantee an optimal solution. Therefore, we can use Newton's method to find the optimal solution. Hessian matrix is

$$
\begin{aligned}
H(\omega) &= \frac{\partial g(\omega)}{\partial \omega^T} \\
&= \frac{\partial(\sum_{i=1}^N[\sigma(\omega^Tx_i)-y_i]x_i)}{\partial \omega^T}\\
&= \sum_{i=1}^N\frac{\partial(\sigma(\omega^Tx_i)-y_i)x_i}{\partial \omega^T}\\
&= \sum_{i=1}^N\sigma(\omega^Tx_i)(1-\sigma(\omega^Tx_i))x_ix_i^T\\
&= X^TSX
\end{aligned}
$$

where $$S \triangleq diag(\sigma(\omega^Tx_i)(1-\sigma(\omega^Tx_i)))$$. $$\omega$$ is updated by

$$
\omega^{(t+1)}=\omega^{(t)}-H^{-1}(\omega^{(t)})g(\omega^{(t)})
$$

## Multiclass Logistic Regression

Multiclass logistic regression predicts the probability of each class. The predicted class is the one with the highest probability (via softmax function).

$$
p(y=c|x,W)=\frac{e^{\omega_c^Tx}}{\sum_{c'=1}^Ce^{\omega_{c'}^Tx}}
$$

also defined as

$$
\sigma(z)_c=\frac{e^{z_c}}{\sum_{c'=1}^Ce^{z_{c'}}}
$$

The log-likelihood function is

$$
\begin{aligned}
\ell(W) &= \sum_{i=1}^N\ln (\prod_{c=1}^Cp(y=c|x_i,W)^{y_{i,c}}) \\
&=\sum_{i=1}^N\sum_{c=1}^Cy_{i,c}\ln p(y=c|x_i,W) \\
\end{aligned}
$$

Then the loss function is

$$
\begin{aligned}
J(W) &= -\ell(W) \\
&= -\sum_{i=1}^N\sum_{c=1}^Cy_{i,c}\ln p(y=c|x_i,W) \\
&= -\sum_{i=1}^N\sum_{c=1}^Cy_{i,c}\ln\frac{e^{\omega_c^Tx_i}}{\sum_{c'=1}^Ce^{\omega_{c'}^Tx_i}} \\
&= -\sum_{i=1}^N\sum_{c=1}^Cy_{i,c}\ln e^{\omega_c^Tx_i}+\sum_{i=1}^N\sum_{c=1}^Cy_{i,c}\ln\sum_{c'=1}^Ce^{\omega_{c'}^Tx_i} \\
&= -\sum_{i=1}^N\sum_{c=1}^Cy_{i,c}\omega_c^Tx_i+\sum_{i=1}^N\sum_{c=1}^Cy_{i,c}\ln\sum_{c'=1}^Ce^{\omega_{c'}^Tx_i} \\
\end{aligned}
$$

## Evaluation

### Cross-entropy

$$
\text{logloss}(Y,\hat{Y})=-\frac{1}{N}\sum_{i=1}^{N}\sum_{j=1}^{C}y_{i,j}\ln(\hat{y}_{i,j})
$$

### Hinge loss

$$
\text{Hingeloss}(Y,\hat{Y})=\frac{1}{N}\sum_{i=1}^{N}max(1,y_i\hat{y_i})
$$

### Confusion matrix

General metrics from confusion matrix are detailed in [Evaluation in Data Science](/blog/2023/EVA/)


## Homework

### Gradient on single sample

$$
\begin{aligned}
\mu(x) &= \sigma(w^Tx+b) \\
L(y, \mu(x)) &= -y\ln\mu(x)-(1-y)\ln(1-\mu(x)) \\
R(\omega) &= \frac{1}{2}\omega^T\omega \\
J(\mu) &= L(y, \mu(x)) + R(\omega)\\
\frac{\partial J(\mu)}{\partial \omega} &= \frac{\partial L(y, \mu(x))}{\partial \omega} + \frac{\partial R(\omega)}{\partial \omega} \\
\frac{\partial L(y, \mu(x))}{\partial w} &= \frac{\partial}{\partial w}(-y\ln\mu(x)-(1-y)\ln(1-\mu(x))) \\
&= -y\frac{\partial}{\partial w}\ln\mu(x)-(1-y)\frac{\partial}{\partial w}\ln(1-\mu(x)) \\
&= -y\frac{1}{\mu(x)}\frac{\partial}{\partial w}\mu(x)-(1-y)\frac{1}{1-\mu(x)}\frac{\partial}{\partial w}(1-\mu(x)) \\
&= -y\frac{1}{\mu(x)}\frac{\partial}{\partial w}\sigma(w^Tx+b)+(1-y)\frac{1}{1-\mu(x)}\frac{\partial}{\partial w}\sigma(w^Tx+b) \\
&=(\frac{1-y}{1-\mu(x)}-\frac{y}{\mu(x)})\frac{\partial}{\partial w}\sigma(w^Tx+b) \\
&=(\frac{1-y}{1-\mu(x)}-\frac{y}{\mu(x)})\sigma(w^Tx+b)(1-\sigma(w^Tx+b))\frac{\partial}{\partial w}(w^Tx+b) \\
&=(\frac{1-y}{1-\mu(x)}-\frac{y}{\mu(x)})\sigma(w^Tx+b)(1-\sigma(w^Tx+b))x \\
&=(\frac{1-y}{1-\mu(x)}-\frac{y}{\mu(x)})\mu(x)(1-\mu(x))x \\
&=(1-y)\mu(x)x-y(1-\mu(x))x \\
&=(\mu(x)-y)x\\
\frac{\partial L(y, \mu(x))}{\partial b} &= \frac{\partial}{\partial b}(-y\ln\mu(x)-(1-y)\ln(1-\mu(x))) \\
&= (\frac{1-y}{1-\mu(x)}-\frac{y}{\mu(x)})\sigma(w^Tx+b)(1-\sigma(w^Tx+b))\frac{\partial}{\partial b}(w^Tx+b) \\
&=(\frac{1-y}{1-\mu(x)}-\frac{y}{\mu(x)})\sigma(w^Tx+b)(1-\sigma(w^Tx+b)) \\
&=(\mu(x)-y) \\
\frac{\partial R(\omega)}{\partial \omega} &= \frac{\partial}{\partial \omega}\frac{1}{2}\omega^T\omega \\
&= \frac{1}{2}(\frac{\partial}{\partial \omega}\omega^T\omega+\frac{\partial}{\partial \omega}\omega^T\omega) \\
&= \frac{1}{2}(2\omega) \\
&= \omega \\
\frac{\partial J(\mu)}{\partial \omega} &= \frac{\partial L(y, \mu(x))}{\partial \omega} + \frac{\partial R(\omega)}{\partial \omega} \\
&= (\mu(x)-y)x+\omega \\
\frac{\partial J(\mu)}{\partial b} &= \frac{\partial L(y, \mu(x))}{\partial b} + \frac{\partial R(\omega)}{\partial b} \\
&= (\mu(x)-y)+0 \\
&= \mu(x)-y \\
\end{aligned}
$$

Given data as below:

$$
\begin{matrix}
&X_1 &X_2 &X_3 &X_4 &Y \\
1 &5 &3 &1 &1 &1 \\
2 &4 &2 &1 &1 &1 \\
3 &2 &1 &2 &3 &0 \\
4 &1 &2 &3 &2 &0 \\
\end{matrix}
$$

Let $$w=[0.5, 0.5, 0.5, 0.5]^T$$ and $$b=0.5$$, calculate the gradient of $$w$$ and $$b$$ on each sample.

### Predict

```python
w_new = np.array([0.482, 0.179, -0.512, -0.524])
b_new = 0.187
T_5 = np.array([1,3,4,2])
```

$$
\begin{aligned}
\frac{P(y=1|T_5)}{P(y=0|T_5)} &= \frac{\sigma(w_{new}^TT_5+b_{new})}{1-\sigma(w_{new}^TT_5+b_{new})} \\
&=\frac{\frac{1}{1+e^{-w_{new}^TT_5-b_{new}}}}{\frac{e^{-w_{new}^TT_5-b_{new}}}{1+e^{-w_{new}^TT_5-b_{new}}}} \\
&=e^{w_{new}^TT_5+b_{new}} \\
\ln\frac{P(y=1|T_5)}{P(y=0|T_5)} &= w_{new}^TT_5+b_{new} \\
&=-1.89<0 \\
\end{aligned}
$$

So$$P(y=1\vert T_5)<P(y=0\vert T_5)$$，the predicted label is 0.