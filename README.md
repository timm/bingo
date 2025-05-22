<img src="docs/bingo.png" width=300 align=left>

# bingo

This code reads csv data from `-f file`, then divides those rows into 
`-B Bins`  along `-d dimes` random projections. 
 
 After randomly scoring 
`-a a` bins, then `-b b` times, it selects two labeled examples, 
guesses their  y-values via extrapolation, then labels the best guess.
   
Afterwards, `-c c` items from the top bain are labeled for evaluation.
This code is successful if it finds great rows, after just labeling
just a few rows; e.g. `a+b+c<32` in a space of (say) 1,000+ rows.
    
## Options

```
bingo.py: stochastic landscape analysis for multi-objective reasoning
(c) 2025 Tim Menzies, <timm@ieee.org>. MIT license

Options, with (defaults):
  
   -B Bins   number of bins (10)
   -d dims   number of dimensions (4)
   -p p      minkowski coefficient  (2)
   -a a      rows labelled at random during cold start (4)
   -b b      rows labelled while reflecting on labels seen so far (30)
   -c c      rows labels while testing the supposed best bin (5)
   -f file   csv file for data (../../moot/optimize/misc/auto93.csv)
   -k k      Bayes hack (for rare classes)  (1)
   -m m      Bayes hack (for rare frequencies) (2)
   -z zero   ignore bins with zero items; 0=auto choose (0)

Command-line actions:
  -h        show help
```

## In this code:
- `the` is config, parsed from top docstring (can be updated via CLI);
- `_` marks private vars/methods;
- `i` means `self`;
- `col` means `num` or `sym`, often shortenned to `c`.
- `row` = `List[int|num|str]`
- vars called `d,a,n,s` are often dictionary, array, number, string;
- structs use `struct.it` to denote type;
- struct constructors are functions starting with uppercase; e.g. `Sym.,Num`
- stuct variables are named after their constructor. e.g. `sym,num1`
- no classes (so polymorphic methods can stay together in the source).
- `eg__xxx` are CLI demos (run with `--xxx`);
- The input data is csv,  where row one names the column;  e.g.
```
name   , ShoeSize, Age+
tim    ,  12     ,   50
junjie ,   5     ,  100
...    ,  ...    ,  ...
```
In row1, upper case names denote numeric columns. Names ending with `+`, `-` are
the `y` goals  to be maximized/minimize. Other columns are the 
`x` independent variables. The input data has all the `y` values known, but that
is just for testing purposes. The core `bingo` algorithm only ever glances at
a handful of those labels.

```
