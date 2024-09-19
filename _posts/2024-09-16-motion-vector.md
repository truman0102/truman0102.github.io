---
layout: post
title: Motion Vector
date: 2024-09-16 00:00:00-0400
description: An introduction to the motion vector in computer vision.
tags: 
categories: 
related_posts: false
giscus_comments: true
thumbnail: 
toc:
  beginning: true
---

## Introduction

A motion vector is calculated by comparing the motion of an object in two consecutive frames, or finding a correspondence between rectangles at time $$t$$ and $$t-1$$, where $$t$$ is the frame index in a video sequence.

$$
\vec{v} = \arg\min\Vert I(x, y, t) - I(x-v_1, y-v_2, t-1)\Vert
$$

where $$I(x, y, t)$$ is the intensity of the pixel at $$(x, y)$$ in frame $$t$$, and $$\vec{v} = (v_1, v_2)$$ is the motion vector that minimizes the difference between the two frames. The difference can usually be written as $$\Delta I = I(x, y, t) - I(x-v_1, y-v_2, t-1)$$. If $$0\leq\Delta I\leq255$$, the motion is usually coded with 8 bits; if $$-8\leq\Delta I\leq7$$, then 4 bits are used.

## Optical Flow

The basic idea of optical flow is to treat the motion vector as a continuous function of the spatial coordinates $$(x, y)$$:

$$
I(x+\Delta x, y+\Delta y, t+\Delta t) = I(x, y, t) + \frac{\partial I}{\partial x}\Delta x + \frac{\partial I}{\partial y}\Delta y + \frac{\partial I}{\partial t}\Delta t + \epsilon
$$

In practice, the optical flow is estimated by solving the following equation:

$$
\begin{aligned}
\frac{\partial I}{\partial x} &= I(x, y, t) - I(x-1, y, t) \\
\frac{\partial I}{\partial y} &= I(x, y, t) - I(x, y-1, t) \\
\frac{\partial I}{\partial t} &= I(x, y, t) - I(x, y, t-1)
\end{aligned}
$$

Suppose the intensity remains constant in a small neighborhood, the optical flow can be approximated as:

$$
\begin{aligned}
\frac{\partial I}{\partial x}\Delta x + \frac{\partial I}{\partial y}\Delta y + \frac{\partial I}{\partial t}\Delta t &= 0 \\
\frac{\partial I}{\partial x}\frac{\Delta x}{\Delta t} + \frac{\partial I}{\partial y}\frac{\Delta y}{\Delta t} &= -\frac{\partial I}{\partial t}
\end{aligned}
$$

Let $$\vec{v} = (\frac{\Delta x}{\Delta t}, \frac{\Delta y}{\Delta t})$$, the optical flow equation can be written as:

$$
\nabla I\cdot\vec{v} = -\frac{\partial I}{\partial t}
$$

where $$\nabla I = (\frac{\partial I}{\partial x}, \frac{\partial I}{\partial y})$$ is the gradient of the intensity.

## Lucas-Kanade Method

The Lucas-Kanade method is a popular algorithm for optical flow estimation. It assumes that the motion is constant in a small neighborhood, and solves the following equation:

$$
\begin{aligned}
\begin{pmatrix}
\frac{\partial I(\vec{r_1})}{\partial x} & \frac{\partial I(\vec{r_1})}{\partial y} \\
\frac{\partial I(\vec{r_2})}{\partial x} & \frac{\partial I(\vec{r_2})}{\partial y} \\
\vdots & \vdots \\
\frac{\partial I(\vec{r_n})}{\partial x} & \frac{\partial I(\vec{r_n})}{\partial y}
\end{pmatrix}
\underbrace{\begin{pmatrix}
v_1 \\
v_2
\end{pmatrix}}_{\vec{v}} &= -\underbrace{\begin{pmatrix}
\frac{\partial I(\vec{r_1})}{\partial t} \\
\frac{\partial I(\vec{r_2})}{\partial t} \\
\vdots \\
\frac{\partial I(\vec{r_n})}{\partial t}
\end{pmatrix}}_{\vec{b}} + \vec{\epsilon} \\
A\vec{v} &= -\vec{b}
\end{aligned}
$$

The solution is given by the pseudo-inverse of $$A$$:

$$
\vec{v} = -(A^TA)^{-1}A^T\vec{b}
$$