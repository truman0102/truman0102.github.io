---
layout: post
title: Functional Dependencies
date: 2023-10-18 00:00:00-0400
description: An introduction to functional dependencies in database systems.
tags: functional-dependencies DB
categories: database
pretty_table: true
related_posts: false
giscus_comments: false
toc:
  sidebar: left
---

## What are Functional Dependencies?

Functional dependencies are constraints between two sets of attributes in a relation from a database. The functional dependency is a relationship between two attributes, usually between the primary key and non-key attributes. The functional dependency is denoted by $$X \rightarrow Y$$, where $$X$$ is the determinant and $$Y$$ is the dependent.

### Partial Functional Dependencies

Let FD $$X\rightarrow Y$$ be a functional dependency. $$X\rightarrow Y$$ is a partial functional dependency if there exists a proper subset $$Z$$ of $$X$$ such that $$Z\rightarrow Y$$, otherwise $$X\rightarrow Y$$ is a full functional dependency.

### Transitive Functional Dependencies

Let FD $$X\rightarrow Y$$ and $$Y\rightarrow Z$$ be functional dependencies. $$X\rightarrow Z$$ is a transitive functional dependency if $$Z$$ is not a subset of $$X$$ and $$Y\nrightarrow X$$.

### Trivial Functional Dependencies

Let FD $$X\rightarrow Y$$. If $$Y\subseteq X$$, then $$X\rightarrow Y$$ is a trivial functional dependency, otherwise it is a non-trivial functional dependency.

## Functional Dependency Rules

Armstrong's axioms are a set of inference rules used to infer all the functional dependencies from a given set of functional dependencies. The axioms are as follows:

### Reflexivity

If $$Y \subseteq X$$, then $$X \rightarrow Y$$.

### Augmentation

If $$X \rightarrow Y$$, then $$XZ \rightarrow YZ$$.

### Transitivity

If $$X \rightarrow Y$$ and $$Y \rightarrow Z$$, then $$X \rightarrow Z$$.

### Union

If $$X \rightarrow Y$$ and $$X \rightarrow Z$$, then $$X \rightarrow YZ$$.

### Decomposition

If $$X \rightarrow YZ$$, then $$X \rightarrow Y$$ and $$X \rightarrow Z$$.

### Pseudotransitivity

If $$X \rightarrow Y$$ and $$WY \rightarrow Z$$, then $$WX \rightarrow Z$$.

## Functional Dependency Closure

{::nomarkdown}
{% assign jupyter_path = "assets/jupyter/db/functional_dependency_closure.ipynb" | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/db/functional_dependency_closure.ipynb %}{% endcapture %}
{% if notebook_exists == "true" %}
    {% jupyter_notebook jupyter_path %}
{% else %}
    <p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}

## Lossless Decomposition

A decomposition of a relation is lossless if the original relation can be recovered from the decomposed relations.

Let $$R(A,B,C,D,E)$$, $$F$$ be a set of functional dependencies on $$R$$, and $$F=\left\{A\rightarrow D, E\rightarrow D, D\rightarrow B,BC\rightarrow D,DC\rightarrow A\right\}$$. The relation $$R$$ is decomposed into $$\left\{AB,AE,CE,BCD,AC\right\}$$. A table can be constructed to show the decomposition:

|     | A           | B           | C           | D           | E           |
| --- | ----------- | ----------- | ----------- | ----------- | ----------- |
| AB  | $$a_1$$     | $$a_2$$     | $$b_{1,3}$$ | $$b_{1,4}$$ | $$b_{1,5}$$ |
| AE  | $$a_1$$     | $$b_{2,2}$$ | $$b_{2,3}$$ | $$b_{2,4}$$ | $$a_5$$     |
| CE  | $$b_{3,1}$$ | $$b_{3,2}$$ | $$a_3$$     | $$b_{3,4}$$ | $$a_5$$     |
| BCD | $$b_{4,1}$$ | $$a_2$$     | $$a_3$$     | $$a_4$$     | $$b_{4,5}$$ |
| AC  | $$a_1$$     | $$b_{5,2}$$ | $$a_3$$     | $$b_{5,4}$$ | $$b_{5,5}$$ |

Considering $$A\rightarrow D$$

|     | A           | B           | C           | D                                    | E           |
| --- | ----------- | ----------- | ----------- | ------------------------------------ | ----------- |
| AB  | $$a_1$$     | $$a_2$$     | $$b_{1,3}$$ | <font color='red'>$$b_{1,4}$$</font> | $$b_{1,5}$$ |
| AE  | $$a_1$$     | $$b_{2,2}$$ | $$b_{2,3}$$ | <font color='red'>$$b_{1,4}$$</font> | $$a_5$$     |
| CE  | $$b_{3,1}$$ | $$b_{3,2}$$ | $$a_3$$     | $$b_{3,4}$$                          | $$a_5$$     |
| BCD | $$b_{4,1}$$ | $$a_2$$     | $$a_3$$     | $$a_4$$                              | $$b_{4,5}$$ |
| AC  | $$a_1$$     | $$b_{5,2}$$ | $$a_3$$     | <font color='red'>$$b_{1,4}$$</font> | $$b_{5,5}$$ |

