# Coding style:

- No forward references. Everything used in a function is found above
- Balance between short (which is good) and readability (which is better)
  - Short functions, few lines: 10-20=ok, less than 10=better, less than 5=great
- Structs (no classes), so polymorphic code can be shown together,
  - `.it` in structs denotes type
  - Uppercase functions are constructors (e.g. `Sym`), and their matching
  - lowercase names are variables from that constructor (e.g. `sym`),
- `the` is for CLI config,
- `row` is a list,
- prefix `_` means "private", 
- `col` or `c` means `Num` or `Sym`,
- `eg__xxx` are CLI demos (e.g. `--xxx`),
- CSV files:
  - In CSV input files, uppercase names on row1 denotes numeric; `+`/`-`
  - show `y`-goals (others `x`). 
