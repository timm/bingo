[home](../README.md) | [maths](maths.md) | [se](se.md) | [ai](ai.md) | [code](code.md) | [tut](tutorial.md) | [make](prompt.txt) | [license](license.md)
---
# Artificial Intelligence Concepts in `bingo.py`

## Terms to watch for

- Active Learning
- Clustering
- Decision Trees
- Extrapolation
- Locality Sensitive Hashing (LSH)
- Multi-objective Optimization
- Random Projections
- Stochastic Landscape Analysis
- XAI (Explainable AI)

`bingo.py` implements several AI techniques, primarily focused on data analysis, learning from limited labeled data, and multi-objective reasoning.

### Core AI Themes
- **Stochastic Landscape Analysis**: The overall goal, as stated in its docstring, is "stochastic landscape analysis for multi objective reasoning." This involves understanding complex problem spaces by sampling and modeling.
- **Active Learning**: The script aims to "label less, learn more." It actively selects which data points to label (simulated by looking up known y-values) rather than passively using all available labels. This is seen in the main process: score random bins (`-a`), then reflect on labels seen so far (`-b`).
- **Multi-objective Optimization**: The `y` columns in the data can specify goals to be maximized (`+`) or minimized (`-`). The `heaven` attribute in `Num` objects (0 for minimize, 1 for maximize) and the `ydist` function reflect this. The `ydist` function calculates a row's "distance to heaven," a measure of how well it satisfies the objectives. (`Distance Metrics` protocol)

### Data Structures for AI
- **Custom Aggregation (`Num`, `Sym`, `Data`)**: These structures (`Data Structure Factories` protocol) are essential for summarizing data characteristics, which then feed into learning and decision-making processes. `Num` tracks statistics for numerical features, `Sym` for symbolic ones, and `Data` holds collections of rows and their column summaries.

### Key AI Techniques
1.  **Random Projections & Clustering**:
    - The script bins rows along random projections (`-d dims`). This is a dimensionality reduction technique.
    - `project(data, row, a, b)`: Projects a `row` onto a line defined by two other rows `a` and `b`. This is a core step in one form of random projection. (`Clustering & Projection` protocol)
    - `bucket(data, row, a, b)`: Assigns a `row` to one of `-B` bins based on its projection.
    - `lsh(data, corners)`: Implements a form of Locality Sensitive Hashing by creating buckets based on multiple projections (dimensions). Rows in the same bucket are considered similar.

2.  **Extrapolation & Active Selection**:
    - `extrapolate(data, row, a, b)`: Guesses the `y`-value (distance to heaven) of an unlabeled `row` by extrapolating from two labeled examples `a` and `b` based on the row's projection. This is used in the active learning loop. (`Clustering & Projection` protocol)
    - The core learning loop involves scoring some bins randomly, then for `-b` iterations, it "selects two labeled examples, guesses their y-values via extrapolation, then labels the best guess."

3.  **Decision Trees for XAI (Explainable AI)**:
    - `tree(data, ...)`: Builds a decision tree to model the data. The tree itself can be seen as an explainable model. (`Decision Trees` protocol)
    - `cuts(col, rows, Y, Klass)`: Finds the best way to split a set of `rows` based on a `col`'s values to minimize the diversity of `Y` values in the resulting subsets. This is the core of the tree-building heuristic.
    - `show(data, ...)`: Prints a textual representation of the decision tree, making the model's logic transparent. The "win" column (distance to heaven normalized) helps interpret leaf quality.

4.  **Bayesian Classification (Implicit)**:
    - `like(data, row, ...)`: Calculates the likelihood of a `row` belonging to a `data` cluster/summary using a Naive Bayes-like approach. It combines probabilities from individual column PDFs. (`Bayesian Classification` protocol)
    - `pdf(col, v, prior)`: Calculates the probability density function for a value `v` in a column `col`. For `Num` columns, it uses a Gaussian PDF; for `Sym` columns, it uses frequency counts with an m-estimate.

### Evaluation
- The script evaluates its success by checking if "trees learned from (from `a+b` labels) finds stuff as good as anything else (after seeing very few labels)." This is tested by labeling `-c` items from the supposed "best bin."

### References
[^1]: Domingos, P. (1996). *The Role of Occam's Razor in Knowledge Discovery*. Data Mining and Knowledge Discovery, 3, 409-425. (General machine learning concept).
[^2]: Aggarwal, C. C. (2015). *Data Mining: The Textbook*. Springer. (Covers clustering, decision trees).
[^3]: Menzies, T., & Hu, Y. (2003). Data mining for very busy people. *IEEE Computer*, 36(11), 22-29. (Illustrative of relevant work by the author, specific content may vary).
[^4]: Settles, B. (2009). *Active Learning Literature Survey*. University of Wisconsin-Madison. (Comprehensive overview of Active Learning).


### Review Questions
1. How does `bingo.py` implement the concept of active learning? What is the role of extrapolation in this process?
2. Explain the purpose of random projections and the `lsh` function in `bingo.py`. How do they relate to finding similar data points?
3. Describe how decision trees in `bingo.py` can contribute to Explainable AI (XAI). What information does the `show` function provide?
