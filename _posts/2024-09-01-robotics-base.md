---
layout: post
title: Fundamentals of Robotics
date: 2024-09-01 00:00:00-0400
description: An introduction to the basics of robotics.
tags: 
categories: 
related_posts: false
giscus_comments: true
thumbnail: 
toc:
  beginning: true
---

## Foundations of Robot Motion

### Degrees of Freedom

### Configuration Space

### Velocity Constraints

### Task Space and Workspace

### Rotation Matrices

Given two coordinate frames, the rotation matrix $$R$$ transforms a vector from one frame to another. The rotation matrix is orthogonal, meaning that $$R^T = R^{-1}$$, and has a determinant of 1. The rotation matrix can be used to rotate a vector in 3D space. A possible representation of c-coordinate frame $$C$$ with respect to the s-coordinate frame $$S$$ is given by:

$$
R_{sc} = \begin{bmatrix}
r_{11} & r_{12} & r_{13} \\
r_{21} & r_{22} & r_{23} \\
r_{31} & r_{32} & r_{33}
\end{bmatrix} = \begin{bmatrix}
r_1 \\
r_2 \\
r_3
\end{bmatrix}
$$

where the columns or rows of the matrix represent the basis vectors of the rotated frame, and the inverse of the matrix represents the rotation from the rotated frame back to the original frame $$R_{cs} = R_{sc}^{-1}$$. This transfer mode of the rotation matrix is transitive, meaning that $$R_{sc} = R_{s\cancel{b}}R_{\cancel{b}c}$$. A position vector $$p$$ in the rotated frame can be transformed to the original frame by:

$$
p_s = R_{sc}p_c
$$

The rotation matrix can be used to rotate a vector $$v$$ from the original frame to the rotated frame while preserving the magnitude of the vector:

$$
v_{rotated} = Rv, \quad \Vert v_{rotated} \Vert = \Vert v \Vert
$$

### Rotations and Exponential Coordinates

Rotations can be represented by 3-element vectors, given normalized rotation axis $$\hat{\omega}$$ and rotation angle $$\theta$$. The rotation matrix can be expressed as:

$$
\omega = \theta\hat{\omega}
$$

If a vector $$p(0)$$ is rotated by an angle $$\theta$$ about the axis $$\hat{\omega}$$, the rotated vector $$p(\theta)$$ can be expressed as:

$$
p(\theta) = \exp([\hat{\omega}]\theta)p(0)
$$

where the skew-symmetric matrix $$[\hat{\omega}]$$ is defined as:

$$
[\hat{\omega}] = \begin{bmatrix}
0 & -\omega_z & \omega_y \\
\omega_z & 0 & -\omega_x \\
-\omega_y & \omega_x & 0
\end{bmatrix}
$$

It can be shown as following, known as the Rodrigues' rotation formula:

$$
Rot(\hat{\omega}, \theta) = I + \sin(\theta)[\hat{\omega}] + (1 - \cos(\theta))[\hat{\omega}]^2
$$

### Homogeneous Transformations

Homogeneous transformations are used to represent the position and orientation of one frame relative to another. The homogeneous transformation matrix $$T$$ is a 4x4 matrix that combines a rotation matrix $$R$$ and a translation vector $$p$$:

$$
T_{4\times 4} = \begin{bmatrix}
R_{3\times 3} & p_{3\times 1} \\
0_{1\times 3} & 1
\end{bmatrix}
$$

Usually $$T_{sc}$$ represents the position and orientation of the coordinate frame $$C$$ with respect to the coordinate frame $$S$$, where $$p$$ is the position of the origin of the frame $$C$$ with respect to the frame $$S$$, and $$R_{sc}$$ is the rotation matrix that represents the orientation of the frame $$C$$ with respect to the frame $$S$$. The inverse of $$T_{sc}$$ is the transformation matrix that represents the position and orientation of the frame $$S$$ with respect to the frame $$C$$, with inverse rotation matrix $$R_{cs} = R_{sc}^T$$ and inverse translation vector $$p_{cs} = -R_{sc}^Tp_{sc}$$:

$$
T^{-1} = \begin{bmatrix}
R^T & -R^Tp \\
0 & 1
\end{bmatrix}
$$

The multiplication of two homogeneous transformation matrices is equivalent to the composition of the transformations they represent:

$$
T_{ab} = T_{a\cancel{c}}T_{\cancel{c}b}
$$

To transform a position vector $$p$$ from one frame to another, the position vector is augmented with a 1 to form a 4x1 vector, and the transformation matrix is used to transform the vector:

$$
\begin{bmatrix}
p_s \\
1
\end{bmatrix} = T_{sc}\begin{bmatrix}
p_c \\
1
\end{bmatrix}
$$

To displace a vector or a frame given the rotation axis $$\hat{\omega}$$, rotation distance $$\theta$$, and the translation vector $$p$$, the exponential coordinates for homogeneous transformations can be used:

$$
T = Trans(p)Rot(\hat{\omega}, \theta)
$$

### Twist Coordinates

A twist is a 6-element vector consisting of a 3-vector expressing the angular velocity and a 3-vector expressing the linear velocity. Both of them are expressed in the same coordinate frame and the linear velocity refers to the linear velocity of a point at the origin of the frame. 

$$
S = (S_{\omega}, S_v),\quad \Vert S_{\omega} \Vert = 1\;\text{or}\;\Vert S_v \Vert = 1\;\&\;S_{\omega} = 0
$$

Body twist and spatial twist are two types of twists. The body twist is expressed in the body frame, while the spatial twist is expressed in the space frame.

To transform a twist from one frame to another, a $$6\times 6$$ adjoint matrix is used:

$$
\begin{bmatrix}
R & 0 \\
[p]R & R 
\end{bmatrix}
$$