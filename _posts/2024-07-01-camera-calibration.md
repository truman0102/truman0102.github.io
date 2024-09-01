---
layout: post
title: Camera Calibration and 3D Reconstruction
date: 2024-07-01 00:00:00-0400
description: An introduction to camera calibration and 3D reconstruction, including the theory and practical implementation.
tags: 
categories: image-processing
related_posts: false
giscus_comments: true
thumbnail: 
toc:
  sidebar: left
---

## Introduction
Camera calibration is the process of estimating the intrinsic and extrinsic parameters of a camera, which are used to describe how a 3D point in the world is projected onto a 2D image. The intrinsic parameters include the focal length, principal point, and lens distortion, while the extrinsic parameters include the rotation and translation of the camera with respect to the world coordinate system.

In this post, we will discuss the theory behind camera calibration and 3D reconstruction, as well as the practical implementation using Python.

## Definitions
- World Coordinate System $(X_w, Y_w, Z_w)$: The 3D coordinate system in the real world.
- Camera Coordinate System $(X_c, Y_c, Z_c)$: The 3D coordinate system of the camera.
- Image Coordinate System $(u, v)$: The 2D coordinate system of the image.
- Pixel Coordinate System $(x, y)$: The discrete 2D coordinate system of the image.
- Extrinsic Parameters: The 3$\times$4 transformation matrix that describes the rotation and translation of the camera with respect to the world coordinate system. It is denoted as $[R\vert t]\in\mathbb{R}^{3\times 4}$, where $R$ is the 3$\times$3 rotation matrix indicating the orientation of the camera, and $t$ is the 3$\times$1 translation vector indicating the position of the camera. The extrinsic matrix can be decomposed into a rotation matrix and a translation matrix.

$$
[R\vert t] = [I\vert t]\begin{bmatrix}
R & 0 \\
0 & 1
\end{bmatrix}
= \underbrace{\begin{bmatrix}
1 & 0 & 0 & t_x \\
0 & 1 & 0 & t_y \\
0 & 0 & 1 & t_z
\end{bmatrix}}_{\text{Translation Matrix}}
\underbrace{\begin{bmatrix}
r_{11} & r_{12} & r_{13} & 0 \\
r_{21} & r_{22} & r_{23} & 0 \\
r_{31} & r_{32} & r_{33} & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}}_{\text{Rotation Matrix}}
$$

- Intrinsic Parameters: The 3$\times$3 matrix that describes the internal characteristics of the camera, where $f_x$ and $f_y$ are the focal lengths in the $x$ and $y$ directions, and $(c_x, c_y)$ is the principal point. Let $F$ be the focal length in world units, $f$ be the focal length in pixels, and $p$ be the pixel size in world units. Then, $f = F/p$.

$$
\begin{aligned} 
K & =
\begin{bmatrix}
f_x & s & c_x \\
0 & f_y & c_y \\
0 & 0 & 1
\end{bmatrix} \\&=
\underbrace{\begin{bmatrix}
1 & 0 & c_x \\
0 & 1 & c_y \\
0 & 0 & 1
\end{bmatrix}}_{\text{2D Translation}}
\underbrace{\begin{bmatrix}
f_x & 0 & 0 \\
0 & f_y & 0 \\
0 & 0 & 1
\end{bmatrix}}_{\text{2D Scaling}}
\underbrace{\begin{bmatrix}
1 & \frac{s}{f_x} & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}}_{\text{2D Shear}}\\
&=
\underbrace{\begin{bmatrix}
1 & 0 & c_x \\
0 & 1 & c_y \\
0 & 0 & 1
\end{bmatrix}}_{\text{2D Translation}}
\underbrace{\begin{bmatrix}
1 & \frac{s}{f_y} & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}}_{\text{2D Shear}}
\underbrace{\begin{bmatrix}
f_x & 0 & 0 \\
0 & f_y & 0 \\
0 & 0 & 1
\end{bmatrix}}_{\text{2D Scaling}}
\end{aligned}
$$

where $c_x = c_y = 0$ for no translation, $s = 0$ for no shear.

## Calculation

The projection of a 3D point $(X_w, Y_w, Z_w)$ in the world coordinate system onto a 2D image $(u, v)$ can be calculated using the following equation:

$$
\begin{bmatrix}
u \\
v \\
w
\end{bmatrix} = 
\underbrace{\begin{bmatrix}
f_x & 0 & c_x & 0 \\
0 & f_y & c_y & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}}_{\text{Intrinsic Matrix}}
\underbrace{\begin{bmatrix}
R_{3\times3} & t_{3\times1} \\
0_{1\times3} & 1
\end{bmatrix}}_{\text{Extrinsic Matrix}}
\begin{bmatrix}
X_w \\
Y_w \\
Z_w \\
1
\end{bmatrix}
$$

where $u$ and $v$ are the pixel coordinates of the image, $f_x$ and $f_y$ are the focal lengths in the $x$ and $y$ directions, $c_x$ and $c_y$ are the principal points, $R$ is the rotation matrix, and $t$ is the translation vector, and $w$ is the scaling factor, which is used to normalize the coordinates to the homogeneous form.

### World to Camera Transformation

The transformation from the world coordinate system to the camera coordinate system can be represented as:

$$
\begin{bmatrix}
X_c \\
Y_c \\
Z_c \\
1
\end{bmatrix} =
\begin{bmatrix}
R_{3\times3} & t_{3\times1} \\
0_{1\times3} & 1
\end{bmatrix}
\begin{bmatrix}
X_w \\
Y_w \\
Z_w \\
1
\end{bmatrix}
$$

### Camera to Image Transformation

According to the pinhole camera model, the projection of a 3D point $(X_c, Y_c, Z_c)$ in the camera coordinate system onto a 2D image $(u, v)$ can be calculated using the following equation:

$$
\begin{bmatrix}
u \\
v \\
1
\end{bmatrix} =
\begin{bmatrix}
f_x & 0 & c_x & 0 \\
0 & f_y & c_y & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
X_c \\
Y_c \\
Z_c \\
1
\end{bmatrix}
$$

### Image to Pixel Transformation

## 3D Reconstruction

With the intrinsic and RGB-D images, we can reconstruct the 3D points in the world coordinate system from the 2D image coordinates. The 3D reconstruction process involves the following steps:



## Summary

### Transfomations

1. **World to Camera**: 3D-3D projection, rotation, scaling, and translation.
2. **Camera to Image**: 3D-2D projection,
3. **Image to Pixel**: 2D-2D projection, continuous to discrete. Quantization and origin shift.
4. Camera **Extrinsic** (World to Camera)
5. Camera **Intrinsic** (Camera to Image, Image to Pixel)