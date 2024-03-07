## Ziggurat Algorithm
This simple code demonstrates how to generate random variables using Ziggurat Algorithm.
In this specific case we generate $n=100,000$ random variables from Pareto distribution with shape parameter $\alpha \ge 1$.

The code is written as a learning task and should not be used for professional purposes as it may contain unknown errors and bugs.

To run the code just simply put both modules *ziggurat.py* and *output.py* into the same folder and run the code using the latter file.

## Algorithm description

Modified Ziggurat Algorithm: 
1. Determine the common area of rectangles of the algorithm using the formula: $v = r \cdot f(r) + \int_r^\infty f(x) dx$ 
2. Generate a vector of lengths $x_i = f^{-1}(v/x_{i+1} + f(x_{i+1}))$, for $i = 254, 253, ... , 0$, where $x_{255} = r $. 
3. Use the bisection method to adjust the parameter $r$ such that: $v - x_0 + x_0 \cdot f(x_0) = 0$.
4. Generate a vector of length ratios $k$ using the formula $k = \frac{x_i}{x_{i+1}}$, for $i = 255, 253, ... , 1$. Let $k_0 = \frac{r \cdot f(r)}{v}$. 
5. Generate a random variable $j$ from the distribution $U(0,1)$ and a random variable $i$ from $DU(0,255)$. 
6. Set $x=w_i$. If $j < k_i$, return $x$. Otherwise, regenerate $j$ from the distribution $U(0,1)$. 
7. If $j \cdot(f(x_{i-1}) - f(x_i)) < f(x) - f(x_i)$, return $x$. 
8. Return to step 5. 


The modification involves a slight change in the method of generating variables $i$ and $j$, as well as vectors of lengths $w$ and length ratios $k$.

In this specific case, the algorithm is adapted to generate variables from a Pareto distribution. After running the algorithm, you need to provide the parameter $\alpha$. The program requires that $\alpha \ge 1$.

If you want to use this code with another distribution, remember that the new distribution must be monotonically decreasing!

