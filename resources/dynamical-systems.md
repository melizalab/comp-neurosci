---
title: 'Computational Neuroscience'
subtitle: 'A quick guide to dynamical systems'
documentclass: scrartcl
linkcolor: blue
header-includes:
    - \usepackage[letterpaper, margin=1in]{geometry}
    - \usepackage{mathpazo}
    - \usepackage{eulervm}
	- \usepackage{physics}
---

A **dynamical system** is defined by one or more **state variables** $x \in \mathbb{R}^n$, and how they change with time, $t$. This description can be a **differential equation** (or **vector field**) of the form

\begin{equation}
\dot{x} = \frac{dx}{dt} = f(x, t; \mu)
\end{equation}

or a **difference equation** (or **map**) of the form

\begin{equation}
x \mapsto g(x; \mu).
\end{equation}

In both forms, $\mu \in \mathbb{R}^p$ is a vector of parameters that do not change. In this course, we will be working almost entirely with differential equations. A **solution** to (1) is any function $t \mapsto x(t)$ that satisfies this relationship, which we can think of as a curve or **trajectory** in the **state space** (or **phase space**) $\mathbb{R}^n$ that has a tangent $f(x, t; \mu)$.

A system that does not explicitly depend on time ($\dot{x} = f(x;\mu)$) is called **autonomous** or **homogeneous**. A system that does depend on is called **nonautonomous** or **time-dependent**. Often the time-dependent aspect of the system is referred to as **forcing**. Sometimes we suppress the notation for the parameters $\mu$.

Because vector fields are defined over the whole state space, solutions will in general depend on **initial conditions** ($t_0,x(t_0)$). This means the trajectory is really $x(t, t_0, x_0)$. The set of all points on a trajectory passing through a particular $x_0$ is called an **orbit**.

An **equilibrium solution** or **fixed point** of a vector field is a point $\bar{x} \in \mathbb{R}^n$ where $f(\bar{x}) = 0$. A system that is at a fixed point does not change. A fixed point is **stable** if trajectories in the immediate vicinity tend to stay near the fixed point, and it is **unstable** if nearby trajectories tend to diverge.

We can determine the stability of a fixed point, we let $x = \bar{x} + y$ and Taylor expand around $\bar{x}$, giving

\begin{equation}
\dot{x} = f(\bar{x}) + f'(\bar{x})y + \mathcal{O}(|y^2|).
\end{equation}

Since $f(\bar{x}) = 0$ and $\mathcal{O}(|y^2|)$ are higher-order terms we can ignore close to $\bar{x}$, the trajectories around $\bar{x}$ are described by the associated **linear system** $y = f'(\bar{x})y$. Linear systems of this form have the solution 

\begin{equation}
y(t) = e^{f'(\bar{x})t} y_0.
\end{equation}

In a 1-dimensional system ($x \in \mathbb{R}^1$), $f'(\bar{x})$ is a scalar $\lambda$, so the system is asymptotically stable when $\lambda < 0$ and unstable when $\lambda > 0$. When $\lambda = 0$, the system is at a **bifurcation point**. Small changes to the parameters of a system near a bifurcation point can result in large, qualitatative changes in behavior.

In higher-dimensional systems ($n > 1$), the derivative $f'(\bar{x})$ is taken with respect to each component of $x$, resulting in a matrix called the **Jacobian**. For example, if $x = (u, v)$ and $f(x) = (g(u,v), h(u,v)$, the Jacobian is

\begin{equation}
f'(x) = \begin{pmatrix} \pdv{g}{u} & \pdv{g}{v} \\ \pdv{h}{u} & \pdv{h}{v} \end{pmatrix}.
\end{equation}

Evaluating the Jacobian $f'(\bar{x})$ gives an $n \times n$ matrix. The **eigenvalues** of this matrix may be complex numbers. If all the eigenvalues have negative real components, the system is asymptotically stable around $\bar{x}$. Otherwise, the system is unstable. If some eigenvalues have imaginary components, the system will exhibit oscillatory behaviors. There may be a mixture of positive- and negative-magnitude, resulting in a **saddle**. If any of the eigenvalues have a zero real component, the system is at a bifurcation.

### Further reading

- Strogatz, *Nonlinear Dynamics and Chaos*. 2nd ed. Taylor and Francis (also see the author's [lectures on youtube](https://www.youtube.com/watch?v=ycJEoqmQvwg)).
- Hirsch, Smale, and Devaney, *Differential Equations, Dynamical Systems, and an Introduction to Chaos*. Springer.
- Wiggins. *Introduction to Applied Nonlinear Dynamical Systems and Chaos*. Springer. Advanced and authoritative; the main source for this guide.
