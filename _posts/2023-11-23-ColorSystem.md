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

### Digital Color Systems

#### YIQ

The YIQ color system is used in NTSC television broadcasting. In YIQ, $$Y$$ component represents the luma information, and is the only component used by black-and-white television receivers. $$I$$ and $$Q$$ components represent the chrominance information, $$I$$ stands for in-phase, and $$Q$$ stands for quadrature. 

To convert from RGB to YIQ, the following formula is used:

$$
\begin{bmatrix}
Y\\
I\\
Q
\end{bmatrix}
=
\begin{bmatrix}
0.299 & 0.587 & 0.114\\
0.596 & -0.274 & -0.322\\
0.211 & -0.523 & 0.312
\end{bmatrix}
\begin{bmatrix}
R\\
G\\
B
\end{bmatrix}
$$

To convert from YIQ to RGB, the following formula is used:

$$
\begin{bmatrix}
R\\
G\\
B
\end{bmatrix}
=
\begin{bmatrix}
1 & 0.956 & 0.621\\
1 & -0.272 & -0.647\\
1 & -1.106 & 1.703
\end{bmatrix}
\begin{bmatrix}
Y\\
I\\
Q
\end{bmatrix}
$$

#### YCbCr

YCbCr color spaces are defined by a mathematical coordinate transformation from an associated RGB primaries and white point. Y stands for luma, Cb stands for blue-difference chroma, and Cr stands for red-difference chroma. To convert from RGB to YCbCr, the following formula is used:

$$
\begin{bmatrix}
Y\\
Cb\\
Cr
\end{bmatrix}
=
\begin{bmatrix}
16\\
128\\
128
\end{bmatrix}
+
\begin{bmatrix}
65.481 & 128.553 & 24.966\\
-37.797 & -74.203 & 112\\
112 & -93.786 & -18.214
\end{bmatrix}
\begin{bmatrix}
R\\
G\\
B
\end{bmatrix}
/256(about)
$$


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

The disadvantage of the RGB color system and the CMY(K) color system is that they are not easy to understand for humans. Usually, humans describe colors using hue, saturation, and brightness. Hue is the category of the color, saturation is the purity of the color, and brightness is the amount of light reflected by the color. Accordingly, there are several color systems that are designed to be more intuitive for humans, such as HSL, HSV, and HSI.

#### HSI

The HSI color model represents every color with three components: hue (H), saturation (S), and intensity (I). The hue component is a value between 0 and 360, 0 being red, 120 being green, and 240 being blue. 

$$
H = \left\{
\begin{aligned}
\theta &\text{ if } B \le G\\
360 - \theta &\text{ if } B > G
\end{aligned}
\right.
$$

$$
\theta = \arccos\left(\frac{\frac{1}{2}[(R - G) + (R - B)]}{\sqrt{(R - G)^2 + (R - B)(G - B)}}\right)
$$

$$
S = 1 - \frac{3}{R + G + B} \times \min(R, G, B)
$$

$$
I = \frac{1}{3}(R + G + B)
$$

To convert from HSI to RGB:

- If $$H \in [0, 120]$$, then

$$
\begin{aligned}
B &= I(1 - S)\\
R &= I\left[1 + \frac{S\cos(H)}{\cos(60 - H)}\right]\\
G &= 3I - (R + B)
\end{aligned}
$$

- If $$H \in [120, 240]$$, then

$$
\begin{aligned}
H &= H - 120\\
R &= I(1 - S)\\
G &= I\left[1 + \frac{S\cos(H)}{\cos(60 - H)}\right]\\
B &= 3I - (R + G)
\end{aligned}
$$

- If $$H \in [240, 360]$$, then

$$
\begin{aligned}
H &= H - 240\\
G &= I(1 - S)\\
B &= I\left[1 + \frac{S\cos(H)}{\cos(60 - H)}\right]\\
R &= 3I - (G + B)
\end{aligned}
$$

<div>{% include figure.html path="assets/img/image-processing/HSI.png" class="img-fluid rounded z-depth-1" %}</div>

#### HSV

An HSV color model is the most accurate color model as long as the way humans perceive colors. How humans perceive colors is not like how RGB or CMYK make colors. They are just primary colors fused to create the spectrum. The H stands for Hue, S stands for Saturation, and the V stand for value. 