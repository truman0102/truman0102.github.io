---
layout: post
title: Advanced Q-Learning
date: 2024-03-08 00:00:00-0400
description: An introduction to Q-Learning and its advanced concepts.
tags: rl
categories: reinforcement-learning
related_posts: false
giscus_comments: false
toc:
    sidebar: left
---

## Introduction

Q-Learning is a model-free reinforcement learning algorithm that is used to find the optimal action-selection policy for any given finite Markov decision process (MDP). It is a value-based algorithm that uses the Q-function to find the optimal policy. The Q-function is a function that takes a state and an action as input and returns the expected cumulative reward for taking that action in that state and following the optimal policy thereafter. Temporal difference learning is used to update the Q-function iteratively.

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \max_a Q(s_{t+1}, a) - Q(s_t, a_t) \right]
$$

It is worth noting that Q-Learning is an off-policy algorithm, meaning that it learns the optimal policy independently of the policy being followed. This is in contrast to on-policy algorithms like SARSA, which learn the value of the policy being followed.

In this post, we will discuss some advanced concepts in Q-Learning, including:

- Double Q-Learning
- Deep Q-Networks
- Double DQN
- Dueling DQN
- Prioritized Experience Replay
- Noisy Nets
- $$\dots$$

## Double Q-Learning
