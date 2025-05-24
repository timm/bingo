[home](../README.md) | [maths](maths.md) | [se](se.md) | [ai](ai.md) | [code](code.md) | [tut](tutorial.md) | [make](prompt.txt) | [license](license.md)
---
# Mathematical and Statistical Concepts in `bingo.py`

## Terms to watch for

- Bayesian Probability (Likelihood, Prior)
- Entropy (Shannon Entropy)
- Gaussian Distribution
- Mean
- Minkowski Distance
- Normalization
- Probability Density Function (PDF)
- Standard Deviation

`bingo.py` relies on several mathematical and statistical concepts to process data, make inferences, and guide its learning algorithms.

### Descriptive Statistics
These are primarily handled by the `Num` and `Sym` data structures (`Data Structure Factories` protocol) and their associated functions (`Statistical Summaries` protocol).

- **Mean (`mu`)**: Calculated incrementally in `Num` for numerical columns.
  ```python
  # From add() -> _num()
  num.mu  += inc * (d / num.n) 
  ```
- **Standard Deviation (`div`)**: Calculated from `_m2` (sum of squared differences from the mean) in `Num`.
  ```python
  # From div() -> _num() for Num
  return (max(num._m2,0)/(num.n - 1))**0.5
  ```
- **Mode**: For symbolic columns, `mid(col)` for a `Sym` object returns the most frequent symbol (the mode).
  ```python
  # From mid() for Sym
  max(col.has, key=col.has.get)
  ```
- **Range (`lo`, `hi`)**: `Num` objects track the minimum (`lo`) and maximum (`hi`) values seen.

### Normalization
- **`norm(i, v)`**: Normalizes a numeric value `v` from column `i` to a 0-1 scale based on the column's `lo` and `hi` values. This is crucial for distance calculations where features might have different scales. (`Distance Metrics` protocol)
  ```python
  # From norm()
  (v - i.lo)/(i.hi - i.lo + 1/BIG) # BIG is a large number to prevent division by zero
  ```

### Distance Metrics
- **`dist(col, v, w)`**: Calculates the distance between two values `v` and `w` in a column `col`.
    - For `Num` columns: It's the absolute difference of their normalized values.
    - For `Sym` columns: It's 0 if `v == w`, else 1 (Hamming-like distance).
- **Minkowski Distance (`minkowski(a)`)**: A generalized distance metric. `bingo.py` uses it to combine distances across multiple columns. The parameter `p` (from `the.p`, default 2) determines the type of distance:
    - `p=1`: Manhattan distance
    - `p=2`: Euclidean distance
  ```python
  # From minkowski()
  return (total / n)**(1 / the.P)
  ```
- **`xdist(data, row1, row2)`**: Calculates the distance between two rows `row1` and `row2` based on their independent 'x' columns, using Minkowski distance.
- **`ydist(data, row)`**: Calculates a row's "distance to heaven" – a measure of its quality with respect to the optimization goals defined in 'y' columns. It's the Minkowski distance between the row's normalized 'y' values and their "heaven" values (0 for minimization, 1 for maximization).

### Probability & Bayesian Concepts
(`Bayesian Classification` protocol)
- **Probability Density Function (`pdf(col, v, prior)`)**:
    - For `Num` columns: Assumes a Gaussian (normal) distribution. It calculates the probability density of value `v` given the column's `mu` (mean) and `div` (standard deviation).
      ```python
      # From pdf() -> _num()
      math.exp(-z) / (2 * math.pi * var) ** 0.5 
      ```
    - For `Sym` columns: Calculates probability using frequency counts, adjusted by an m-estimate (`the.m` and `prior`) to handle unseen symbols and smooth probabilities.
      ```python
      # From pdf() -> _sym()
      (sym.has.get(s,0) + the.m*prior) / (col.n + the.m + 1/BIG)
      ```
- **Likelihood (`like(data, row, ...)`):** Calculates the likelihood of a `row` belonging to the class/cluster represented by `data`. It uses a Naive Bayes approach by multiplying the PDFs of the row's values in each 'x' column, and then incorporates a prior probability. Logarithms are used to prevent underflow.
  ```python
  # From like()
  sum(math.log(n) for n in tmp + [prior] if n>0)
  ```
- **Prior Probability**: In `like()`, the prior is calculated as `(data.n + the.k) / (nall + the.k*nh)`, where `data.n` is items in this cluster, `nall` is total items, `nh` is number of hypotheses (clusters), and `the.k` is a smoothing factor.

### Information Theory
- **Entropy (`div` for `Sym`)**: For symbolic columns, `div(col)` calculates the Shannon entropy of the symbol distribution. This measures the uncertainty or information content. (`Statistical Summaries` protocol)
  ```python
  # From div() -> _sym() for Sym
  -sum(v/sym.n * math.log(v/sym.n, 2) for v in sym.has.values() if v>0)
  ```

### Logarithms and Exponentiation
- `math.log`: Used in `like()` for numerical stability and in `div()` for `Sym` (entropy calculation).
- `math.exp`: Used in `pdf()` for `Num` (Gaussian PDF calculation).
- `**0.5`: Used for square root (e.g., in standard deviation).
- `**the.P`: Used in `minkowski` distance.

### References
[^1]: Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill. (Covers Naive Bayes, decision trees).
[^2]: James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning*. Springer.
[^3]: Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory*. Wiley-Interscience. (For entropy).

### Review Questions
1. Explain how `bingo.py` calculates the distance between two rows (`xdist`). What is the role of normalization and the Minkowski coefficient (`the.p`) in this?
2. Describe the probability density function (`pdf`) used for numerical columns. What statistical properties of the column does it rely on?
3. What is Shannon entropy, and how is it calculated and used for symbolic columns in `bingo.py` (via the `div` function)?
