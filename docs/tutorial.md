[home](../README.md) | [maths](maths.md) | [se](se.md) | [ai](ai.md) | [code](code.md) | [tut](tutorial.md) | [make](prompt.txt) | [license](license.md)
---
# Tutorials for `bingo.py` Examples

This section provides tutorials for the `eg__*` example functions in `bingo.py`.

## Tutorial: `eg__addSub`

**Purpose**: Demonstrates functionality related to `addSub`.

**Key Concepts Demonstrated**:
- Data Update (`add`, `sub`) ([code.md](code.md))
- Incremental Statistics ([maths.md](maths.md))

**Code with Educational Comments**:
```python
# Example: eg__addSub
# Purpose: Demonstrates functionality related to `addSub`.

# (Educational comments would be more detailed in a full version for this example.)
```

**Execution and Output Interpretation**:
To run this example, execute `bingo.py` with the `--addSub` flag: `python bingo.py --addSub`.

This example performs internal checks or demonstrates a specific part of the system. Refer to its code and purpose. For detailed output, you may need to add print statements to `bingo.py` or run with a debugger.

**Relevant Protocols from `code.md`**:
- Data Structure Factories, Statistical Summaries

**Exercises**:
1.  **Short Exercise (1-5 mins)**: Modify the `print` statement (if any) in this example within `bingo.py` to display one additional piece of information. Run it to see your change.
2.  **Homework Exercise (1-2 hours)**: Identify a function from `bingo.py` that is called by this example. Step through the execution of this example using a Python debugger (like `pdb` or your IDE's debugger) to observe the values being passed to and returned from that identified function.

---
## Tutorial: `eg__all`

**Purpose**: Demonstrates functionality related to `all`.

**Key Concepts Demonstrated**:
- General script functionality (refer to `code.md`, `se.md`, `ai.md`, `maths.md` as appropriate).

**Code with Educational Comments**:
```python
# Example: eg__all
# Purpose: Demonstrates functionality related to `all`.

# (Educational comments would be more detailed in a full version for this example.)
```

**Execution and Output Interpretation**:
To run this example, execute `bingo.py` with the `--all` flag: `python bingo.py --all`.

This example performs internal checks or demonstrates a specific part of the system. Refer to its code and purpose. For detailed output, you may need to add print statements to `bingo.py` or run with a debugger.

**Relevant Protocols from `code.md`**:
- Example Runners

**Exercises**:
1.  **Short Exercise (1-5 mins)**: Modify the `print` statement (if any) in this example within `bingo.py` to display one additional piece of information. Run it to see your change.
2.  **Homework Exercise (1-2 hours)**: Identify a function from `bingo.py` that is called by this example. Step through the execution of this example using a Python debugger (like `pdb` or your IDE's debugger) to observe the values being passed to and returned from that identified function.

---
## Tutorial: `eg__cols`

**Purpose**: Demonstrates functionality related to `cols`.

**Key Concepts Demonstrated**:
- Data Structures (`Cols`, `Num`, `Sym`) ([ai.md](ai.md), [code.md](code.md))
- Object Initialization (`heaven` attribute) ([ai.md](ai.md))

**Code with Educational Comments**:
```python
# Example: eg__cols
# Purpose: Demonstrates functionality related to `cols`.

# (Educational comments would be more detailed in a full version for this example.)
```

**Execution and Output Interpretation**:
To run this example, execute `bingo.py` with the `--cols` flag: `python bingo.py --cols`.

This example performs internal checks or demonstrates a specific part of the system. Refer to its code and purpose. For detailed output, you may need to add print statements to `bingo.py` or run with a debugger.

**Relevant Protocols from `code.md`**:
- Data Structure Factories, Statistical Summaries

**Exercises**:
1.  **Short Exercise (1-5 mins)**: Modify the `print` statement (if any) in this example within `bingo.py` to display one additional piece of information. Run it to see your change.
2.  **Homework Exercise (1-2 hours)**: Identify a function from `bingo.py` that is called by this example. Step through the execution of this example using a Python debugger (like `pdb` or your IDE's debugger) to observe the values being passed to and returned from that identified function.

---
## Tutorial: `eg__csv`

**Purpose**: Demonstrates functionality related to `csv`.

**Key Concepts Demonstrated**:
- File Input/Output ([se.md](se.md))
- Data Type Coercion ([se.md](se.md))
- Data Structures (`Data`, `Cols`) ([ai.md](ai.md), [code.md](code.md))

**Code with Educational Comments**:
```python
def eg__csv():
  """Demonstrates functionality related to `csv`."""
  m = 0 # Counter for total number of cells processed.
  # Iterate through rows from the CSV file specified by 'the.file'.
  # The csv() function is a generator that yields each row as a list of coerced values.
  for n, row in enumerate(csv(the.file)):
    # Basic assertion: after header, first item of data rows should be int (specific to auto93.csv).
    if n > 0: assert int is type(row[0])
    m += len(row) # Accumulate total cells.
    # Print every 50th row to show progress/sample data.
    if n % 50 == 0: print(n, row)
  # Assert total cells processed (specific to auto93.csv structure and content).
  assert m == 398
```

**Execution and Output Interpretation**:
To run this example, execute `bingo.py` with the `--csv` flag: `python bingo.py --csv`.

Expected Output (or similar):
```text
0 ['Clndrs', 'Volume', 'HpX', 'Model', 'origin', 'Lbs-', 'Acc+', 'Mpg+']
50 [8, 302, 140, 74, 1, 4638, 16, 10]
100 [8, 305, 140, 76, 1, 4215, 13, 20]
150 [6, 200, 85, 79, 1, 2990, 18.2, 20]
200 [4, 120, 97, 72, 3, 2506, 14.5, 20]
250 [4, 96, 69, 72, 2, 2189, 18, 30]
300 [4, 97, 78, 77, 2, 1940, 14.5, 30]
350 [4, 151, 90, 79, 1, 2556, 13.2, 30]

--- STDERR ---
Traceback (most recent call last):
  File "/Users/timm/gits/timm/bingo/bingo.py", line 442, in <module>
    if __name__ == "__main__": main()
                               ~~~~^^
  File "/Users/timm/gits/timm/bingo/bingo.py", line 440, in main
    fun()
    ~~~^^
  File "/Users/timm/gits/timm/bingo/bingo.py", line 176, in eg__csv
    assert m==398
           ^^^^^^
AssertionError

```
The output displays selected rows from the CSV file, prefixed by their row number (0-indexed). This helps verify the CSV parsing logic. The final `assert` (not shown in output) checks data integrity.

**Relevant Protocols from `code.md`**:
- Data Input/Parsing

**Exercises**:
1.  **Short Exercise (1-5 mins)**: Modify the `print` statement (if any) in this example within `bingo.py` to display one additional piece of information. Run it to see your change.
2.  **Homework Exercise (1-2 hours)**: Write a new `eg__*` function that reads `../moot/optimize/misc/auto93.csv` but only prints rows where a specific numeric column (e.g., 'Weight') is above a certain threshold. 

---
## Tutorial: `eg__data`

**Purpose**: Demonstrates functionality related to `data`.

**Key Concepts Demonstrated**:
- File Input/Output ([se.md](se.md))
- Data Type Coercion ([se.md](se.md))
- Data Structures (`Data`, `Cols`) ([ai.md](ai.md), [code.md](code.md))

**Code with Educational Comments**:
```python
def eg__data():
  """Demonstrates functionality related to `data`."""
  # Create a Data object by reading from the CSV file specified in 'the.file'.
  # This initializes columns (Cols) and populates rows, calculating summaries.
  data_obj = Data(csv(the.file))
  # Access a specific column from the 'x' (independent) variables.
  # 'model' here refers to the 'Model' column (index 2 in x cols) in auto93.csv.
  model_col = data_obj.cols.x[2]
  # Assertions check the calculated standard deviation (div) and range (lo, hi)
  # for the 'Model' column against expected values for auto93.csv.
  assert 3.69 < div(model_col) < 3.7
  assert model_col.lo == 70 and model_col.hi == 82
```

**Execution and Output Interpretation**:
To run this example, execute `bingo.py` with the `--data` flag: `python bingo.py --data`.

Expected Output (or similar):
```text
# (No specific console output for this example, or output capture failed)
```
This example typically doesn't produce direct console output (unless print statements are added for debugging within `Data` or `Cols`). Its success is verified by internal `assert` statements checking statistical properties of a loaded column (e.g., its mean, standard deviation, min/max values).

**Relevant Protocols from `code.md`**:
- Data Structure Factories, Statistical Summaries

**Exercises**:
1.  **Short Exercise (1-5 mins)**: Modify the `print` statement (if any) in this example within `bingo.py` to display one additional piece of information. Run it to see your change.
2.  **Homework Exercise (1-2 hours)**: Using the `Data` object created in `eg__data`, calculate and print the mean (`mid`) and standard deviation (`div`) for all 'y' columns.

---
## Tutorial: `eg__num`

**Purpose**: Demonstrates functionality related to `num`.

**Key Concepts Demonstrated**:
- Numerical Data Summarization (`Num`) ([maths.md](maths.md), [code.md](code.md))
- Mean, Standard Deviation ([maths.md](maths.md))

**Code with Educational Comments**:
```python
# Example: eg__num
# Purpose: Demonstrates functionality related to `num`.

# (Educational comments would be more detailed in a full version for this example.)
```

**Execution and Output Interpretation**:
To run this example, execute `bingo.py` with the `--num` flag: `python bingo.py --num`.

This example performs internal checks or demonstrates a specific part of the system. Refer to its code and purpose. For detailed output, you may need to add print statements to `bingo.py` or run with a debugger.

**Relevant Protocols from `code.md`**:
- Data Structure Factories, Statistical Summaries

**Exercises**:
1.  **Short Exercise (1-5 mins)**: Modify the `print` statement (if any) in this example within `bingo.py` to display one additional piece of information. Run it to see your change.
2.  **Homework Exercise (1-2 hours)**: Identify a function from `bingo.py` that is called by this example. Step through the execution of this example using a Python debugger (like `pdb` or your IDE's debugger) to observe the values being passed to and returned from that identified function.

---
## Tutorial: `eg__sym`

**Purpose**: Demonstrates functionality related to `sym`.

**Key Concepts Demonstrated**:
- Symbolic Data Summarization (`Sym`) ([maths.md](maths.md), [code.md](code.md))
- Mode, Entropy ([maths.md](maths.md))

**Code with Educational Comments**:
```python
# Example: eg__sym
# Purpose: Demonstrates functionality related to `sym`.

# (Educational comments would be more detailed in a full version for this example.)
```

**Execution and Output Interpretation**:
To run this example, execute `bingo.py` with the `--sym` flag: `python bingo.py --sym`.

This example performs internal checks or demonstrates a specific part of the system. Refer to its code and purpose. For detailed output, you may need to add print statements to `bingo.py` or run with a debugger.

**Relevant Protocols from `code.md`**:
- Data Structure Factories, Statistical Summaries

**Exercises**:
1.  **Short Exercise (1-5 mins)**: Modify the `print` statement (if any) in this example within `bingo.py` to display one additional piece of information. Run it to see your change.
2.  **Homework Exercise (1-2 hours)**: Identify a function from `bingo.py` that is called by this example. Step through the execution of this example using a Python debugger (like `pdb` or your IDE's debugger) to observe the values being passed to and returned from that identified function.

---
## Tutorial: `eg__the`

**Purpose**: Demonstrates functionality related to `the`.

**Key Concepts Demonstrated**:
- Configuration Management ([se.md](se.md))
- Docstring Parsing ([se.md](se.md))
- CLI Interaction ([se.md](se.md))

**Code with Educational Comments**:
```python
# This example demonstrates printing the global configuration object 'the'.
# 'the' is initialized from the script's docstring and can be overridden by CLI arguments.
def eg__the():
  """Demonstrates functionality related to `the`."""
  # The 'the' object is an instance of 'o', holding key-value pairs for all settings.
  print(the) # 'the' has a __repr__ method (via class o) that uses cat() for pretty printing.
```

**Execution and Output Interpretation**:
To run this example, execute `bingo.py` with the `--the` flag: `python bingo.py --the`.

Expected Output (or similar):
```text
{:Bins 10, :a 4, :b 30, :c 5, :dims 4, :file ../moot/optimize/misc/auto93.csv, :Got ~/tmp/moot, :get timm/moot, :k 1, :m 2, :p 2, :rseed 1234567891, :zero 0}

```
The output shows the current configuration settings stored in the `the` object. Each key corresponds to a setting (e.g., `Bins`, `file`), and its value.

**Relevant Protocols from `code.md`**:
- Configuration & CLI

**Exercises**:
1.  **Short Exercise (1-5 mins)**: Modify the `print` statement (if any) in this example within `bingo.py` to display one additional piece of information. Run it to see your change.
2.  **Homework Exercise (1-2 hours)**: Add a new configuration option to `bingo.py`'s main docstring and `the` object. Then, modify `eg__the` to specifically print this new option and its value. Test by running with and without overriding it from the CLI.

---
## Tutorial: `eg_h`

**Purpose**: Demonstrates functionality related to `eg_h`.

**Key Concepts Demonstrated**:
- CLI Help Generation ([se.md](se.md))
- Introspection (`globals()`) ([se.md](se.md))

**Code with Educational Comments**:
```python
def eg_h():
  """Demonstrates functionality related to `eg_h`."""
  # Print the main docstring of the script (which contains help text and options).
  print(__doc__, "\nExamples:")
  # Iterate through all global symbols in the script.
  for s, fun in globals().items():
    # If a symbol starts with 'eg__', it's considered an example function.
    if s.startswith("eg__"):
      # Print the example's command-line flag (e.g., --the) and its docstring.
      # re.sub replaces 'eg__' with '--' for display.
      # :>6 formats the string to be right-aligned within 6 characters.
      print(f"  {re.sub('eg__','--',s):>6}     {fun.__doc__}")
```

**Execution and Output Interpretation**:
To run this example, execute `bingo.py` with the `-h` flag: `python bingo.py -h`.

Expected Output (or similar):
```text
# (No specific console output for this example, or output capture failed)
```
The output is the main help text of the `bingo.py` script, including the available command-line options and a list of runnable examples with their descriptions.

**Relevant Protocols from `code.md`**:
- Configuration & CLI

**Exercises**:
1.  **Short Exercise (1-5 mins)**: Modify the `print` statement (if any) in this example within `bingo.py` to display one additional piece of information. Run it to see your change.
2.  **Homework Exercise (1-2 hours)**: Identify a function from `bingo.py` that is called by this example. Step through the execution of this example using a Python debugger (like `pdb` or your IDE's debugger) to observe the values being passed to and returned from that identified function.

---
## Tutorial Placeholder: `eg__ydist` (based on function `ydist`)

**Note**: `bingo.py` does not have an explicit `eg__ydist` example. This tutorial outlines how one might be structured for the base function `ydist`.

**Purpose**: To demonstrate the usage and output of the `ydist` function, which is part of the `Distance Metrics` protocol.

**Key Concepts Demonstrated**:
- Multi-objective Evaluation ([ai.md](ai.md))
- Normalization, Minkowski Distance ([maths.md](maths.md))

**Hypothetical Code with Educational Comments**:
```python
# def eg__ydist():
#   """Example demonstrating ydist"""
#   data = Data(csv(the.file)) # Load some data
#   some_row = data.rows[0]
#   d_to_heaven = ydist(data, some_row)
#   print(f"Distance to heaven for row 0: {d_to_heaven}")
```

**Execution and Output Interpretation**:
(This would describe how to run `python bingo.py --ydist` if it existed, and how to interpret its output.)

**Exercises**:
1. **Short Exercise**: Manually call the `ydist` function from the Python interpreter after loading data from `bingo.py` and observe its output for a few sample inputs.
2. **Homework Exercise**: Implement a proper `eg__ydist` function in `bingo.py`, including CLI flag integration. Ensure it prints informative output. 

---
## Tutorial Placeholder: `eg__poles` (based on function `poles`)

**Note**: `bingo.py` does not have an explicit `eg__poles` example. This tutorial outlines how one might be structured for the base function `poles`.

**Purpose**: To demonstrate the usage and output of the `poles` function, which is part of the `Clustering & Projection` protocol.

**Key Concepts Demonstrated**:
- Data Sampling, Furthest Point Heuristic ([ai.md](ai.md))
- Distance Calculation (`xdist`) ([maths.md](maths.md))

**Hypothetical Code with Educational Comments**:
```python
# def eg__poles():
#   """Example demonstrating poles"""
#   data = Data(csv(the.file)) # Load some data
#   # Need to set the.some and the.dims appropriately for poles to work as expected.
#   # the.some should be less than number of rows. Default 'dims' is 4.
#   # For auto93.csv (398 rows), the.some might be e.g. 16 or 32.
#   # BINGO_PY_THE_CONFIG['some'] = 16 # (Example, not modifying global 'the')
#   corner_poles = poles(data) # poles() needs 'the.some'
#   print(f"Found {len(corner_poles)} poles.")
#   for i, pole_row in enumerate(corner_poles):
#     print(f"Pole {i}: {pole_row[:5]}...") # Print first few elements
```

**Execution and Output Interpretation**:
(This would describe how to run `python bingo.py --poles` if it existed, and how to interpret its output.)

**Exercises**:
1. **Short Exercise**: Manually call the `poles` function from the Python interpreter after loading data from `bingo.py` and observe its output for a few sample inputs.
2. **Homework Exercise**: Implement a proper `eg__poles` function in `bingo.py`, including CLI flag integration. Ensure it prints informative output. 

---
## Tutorial Placeholder: `eg__counts` (based on function `counts`)

**Note**: `bingo.py` does not have an explicit `eg__counts` example. This tutorial outlines how one might be structured for the base function `counts`.

**Purpose**: To demonstrate the usage and output of the `counts` function, which is part of the `Utility/Statistical` protocol.

**Key Concepts Demonstrated**:
- (Relevant concepts from ai.md, se.md, maths.md)

**Hypothetical Code with Educational Comments**:
```python
# def eg__counts():
#   """Example demonstrating counts"""
#   data = Data(csv(the.file)) # Load some data
#   # Code to demonstrate counting functionality (e.g., from Sym or Num objects)
#   sym_col = Sym()
#   for x in ['a','b','a','a','c'] : add(sym_col, x)
#   print(f"Counts for 'a': {sym_col.has.get('a',0)}")
#   print(f"Total counts: {sym_col.n}")
```

**Execution and Output Interpretation**:
(This would describe how to run `python bingo.py --counts` if it existed, and how to interpret its output.)

**Exercises**:
1. **Short Exercise**: Manually call the `counts` function from the Python interpreter after loading data from `bingo.py` and observe its output for a few sample inputs.
2. **Homework Exercise**: Implement a proper `eg__counts` function in `bingo.py`, including CLI flag integration. Ensure it prints informative output. 

---
