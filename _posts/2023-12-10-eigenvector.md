---
layout: post
title: Eigenvalue and eigenvector
date: 2023-02-11 00:00:00-0400
description: An introduction to eigenvalue and eigenvector in linear algebra.
tags: eigenvalue eigenvector math
categories: linear-algebra
related_posts: false
giscus_comments: false
thumbnail: 
toc:
  sidebar: left
---

## Introduction

Eigenvalue and eigenvector are important concepts in linear algebra. They are used in many applications such as image processing, data compression, and machine learning. In this post, we will introduce the concept of eigenvalue and eigenvector and show some examples.

## What is an eigenvector?

An eigenvector is a vector that does not change its direction when a linear transformation is applied to it. It can be represented as a column matrix.

$$
\vec{v} = \begin{bmatrix} v_1,v_2,\dots,v_n \end{bmatrix}^T \in \mathbb{R}^n
$$

## What is an eigenvalue?

An eigenvalue is a scalar value that represents how much the eigenvector is stretched or squished when a linear transformation is applied to it. It can be represented as a scalar value.

$$
\lambda \in \mathbb{R}
$$

## Relationship between eigenvalue and eigenvector

An eigenvector $$\vec{v}$$ and its corresponding eigenvalue $$\lambda$$ satisfy the following equation.

$$
A\vec{v} = \lambda\vec{v}
$$

where $$A$$ is a square matrix.

## How to find eigenvalue and eigenvector?

To find eigenvalue and eigenvector, we need to solve the following equation.

$$
\det(A-\lambda I) = 0
$$

where $$A$$ is a square matrix and $$I$$ is an identity matrix.

## Example

Let's find the eigenvalue and eigenvector of the following matrix.

$$
A = \begin{bmatrix} 2 & 4 \\ -3 & 10 \end{bmatrix}
$$

First, we need to find the determinant of $$A-\lambda I$$.

$$
\begin{aligned}
\det(A-\lambda I) &= \det\left(\begin{bmatrix} 2 & 4 \\ -3 & 10 \end{bmatrix} - \begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix}\right) \\
&= \det\left(\begin{bmatrix} 2-\lambda & 4 \\ -3 & 10-\lambda \end{bmatrix}\right) \\
&= (2-\lambda)(10-\lambda) - (-3)(4) \\
&= \lambda^2 - 12\lambda + 32 \\
&= (\lambda - 8)(\lambda - 4)
\end{aligned}
$$

Then, we need to solve the following equation.

$$
\begin{aligned}
\det(A-\lambda I) &= 0 \\
(\lambda - 8)(\lambda - 4) &= 0 \\
\lambda - 8 &= 0 \quad \text{or} \quad \lambda - 4 = 0 \\
\lambda &= 8 \quad \text{or} \quad \lambda = 4
\end{aligned}
$$

Therefore, the eigenvalues of $$A$$ are $$\lambda = 8$$ and $$\lambda = 4$$.

Next, we need to find the eigenvectors of $$A$$.

When $$\lambda = 8$$, we need to solve the following equation.

$$
\begin{aligned}
A\vec{v} &= \lambda\vec{v} \\
\begin{bmatrix} 2 & 4 \\ -3 & 10 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} &= 8\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} \\
\begin{bmatrix} 2v_1 + 4v_2 \\ -3v_1 + 10v_2 \end{bmatrix} &= \begin{bmatrix} 8v_1 \\ 8v_2 \end{bmatrix} \\
\begin{bmatrix} 2v_1 + 4v_2 - 8v_1 \\ -3v_1 + 10v_2 - 8v_2 \end{bmatrix} &= \begin{bmatrix} 0 \\ 0 \end{bmatrix} \\
\begin{bmatrix} -6v_1 + 4v_2 \\ -3v_1 + 2v_2 \end{bmatrix} &= \begin{bmatrix} 0 \\ 0 \end{bmatrix} \\
3v_1 &= 2v_2 \\
\end{aligned}
$$

Let $$v_1 = 2$$, then $$v_2 = 3$$. Therefore, the eigenvector of $$A$$ when $$\lambda = 8$$ is

$$
\vec{v} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}
$$

When $$\lambda = 4$$, we need to solve the following equation.

$$
\begin{aligned}
A\vec{v} &= \lambda\vec{v} \\
\begin{bmatrix} 2 & 4 \\ -3 & 10 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} &= 4\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} \\
\begin{bmatrix} 2v_1 + 4v_2 \\ -3v_1 + 10v_2 \end{bmatrix} &= \begin{bmatrix} 4v_1 \\ 4v_2 \end{bmatrix} \\
\begin{bmatrix} 2v_1 + 4v_2 - 4v_1 \\ -3v_1 + 10v_2 - 4v_2 \end{bmatrix} &= \begin{bmatrix} 0 \\ 0 \end{bmatrix} \\
\begin{bmatrix} -2v_1 + 4v_2 \\ -3v_1 + 6v_2 \end{bmatrix} &= \begin{bmatrix} 0 \\ 0 \end{bmatrix} \\
v_1 &= 2v_2 \\
\end{aligned}
$$

Let $$v_1 = 2$$, then $$v_2 = 1$$. Therefore, the eigenvector of $$A$$ when $$\lambda = 4$$ is

$$
\vec{v} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}
$$
