---
layout: post
title: Object Recognition
date: 2024-05-25 00:00:00-0400
description:
tags: DL CV
categories: deep-learning computer-vision
related_posts: false
giscus_comments: false
toc:
    sidebar: left
---

## Introduction

Object recognition is a computer vision task that involves identifying and classifying objects in images or videos. It is a fundamental problem in computer vision and has many applications, such as image retrieval, image annotation, and object tracking.


## Metrics

### Intersection over Union (IoU)

Intersection over Union (IoU) is a metric used to evaluate the performance of an object detection algorithm. It is calculated as the ratio of the area of the intersection of the predicted bounding box and the ground truth bounding box to the area of their union. The IoU value ranges from 0 to 1, where 0 indicates no overlap between the predicted and ground truth bounding boxes, and 1 indicates perfect overlap.

$$
IoU = \frac{A \cap B}{A \cup B}
$$

where $A$ is the area of the predicted bounding box and $B$ is the area of the ground truth bounding box. Usually, a threshold value of 0.5 is used to determine whether a predicted bounding box is considered a true positive or a false positive.

### Mean Average Precision (mAP)

## Models

### R-CNN

R-CNN (Region-based Convolutional Neural Network) is a deep learning model for object detection that consists of two main components: a region proposal network (RPN) and a region-based CNN. The RPN generates candidate object bounding boxes, and the region-based CNN classifies and refines these bounding boxes.

### YOLO

### SSD