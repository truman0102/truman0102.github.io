---
layout: post
title: Reinforcement Learning
date: 2023-09-01 00:00:00-0400
description: An tutorial for reinforcement learning
tags: RL tutorial
categories: reinforcement-learning
related_posts: false
featured: true
giscus_comments: true
thumbnail: assets/img/reinforcement_learning/rl.png
---

# Reinforcement Learning

The goal of this tutorial is to provide a brief introduction to reinforcement learning. We will cover the basic concepts of reinforcement learning and some of the most popular algorithms. The tutorial is organized as follows:

## Introduction

Reinforcement learning is a branch of machine learning that deals with sequential decision making. It is a learning paradigm that is inspired by the way humans learn to interact with the environment. In reinforcement learning, an agent interacts with the environment by taking actions and receiving rewards. The agent's goal is to learn a policy that maximizes the cumulative reward. Different from supervised learning, reinforcement learning does not label the data. Instead, it learns from the feedback of the environment. Besides, the feedback is often delayed, which makes the problem more challenging.

## Basic Concepts

Some of the basic concepts in reinforcement learning are as follows:

- **Agent**: The agent is the learner or decision maker. It interacts with the environment by taking actions and receiving rewards.
- **Environment**: The environment is the world in which the agent lives. It is often modeled as a Markov decision process.
- **State** ($$S$$): The state is a representation of the environment. It is often modeled as a node in a Markov decision graph or the tree of a Markov decision process. A state can be fully observable or partially observable. And it can be discrete or continuous, also can be a single value or a vector.
- **Action** ($$a$$): The action is the decision made by the agent. It can be discrete if the action set is finite, or continuous if the action space is continuous.
- **Reward** ($$r$$): The reward is the feedback from the environment. It is a scalar value that indicates how good the action is. The goal of the agent is to maximize the cumulative reward. Given a state $$s$$ and an action $$a$$, the reward is defined as $$r(s, a)$$.
- **Policy** ($$\pi$$): The policy is the strategy that the agent uses to select actions. It is a mapping from states to actions. The goal of the agent is to learn a policy that maximizes the cumulative reward. The policy can be deterministic or stochastic. A deterministic policy is a mapping from states to actions $$a^{*} = \arg \max_{a} \pi(s, a)$$, while a stochastic policy is a probability distribution over actions $$\pi(a\vert s)=p(a_t=a\vert s_t=s)$$.
- **Value Function**: The value function is a function that estimates how good a state or an action is. It is often used to evaluate the policy. If the value function is defined for states, it is called the state-value function, denoted as $$V(s)$$, which is the expected cumulative reward starting from state $$s$$. If the value function is defined for actions, it is called the action-value function, denoted as $$Q(s, a)$$, which is the expected cumulative reward starting from state $$s$$, taking action $$a$$.

### Agent

Value-based agents, policy-based agents, and actor-critic agents are three types of agents in reinforcement learning. Value-based agents learn the value function and use it to select actions. Policy-based agents learn the policy directly without learning the value function. Actor-critic agents learn both the policy and the value function.

For value-based agents, the policy is derived from the value function. The agent selects the action with the highest value. If the environment is discrete, the agent can use a `q-table` to store the value function. If the environment is continuous, the agent can use a function approximator to estimate the value function. Algorithms such as Q-learning and SARSA are value-based agents.

If the agent knows the transition probability $$p(s'\vert s, a)$$ and the reward function $$r(s, a)$$, it is called a model-based agent. If the agent does not know the transition probability and the reward function, it is called a model-free agent. `Q-learning` and `SARSA` are common model-free agents. Actually, most of the reinforcement learning algorithms are model-free agents.

### Markov Decision Process

$$
p(s_{t+1}\vert s_t) = \sum_a p(s_{t+1}\vert s_t, a) \pi(a\vert s_t)
$$

$$
p(\tau \vert \pi) = p(s_0) \prod_{t=0}^{\infty} p(s_{t+1}\vert s_t, a_t) \pi(a_t\vert s_t)
$$

### Markov Reward Process

A trajectory $$\tau$$ of a Markov decision process is a sequence of state, action, and reward. It is defined as $$\tau = (S_0, A_0, R_1, S_1, A_1, R_2, S_2, \cdots)$$, where $$S_t$$ is the state at time $$t$$, $$A_t$$ is the action at time $$t$$, and $$R_{t+1}$$ is the reward of State $$S_t$$ and Action $$A_t$$. 

$$
R_{t+1} = r(S_t, A_t)
$$

The reward of a trajectory is defined as the sum of the rewards of each step. It is defined as 

$$R(\tau) = \sum_{t=0}^{\infty} R_{t+1}$$

, which is undiscounted. If the reward is discounted, it is defined as 

$$G_{t:t+n} = \sum_{k=0}^{n-1} \gamma^k R_{t+k+1}$$

, where $$\gamma$$ is the discount factor.

### Value Function

$$
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}
$$

$$
G_t = R_{t+1} + \gamma G_{t+1}
$$

$$
V(s) = \mathbb{E}[G_t\vert S_t=s]
$$

$$
Q(s, a) = \mathbb{E}[G_t\vert S_t=s, A_t=a]
$$

$$
V(s) = \sum_a \pi(a\vert s) Q(s, a)
$$

### Bellman Equation

$$
V(s) = \mathbb{E}[G_t\vert S_t=s] = \mathbb{E}[R_{t+1} + \gamma V(S_{t+1})\vert S_t=s] = \sum_a \pi(a\vert s) \sum_{s'} p(s'\vert s, a) [r(s, a) + \gamma V(s')]
$$