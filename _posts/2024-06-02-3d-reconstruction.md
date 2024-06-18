---
layout: post
title: 3D Reconstruction
date: 2024-06-02 00:00:00-0400
description:
tags: DL CV
categories: deep-learning computer-vision
related_posts: false
giscus_comments: false
toc:
    sidebar: left
---

## Introduction

3D Reconstruction is the task of creating a 3D model or representation of an object or scene from 2D images or other data sources.

The main methods for displaying data include point clouds, voxels, and meshes, which belong to the category of geometric representations and explicitly represent the 3D structure of the scene. On the other hand, neural radiance fields (NeRF) and 3D Gaussian splatting are examples of implicit representations, which model the scene as a continuous function, offering a more flexible and saving-efficient way to represent 3D scenes.

## Point Cloud


## Voxel

## Mesh

## NeRF

The discrete estimation of NeRF is given by the following equation:

$$
\begin{aligned}
\color{red}{\hat{C}(r)} &= \sum_{i=1}^{N} \color{blue}{\omega_i} \color{black}{c_i} \\
\color{blue}{\omega_i} &= \color{green}{T_i}\color{black}{(1-\exp(-\sigma_i \delta_i))} \\
\color{green}{T_i} &= \exp(-\sum_{j=1}^{i-1} \sigma_j \delta_j) \\
\end{aligned}
$$

$\color{red}{\hat{C}(r)}$: This represents the estimated color of a ray, $r$, which aggregates the contribution of colors from different sampled points along the path of the ray observed from a specific viewpoint.

$N$: This is the number of sampled points along the light ray path.

$\color{blue}{\omega_i}$: This is the weight coefficient for the $i$-th sampled point, reflecting the contribution that this point makes to the final estimated color.

$\color{black}{c_i}$: This is the color at the $i$-th sampled point.

$\color{green}{T_i}$: This denotes the accumulated transparency from the start of the ray up to the point just before the $i$-th sample. It encompasses the effects of absorption and scattering of the medium through which the ray travels (i.e., the cumulative extinction effect of the medium from the source up to the current point $i$).

$\sigma_i$: This stands for the density of the medium at the $i$-th sampled point, related to the medium's opacity.

$\delta_i$: This is the distance between the $i$-th sample point and next sample point along the ray, $\delta_i = t_{i+1} - t_i$.

$\exp(-\sigma_i \delta_i)$: This expression represents the attenuation of light intensity as the ray travels through the medium between the $(i-1)$-th and $i$-th points due to absorption by the medium. And $\alpha_i = 1-\exp(-\sigma_i \delta_i)$ is the local transparency at the $i$-th point, which is the proportion of light that is absorbed at that point.

## 3D Gaussian

## References

- [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](http://arxiv.org/abs/2003.08934)
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering](http://arxiv.org/abs/2308.04079)
- [A Comprehensive Review of Vision-Based 3D Reconstruction Methods](https://www.mdpi.com/1424-8220/24/7/2314)
- [CS231A: Computer Vision, From 3D Perception to 3D Reconstruction and beyond](https://web.stanford.edu/class/cs231a/index.html)