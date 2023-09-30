
## Terminology:

- regression: when we predict quantitative outputs 
- classification: when we predict qualitative outputs



notations:

- input variable is usually used by $X$
- if $X$ is a vector its components are $X_j$
- Quantitative outputs will be denoted by $Y$
- Uppercase letter is used for generic aspects of letters but the observed values use lower case: <br/>
    $x_{i}$ is the $ith$ observed value of $X$
- all vectors are column vectors
- $\widehat{Y}$ is the predicted value of Y


---

## Least Squares Method

Given a vector: $ X^T=(X_1, X_2, .., X_p) $ we predict the output: <br />

$$
    \widehat{Y} = \widehat{\beta} + \sum_{i=1}^{p} X_i \widehat{\beta}
$$
by including $\widehat{\beta}$ into the matrix we have:

$$
    (I) \;\;\;\;
    \widehat{Y} = X^T\widehat{\beta}
$$


more datails:

for $X_i^T = (X_{i1}, X_{i2}, \cdots, X_{ip})$ as the $ith$ input and $\widehat{Y_i}$ as the $ith$ predicted output and $Y_i$ and the training output:
$$
(II) \;\;\;\;
    \widehat{Y} = 
    \begin{bmatrix}
        \widehat{Y_1} \\
        \widehat{Y_2} \\
        \vdots \\
        \widehat{Y_N}
    \end{bmatrix}
    =
    \begin{bmatrix}
        X_1^T \\
        X_2^T \\
        \vdots \\
        X_N^T
    \end{bmatrix}
    
    \begin{bmatrix}
        \widehat{\beta_1} \\
        \widehat{\beta_2} \\
        \vdots \\
        \widehat{\beta_N}
    \end{bmatrix}
    = X\widehat{\beta}

$$

*note: each row in $X$ in equation $II$ is a training data $X^T$ in equation $I$


---


## K Nearest Neighbors


---

## 2.4 Statistical Decision Theory

the derivation of formula (2.7):
$$

    \begin{align*}
    EPE(f) &= \int [y - f(x)]^2 Pr(dx, dy) \\
    &= \int [y - f(x)]^2p(x,y)dxdy \\
    &= \int_x \int_y [y - f(x)]^2p(x,y)dxdy \\
    &= \int_x \int_y [y - f(x)]^2p(x)p(y|x)dxdy \\
    &= \int_x\left( \int_y [y - f(x)]^2p(y|x)dy \right)p(x)dx \\
    &= \int_x \left( E_{Y|X}([Y - f(X)]^2|X = x) \right) p(x)dx\\
    &= E_{X}E_{Y|X}([Y - f(X)]^2| X = x)
    \end{align*}

$$