Considering $$E\rightarrow D$$

|     | A           | B           | C           | D                                    | E           |
| --- | ----------- | ----------- | ----------- | ------------------------------------ | ----------- |
| AB  | $$a_1$$     | $$a_2$$     | $$b_{1,3}$$ | $$b_{1,4}$$                          | $$b_{1,5}$$ |
| AE  | $$a_1$$     | $$b_{2,2}$$ | $$b_{2,3}$$ | $$b_{1,4}$$                          | $$a_5$$     |
| CE  | $$b_{3,1}$$ | $$b_{3,2}$$ | $$a_3$$     | <font color='red'>$$b_{1,4}$$</font> | $$a_5$$     |
| BCD | $$b_{4,1}$$ | $$a_2$$     | $$a_3$$     | $$a_4$$                              | $$b_{4,5}$$ |
| AC  | $$a_1$$     | $$b_{5,2}$$ | $$a_3$$     | $$b_{1,4}$$                          | $$b_{5,5}$$ |

Considering $$D\rightarrow B$$

|     | A           | B                                | C           | D           | E           |
| --- | ----------- | -------------------------------- | ----------- | ----------- | ----------- |
| AB  | $$a_1$$     | $$a_2$$                          | $$b_{1,3}$$ | $$b_{1,4}$$ | $$b_{1,5}$$ |
| AE  | $$a_1$$     | <font color='red'>$$a_2$$</font> | $$b_{2,3}$$ | $$b_{1,4}$$ | $$a_5$$     |
| CE  | $$b_{3,1}$$ | <font color='red'>$$a_2$$</font> | $$a_3$$     | $$b_{1,4}$$ | $$a_5$$     |
| BCD | $$b_{4,1}$$ | $$a_2$$                          | $$a_3$$     | $$a_4$$     | $$b_{4,5}$$ |
| AC  | $$a_1$$     | <font color='red'>$$a_2$$</font> | $$a_3$$     | $$b_{1,4}$$ | $$b_{5,5}$$ |

Considering $$BC\rightarrow D$$

|     | A           | B       | C           | D                                | E           |
| --- | ----------- | ------- | ----------- | -------------------------------- | ----------- |
| AB  | $$a_1$$     | $$a_2$$ | $$b_{1,3}$$ | $$b_{1,4}$$                      | $$b_{1,5}$$ |
| AE  | $$a_1$$     | $$a_2$$ | $$b_{2,3}$$ | $$b_{1,4}$$                      | $$a_5$$     |
| CE  | $$b_{3,1}$$ | $$a_2$$ | $$a_3$$     | <font color='red'>$$a_4$$</font> | $$a_5$$     |
| BCD | $$b_{4,1}$$ | $$a_2$$ | $$a_3$$     | $$a_4$$                          | $$b_{4,5}$$ |
| AC  | $$a_1$$     | $$a_2$$ | $$a_3$$     | <font color='red'>$$a_4$$</font> | $$b_{5,5}$$ |

Considering $$DC\rightarrow A$$

|     | A                                | B       | C           | D           | E           |
| --- | -------------------------------- | ------- | ----------- | ----------- | ----------- |
| AB  | $$a_1$$                          | $$a_2$$ | $$b_{1,3}$$ | $$b_{1,4}$$ | $$b_{1,5}$$ |
| AE  | $$a_1$$                          | $$a_2$$ | $$b_{2,3}$$ | $$b_{1,4}$$ | $$a_5$$     |
| CE  | <font color='red'>$$a_1$$</font> | $$a_2$$ | $$a_3$$     | $$a_4$$     | $$a_5$$     |
| BCD | <font color='red'>$$a_1$$</font> | $$a_2$$ | $$a_3$$     | $$a_4$$     | $$b_{4,5}$$ |
| AC  | $$a_1$$                          | $$a_2$$ | $$a_3$$     | $$a_4$$     | $$b_{5,5}$$ |

In the above example, the decomposition is lossless because the third row of the final table are all a, which means that the original relation can be recovered from the decomposed relations.

Let $$\rho={R_1,R_2}$$ be a decomposition of $$R$$, the decomposition is lossless if$$F\vert=(R_1\cap R_2)\rightarrow (R_1-R_2)\vert$$ or $$F\vert=(R_1\cap R_2)\rightarrow (R_2-R_1)\vert$$.

## Dependency Preservation

{::nomarkdown}
{% assign jupyter_path = "assets/jupyter/db/dependency_preservation.ipynb" | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/db/dependency_preservation.ipynb %}{% endcapture %}
{% if notebook_exists == "true" %}
    {% jupyter_notebook jupyter_path %}
{% else %}
    <p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}