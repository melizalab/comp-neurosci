---
title: 'Probability: a quick guide'
subtitle: 'Computational Neuroscience -- CD Meliza'
documentclass: scrartcl
linkcolor: blue
header-includes:
    - \usepackage[letterpaper, margin=1in]{geometry}
    - \usepackage{mathpazo}
    - \usepackage{eulervm}
---

A **random variable** (RV) is defined by a set of possible numerical outcomes (also called measurement space, domain, or support) and a **probability distribution**.

- A **discrete** RV can only take on a countable set of distinct values, like $\{0,1,2,\ldots\}$. Note that a set may be unbounded while still being countable.
- A **continuous** RV can take on an uncountably infinite number of possible values within an interval. Usually a measurement of a physical quantity.
- RVs are denoted with capital letters ($X$, $Y$), specific outcomes by lowercase letters ($x$, $y$).

The distribution of a discrete RV is defined by a **probability mass function** (PMF):

- $p_X(x_i)$ is the probability that $X = x_i$  ($x_i$ is a specific outcome).
- $0 \leq p_X(x_i) \leq 1$
- $\sum_i^N p_X(x_i) = 1$ ($N$ is the number of outcomes). Alternative formulation: $\sum_X p_X(x_i)$
- *Complement Rule*: $\neg p_X(x_i)$, the probability that $X$ is *not* $x_i$, is $1 - p_X(x_i)$
- *Expected value*: $\mathrm{E}(X) = \sum_X x_i p_X(x_i)$. This is also the *mean*.

For continuous RVs, the probability of a specific value $x$ is zero. Instead we look at the probability in a small interval *around* $x$. This is called a **probability density function** (PDF).

- $p_X(x)$ is the probability of a value between $x$ and $x + \delta$ (in the limit of $\delta \rightarrow 0$)
- $0 \leq p_X(x) \leq 1$
- $\int_X p_X(x) dx = 1$. If $X$ can be any real number, then integrate from $-\infty$ to $\infty$.
- *Expected value*: $\mathrm{E}(X) = \int_X x\;p_X(x_i) dx$.

When there is more than one RV, they may be **dependent** on each other or not.

- *Conditional distribution*: $p_X(x|y)$ is the probability that $X = x$ when $Y = y$[^1].
- *Joint distribution*: $p_{X,Y}(x,y)$ is the probability that $X = x$ and $Y = y$.
- *Multiplication Rule*: $p_{X,Y}(x,y) = p_X(x|y)p_Y(y)$
- *Marginalization*: $p_X(x) = \sum_Y p_X(x|y)p_Y(y)$. $p_X(x)$ is the *marginal* (or *unconditional*) distribution for $X$. For a continuous $Y$, $p_X(x) = \int_Y p_{X}(x|y)p_Y(y) dy$.
- *Bayes' Rule*: $p_X(x|y) = p_Y(y|x) p_X(x)/p_Y(y)$. Follows from definitions of joint and conditional probability.
- *Independence*: If (and only if) $X$ and $Y$ are independent, then $p_X(x|y) = p_X(x)$, $p_Y(y|x) = p_Y(y)$, and $p_{X,Y}(x,y) = p_X(x)p_Y(y)$.

### Further reading

- Easton and McColl (1997). [Statistics Glossary](http://www.stats.gla.ac.uk/steps/glossary/).
- Stirzaker (2012). [Probability and Random Variables: A beginner's guide](https://dx.doi.org/10.1017/CBO9780511813627) (light on math, introductory, but quite detailed)
- Proschan and Shaw (2016). [Essentials of Probability Theory for Statisticians](https://dx.doi.org/10.1201/9781315370576) (more rigorous, graduate level)
- Gelman et al (2013). [Bayesian Data Analysis, 3rd edition](http://www.stat.columbia.edu/~gelman/book/)


[^1]: Or around $x$ and $y$ for continuous RVs
