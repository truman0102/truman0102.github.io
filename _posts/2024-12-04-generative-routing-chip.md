---
layout: post
title: The Policy-gradient Placement and Generative Routing Neural Networks for Chip Design
date: 2024-12-04 13:00:00-0400
description:
tags: chip RL
categories: paper-reading
related_posts: false
---

## Introduction

这篇文章是[布局学习](/blog/2024/joint-learning-chip)的续作，在宏放置工作的基础上，提出了混合尺寸宏放置和生成式路由方法。

## Fundamentals

### Global Routing Grid Protocol

在全局路由中，物理芯片被分割成多个矩形网格，每个网格代表一个节点，相邻网格的公共边表示两个节点之间的连接，也将这个节点称作全局路由单元。所有路由都应遵循Rectilinear Steiner Tree (RST)规则，连接路径仅限于水平和垂直线段。

## Methodology

### Placement

与前一篇工作基本一致，主要有两点改进
1. 考虑了宏的尺寸，在采取放置动作时，选择宏的中心点并在二元矩阵中对整个宏的位置进行标记。
2. 在奖励函数中额外引入了对重叠的惩罚。

Placement作为pipeline的第一阶段，与路由任务都接受布线长度作为奖励信号，这里采用了变权的长度估计方法，总结来说就是训练前期采用HPWL，训练后期采用生成模型的路由结果，这样的设计是考虑到前期的布线结果可能不够准确。

### Generative Routing

输入是基于放置结果的与全局路由单元网格等大的图像，包括三个通道，分别是引脚的位置、水平和垂直网格边缘的可用性，输出是一个图像，其单元格取值表示是否属于路由的概率，对应生成式路由模型。路由生成模型是一个生成对抗网络，它包含一个基模型$$G_{\text{base}}$$和一个处理边长超过$$64$$的大模型$$G_{\text{large}}$$。$$G_{\text{base}}$$的热力图和$$G_{\text{large}}$$的热力图相加用于生成更大的路由图。

{% include figure.liquid loading="eager" path="assets/img/paper_reading/cGAN.png" class="img-fluid rounded z-depth-1" %}

判别器评估路由结果的连通性和真实性，这是路由任务的主要对抗损失。此外，作者采用了focal loss去学习大量琐碎的否定点和少量的正点。考虑到HPWL可以作为路由的理论下界，可以将路由结果的长度与半周长的差值作为限制线长的正则项。

### Learning Net Order to Route

## Experiment

### Benchmark

ISPD-2005 for placement and ISPD-07 for routing