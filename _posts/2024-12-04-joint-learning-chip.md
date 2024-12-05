---
layout: post
title: On Joint Learning for Solving Placement and Routing in Chip Design
date: 2024-12-04 11:00:00-0400
description:
tags: chip RL
categories: paper-reading
related_posts: false
bibliography: 2024-12-04-joint-learning-chip.bib
---

## Methodology

布局布线任务主要由三部分组成，分别是宏单元的放置、标准单元的放置和路由，这篇文章的主要工作是提出了应用强化学习方法的宏单元放置方法，至于标准单元的放置和路由，则采用了现有的DREAMPlace和DeepPR方法。下面将围绕强化学习方法介绍主要内容。

### State

状态分为两部分，分别是描述全局的布局图$$I$$和包含已放置宏的详细位置的网表图$$H$$，$$I$$是一个二进制矩阵，用于表示单元格是否被占用。

### Action

RL agent每次可以选择一个宏单元进行放置，放置的位置由一个二维坐标$$(x, y)$$表示。因此动作空间是$$I$$中所有未被占用的位置。

### Reward

奖励分为外部奖励和内部奖励，外部奖励粗略估计布局布线的质量，内部奖励用于解决稀疏奖励问题，鼓励agent进行探索。

外部奖励由线长和拥塞组成，真实线长取决于路由结果，为了快速评估，所以用半周长线长(HPWL)代替。拥塞通过[矩形均匀线密度](https://circuitnet.github.io/feature/routability%20features.html#rudy-%E2%91%AA--%E2%91%AE)(RUDY)计算，文中路由拥塞的阈值设为0.1。

$$
R_E = -\text{WireLength}(P,H) - \lambda\text{Congestion}(P,H)
$$

其中$$P$$是放置结果，$$H$$是网表图，$$\lambda$$是权重。

内部奖励采用了随机网络蒸馏(Random Network Distillation, RND)的方法，用于解决稀疏奖励问题。RND的目标是预测随机网络的输出，奖励是预测误差。

$$
R_I = \Vert \hat{f}_\theta(o) - f(o) \Vert^2
$$

### Model

策略网络的输入是$$I$$和$$H$$，使用了一个CNN和一个GNN对状态分别进行编码，然后将两个编码结果拼接，输入到一个MLP中，输出动作的概率分布，实现了PPO算法。

### Pretraining

类似课程学习的思想，预训练阶段只对宏单元放置进行训练，学习一个中间位置。

## Experiment

Benchmark选择的是ISPD-2005