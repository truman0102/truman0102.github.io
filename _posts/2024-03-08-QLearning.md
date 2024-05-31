---
layout: post
title: Advanced Q-Learning
date: 2024-03-08 00:00:00-0400
description: An introduction to Q-Learning and its advanced concepts.
tags: RL
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

The Q-learning algorithm is as follows:

1. Initialize $$Q(s,a)$$ arbitrarily
2. Repeat (for each episode):
    1. Initialize $$s$$
    2. Repeat (for each step of episode):
        1. Choose $$a$$ from $$s$$ using policy derived from $$Q$$ (e.g., $$\epsilon$$-greedy)
        2. Take action $$a$$, observe $$r$$, $$s^{\prime}$$
        3. $$Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$$
        4. $$s \leftarrow s'$$
    3. until $$s$$ is terminal or truncated
3. until number of episodes reached or $$Q$$ has converged

In this post, we will discuss some advanced concepts in Q-Learning, including:

- Double Q-Learning
- Deep Q-Networks
- Double DQN
- Dueling DQN
- Noisy Nets
- ...

### Target Network

The problem with DQN is that the neural network is constantly changing, so the target $Q$ is also constantly changing. This makes the training unstable if we use the model to interact with the environment and train at each step.

Let the target network be $\hat{Q}$, and the training network be $Q$. The target network is a copy of the training network, but it is only updated every $C$ steps. The target network is used to calculate the target $Q$ for training, and the training network is used to calculate the current $Q$ for training. Given a state-action pair $(s,a)$, the reward $r$ and the next state $s^{\prime}$, the target network gives the target $\hat{Q}(s,a)$ as follows:

$$
\begin{aligned}
\hat{Q}(s,a) &= r + \gamma \hat{Q}(s^{\prime}, \pi(s^{\prime})) \\
&= r + \gamma \hat{Q}(s^{\prime}, \arg\max_{a^{\prime}} Q(s^{\prime}, a^{\prime})) \\
&= r + \gamma \max_{a^{\prime}} \hat{Q}(s^{\prime}, a^{\prime})
\end{aligned}
$$

And the training network gives the current evaluation $Q(s,a)$ to regress to the target $\hat{Q}(s,a)$. The loss function is the mean squared error between the target and the current evaluation:

$$
\begin{aligned}
L(\theta) &= \mathbb{E}_{(s,a,r,s^{\prime}) \sim U(D)} \left[ \left( \hat{Q}(s,a) - Q(s,a;\theta) \right)^2 \right] \\
&= \mathbb{E}_{(s,a,r,s^{\prime}) \sim U(D)} \left[ \left( r + \gamma \max_{a^{\prime}} \hat{Q}(s^{\prime}, a^{\prime}) - Q(s,a;\theta) \right)^2 \right]
\end{aligned}
$$

where $U(D)$ is the uniform distribution over the experience replay buffer $D$. The experience replay buffer is a finite-sized cache of the most recent experiences, used to store the experiences $(s,a,r,s^{\prime})$ and sample a batch of experiences from it to train the model.

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
