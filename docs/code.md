[home](../README.md) | [maths](maths.md) | [se](se.md) | [ai](ai.md) | [code](code.md) | [tut](tutorial.md) | [make](prompt.txt) | [license](license.md)
---
# Code Overview: `bingo.py`

This document provides an overview of the structure, classes (struct-like objects), and functions within `bingo.py`.

## Classes and Data Structures

`bingo.py` uses a lightweight approach to objects. A single class `o` is defined, and factory functions (`Num`, `Sym`, `Cols`, `Data`) create instances of `o` to act as specialized data structures.

### o

A generic class for creating simple, struct-like objects with attributes assigned at instantiation.

| Attribute | Default Value / Source | Description (max 15 words) |
|-----------|------------------------|----------------------------|
| `**d` | `N/A (kwargs)` | Arbitrary keyword arguments to initialize object attributes. |
| `it` | `None (optional)` | Typically stores the constructor function, acting as a type tag. |

### Num

Summarizes a stream of numbers, tracking count, mean, standard deviation, min, and max.

| Attribute | Default Value / Source | Description (max 15 words) |
|-----------|------------------------|----------------------------|
| `it` | `Num` | Represents it of the Num. |
| `n` | `0` | Represents n of the Num. |

### Sym

Summarizes a stream of symbols, tracking counts of each symbol and mode.

| Attribute | Default Value / Source | Description (max 15 words) |
|-----------|------------------------|----------------------------|
| `it` | `Sym` | Represents it of the Sym. |
| `n` | `0` | Represents n of the Sym. |

### Cols

Manages a collection of columns (Num or Sym), distinguishing 'x' (independent) and 'y' (dependent) variables.

No specific attributes table generated for `Cols` (manual review of `bingo.py` needed for dynamic attributes or complex setup).

### Data

Holds rows of data and a `Cols` object that summarizes the data.

No specific attributes table generated for `Data` (manual review of `bingo.py` needed for dynamic attributes or complex setup).

## Functions and Protocols

Functions in `bingo.py` are grouped into the following conceptual protocols:

### Protocol: Configuration & CLI

- **`cli`**: Performs an operation related to cli.
  ```python
  def cli(d):
  ```
- **`coerce`**: Performs an operation related to coerce.
  ```python
  def coerce(x):
  ```
- **`the`**: Global configuration object, populated from command-line arguments and docstring defaults.
  ```python
  the= o(**{m[1]: coerce(m[2])
          for m in re.finditer(...)})
  ```
- **`eg_h`**: Performs an operation related to eg h.
  ```python
  def eg_h():
  ```

### Protocol: Core Object System

- **`o`**: A simple class for creating struct-like objects with dynamic attributes.
  ```python
  class o:
  __init__= lambda i, **d: i.__dict__.update(**d)
  __repr__= ...
  ```

### Protocol: Data Structure Factories

- **`Num`**: Performs an operation related to Num.
  ```python
  def Num(init=[], txt=" ",at=0):
  ```
- **`Sym`**: Performs an operation related to Sym.
  ```python
  def Sym(init=[], txt=" ",at=0):
  ```
- **`Cols`**: Performs an operation related to Cols.
  ```python
  def Cols(names):
  ```
- **`Data`**: Performs an operation related to Data.
  ```python
  def Data(init=[]):
  ```
- **`clone`**: Performs an operation related to clone.
  ```python
  def clone(data, rows=[]):
  ```

### Protocol: Initialization & Update

- **`inits`**: Performs an operation related to inits.
  ```python
  def inits(things, i):
  ```
- **`add`**: Performs an operation related to add.
  ```python
  def add(i,v, inc=1, purge=False):
  ```
- **`sub`**: Performs an operation related to sub.
  ```python
  def sub(i,v,purge=False):
  ```

### Protocol: Data Input/Parsing

- **`csv`**: Performs an operation related to csv.
  ```python
  def csv(s):
  ```
- **`webdata`**: Performs an operation related to webdata.
  ```python
  def webdata(fn):
  ```
- **`eg__csv`**: Example demonstrating csv functionality.
  ```python
  def eg__csv():
  ```
- **`eg__cols`**: Example demonstrating cols functionality.
  ```python
  def eg__cols():
  ```

### Protocol: Statistical Summaries

- **`mid`**: Performs an operation related to mid.
  ```python
  def mid(col):
  ```
- **`div`**: Performs an operation related to div.
  ```python
  def div(col):
  ```
- **`mids`**: Performs an operation related to mids.
  ```python
  def mids(data):
  ```
