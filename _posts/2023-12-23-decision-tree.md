---
layout: post
title: Decision Tree
date: 2023-12-20 23:00:00-0400
description: An introduction to decision trees in Machine Learning.
tags: ML entropy decision-tree math
categories: data-science
related_posts: false
giscus_comments: true
disqus_comments: false
thumbnail: /assets/img/data_science/dt.png
toc:
  beginning: true
---

## Basics

### Entropy

Entropy is a measure of the randomness in the information being processed. It is a measure of the impurity of the data. The higher the entropy, the more the information is disordered. Given a set of data with labels $$y=1,2,3,\dots,C$$, the entropy is given by:

$$
H(Y) = -\sum_{i=1}^{C} p_i \log_2 p_i = -\sum_{i=1}^{C} \frac{N_i}{N} \log_2 \frac{N_i}{N}
$$

where $$p_i$$ is the probability of the $$i^{th}$$ label. The entropy is maximum when all the labels are equally likely:

$$
H_{max}(Y) = -\sum_{i=1}^{C} \frac{1}{C} \log_2 \frac{1}{C} = \log_2 C
$$

### Conditional Entropy

A dataset $$D$$ can be regarded as a collection of data point $$x$$ and its corresponding label $$y$$, $$D_{i=1}^{N} = \{(X_i, y_i)\}$$. The conditional entropy of $$y$$ given $$x$$ is given by:

$$
H(Y|X) = -\sum\limits_{m} p(X=m) \sum_{c=1}^{C} p(Y=c|X=m) \log_2 p(Y=c|X=m)
$$

where $$m$$ represents the unique values of $$X$$ and $$p(X=m)$$ is the probability of $$X$$ taking the value $$m$$, and $$p(Y=c|X=m)$$ is the probability of $$Y$$ taking the value $$c$$ given that $$X$$ takes the value $$m$$. Thus, conditional entropy is a weighted average of the entropy of $$Y$$ given $$X=m$$, where the weights are the probabilities of $$X$$ taking the value $$m$$, describing how uncertain we are about $$Y$$ given a particular value of $$X$$ (usually one of the features).

### Empirical Conditional Entropy

The empirical conditional entropy is the conditional entropy calculated from the data, and is given by replacing the probabilities with their empirical estimates:

$$
H(Y|X) = -\sum\limits_{m} \frac{N_m}{N} \sum_{c=1}^{C} \frac{N_{m,c}}{N_m} \log_2 \frac{N_{m,c}}{N_m}
$$

where $$N_m$$ is the number of data points with $$X=m$$, and $$N_{m,c}$$ is the number of data points with $$X=m$$ and $$Y=c$$.

### Information Gain

The information gain is the difference between the entropy of the labels and the conditional entropy of the labels given a feature. It is a measure of how much information about the labels is gained by knowing the value of the feature. It is given by:

$$
IG(Y|X) = H(Y) - H(Y|X)
$$

The greater the information gain, the more information about the labels is gained by knowing the value of the feature, and the better the feature is at predicting the labels.

### Information Gain Ratio

ID3 chooses the feature with the highest information gain. However, information gain is biased towards features with a large number of values. The information gain ratio is a modification of the information gain that penalizes features with a large number of values, used by C4.5. It is given by:

$$
IGR(Y|X) = \frac{IG(Y|X)}{H(X)}
$$

where $$H(X)$$ is the entropy of the feature. Information gain ratio is biased towards features with a small number of unique values. The smaller the number of unique values, the greater the information gain ratio, and the better the feature is at predicting the labels, as well as having a small number of leaves in the decision tree.

### Gini Impurity

Gini impurity is another measure of the impurity of the data. It is given by:

$$
G(Y) = 1 - \sum_{i=1}^{C} p_i^2 = 1 - \sum_{i=1}^{C} \frac{N_i^2}{N^2}
$$

## Decision Tree

A decision tree is a tree where each node represents a feature, each branch represents a value of the feature, and each leaf represents a label. The tree is constructed by recursively splitting the data into subsets based on the values of the features, until the data is pure (all the data points in the subset have the same label) or the maximum depth is reached. The tree is then used to predict the label of a data point by traversing the tree from the root to a leaf, where the leaf represents the predicted label. 

Each time to split a node, the feature with the highest information gain (for ID3) or information gain ratio (for C4.5) is chosen, and the node is split into branches for each value of the feature, until the data is pure or the maximum depth is reached, which means that all impure features in the subset of the node need to be iterated through to compute their information gain or information gain ratio. This can be computationally expensive, especially when the number of features is large. For continuous features, the values of the feature are sorted, and the split is chosen to be the midpoint between two consecutive values, similar to a binary search. For categorical features, the splitting is regarded as a `One vs. Rest` problem, where the feature is split into two branches, one for the value of the feature and one for the rest of the values of the feature. Some implementations of decision trees split the node into branches for each value of the categorical feature, too.

The target of decision tree is to `minimize the conditional entropy` of the labels given the features, which is equivalent to `maximizing the information gain` or `information gain ratio`.