---
layout: post
title: Learning Global Routing via Hub Generation and Pin-hub Connection
date: 2024-12-04 15:00:00-0400
description:
tags: chip RL
categories: paper-reading
related_posts: false
---

## Introduciton

## Fundamentals

### Hub

Hub是网格中的一个连接点，类似于交通路段的路口，根据上下左右网格的连接情况，可以分为四种类型：

$$
\begin{aligned}
&+: &r_{(i-1)j} = r_{(i+1)j} = r_{i(j-1)} = r_{i(j+1)} = 1 \\
&\perp: &r_{(i-1)j} + r_{(i+1)j} = r_{i(j-1)} + r_{i(j+1)} = 3 \\
&\llcorner: &r_{(i-1)j} + r_{(i+1)j} = 1 \;\text{and}\; r_{i(j-1)} + r_{i(j+1)} = 1 \\
&\cdot: &r_{(i-1)j} + r_{(i+1)j} + r_{i(j-1)} + r_{i(j+1)} = 1 \\
\end{aligned}
$$

### RSMT

## Methodology

{% include figure.liquid loading="eager" path="assets/img/paper_reading/HUB.png" class="img-fluid rounded z-depth-1" %}

### Hub Generation

Hub的生成使用的是条件生成模型，输出以生成Hub为主，同时还生成了用于过滤噪声点的stripe mask和未被使用的预路由路径。

stripe是一个布尔值矩阵，可用于拒绝部分生成的错误Hub。在具体过滤时，stripe mask按行或列进行计算，如果行或列上有超过半数的mask为真，则该行或列被保留。所以stripe mask是一个部分列或行全部为真的矩阵。

### Pin-hub Connection

连接hub和pin被视为一个RSMT构建问题，引入hub的构建方法的好处是
1. 可以降低复杂度至$$O(n\log n)$$
1. RSMT只能找到最短路径，引入hub可以支持其他约束条件

具体地，参考REST^[J. Liu, G. Chen, and E. F. Young. Rest: Constructing rectilinear steiner minimum tree via reinforcement learning. In 2021 58th ACM/IEEE Design Automation Conference (DAC), pages 1135–1140. IEEE, 2021.]学习Rectilinear edge sequence (RES)的方法，应用了actor critic算法。actor根据给定的点坐标生成RES，critic预测RSMT的长度，这个预测值在训练时向真实值靠拢，以达到优化目的。

## Experiment

### Dataset

在routing benchmark ISPD-07上应用NCTU-GR^[W.-H. Liu, W.-C. Kao, Y.-L. Li, and K.-Y. Chao. Nctu-gr 2.0: Multithreaded collision-aware global routing with bounded-length maze routing. IEEE Transactions on computer-aided design of integrated circuits and systems, 32(5):709–722, 2013.]获取真实的路由示例。额外引入的路由数据集包括ISPD-98、DRL-8和DRL-16.