- **`divs`**: Performs an operation related to divs.
  ```python
  def divs(data):
  ```
- **`eg__num`**: Example demonstrating num functionality.
  ```python
  def eg__num():
  ```
- **`eg__sym`**: Example demonstrating sym functionality.
  ```python
  def eg__sym():
  ```
- **`eg__data`**: Example demonstrating data functionality.
  ```python
  def eg__data():
  ```
- **`eg__addSub`**: Example demonstrating addSub functionality.
  ```python
  def eg__addSub():
  ```

### Protocol: Bayesian Classification

- **`like`**: Performs an operation related to like.
  ```python
  def like(data, row, nall=2, nh=100):
  ```
- **`pdf`**: Performs an operation related to pdf.
  ```python
  def pdf(col,v, prior=0):
  ```

### Protocol: Distance Metrics

- **`norm`**: Performs an operation related to norm.
  ```python
  def norm(i,v):
  ```
- **`dist`**: Performs an operation related to dist.
  ```python
  def dist(col,v,w):
  ```
- **`minkowski`**: Performs an operation related to minkowski.
  ```python
  def minkowski(a):
  ```
- **`ydist`**: Performs an operation related to ydist.
  ```python
  def ydist(data, row):
  ```
- **`xdist`**: Performs an operation related to xdist.
  ```python
  def xdist(data, row1, row2):
  ```

### Protocol: Clustering & Projection

- **`project`**: Performs an operation related to project.
  ```python
  def project(data, row, a, b):
  ```
- **`bucket`**: Performs an operation related to bucket.
  ```python
  def bucket(data,row,a,b):
  ```
- **`extrapolate`**: Performs an operation related to extrapolate.
  ```python
  def extrapolate(data,row,a,b):
  ```
- **`poles`**: Performs an operation related to poles.
  ```python
  def poles(data):
  ```
- **`lsh`**: Performs an operation related to lsh.
  ```python
  def lsh(data, corners):
  ```
- **`neighbors`**: Performs an operation related to neighbors.
  ```python
  def neighbors(c, hi):
  ```

### Protocol: Decision Trees

- **`selects`**: Performs an operation related to selects.
  ```python
  def selects(row, op, at, y):
  ```
- **`cuts`**: Performs an operation related to cuts.
  ```python
  def cuts(col,rows,Y,Klass):
  ```
- **`tree`**: Performs an operation related to tree.
  ```python
  def tree(data, Klass=Num, Y=None, how=None):
  ```
- **`nodes`**: Performs an operation related to nodes.
  ```python
  def nodes(data1, lvl=0, key=None):
  ```
- **`leaf`**: Performs an operation related to leaf.
  ```python
  def leaf(data1,row):
  ```
- **`show`**: Performs an operation related to show.
  ```python
  def show(data, key=lambda z:z.ys.mu):
  ```

### Protocol: Utility Functions

- **`cat`**: Performs an operation related to cat.
  ```python
  def cat(v):
  ```

### Protocol: Example Runners

- **`eg__all`**: Example demonstrating all functionality.
  ```python
  def eg__all():
  ```

### Protocol: Main Program Flow

- **`main`**: Performs an operation related to main.
  ```python
  def main():
  ```

### Protocol: Other Functions

- **`_sym`**: Performs an operation related to  sym.
  ```python
  def _sym(sym,s):
  ```
- **`_data`**: Performs an operation related to  data.
  ```python
  def _data(data,row):
  ```
- **`_num`**: Performs an operation related to  num.
  ```python
  def _num(num,n):
  ```
- **`_num`**: Performs an operation related to  num.
  ```python
  def _num(num):
  ```
- **`_sym`**: Performs an operation related to  sym.
  ```python
  def _sym(sym):
  ```
- **`_sym`**: Performs an operation related to  sym.
  ```python
  def _sym(sym,s):
  ```
- **`_num`**: Performs an operation related to  num.
  ```python
  def _num(num,n):
  ```
- **`_sym`**: Performs an operation related to  sym.
  ```python
  def _sym(_,s1,s2):
  ```
- **`_num`**: Performs an operation related to  num.
  ```python
  def _num(num,n1,n2):
  ```
- **`go`**: Performs an operation related to go.
  ```python
  def go(i, p):
  ```
- **`_sym`**: Performs an operation related to  sym.
  ```python
  def _sym(sym):
  ```
- **`_num`**: Performs an operation related to  num.
  ```python
  def _num(num):
  ```

