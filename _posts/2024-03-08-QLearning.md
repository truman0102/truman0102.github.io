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
- Noisy Nets
- ...

## Double Q-Learning

Double Q-Learning is an extension of Q-Learning that addresses the overestimation of action values in Q-Learning. In Q-Learning, the memory is double-buffered, and two Q-functions are learned by referring to the other Q-function to compute the target Q-value.

$$
Q_1(s_t, a_t) \leftarrow Q_1(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma Q_2(s_{t+1}, \arg\max_a Q_1(s_{t+1}, a)) - Q_1(s_t, a_t) \right]
$$

where $$Q_1$$ and $$Q_2$$ are two Q-functions, and the target Q-value is computed using the other Q-function after selecting the action with the highest value from current Q-function. $$Q_1$$ and $$Q_2$$ can be swapped.

## Deep Q-Networks

Deep Q-Networks (DQN) is an extension of Q-Learning that uses a neural network to approximate the Q-function. If action space is discrete, the neural network takes the state as input and returns the Q-values for all actions. The neural network is trained using the Q-Learning update rule.

One of the most important method in DQN is experience replay, where the agent stores the experiences in a replay buffer and samples a batch of experiences to train the neural network. Experience replay helps to break the correlation between consecutive experiences and stabilize the training. So DQN is an off-policy algorithm.

Another important trick in DQN is target network, where the agent uses two neural networks, one for the Q-function and the other for the target Q-function. The target network is updated less frequently than the Q-network to stabilize the training. The target network is used to compute the target Q-value, in other words, the value of the next state-action pair when selecting the action with the highest value from the Q-network. Target network can be seen as $$Q_2$$ in [Double Q-Learning](#double-q-learning), which is updated after a certain number of steps.

$$\epsilon$$-greedy policy is used to explore the environment, where the agent selects the action with the highest value with a probability of $$1-\epsilon$$ and selects a random action with a probability of $$\epsilon$$.

## Double DQN

Selecting action from frequently updated Q-network and computing target Q-value from less frequently updated target network are basic ideas in Double DQN, in contrast to DQN where both action selection and target Q-value computation are done using the fixed Q-network. In Double DQN, the action is selected from the Q-network, and the target Q-value is computed from the target network.

## Dueling DQN

Dueling DQN regards the Q-function as the sum of the value function and the advantage function, where the value function is the expected cumulative reward for being in a state, and the advantage function is the value of taking an action in that state compared to the average value of all actions in that state. The neural network takes the state as input and returns the value function and the advantage function separately, and the Q-values are computed by adding the value function and the advantage function.

$$
Q(s, a) = V(s) + \underbrace{A(s, a) - \frac{1}{\vert A\vert} \sum_{a^{\prime}} A(s, a^{\prime})}_{\text{advantage function with sum-to-zero constraint}}
$$

where $$V(s)$$ is the value function, $$A(s, a)$$ is the advantage function, and $$\vert A\vert$$ is the number of actions.

## Noisy Nets

Noisy Nets is a method to add noise to the weights of the neural network to encourage exploration. The neural network is trained to learn the mean of the Q-values, and the noise is added to the weights to encourage exploration, using the factorized Gaussian noise, or the independent Gaussian noise.
