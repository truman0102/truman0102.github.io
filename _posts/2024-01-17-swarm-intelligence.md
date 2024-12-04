---
layout: post
title: Swarm Intelligence
date: 2024-01-17 00:00:00-0400
tags: AI
categories: artificial-intelligence
toc:
    beginning: true
giscus_comments: false
related_posts: false
---

## 群体智能

### 蚁群算法

蚁群算法适用于空间搜索，在图搜索中寻找最短路径，如旅行商问题。蚁群算法的基本思想是

- 每个蚂蚁表示一个agent，蚂蚁在空间中随机移动求解问题
- 蚂蚁经过一条路径后，会在路径上留下信息素，信息素浓度与路径的优劣有关
- 蚂蚁的移动是一个概率过程，与移动路径上的信息素浓度有关，信息素浓度越高，蚂蚁越有可能选择该路径
- 每当所有蚂蚁完成一轮搜索后，根据他们的路径更新信息素浓度
- 重复上述过程，直到解不再变化或达到最大迭代次数

位于城市$$i$$的第$$k$$只蚂蚁移动到直接可达的城市$$j$$的概率为

$$
p_{ij}^k = \frac{(\tau_{ij})^\alpha (\eta_{ij})^\beta}{\sum_{l \in allowed} (\tau_{il})^\alpha (\eta_{il})^\beta}
$$

其中$$\tau_{ij}$$为城市$$i$$到城市$$j$$的信息素浓度，浓度越大概率越大；$$\eta_{ij}=\frac{1}{d_{ij}}$$为城市$$i$$到城市$$j$$的启发式信息，距离越远概率越小；$$\alpha$$和$$\beta$$为参数，控制信息素浓度和启发式信息的重要程度；$$allowed$$为蚂蚁$$k$$从城市$$i$$出发可以直接到达且未访问过的城市集合。

更新城市$$i$$到城市$$j$$的信息素浓度的公式为

$$
\begin{aligned}
\tau_{ij} &= \rho\tau_{ij} + \Delta \tau_{ij} &\rho\text{反映信息素的挥发速度} \\
\Delta \tau_{ij} &= \sum_{k=1}^m \Delta \tau_{ij}^k &m \text{为蚂蚁数量} \\
\Delta \tau_{ij}^k &= \begin{cases}
Q/L_k & \text{蚂蚁}k\text{经过路径}(i,j) \\
0 & \text{蚂蚁}k\text{未经过路径}(i,j)
\end{cases}&Q\text{为常数，}L_k\text{为蚂蚁}k\text{经过的路径长度}
\end{aligned}
$$

一般蚂蚁个数不超过节点/城市的个数

### 粒子群算法

粒子群算法适用于连续空间搜索，如函数优化问题。通常有一个适应度函数$$(x)$$，用于评判当前位置解的好坏，每个粒子都有一个速度$$v$$和位置$$x$$，其中$$x$$是问题可能的解，$$v$$是粒子在解空间中的移动速度，也可以理解为移动方向和步长。粒子群算法的基本思想是多个粒子在解空间中随机移动求解问题，记录每个粒子的历史最优解（根据适应度函数）以及全局最优解，每个粒子的移动速度由历史最优解和全局最优解决定，每次迭代更新粒子的位置和速度，直到解不再变化或达到最大迭代次数。

$$
\begin{aligned}
v_i^{t+1} &= v_i^t + c_1r_1(p_i^t - x_i^t) + c_2r_2(g^t - x_i^t) \\
x_i^{t+1} &= x_i^t + v_i^{t+1}= x_i^t + \underbrace{v_i^t}_{\text{惯性}} + \underbrace{c_1r_1(p_i^t - x_i^t)}_{\text{记忆项}} + \underbrace{c_2r_2(g^t - x_i^t)}_{\text{社会项}} \\
\end{aligned}
$$

其中$$i$$为粒子编号，$$t$$为迭代次数，$$v_i^t$$为粒子$$i$$在$$t$$时刻的速度，$$x_i^t$$为粒子$$i$$在$$t$$时刻的位置，$$p_i^t$$为粒子$$i$$在$$t$$时刻的历史最优位置，$$g^t$$为全局最优位置，$$c_1$$和$$c_2$$为常数，$$r_1$$和$$r_2$$为随机数。

### [遗传算法](/blog/2023/search/#genetic-algorithms-遗传算法)
