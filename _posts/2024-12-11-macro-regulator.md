---
layout: post
title: Reinforcement Learning Policy as Macro Regulator Rather than Macro Placer
date: 2024-12-11 00:00:00-0400
description:
tags: chip RL
categories: paper-reading
related_posts: false
---

## Introduction

这篇文章提出了一个在现有布局结果上重排的优化方法，聚焦的主要问题是现有方法只优化HPWL，可能会使macro靠近chip中心，远离边缘，其实是一种过拟合的不合理的现象，所以实质上是在给奖励函数打补丁。另外这篇工作在现有工具上量化了PPA性能，更贴近实际工程应用。

{% include figure.liquid loading="eager" path="assets/img/paper_reading/regulator_res.png" class="img-fluid rounded z-depth-1" %}

## Methodology

所谓的regulator其实就是度量macro距离chip边缘的距离，越靠近边缘regularity越小，优化目标就是HPWL + regularity。

{% include figure.liquid loading="eager" path="assets/img/paper_reading/regulator_overview.png" class="img-fluid rounded z-depth-1" %}

## Experiment