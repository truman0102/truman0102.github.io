---
layout: post
title: Relational Algebra
date: 2023-10-17 00:00:00-0400
description: An introduction to relational algebra in database systems.
tags: relational-algebra DB
categories: database
related_posts: false
giscus_comments: false
toc:
  sidebar: left
---

## What is Relational Algebra?

Relational algebra is a procedural query language that is used to query the relational database. It uses operators to perform queries. The result of relational algebra is a new relation, which may have been formed from one or more input relations. General operations in relational algebra are union $$\cup$$, intersection $$\cap$$, difference $$-$$, selection $$\sigma$$, projection $$\pi$$, cartesian product $$\times$$, join $$\bowtie$$, division $$\div$$, and rename $$\rho$$.

## Relational Algebra Operators

### Union

The union operator $$\cup$$ is used to combine two relations. The relations must be union-compatible, which means that they must have the same number of attributes and the corresponding attributes must have the same domain. The union operator is commutative and associative.

$$
R \cup S = \{t \mid t \in R \vee t \in S\}
$$

### Intersection

The intersection operator $$\cap$$ is used to find the common tuples in two relations. The relations must be union-compatible. The intersection operator is commutative and associative.

$$
R \cap S = \{t \mid t \in R \wedge t \in S\}
$$

### Difference

The difference operator $$-$$ is used to find the tuples in one relation that are not in another relation. The relations must be union-compatible. The difference operator is not commutative or associative.

$$
R - S = \{t \mid t \in R \wedge t \notin S\}
$$

### Complement

The complement operator $$\overline{R}$$ ($$dom(R)-R$$) is used to find the tuples that are not in a relation. The complement operator is not commutative or associative.

$$
\overline{R} = \{t \mid t \notin R \wedge t \in D\}
$$

where $$D$$ is the domain of the relation. For example, if we have a relation $$S$$ that contains all students and a relation $$SC$$ that contains all students and their courses, we can find all students that are not taking any courses by taking the complement of $$SC$$.

Noting: $$adom(r)$$ is different from $$\overline{r}$$. $$adom(r)$$ is the set of all possible tuples that can be formed from the attributes of $$r$$, while $$\overline{r}$$ is the set of all possible tuples that can be formed from the domain of $$r$$.

$$
adom(r) = \{t \mid t \in dom(A_1) \times dom(A_2) \times \dots \times dom(A_n) \wedge t\notin r\}
$$

### Selection

The selection operator $$\sigma$$ is used to select tuples that satisfy a given predicate. The predicate is a Boolean expression that is applied to each tuple in the relation. The selection operator is commutative and associative.

$$
\sigma_{P}(R) = \{t \mid t \in R \wedge P(t)\}
$$

### Projection

The projection operator $$\pi$$ is used to select attributes from a relation. The projection operator is not commutative or associative.

$$
\pi_{A_1, A_2, \dots, A_n}(R) = \{t[A_1, A_2, \dots, A_n] \mid t \in R\}
$$

### Cartesian Product

The cartesian product operator $$\times$$ is used to combine two relations. The cartesian product operator is not commutative or associative.

$$
R \times S = \{t \mid t = t_1 \cup t_2 \mid t_1 \in R \wedge t_2 \in S\}
$$

### Join

The join operator $$\bowtie$$ is used to combine two relations based on a common attribute or set of attributes. The join operator is not commutative or associative. Usually, we need to specify the attributes that we want to join on. In this case, we can use the following notation.

$$
R \mathop{\bowtie}\limits_{A_1 = A_2} S = \{t \mid t = t_1 \cup t_2 \mid t_1 \in R \wedge t_2 \in S \wedge t_1[A_1] = t_2[A_2]\}
$$

If there are multiple attributes that we want to join on, we can use the following notation.

$$
R \mathop{\bowtie}\limits_{A_1 = A_2 \wedge A_3 = A_4} S = \{t \mid t = t_1 \cup t_2 \mid t_1 \in R \wedge t_2 \in S \wedge t_1[A_1] = t_2[A_2] \wedge t_1[A_3] = t_2[A_4]\}
$$

When no attributes are specified, the join operator will join on all common attributes, which is called a natural join.

$$
R \bowtie S = \{t \mid t = t_1 \cup t_2 \mid t_1 \in R \wedge t_2 \in S \wedge t_1[A] = t_2[A]\}
$$

Semi-join is a special case of join. It is used to find tuples in one relation that are related to tuples in another relation. The semi-join operator is not commutative or associative.

$$
\begin{aligned}
R \mathop{\ltimes}\limits_{A=B} S &= \{t \mid t \in R \wedge \exists s \in S \mid t[A] = s[B]\}\\
&=R \mathop{\bowtie}\limits_{A=B} \pi_{B}(S)\\
\end{aligned}
$$

### Division

The division operator $$\div$$ is used to find tuples in one relation that are related to all tuples in another relation. The division operator is not commutative or associative. For example, if we have a relation $$S$$ that contains all students and a relation $$SC$$ that contains all students and their courses, we can find all students that are taking all courses by dividing $$S$$ by $$SC$$. Similarly, we could find courses that are selected by all students by dividing $$SC$$ by $$S$$.

$$
R \div S = \{t[U-A] \mid t \in R \wedge \forall s \in S \mid t[A] = s[A]\}
$$

### Rename

The rename operator $$\rho$$ is used to rename a relation or attribute. The rename operator is not commutative or associative.

$$
\rho_{R}(S) = \{t \mid t \in S\}
$$