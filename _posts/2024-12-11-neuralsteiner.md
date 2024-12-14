---
layout: post
title: Learning Steiner Tree for Overflow-avoiding Global Routing in Chip Design
date: 2024-12-11 02:00:00-0400
description:
tags: chip RL
categories: paper-reading
related_posts: false
---

## Introduction

全局路由问题是构建一棵连接所有引脚的直角树，一般用Hanan网格或逃逸图来生成避障最短路径RSMT，在大规模集成电路上一般很难优化拥塞问题。

在最小生成树中有必要考虑边的容量，定义边$$e(u,v)\in E$$的容量为$$c(u, v)$$，$$d(u, v)$$表示通过$$e(u, v)$$的路由的数量，$$r(u,v)=c(u,v)-d(u,v)$$是边的可用资源，理想情况下我们应当维持$$r\geq 0$$，不然就会导致溢出 (overflow) 问题。

基于学习的路由方法生成路由结果构建最短斯坦纳树，但事实上有时一个路径长度次优的路由结果可以减少拥塞或者减少溢出的可能性。

## Methodology

### Grouped Parallel

### Point Prediction

点预测被理解为一个像素级分类问题，识别潜在的Steiner点。与HubRouter工作一样使用了CUGR方法在benchmark上构建专家路由结果，应用其逻辑斯蒂函数计算溢出值，得到减小拥塞的路由结果，并选出可参考的Steiner点。

网络结构是ResNet + recurrent crisscross attention mechanism (RCCA)

目标函数有三个部分，前两个目标函数针对点预测问题，第三个目标函数针对溢出问题
1. focal loss:$$-\alpha(1-p_t)^\gamma\log(p_t)$$
1. dice loss: $$1-\frac{2\sum p_{xy}g_{xy}+\epsilon}{\sum p_{xy} + \sum g_{xy} + \epsilon}$$
1. overflow loss: $$\frac{\sum p_{xy}o_{xy}+\epsilon}{\sum p_{xy}+\epsilon}$$

### Net Augmented Graph

将pin grid和point grid合并可以得到一个潜在连接点网格，将网格中有值的点（pin或者Steiner点）连接起来，得到一个Net Augmented Graph。边的选择规则如下
1. 两个point在水平或垂直方向上一致
1. 两点中间没有其他点

边的权重计算方式为

$$
\mathcal{W}(e) = w_d(\vert x_p - x_q \vert + \vert y_p - y_q \vert) + w_o\sum o_{xy}
$$

这个权重函数包含了两个部分，一个是两点之间的曼哈顿距离，另一个是两点之间的溢出值。

### RST Construction

依据pin之间的连通性，芯片上的pin被分成多个group，每次迭代都计算group之间的距离，然后对group贪心地合并，即每次合并两个最近的group，然后更新距离，直到只剩下一个group。这其实是一种层次化的聚类方法。

## Experiment

Benchmark 包括 ISPD98/07/18/19