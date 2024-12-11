---
layout: post
title: Macro Placement by Wire-Mask-Guided Black-Box Optimization
date: 2024-12-09 10:00:00-0400
description:
tags: chip RL
categories: paper-reading
related_posts: false
---

## Introduction

## Background

这篇文章的背景部分概括问题比较好，因此我直接引用了原文的内容。

### Macro Placement

Macro placement的输入是网表$$H=(V,E)$$，$$V$$是所有cell的信息，$$E$$是所有的边的信息，输出是所有macro的二维坐标。

HPWL是常用的评价指标，也可以作为RL的reward，具体来说就是$$E$$中所有边构成的矩形的半周长之和。

拥塞度是另一个重要的指标，RUDY为常见的计算拥塞度的方法。具体计算方法为取前$$10\%$$的grid，构成一个子图$$G^{\prime}$$，然后计算$$G^{\prime}$$中每个点所属的所有超边的矩形区域的平均拥塞度$$\frac{1}{\vert G^{\prime} \vert}\sum_{g_i\in G^{\prime}}\sum_{e_j\in E(g_i)}\frac{w_j+h_j}{w_j\cdot h_j}$$。

密度用于衡量重叠程度，由于无重叠是宏布局的硬约束，因此有些方法中不作讨论。

面积是包围所有宏的最小矩形的面积，在一个固定面积的芯片中布局时，优化目标一般不是面积而是HPWL等。

### Packing-based Methods

macro placement任务中，每个macro以矩形表示，在芯片内部进行放置。目前几种表示方法有sequence-pair, $$\text{B}^\prime$$树, corner block list等。

对于marco和标准单元的放置一般采用分而治之的方法，对标准单元进行聚类，然后对marco和类团进行放置，再对类团重新分配，优化布局。聚类方法虽然能缩减任务规模，但可能会切断一些连接，妨碍找到最优解。

### Analytical Methods

Analytical methods是一种基于数学模型的方法，通过建立数学模型，求解最优解，以DREAMPlce为代表，将整个placement任务视为最小化目标函数的问题，目标函数包括平滑加权平均线长和密度。分析方法的缺点是不能保证单元之间不重叠，即不能保证硬约束。

### Intensive Reward in MaskPlace

将放置macro后HPWL的增加值作为reward，提供即时奖励。

## Methodology

- 对macro进行排序，依据是与其相连接的单元的面积和。
- wire-mask-guided placement: 通过计算满足硬约束位置的HPWL增量来指导macro的有序放置。
- black-box optimization
    - random search
    - bayesian optimization
    - evolutionary algorithm: 随机选择两个位置交换位置