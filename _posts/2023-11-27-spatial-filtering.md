---
layout: post
title: Spatial Filtering
date: 2023-10-10 01:00:00-0400
description: An introduction to spatial filtering in image processing.
tags: spatial-filtering
categories: image-processing
related_posts: false
giscus_comments: true
thumbnail: 
toc:
  sidebar: left
---

## What is Spatial Filtering?

The spatial domain enhancement is based on pixels in a small range (neighbor). This means the transformed intensity is determined by the gray values of those points within the neighborhood, and thus the spatial domain enhancement is also called neighborhood operation or neighborhood processing.

A digital image can be viewed as a two-dimensional function, $$f(x, y)$$, where $$x$$ and $$y$$ are spatial coordinates. The value of $$f$$ at any point $$(x, y)$$ is called the intensity or gray level of the image at that point. The filtering operation based on the values of $$f(x, y)$$ in the neighborhood of $$(x, y)$$ is called spatial filtering.