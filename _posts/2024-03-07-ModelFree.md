---
layout: post
title: Model Free Reinforcement Learning
date: 2024-03-07 00:00:00-0400
description: An introduction to model free reinforcement learning
tags: rl
categories: reinforcement-learning
related_posts: false
giscus_comments: false
toc:
    sidebar: left
---

## Introduction

Model-free reinforcement learning is a type of reinforcement learning where the agent learns from interacting with the environment without knowing the dynamics of the environment, in other words, without knowing the transition probabilities and the reward function. The agent learns from the experiences it collects by interacting with the environment, usually by learning the value function or the policy. Model-free reinforcement learning is further divided into two categories: policy-based methods and value-based methods.

## Monte Carlo Methods

Monte Carlo methods are a type of model-free reinforcement learning methods that learn from complete episodes. In Monte Carlo methods, the agent learns from the complete episode by updating the value function at the end of the episode, estimating the value of the state-action pair by averaging the returns from the state-action pair. The value function is updated using the following formula:

$$
V(S_t) \leftarrow V(S_t) + \alpha(G_t - V(S_t))
$$

Where $$V(S_t)$$ is the value of the state $$S_t$$, $$G_t$$ is the return from the state $$S_t$$, and $$\alpha$$ is the learning rate, sometimes the learning rate is replaced by the step size $$\frac{1}{N(S_t)}$$ where $$N(S_t)$$ is the number of times the state $$S_t$$ has been visited.

## Temporal Difference Learning

Temporal difference learning is another type of model-free reinforcement learning methods that learn from incomplete episodes. In temporal difference learning, the agent learns from each or a sequence of states by updating the value function at each state, estimating the value of the state-action pair by bootstrapping the value of the next state-action pair. The value function is updated using the following formula:

$$
V(S_t) \leftarrow V(S_t) + \alpha(R_{t+1} + \gamma V(S_{t+1}) - V(S_t))
$$

Where $$V(S_t)$$ is the value of the state $$S_t$$, $$R_{t+1}$$ is the reward from the state $$S_t$$ to the state $$S_{t+1}$$, $$\gamma$$ is the discount factor, and $$\alpha$$ is the learning rate.

The advantage of temporal difference learning over Monte Carlo methods is that temporal difference learning can learn from incomplete episodes, and it can learn online, meaning that it can learn while interacting with the environment. Besides, temporal difference learning has lower variance than Monte Carlo methods, and it can learn from an infinite number of states and actions.

Advanced temporal difference learning methods learn from several states and actions, and they are called n-step methods, where n is the number of states and actions the agent learns from. If n is close to infinity, the method becomes a Monte Carlo method, and if n is close to 1, the method becomes a one-step method.

$$
\begin{aligned}
n=1: & V(S_t) \leftarrow V(S_t) + \alpha(R_{t+1} + \gamma V(S_{t+1}) - V(S_t)) \\
n=2: & V(S_t) \leftarrow V(S_t) + \alpha(R_{t+1} + \gamma R_{t+2} + \gamma^2 V(S_{t+2}) - V(S_t)) \\
\vdots \\
n=\infty: & V(S_t) \leftarrow V(S_t) + \alpha(G_t - V(S_t))
\end{aligned}
$$

## Generalized Policy Iteration

Generalized policy iteration is a framework that combines policy evaluation and policy improvement. In generalized policy iteration, the agent learns the action-value function or the q-value function other than the value function since the transition probabilities are unknown.

Greedy policy improvement is used to improve the policy by selecting the action with the highest value. To explore the environment, an $$\epsilon$$-greedy policy is used, where the agent selects the action with the highest value with a probability of $$1-\epsilon$$ and selects a random action with a probability of $$\epsilon$$.

Monte Carlo methods with $$\epsilon$$-greedy policy improvement are called Monte Carlo control, and temporal difference learning with $$\epsilon$$-greedy policy improvement is called Q-learning. It can be proved that monte carlo control is guaranteed to converge to the optimal policy:

$$
\begin{aligned}
Q_{\pi}(S,\pi^{\prime}(S)) &= \sum_{a} \pi^{\prime}(a|S) Q_{\pi}(S,a) \\
&= \frac{\epsilon}{\vert A\vert} \sum_{a} Q_{\pi}(S,a) + (1-\epsilon) \max_{a} Q_{\pi}(S,a) \\
&\geq \frac{\epsilon}{\vert A\vert} \sum_{a} Q_{\pi}(S,a) + (1-\epsilon) \sum_{a} \frac{\pi(a|S) - \frac{\epsilon}{\vert A\vert}}{1-\epsilon} Q_{\pi}(S,a) \\
&= \sum_{a} \pi(a|S) Q_{\pi}(S,a)\\
&= V_{\pi}(S)
\end{aligned}
$$

### Sarsa

Sarsa is an on-policy temporal difference learning method that learns the action-value function. Sarsa learns the action-value function by interacting with the environment and updating the action-value function at each state-action pair. The action-value function is updated using the following formula:

$$
Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha(R_{t+1} + \gamma Q(S_{t+1},A_{t+1}) - Q(S_t,A_t))
$$

Where $$Q(S_t,A_t)$$ is the action-value function of the state-action pair $$(S_t,A_t)$$, $$R_{t+1}$$ is the reward from the state-action pair $$(S_t,A_t)$$ to the state-action pair $$(S_{t+1},A_{t+1})$$, $$\gamma$$ is the discount factor, and $$\alpha$$ is the learning rate.

If replacing the reward of the next step with the reward of several steps, the method becomes an n-step Sarsa method.

### Q-learning

Q-learning is an off-policy temporal difference learning method that learns the action-value function. The difference between Q-learning and Sarsa is that Q-learning repalces the next action with the action with the highest value. The action-value function is updated using the following formula:

$$
Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha(R_{t+1} + \gamma \max_{a} Q(S_{t+1},a) - Q(S_t,A_t))
$$

Know more about Q-learning and Deep Q-Networks (DQN) in the next [post](/blog/2024/QLearning).
