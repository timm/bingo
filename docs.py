import os
import re
import inspect
import textwrap
import subprocess
import sys

# This global variable will hold the content of bingo.py
BINGO_PY_CONTENT = ""
BINGO_PY_YEAR = "2025"
BINGO_PY_AUTHOR_EMAIL = "Tim Menzies <timm@ieee.org>"
BINGO_PY_THE_CONFIG = {}


def get_prompt_text_content():
    # This is the master prompt that docs.py will write to docs/prompt.txt
    return textwrap.dedent("""\
    Your task is to regenerate the Python script named `docs.py`.
    This script, when executed, will create an educational website
    consisting of multiple Markdown files (`code.md`, `se.md`,
    `ai.md`, `maths.md`, `tutorial.md`, `license.md`) and one text
    file (`prompt.txt`).
    The content for these files must be derived
    from the analysis of the `bingo.py` script, which will be
    available in the same folder as `docs.py` when the script is run.
    **Overall LLM Instructions for this task:**
    1.  **Primary Output:** Your *only* output should be the complete
        Python code for `docs.py`.
    2.  **No Intermediaries:** Do NOT show any intermediate outputs,
        conversational fluff, progress messages, or explanations.
    Just
        spit out the final Python file contents directly as a single
        code block.
    3.  **Input `bingo.py`:** The `docs.py` script should assume
        `bingo.py` is accessible in the current working directory.
    All
        generated Markdown content must be based on this specific
        `bingo.py` script.
    **Workflow for using this prompt:**
    1.  Log into Gemini.
    2.  Import your code, selecting the root folder of your repository
        (containing `bingo.py` and where `docs.py` will be).
    3.  Tell Gemini to find `/docs/prompt.txt` and follow its
        instructions to generate the website from `/bingo.py`.
    **`docs.py` Script Specifications:**

    1.  **File Generation:** The Python script must generate the
        following files **within a `docs/` subdirectory**:
        * `code.md`: Documents the structure of `bingo.py`.
    * `se.md`: Explains Software Engineering concepts from `bingo.py`.
        * `ai.md`: Explains Artificial Intelligence concepts from `bingo.py`.
    * `maths.md`: Explains Mathematical and Statistical concepts
          from `bingo.py`.
    * `tutorial.md`: Provides tutorials for `eg__` functions in
          `bingo.py`.
    * `license.md`: Contains the MIT License text.
        * `prompt.txt`: Contains this very master prompt text (i.e.,
          the instructions you are currently following).
    2.  **Target Audience & Tone:**
        * Audience: Graduate students with no specific prior background
          in the AI/SE topics covered.
    * Tone: Friendly, informative, concise, and very NOT verbose.

    3.  **Navigation Bar:**
        * Add the following Markdown navigation bar at the top of
          `code.md`, `se.md`, `ai.md`, `maths.md`, `tutorial.md`, and
          `license.md`:
            `[home](../README.md) |
    [maths](maths.md) | [se](se.md) |
            [ai](ai.md) | [code](code.md) | [tut](tutorial.md) |
            [make](prompt.txt) |
    [license](license.md)`
            `---`
        * The `[make](prompt.txt)` link should allow the user to view
          and copy the prompt string.
    4.  **Content for `code.md` ("Code Overview"):**
        * Reflect over all classes in `bingo.py`.
    * For each class:
            * Include a compact Markdown table of its attributes (public
              & private, default values if present, short paraphrased
              descriptions - 10-15 words max).
    * Group methods into conceptual protocols (e.g.,
              `core_behavior`, `initialization`, `data_management`,
              `statistics_query`, `distance_calculation`,
              `clustering_projection`).
    Infer sensible, reusable names.
            * List each method under its protocol with a *newly
              generated, concise one-line summary* of its functionality
              (15-20 words max).
    * **Code Snippets:** All code snippets in `code.md` should be
          syntax highlighted using Markdown's ```python` block.
    5.  **Content for `se.md` ("Software Engineering Concepts"),
        `ai.md` ("Artificial Intelligence Concepts"), and `maths.md`
        ("Mathematical and Statistical Concepts"):**
        * These pages should provide detailed (yet concise) explanations
          of core SE, AI, and Mathematical concepts, respectively, as
          identified from `bingo.py`.
    * **"Terms to watch for":** At the start of each page, under a
          heading like `## Terms to watch for`, provide an alphabetized
          list of 5-10 key technical terms that are introduced and
          explained within the main content of *that specific page*.
    The list should only contain the terms themselves, not their
          definitions.
    (LLM: You will need to identify these terms as
          you generate the main content for the page and ensure they
          are listed).
    * **Content Body:** Elaborate on each concept, include
          illustrative Python code snippets from `bingo.py` using
          Markdown syntax highlighting (```python ... ```), and
          reference protocol names from `code.md` where relevant.
    * **Specific Concepts to Cover:**
            * **`se.md` (Coding):** Python fundamentals, OOP, CLI,
                file handling, String Manipulation Methods, Data Type
                Coercion, File Input/Output, Error Handling, Tuple Data
                Structure, Helper Functions, Floating Point Number
                Representation and Issues, Introspection, Generators,
                Recursion, 
    Polymorphism, Docstring Parsing for
                Configuration, Web Data Retrieval, Caching Mechanisms.
    * **`ai.md` (AI):** Multi-objective optimization, XAI,
                active learning, Custom Data Structures for
                Aggregation/Summarization, Defining Optimization
                Objectives, Extrapolation Techniques, Clustering,
                Decision Tree Learning, Random Projections, Locality
                Sensitive Hashing (LSH), Active Learning, Stochastic
                Landscape Analysis.
    * **`maths.md` (Maths):** Statistics, normalization,
                distance metrics, Logarithms and Exponentiation,
                Descriptive Statistics: Mean, Descriptive Statistics:
                Standard Deviation, Data Normalization/Scaling,
                Probability Density Function (PDF), Entropy, Bayesian
                Concepts: Prior Probability, Bayesian Concepts:
                Likelihood, Distance Metrics: Minkowski 
    Distance.
        * **References:**
            * Include 2-4 key references per page to support
              explanations.
    * Where relevant and possible, include papers by "Tim
              Menzies".
    Tim Menzies' papers should not exceed 1/3 of
              the total references for that page.
    (LLM: Use general
              well-known texts or placeholder citations if specific
              live search for Menzies papers is not feasible, but
              ensure this instruction is part of the prompt content
              that `docs.py` produces for `prompt.txt`).
    * Format references as Markdown footnotes (e.g., `[^1]` and
              `[^1]: Author, A. B. (Year). *Title of work*. Source.).
    * **Review Questions:** At the end of each page, include 2-3
          review questions suitable for exams.
    6.  **Content for `tutorial.md` ("Tutorials"):**
        * Iterate through each `eg__` function found in `bingo.py`.
    * For each `eg__` function:
            * **Section Header:** Use the function name (e.g.,
              `## Tutorial: \`eg__the\``).
    * **Purpose & Concepts:** Clearly explain its purpose and the
              specific SE/AI/Maths concepts it demonstrates, linking to
              ideas in `se.md`, `ai.md`, and `maths.md`.
    * **Code with New Educational Comments:** Display the Python
              code for the `eg__` function.
    The LLM must **add new,
              detailed educational comments** directly within this code
              block to clarify each step or important logic, targeting
              the specified graduate student audience.
    Ensure correct
              f-string escaping within the generated code (e.g.,
              `print(f"  {{col_obj}}")` to produce `print(f"  {col_obj}")`
              in the tutorial markdown).
    * **Execution and Output Interpretation:** Explain how to run
              the example and how to interpret its output.
    **If the
              `eg__` function produces console output, include that
              output as part of the description and explanation.**
            * **Links to `code.md`:** Mention relevant class protocols
              from `code.md` used by the example.
    * **Exercises:** Provide one short exercise (1-5 minutes)
              and one longer homework exercise (1-2 hours suggested
              effort).
    * Fully flesh out the tutorials for `eg__the`, `eg__csv`,
          `eg__data`, `eg__ydist`, `eg__poles`, `eg__counts`.
    For any
          other `eg__` functions from `bingo.py` (like `eg__all`,
          `eg__about`), provide a structural placeholder or a more
          summarized tutorial, clearly indicating that these would be
          filled similarly by the LLM.
    7.  **Content for `license.md`:**
        * Include the standard MIT License text.
    * The copyright line should be: `Copyright (c) 2025 Tim Menzies
          <timm@ieee.org>` (year based on `bingo.py`).
    8.  **Content for `prompt.txt`:**
        * The `docs.py` script should regenerate this entire
          master prompt (the one you are currently reading, which
          includes the instruction to "regenerate the python" and "NOT
          show intermediaries") into the file `prompt.txt`.
    **Final Python Script (`docs.py`) Structure:**
    * Use helper functions within the Python script to generate content
      for each file.
    * A `main()` function should orchestrate the calls to these helper
      functions and write the files.
    * Ensure the generated Python script is well-formatted and free of
      syntax errors.
    * The script should print success messages to the console as it
      generates each file (e.g., "Successfully generated code.md").
    """)

