---
title: 'A quick guide to linear algebra'
subtitle: 'Computational Neuroscience'
author: 'C Daniel Meliza'
documentclass: scrartcl
linkcolor: blue
header-includes:
    - \usepackage[letterpaper, margin=1in]{geometry}
    - \usepackage{mathpazo}
    - \usepackage{eulervm}
---

Linear algebra is for working with **vectors**. Vectors belong to **vector spaces**, which are sets in which the elements can be added to each other or multiplied by scalars. For example $(1,2)$ is in the vector space $\mathbb{R}^2 = \{(x,y) : x,y \in \mathbb{R}\}$, where $\mathbb{R}$ is the set (field) of real numbers. Most of the vectors you will work with in this course are finite lists of real numbers ($\mathbb{R}^n$, where n is a positive integer). 

To **add** two vectors in $\mathbb{R}^n$, add the corresponding components to each other: $x + y = (x_1,\ldots,x_n) + (y_1,\ldots,y_n) = (x_1 + y_1,\ldots,x_n + y_n)$.

To **multiply** a vector in $\mathbb{R}^n$ by a scalar, multiply each component by the scalar: $\lambda x = (\lambda x_1,\ldots,\lambda x_n)$.

A **linear combination** of vectors $v_1,\ldots,v_n$ in $\mathbb{R}^n$ is a vector of the form $a_1 v_1 + \cdots a_n v_n$, where $a_1,\ldots,a_n \in \mathbb{R}$.

The **span** of $v_1,\ldots,v_n$ is the vector space containing all their possible linear combinations.

A **basis** of a vector space $V$ is a set of vectors that are *linearly independent* and that *span* the space. Linear independence means none of the vectors is a linear combination of the others. The *standard basis* for $\mathbb{R}^n$ comprises the unit vectors. For example, the standard basis of $\mathbb{R}^2$ is $(1,0),(0,1)$.

The vector space $\mathbb{R}^n$ is an **inner product space**, which means that vectors have lengths and angles with other vectors. 

The **inner product** of two vectors $x,y \in \mathbb{R}^n$ is given by the dot product: $x \cdot y = x_1 y_1 + \cdots + x_n y_n$. 

The length, or **norm**, of a vector $x \in \mathbb{R}^n$ is $||x|| = \sqrt{x \cdot x} = \sqrt{x_1^2 + \cdots + x_n^2}$. Note that this is the Euclidean distance, generalized to higher dimensions.

Two vectors $u, v \in V$ are **orthogonal** if their inner product is 0. The **angle** between $u,v \in V$ is

\begin{equation*}
\cos \theta = \frac{u \cdot v}{\|u\|\|v\|}.
\end{equation*}

A basis is **orthonormal** if each vector has norm 1 and is orthogonal to all other vectors in the basis.

An $\mathbb{R}^{m \times n}$ **matrix** is a rectangular array of real numbers with $m$ rows and $n$ columns,

\begin{equation*}
A = \begin{pmatrix} A_{1,1} & \cdots & A_{1,n} \\ \vdots & & \vdots \\ A_{m,1} & \ldots & A_{m,n} \end{pmatrix}.
\end{equation*}

You can also view a matrix as column vectors or row vectors. As an example, $\mathbb{R}^{3\times 2}$ is:

\begin{equation*}
  A=
  \begin{pmatrix}
    | & |\\
    A_1 & A_2\\
    | & |
  \end{pmatrix}
  =
  \begin{pmatrix}
    - A_1^* -\\
    - A_2^* -\\
    - A_3^* -
  \end{pmatrix}
\end{equation*}

An $\mathbb{R}^{m \times n}$ matrix is a linear map between two vector spaces, $V \in \mathbb{R}^n$ and $W \in \mathbb{R}^m$, *for a given set of bases*. When you multiply a matrix $A$ by a vector $x$, you get a linear combination of the column vectors of $A$:

\begin{equation*}
Ax = 
  x_1 \begin{pmatrix} | \\ A_1 \\ | \end{pmatrix} +
  \cdots +
  x_n \begin{pmatrix} | \\ A_n \\ | \end{pmatrix}
\end{equation*}

You can also multiply a vector by a matrix to map from $W$ to $V$:

\begin{equation*}
yA = 
  y_1 \begin{pmatrix} - A_1^* - \end{pmatrix} +
  \cdots +
  y_m \begin{pmatrix} - A_m^* - \end{pmatrix}
\end{equation*}

The **transpose** of a matrix $A^T$ is formed by swapping rows and columns. The transpose of $A \in \mathbb{R}^{m \times n}$ is in $\mathbb{R}^{n \times m}$. If $m = n$, the matrix is **square**. A square matrix where $S = S^T$ is **symmetric**.

Matrices follow the same algebra for addition and scalar multiplication as vectors: add corresponding components; distribute scalar multiples to all components.

The **product of two matrices** is the composition of their linear maps: $(AB)x = A(Bx)$. The number of columns in the first matrix has to match the number of rows in the second matrix. If $A \in \mathbb{R}^{m \times k}$ and $B \in \mathbb{R}^{k \times n}$, then $AB$ will be $\mathbb{R}^{m \times n}$. In general, multiplication is not commutative: $AB \neq BA$.

You can think about multiplying two matrices as the first matrix multiplying the columns of the second matrix or as the rows of the first matrix multiplying the second matrix:

\begin{equation*}
AB = 
  \begin{pmatrix} | & & | \\ AB_1 & \cdots & AB_n \\ | & & | \end{pmatrix}
   =
  \begin{pmatrix} - A_1^*B - \\ \vdots \\ - A_m^*B - \end{pmatrix}
\end{equation*}

A **diagonal matrix** is a square matrix with 0 everywhere except possibly on the diagonal. Multiplying a matrix by a diagonal matrix scales each column by the values along the diagonal, and vice versa for rows if the diagonal matrix is on the left. The **identity** matrix $I$ is a diagonal matrix with only 1's on the diagonal. $AI = IA = A$.

A square matrix $A$ is **invertible** if there is a matrix $A^{-1}$ of the same size such that $AA^{-1} = A^{-1}A = I$. Not every matrix has an inverse.

If the columns of a square matrix $S$ are orthogonal, then $S^{-1} = S^T$.

### Further reading

- Strang (2020). *Linear Algebra for Everyone*. Wellesley-Cambridge Press. An accessible text with an emphasis on concrete examples and applications in data science.
- Hiranabe (2023). [The Art of Linear Algebra](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra). A useful graphical summary of matrix operations.
- Axler (2025), [*Linear Algebra Done Right*](https://linear.axler.net/), Springer. 4th ed. A more general, proof-based treatment of vector spaces and operators.










