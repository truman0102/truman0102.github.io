---
layout: post
title: Color System
date: 2023-11-23 00:00:00-0400
description: An introduction to color systems in image processing.
tags: IMGP
categories: image-processing
related_posts: false
thumbnail:
giscus_comments: true
toc:
  sidebar: left
---

## What is a Color System?

A color system is a way of representing colors in an image. There are two types of color systems: additive and subtractive. Additive color systems are used for displaying colors on a screen, while subtractive color systems are used for printing colors on paper. The most common color systems are RGB, CMYK, and HSV.

The properties that distinguish different color usually brightness, hue, and saturation. Brightness is the amount of light reflected by the color, hue is the color of the light reflected, and saturation is the purity of the color. The more white light is added to a color, the less saturated the color is.

## Categories of Color Systems

### Additive Color Systems

#### RGB

In RGB color system, each color is represented by a combination of red, green, and blue. The value of each color ranges from 0 to 255. For example, the color red is represented by `(255, 0, 0)`, while the color white is represented by `(255, 255, 255)`, and the color black is represented by `(0, 0, 0)`.

Below is cubical representation of the RGB color system, where each axis represents a color (red, green, and blue). The color white is at the center of the cube, while the color black is at the origin of the cube, and the color white is at the opposite corner of the cube. The other three corners of the cube represent the secondary colors: cyan, magenta, and yellow.

<div>{% include figure.html path="assets/img/image-processing/RGB.png" class="img-fluid rounded z-depth-1" %}</div>

### Subtractive Color Systems

#### CMY

As mentioned above, cyan, magenta, and yellow are the secondary colors in the RGB color system, standing for C, M, and Y in the CMY color system. The CMY color system is a subtractive color system, which means that the more colors are added, the darker the color becomes, as C, M, and Y can be calculated as follows:

$$
\begin{bmatrix}
C\\
M\\
Y
\end{bmatrix}
=
\begin{bmatrix}
1\\
1\\
1
\end{bmatrix}
-
\begin{bmatrix}
R\\
G\\
B
\end{bmatrix}
$$

where all the values are in the range of 0 to 1 ($$p/255$$).

It is worth noting that the surface of pure cyan/magenta/yellow does not reflect red/green/blue light.

#### CMYK

In practice, C, M and Y inks are usually not pure, and the color black is usually added to the ink to make the color darker. The CMYK color system is a subtractive color system that uses cyan, magenta, yellow, and black to represent colors. To convert from CMY to CMYK, the following formula is used:

1. Let $$K$$ be the minimum of $$C$$, $$M$$, and $$Y$$, $$K = min(C, M, Y)$$.
2. If $$K = 1$$, then $$C = M = Y = 0$$. Otherwise, 
$$
\begin{aligned}
C &= \frac{C - K}{1 - K}\\
M &= \frac{M - K}{1 - K}\\
Y &= \frac{Y - K}{1 - K}
\end{aligned}
$$

To convert from CMYK to CMY, the following formula is used:

$$
\begin{aligned}
C &= C \times (1 - K) + K\\
M &= M \times (1 - K) + K\\
Y &= Y \times (1 - K) + K
\end{aligned}
$$

Note that all the values above are in the range $$[0, 1]$$.

### Other Color Systems

#### HSL

HSL stands for Hue, Saturation, and Lightness.

#### HSV

HSV stands for Hue, Saturation, and Value, also known as HSB (Hue, Saturation, and Brightness).

#### HSI