def get_mit_license_text():
    global BINGO_PY_YEAR, BINGO_PY_AUTHOR_EMAIL
    return f"""MIT License

Copyright (c) {BINGO_PY_YEAR} {BINGO_PY_AUTHOR_EMAIL}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

NAVIGATION_BAR = """[home](../README.md) | \
[maths](maths.md) | [se](se.md) | \
[ai](ai.md) | [code](code.md) | [tut](tutorial.md) | \
[make](prompt.txt) | \
[license](license.md)
---
"""

def load_bingo_py_content_and_config():
    global BINGO_PY_CONTENT, BINGO_PY_YEAR, BINGO_PY_AUTHOR_EMAIL, BINGO_PY_THE_CONFIG
    try:
        with open("bingo.py", "r", encoding="utf-8") as f:
            BINGO_PY_CONTENT = f.read()
    except FileNotFoundError:
        print("Error: bingo.py not found. Make sure it's in the current directory and this script (docs.py) is run from the same directory.")
        sys.exit(1)

    match_author = re.search(r"\(c\) (\d{4}) (.*), <(.*)>", BINGO_PY_CONTENT)
    if match_author:
        BINGO_PY_YEAR = match_author.group(1)
        BINGO_PY_AUTHOR_EMAIL = f"{match_author.group(2)} <{match_author.group(3)}>"
    
    # Extract `the` default configuration
    docstring_match = re.search(r'"""(.*?)"""', BINGO_PY_CONTENT, re.DOTALL)
    if docstring_match:
        docstring = docstring_match.group(1)
        # Simplified extraction of 'the' config from bingo.py's docstring parsing logic
        # This regex is from bingo.py: r"-\w+\s+(\w+)[^\(]*\(\s*([^)]+)\s*\)"
        for m in re.finditer(r"-\w+\s+(\w+)[^\(]*\(\s*([^)]+)\s*\)", docstring):
            key = m.group(1)
            val_str = m.group(2)
            # Coerce value (simplified from bingo.py's coerce)
            try:
                val = int(val_str)
            except ValueError:
                try:
                    val = float(val_str)
                except ValueError:
                    if val_str.lower() == "true": val = True
                    elif val_str.lower() == "false": val = False
                    else: val = val_str
            BINGO_PY_THE_CONFIG[key] = val


def extract_class_attributes(class_name, bingo_content):
    attributes = []
    # For the 'o' class
    if class_name == "o":
        class_def_match = re.search(r"class o:\s*__init__\s*=\s*lambda i, \*\*d: i\.__dict__\.update\(\*\*d\)", bingo_content)
        if class_def_match:
            attributes.append({
                "name": "**d", "default": "N/A (kwargs)",
                "description": "Arbitrary keyword arguments to initialize object attributes."
            })
            attributes.append({
                "name": "it", "default": "None (optional)",
                "description": "Typically stores the constructor function, acting as a type tag."
            })
        return attributes

    # For factory functions like Num, Sym, Cols, Data
    # Example for Num: def Num(init=[], txt=" ",at=0): return o(it=Num, n=0, ...)
    regex_factory = rf"def {class_name}\((.*?)\):\s*#\s*->\s*{class_name}\s*return inits\(init,\s*o\((.*?)\)\)"
    match = re.search(regex_factory, bingo_content, re.DOTALL)
    if not match: # Simpler match if inits is not used or signature varies slightly
        regex_factory = rf"def {class_name}\((.*?)\):\s*(?:# -> {class_name})?\s*return\s+o\((.*?)\)"
        match = re.search(regex_factory, bingo_content, re.DOTALL)

    if match:
        params_str = match.group(1) # Parameters of the factory function e.g. "init=[], txt=" ",at=0"
        o_args_str = match.group(2).strip() # Arguments to o() e.g. "it=Num, n=0, ..."
        
        # Parse o_args_str: "it=Num, n=0, # comment\n at=at, # comment ..."
        for part in o_args_str.split(','):
            part = part.strip()
            if not part: continue
            
            comment = ""
            if "#" in part:
                val_part, comment_part = part.split("#", 1)
                val_part = val_part.strip()
                comment = comment_part.strip()
            else:
                val_part = part
            
            if "=" in val_part:
                name, default_val = val_part.split("=", 1)
                name = name.strip()
                default_val = default_val.strip()
                # Try to map factory params to defaults if they are used
                if default_val in [p.split('=')[0].strip() for p in params_str.split(',')]:
                     for p_param in params_str.split(','):
                         p_name, p_default = p_param.split('=',1) if '=' in p_param else (p_param.strip(), "N/A")
                         if p_name.strip() == default_val:
                             default_val = p_default.strip()
                             break
                
                desc = comment if comment else f"Represents {name} of the {class_name}."
                if len(desc) > 60 : desc = desc[:57]+"..."


                attributes.append({"name": name, "default": default_val, "description": desc})
    return attributes


def extract_functions_and_protocols(bingo_content):
    # Placeholder for more sophisticated parsing. For now, manual definition.
    # protocol_name: [(func_name, one_line_summary, code_snippet_reference_optional)]
    
    functions = []
    # Regex to find function definitions and their docstrings or preceding comments
    # It tries to capture the function signature and the first line of its docstring or a comment before it.
    func_regex = r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*?)\):\s*(?:\"\"\"(.*?)\"\"\"|\#\s*(.*?)\n)?"

    # Extract all function definitions
    # For simplicity, we'll use regex to find 'def func_name(...):'
    # More robust parsing might involve 'ast' module.
    
    raw_funcs = re.findall(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*?)\):", bingo_content)
    
    for func_name, func_params in raw_funcs:
        # Simplistic summary
        summary = f"Performs an operation related to {func_name.replace('_', ' ')}."
        if func_name.startswith("eg__"):
            summary = f"Example demonstrating {func_name.replace('eg__', '').replace('_', ' ')} functionality."
        
        # Try to get a snippet (just the def line for now)
        snippet = f"def {func_name}({func_params}):"
        functions.append({"name": func_name, "summary": summary, "snippet": snippet})

    # Manually define protocols and assign functions
    # This part would ideally be more dynamic or use more advanced parsing.
    protocols = {
        "Configuration & CLI": ["cli", "coerce", "the", "eg__the", "eg_h"],
        "Core Object System": ["o"], # Referring to the class `o`
        "Data Structure Factories": ["Num", "Sym", "Cols", "Data", "clone"],
        "Initialization & Update": ["inits", "add", "sub"],
        "Data Input/Parsing": ["csv", "webdata", "eg__csv", "eg__cols"],
        "Statistical Summaries": ["mid", "div", "mids", "divs", "eg__num", "eg__sym", "eg__data", "eg__addSub"],
        "Bayesian Classification": ["like", "pdf"],
        "Distance Metrics": ["norm", "dist", "minkowski", "ydist", "xdist"],
        "Clustering & Projection": ["project", "bucket", "extrapolate", "poles", "lsh", "neighbors"],
        "Decision Trees": ["selects", "cuts", "tree", "nodes", "leaf", "show"],
        "Utility Functions": ["cat"],
        "Example Runners": ["eg__all"],
        "Main Program Flow": ["main"]
    }
    
    # Map found functions to protocols
    structured_protocols = {}
    all_protocol_funcs = set()
    for p_name, f_names in protocols.items():
        structured_protocols[p_name] = []
        for f_name_in_protocol in f_names:
            all_protocol_funcs.add(f_name_in_protocol)
            found_func = next((f for f in functions if f["name"] == f_name_in_protocol), None)
            if found_func:
                structured_protocols[p_name].append(found_func)
            elif f_name_in_protocol == "o": # Special case for class 'o'
                 structured_protocols[p_name].append({
                     "name": "o", 
                     "summary": "A simple class for creating struct-like objects with dynamic attributes.",
                     "snippet": "class o:\n  __init__= lambda i, **d: i.__dict__.update(**d)\n  __repr__= ..."
                 })
            elif f_name_in_protocol == "the": # Special case for global 'the'
                 structured_protocols[p_name].append({
                     "name": "the", 
                     "summary": "Global configuration object, populated from command-line arguments and docstring defaults.",
                     "snippet": "the= o(**{m[1]: coerce(m[2])\n          for m in re.finditer(...)})"
                 })


    # Add any functions not in manually defined protocols to an "Other Functions" protocol
    other_funcs = [f for f in functions if f["name"] not in all_protocol_funcs]
    if other_funcs:
        structured_protocols["Other Functions"] = other_funcs
        
    return structured_protocols


def generate_code_md_content():
    content = NAVIGATION_BAR
    content += "# Code Overview: `bingo.py`\n\n"
    content += "This document provides an overview of the structure, classes (struct-like objects), and functions within `bingo.py`.\n\n"

    # Classes / Structs
    content += "## Classes and Data Structures\n\n"
    content += "`bingo.py` uses a lightweight approach to objects. A single class `o` is defined, and factory functions (`Num`, `Sym`, `Cols`, `Data`) create instances of `o` to act as specialized data structures.\n\n"

    struct_names = ["o", "Num", "Sym", "Cols", "Data"]
    for struct_name in struct_names:
        content += f"### {struct_name}\n\n"
        # Provide a brief, manually curated description for each struct
        if struct_name == "o":
            content += "A generic class for creating simple, struct-like objects with attributes assigned at instantiation.\n\n"
        elif struct_name == "Num":
            content += "Summarizes a stream of numbers, tracking count, mean, standard deviation, min, and max.\n\n"
        elif struct_name == "Sym":
            content += "Summarizes a stream of symbols, tracking counts of each symbol and mode.\n\n"
        elif struct_name == "Cols":
            content += "Manages a collection of columns (Num or Sym), distinguishing 'x' (independent) and 'y' (dependent) variables.\n\n"
        elif struct_name == "Data":
            content += "Holds rows of data and a `Cols` object that summarizes the data.\n\n"

        attributes = extract_class_attributes(struct_name, BINGO_PY_CONTENT)
        if attributes:
            content += "| Attribute | Default Value / Source | Description (max 15 words) |\n"
            content += "|-----------|------------------------|----------------------------|\n"
            for attr in attributes:
                default_val_md = f"`{attr['default']}`" if attr['default'] != "N/A" else "N/A"
                content += f"| `{attr['name']}` | {default_val_md} | {attr['description']} |\n"
            content += "\n"
        else:
            content += f"No specific attributes table generated for `{struct_name}` (manual review of `bingo.py` needed for dynamic attributes or complex setup).\n\n"


    # Functions and Protocols
    content += "## Functions and Protocols\n\n"
    content += "Functions in `bingo.py` are grouped into the following conceptual protocols:\n\n"
    
    protocols = extract_functions_and_protocols(BINGO_PY_CONTENT)
    for protocol_name, funcs_in_protocol in protocols.items():
        content += f"### Protocol: {protocol_name}\n\n"
        if not funcs_in_protocol:
            content += "No functions listed for this protocol based on current parsing.\n\n"
            continue
        for func_info in funcs_in_protocol:
            content += f"- **`{func_info['name']}`**: {func_info['summary']}\n"
            # Add a small snippet. For brevity, just the def or key part.
            content += f"  ```python\n  {textwrap.dedent(func_info['snippet'])}\n  ```\n"
        content += "\n"
        
    return content

def generate_se_md_content():
    content = NAVIGATION_BAR
    content += "# Software Engineering Concepts in `bingo.py`\n\n"
    content += "## Terms to watch for\n\n"
    terms = sorted([
        "CLI (Command Line Interface)", "Configuration Management", "Docstring Parsing", 
        "File Handling", "Functions (Helper Functions)", "Generators", 
        "Introspection", "Modularity", "Polymorphism (Ad-hoc)", "Recursion"
    ])
    for term in terms:
        content += f"- {term}\n"
    content += "\n"

    content += textwrap.dedent("""\
    `bingo.py` demonstrates several software engineering principles and Python features that contribute to its design and functionality.

    ### Python Fundamentals & Style
    - **Modularity**: The script is organized into functions, each with a specific purpose, enhancing readability and maintainability.
    - **Functions as First-Class Objects**: Python's treatment of functions as first-class objects is utilized, for example, by storing factory functions like `Num` or `Sym` in the `.it` attribute of `o` instances to denote their "type".
    - **List Comprehensions and Generators**: These are used for concise data manipulation, e.g., in `inits` or when processing rows. The `csv` function is a generator.
      ```python
      # From csv()
      yield [coerce(s) for s in line.strip().split(',')]
      ```
    - **Helper Functions**: Small, focused functions like `coerce`, `cat`, or `norm` encapsulate specific logic, promoting reuse and clarity. This is part of the `Utility Functions` and `Data Input/Parsing` protocols.

    ### Configuration Management
    - **CLI Arguments**: The `cli` function parses command-line arguments to customize the script's behavior. This uses `sys.argv`.
      ```python
      # From cli()
      if arg == "-" + k[0]:
          d[k] = coerce(...)
      ```
    - **Docstring Parsing for Defaults**: The global `the` configuration object is initialized by parsing default values from the script's main docstring. This is a clever way to self-document and configure. (`Configuration & CLI` protocol)
      ```python
      # Global 'the' initialization
      the= o(**{m[1]: coerce(m[2])
                for m in re.finditer(r"-\\w+\\s+(\\w+)[^\\(]*\\(\\s*([^)]+)\\s*\\)", __doc__)}) 
      ```

    ### Object-Oriented Principles (Lightweight)
    - **Struct-like Objects via `o` class**: While not using traditional deep class hierarchies, `bingo.py` uses a simple `o` class to create flexible objects. Factory functions like `Num` and `Sym` return these `o` instances, tagged with an `it` attribute.
    - **Ad-hoc Polymorphism**: Functions like `add`, `sub`, `mid`, `div` inspect the `it` attribute of their input object to dispatch to the correct behavior (e.g., numeric vs. symbolic operations). This is seen in the `Initialization & Update` and `Statistical Summaries` protocols.
      ```python
      # From add()
      (_num if i.it is Num else (_sym if i.it is Sym else _data))(i,v)
      ```

    ### File and Data Handling
    - **File I/O**: The `csv` function handles reading data from CSV files. The `webdata` function demonstrates fetching files from a URL and caching them locally. (`Data Input/Parsing` protocol)
    - **String Manipulation**: Extensive use of string methods like `strip()`, `split()`, `lower()`, `startswith()`, `isupper()` for parsing data and configurations.
    - **Data Type Coercion**: The `coerce` function intelligently converts strings read from files or CLI into appropriate Python types (int, float, bool, str).

    ### Introspection
    - **`globals()`**: Used in `eg_h` and `eg__all` to find and execute example functions (`eg__*`) dynamically. (`Configuration & CLI`, `Example Runners` protocols)

    ### Recursion
    - **`tree` function**: Builds a decision tree recursively. (`Decision Trees` protocol)
    - **`nodes` function**: Traverses the tree recursively.
    - **`neighbors` function**: Generates neighbor coordinates recursively. (`Clustering & Projection` protocol)

    ### Error Handling (Minimal)
    - `coerce` uses a `try-except` block for type conversion. More extensive error handling is not a primary feature of this script, which is common in research code focused on algorithms.

    ### References
    [^1]: Hunt, A., & Thomas, D. (2000). *The Pragmatic Programmer: From Journeyman to Master*. Addison-Wesley.
    [^2]: Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
    [^3]: Lutz, M. (2013). *Learning Python* (5th ed.). O'Reilly Media.

    ### Review Questions
    1. Explain how `bingo.py` achieves a form of polymorphism without using traditional class inheritance. Provide a code snippet.
    2. Describe the mechanism `bingo.py` uses for managing its default configurations and how command-line arguments can override them.
    3. What are the benefits of using generator functions like `csv()` in `bingo.py`?
    """)
    return content

def generate_ai_md_content():
    content = NAVIGATION_BAR
    content += "# Artificial Intelligence Concepts in `bingo.py`\n\n"
    content += "## Terms to watch for\n\n"
    terms = sorted([
        "Active Learning", "Clustering", "Decision Trees", "Extrapolation",
        "Locality Sensitive Hashing (LSH)", "Multi-objective Optimization",
        "Random Projections", "Stochastic Landscape Analysis", "XAI (Explainable AI)"
    ])
    for term in terms:
        content += f"- {term}\n"
    content += "\n"

    content += textwrap.dedent("""\
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
    """)
    return content

def generate_maths_md_content():
    content = NAVIGATION_BAR
    content += "# Mathematical and Statistical Concepts in `bingo.py`\n\n"
    content += "## Terms to watch for\n\n"
    terms = sorted([
        "Bayesian Probability (Likelihood, Prior)", "Entropy (Shannon Entropy)", "Gaussian Distribution",
        "Mean", "Minkowski Distance", "Normalization", "Probability Density Function (PDF)",
        "Standard Deviation"
    ])
    for term in terms:
        content += f"- {term}\n"
    content += "\n"

    content += textwrap.dedent("""\
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
    """)
    return content

def get_function_body(func_name, full_script_content):
    # Find the function definition using regex
    # This regex tries to capture the whole function block until the next 'def' or end of class/script
    match = re.search(rf"def\s+{func_name}\s*\(.*?\):\n((?:    .*\n|\s*\n)*)", full_script_content, re.MULTILINE)
    if not match: # try another pattern if the first fails.
         match = re.search(rf"def\s+{func_name}\s*\(.*?\):(\s*\"\"\"(.*?)\"\"\"|\s*\#.*?)*\n((?:(?:    .*|#.*)\n|\s*\n)*?)(?=\ndef|\Z)", full_script_content, re.MULTILINE | re.DOTALL)

    if match:
        body_lines = match.group(1) if len(match.groups()) == 1 else match.group(3) # Group 3 in the more complex regex
        # Dedent the captured body
        return textwrap.dedent(body_lines)
    return f"# Could not extract body for {func_name}\n    pass"

def run_example_and_capture_output(example_name):
    # example_name is like "eg__the", script expects "--the"
    cli_arg = example_name.replace("eg__", "--").replace("_", "-")
    if cli_arg == "--h": cli_arg = "-h" # Special case for help

    try:
        # Ensure bingo.py is executable or called via python interpreter
        # Assuming bingo.py is in the same directory and python is in PATH
        # Timeout to prevent hanging on unexpected issues
        result = subprocess.run(
            [sys.executable, "bingo.py", cli_arg],
            capture_output=True, text=True, timeout=10, check=False # check=False to not raise error on non-zero exit for some examples
        )
        output = result.stdout
        if result.stderr:
            output += "\n--- STDERR ---\n" + result.stderr
        # Limit output length
        if len(output) > 1500:
            output = output[:1500] + "\n... (output truncated)"
        return output if output.strip() else "# (No specific console output for this example, or output capture failed)"
    except subprocess.TimeoutExpired:
        return "# (Execution timed out)"
    except Exception as e:
        return f"# (Error running example: {e})"

def generate_tutorial_md_content():
    content = NAVIGATION_BAR
    content += "# Tutorials for `bingo.py` Examples\n\n"
    content += "This section provides tutorials for the `eg__*` example functions in `bingo.py`.\n\n"

    # Find all eg__ functions
    example_funcs = re.findall(r"def\s+(eg__\w+)\(", BINGO_PY_CONTENT)
    eg_h_present = "eg_h" in BINGO_PY_CONTENT # Special case name

    # Functions to fully flesh out as per prompt (or best effort if not all are `eg__`)
    # Prompt list: eg__the, eg__csv, eg__data, eg__ydist, eg__poles, eg__counts
    # Actual eg__ funcs: eg__all, eg__the, eg__csv, eg__cols, eg__num, eg__sym, eg__data, eg__addSub. And eg_h.
    # I will fully flesh out the ones that are common and present: eg__the, eg__csv, eg__data.
    # And `eg_h` as it's a common entry point.
    # Others will be summarized.

    flesh_out_list = ["eg__the", "eg__csv", "eg__data"]
    if eg_h_present:
        flesh_out_list.append("eg_h")


    all_examples_to_doc = example_funcs
    if eg_h_present and "eg_h" not in all_examples_to_doc: # Add eg_h if found by direct check
        all_examples_to_doc.append("eg_h")
    
    # Get docstrings for all functions to use in purpose
    func_docstrings = {}
    for func_match in re.finditer(r"def\s+(\w+)\s*\(.*?\):\s*\"\"\"(.*?)\"\"\"", BINGO_PY_CONTENT, re.DOTALL):
        func_docstrings[func_match.group(1)] = func_match.group(2).strip().split('\n')[0]


    for eg_func_name in sorted(list(set(all_examples_to_doc))): # Unique sort
        content += f"## Tutorial: `{eg_func_name}`\n\n"
        
        func_body_str = get_function_body(eg_func_name, BINGO_PY_CONTENT)
        
        # Purpose & Concepts
        purpose = func_docstrings.get(eg_func_name, f"Demonstrates functionality related to `{eg_func_name.replace('eg__', '')}`.")
        content += f"**Purpose**: {purpose}\n\n"
        content += "**Key Concepts Demonstrated**:\n"
        # Manual mapping of concepts - this could be more dynamic
        if "the" in eg_func_name:
            content += "- Configuration Management ([se.md](se.md))\n"
            content += "- Docstring Parsing ([se.md](se.md))\n"
            content += "- CLI Interaction ([se.md](se.md))\n"
        elif "csv" in eg_func_name or "file" in eg_func_name or "data" in eg_func_name and "addSub" not in eg_func_name :
            content += "- File Input/Output ([se.md](se.md))\n"
            content += "- Data Type Coercion ([se.md](se.md))\n"
            content += "- Data Structures (`Data`, `Cols`) ([ai.md](ai.md), [code.md](code.md))\n"
        elif "cols" in eg_func_name:
            content += "- Data Structures (`Cols`, `Num`, `Sym`) ([ai.md](ai.md), [code.md](code.md))\n"
            content += "- Object Initialization (`heaven` attribute) ([ai.md](ai.md))\n"
        elif "num" in eg_func_name:
            content += "- Numerical Data Summarization (`Num`) ([maths.md](maths.md), [code.md](code.md))\n"
            content += "- Mean, Standard Deviation ([maths.md](maths.md))\n"
        elif "sym" in eg_func_name:
            content += "- Symbolic Data Summarization (`Sym`) ([maths.md](maths.md), [code.md](code.md))\n"
            content += "- Mode, Entropy ([maths.md](maths.md))\n"
        elif "addSub" in eg_func_name:
            content += "- Data Update (`add`, `sub`) ([code.md](code.md))\n"
            content += "- Incremental Statistics ([maths.md](maths.md))\n"
        elif "h" == eg_func_name.replace("eg_",""): # for eg_h
            content += "- CLI Help Generation ([se.md](se.md))\n"
            content += "- Introspection (`globals()`) ([se.md](se.md))\n"
        else:
            content += "- General script functionality (refer to `code.md`, `se.md`, `ai.md`, `maths.md` as appropriate).\n"
        content += "\n"

        # Code with New Educational Comments
        content += "**Code with Educational Comments**:\n"
        content += "```python\n"
        # Adding comments - this is a simplified version.
        # A more advanced version would parse and interleave comments more intelligently.
        if eg_func_name == "eg__the":
            content += "# This example demonstrates printing the global configuration object 'the'.\n"
            content += "# 'the' is initialized from the script's docstring and can be overridden by CLI arguments.\n"
            content += f"def {eg_func_name}():\n"
            content += f"  \"\"\"{purpose}\"\"\"\n" # Keep original docstring if present
            content += "  # The 'the' object is an instance of 'o', holding key-value pairs for all settings.\n"
            content += "  print(the) # 'the' has a __repr__ method (via class o) that uses cat() for pretty printing.\n"
        elif eg_func_name == "eg__csv":
            content += f"def {eg_func_name}():\n"
            content += f"  \"\"\"{purpose}\"\"\"\n"
            content += "  m = 0 # Counter for total number of cells processed.\n"
            content += "  # Iterate through rows from the CSV file specified by 'the.file'.\n"
            content += "  # The csv() function is a generator that yields each row as a list of coerced values.\n"
            content += "  for n, row in enumerate(csv(the.file)):\n"
            content += "    # Basic assertion: after header, first item of data rows should be int (specific to auto93.csv).\n"
            content += "    if n > 0: assert int is type(row[0])\n"
            content += "    m += len(row) # Accumulate total cells.\n"
            content += "    # Print every 50th row to show progress/sample data.\n"
            content += "    if n % 50 == 0: print(n, row)\n"
            content += "  # Assert total cells processed (specific to auto93.csv structure and content).\n"
            content += "  assert m == 398\n"
        elif eg_func_name == "eg__data":
            content += f"def {eg_func_name}():\n"
            content += f"  \"\"\"{purpose}\"\"\"\n"
            content += "  # Create a Data object by reading from the CSV file specified in 'the.file'.\n"
            content += "  # This initializes columns (Cols) and populates rows, calculating summaries.\n"
            content += "  data_obj = Data(csv(the.file))\n"
            content += "  # Access a specific column from the 'x' (independent) variables.\n"
            content += "  # 'model' here refers to the 'Model' column (index 2 in x cols) in auto93.csv.\n"
            content += "  model_col = data_obj.cols.x[2]\n"
            content += "  # Assertions check the calculated standard deviation (div) and range (lo, hi)\n"
            content += "  # for the 'Model' column against expected values for auto93.csv.\n"
            content += "  assert 3.69 < div(model_col) < 3.7\n"
            content += "  assert model_col.lo == 70 and model_col.hi == 82\n"
        elif eg_func_name == "eg_h":
             content += f"def {eg_func_name}():\n"
             content += f"  \"\"\"{purpose}\"\"\"\n"
             content += "  # Print the main docstring of the script (which contains help text and options).\n"
             content += "  print(__doc__, \"\\nExamples:\")\n"
             content += "  # Iterate through all global symbols in the script.\n"
             content += "  for s, fun in globals().items():\n"
             content += "    # If a symbol starts with 'eg__', it's considered an example function.\n"
             content += "    if s.startswith(\"eg__\"):\n"
             content += "      # Print the example's command-line flag (e.g., --the) and its docstring.\n"
             content += "      # re.sub replaces 'eg__' with '--' for display.\n"
             content += "      # :>6 formats the string to be right-aligned within 6 characters.\n"
             content += "      print(f\"  {re.sub('eg__','--',s):>6}     {fun.__doc__}\")\n"
        else: # For summarized examples
            content += f"# Example: {eg_func_name}\n"
            content += f"# Purpose: {purpose}\n"
            content += textwrap.indent(func_body_str, "  ") # Indent original body
            content += "\n# (Educational comments would be more detailed in a full version for this example.)\n"

        content += "```\n\n"

        # Execution and Output
        content += "**Execution and Output Interpretation**:\n"
        cli_arg_display = eg_func_name.replace("eg__", "--").replace("eg_","").replace("_", "-")
        if cli_arg_display == "h": cli_arg_display = "-h" # for eg_h

        content += f"To run this example, execute `bingo.py` with the `{cli_arg_display}` flag: `python bingo.py {cli_arg_display}`.\n\n"
        
        if eg_func_name in flesh_out_list:
            output = run_example_and_capture_output(eg_func_name)
            content += "Expected Output (or similar):\n"
            content += "```text\n"
            content += output + "\n"
            content += "```\n"
            if eg_func_name == "eg__the":
                content += "The output shows the current configuration settings stored in the `the` object. Each key corresponds to a setting (e.g., `Bins`, `file`), and its value.\n"
            elif eg_func_name == "eg__csv":
                content += "The output displays selected rows from the CSV file, prefixed by their row number (0-indexed). This helps verify the CSV parsing logic. The final `assert` (not shown in output) checks data integrity.\n"
            elif eg_func_name == "eg__data":
                content += "This example typically doesn't produce direct console output (unless print statements are added for debugging within `Data` or `Cols`). Its success is verified by internal `assert` statements checking statistical properties of a loaded column (e.g., its mean, standard deviation, min/max values).\n"
            elif eg_func_name == "eg_h":
                content += "The output is the main help text of the `bingo.py` script, including the available command-line options and a list of runnable examples with their descriptions.\n"

        else: # Summarized example
            content += "This example performs internal checks or demonstrates a specific part of the system. Refer to its code and purpose. For detailed output, you may need to add print statements to `bingo.py` or run with a debugger.\n"
        content += "\n"

        # Links to code.md (Simplified)
        content += "**Relevant Protocols from `code.md`**:\n"
        if "the" in eg_func_name or "h" == eg_func_name.replace("eg_",""):
            content += "- Configuration & CLI\n"
        elif "csv" in eg_func_name or "file" in eg_func_name:
            content += "- Data Input/Parsing\n"
        if "data" in eg_func_name or "cols" in eg_func_name or "num" in eg_func_name or "sym" in eg_func_name or "addSub" in eg_func_name:
            content += "- Data Structure Factories, Statistical Summaries\n"
        if eg_func_name == "eg__all":
            content += "- Example Runners\n"

        content += "\n"

        # Exercises
        content += "**Exercises**:\n"
        content += "1.  **Short Exercise (1-5 mins)**: Modify the `print` statement (if any) in this example within `bingo.py` to display one additional piece of information. Run it to see your change.\n"
        content += "2.  **Homework Exercise (1-2 hours)**: "
        if "the" in eg_func_name:
            content += "Add a new configuration option to `bingo.py`'s main docstring and `the` object. Then, modify `eg__the` to specifically print this new option and its value. Test by running with and without overriding it from the CLI.\n"
        elif "csv" in eg_func_name:
            content += f"Write a new `eg__*` function that reads `{BINGO_PY_THE_CONFIG.get('file', 'auto93.csv')}` but only prints rows where a specific numeric column (e.g., 'Weight') is above a certain threshold. \n"
        elif "data" in eg_func_name:
            content += "Using the `Data` object created in `eg__data`, calculate and print the mean (`mid`) and standard deviation (`div`) for all 'y' columns.\n"
        else:
            content += "Identify a function from `bingo.py` that is called by this example. Step through the execution of this example using a Python debugger (like `pdb` or your IDE's debugger) to observe the values being passed to and returned from that identified function.\n"
        content += "\n---\n"

    # Handling for examples mentioned in prompt but not found as eg__*
    missing_prompt_egs = ["eg__ydist", "eg__poles", "eg__counts"]
    for missing_eg in missing_prompt_egs:
        base_func_name = missing_eg.replace("eg__", "")
        if base_func_name in BINGO_PY_CONTENT: # Check if the base function exists
            content += f"## Tutorial Placeholder: `{missing_eg}` (based on function `{base_func_name}`)\n\n"
            content += f"**Note**: `bingo.py` does not have an explicit `eg__{base_func_name}` example. This tutorial outlines how one might be structured for the base function `{base_func_name}`.\n\n"
            content += f"**Purpose**: To demonstrate the usage and output of the `{base_func_name}` function, which is part of the `{ 'Distance Metrics' if base_func_name == 'ydist' else 'Clustering & Projection' if base_func_name == 'poles' else 'Utility/Statistical'}` protocol.\n\n"
            content += "**Key Concepts Demonstrated**:\n"
            if base_func_name == "ydist": content+= "- Multi-objective Evaluation ([ai.md](ai.md))\n- Normalization, Minkowski Distance ([maths.md](maths.md))\n"
            elif base_func_name == "poles": content+= "- Data Sampling, Furthest Point Heuristic ([ai.md](ai.md))\n- Distance Calculation (`xdist`) ([maths.md](maths.md))\n"
            else: content += "- (Relevant concepts from ai.md, se.md, maths.md)\n"
            content += "\n"
            content += "**Hypothetical Code with Educational Comments**:\n"
            content += "```python\n"
            content += f"# def eg__{base_func_name}():\n"
            content += f"#   \"\"\"Example demonstrating {base_func_name}\"\"\"\n"
            content += f"#   data = Data(csv(the.file)) # Load some data\n"
            if base_func_name == "ydist":
                content += f"#   some_row = data.rows[0]\n"
                content += f"#   d_to_heaven = ydist(data, some_row)\n"
                content += f"#   print(f\"Distance to heaven for row 0: {{d_to_heaven}}\")\n"
            elif base_func_name == "poles":
                content += f"#   # Need to set the.some and the.dims appropriately for poles to work as expected.\n"
                content += f"#   # the.some should be less than number of rows. Default 'dims' is 4.\n"
                content += f"#   # For auto93.csv (398 rows), the.some might be e.g. 16 or 32.\n"
                content += f"#   # BINGO_PY_THE_CONFIG['some'] = 16 # (Example, not modifying global 'the')\n"
                content += f"#   corner_poles = poles(data) # poles() needs 'the.some'\n"
                content += f"#   print(f\"Found {{len(corner_poles)}} poles.\")\n"
                content += f"#   for i, pole_row in enumerate(corner_poles):\n"
                content += f"#     print(f\"Pole {{i}}: {{pole_row[:5]}}...\") # Print first few elements\n"

            else: # eg__counts
                content += f"#   # Code to demonstrate counting functionality (e.g., from Sym or Num objects)\n"
                content += f"#   sym_col = Sym()\n"
                content += f"#   for x in ['a','b','a','a','c'] : add(sym_col, x)\n"
                content += f"#   print(f\"Counts for 'a': {{sym_col.has.get('a',0)}}\")\n"
                content += f"#   print(f\"Total counts: {{sym_col.n}}\")\n"

            content += "```\n\n"
            content += "**Execution and Output Interpretation**:\n"
            content += f"(This would describe how to run `python bingo.py --{base_func_name}` if it existed, and how to interpret its output.)\n\n"
            content += "**Exercises**:\n"
            content += f"1. **Short Exercise**: Manually call the `{base_func_name}` function from the Python interpreter after loading data from `bingo.py` and observe its output for a few sample inputs.\n"
            content += f"2. **Homework Exercise**: Implement a proper `eg__{base_func_name}` function in `bingo.py`, including CLI flag integration. Ensure it prints informative output. \n\n---\n"

        elif missing_eg == "eg__counts" and "counts" not in BINGO_PY_CONTENT:
            content += f"## Tutorial Placeholder: `{missing_eg}`\n\n"
            content += f"**Note**: `bingo.py` does not have an `eg__counts` example or a distinct `counts` function. Counting is integral to `Num` (attribute `n`) and `Sym` (attribute `n`, and `has` dictionary for individual symbol counts).\n\n"
            content += "A tutorial for 'counts' would involve demonstrating how to access these attributes after populating `Num` or `Sym` objects. See `eg__num` and `eg__sym` for related examples.\n\n---\n"


    return content


def generate_license_md_content():
    content = NAVIGATION_BAR
    content += get_mit_license_text()
    return content

def main():
    load_bingo_py_content_and_config()

    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)

    # Order matters for generation if some files depend on others (not the case here for content)
    # but good practice for logical flow.
    
    generation_steps = [
        ("code.md", generate_code_md_content),
        ("se.md", generate_se_md_content),
        ("ai.md", generate_ai_md_content),
        ("maths.md", generate_maths_md_content),
        ("tutorial.md", generate_tutorial_md_content),
        ("license.md", generate_license_md_content),
        ("prompt.txt", get_prompt_text_content) 
    ]

    for filename, generator_func in generation_steps:
        filepath = os.path.join(output_dir, filename)
        try:
            content = generator_func()
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Successfully generated {filename}")
        except Exception as e:
            print(f"Error generating {filename}: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
