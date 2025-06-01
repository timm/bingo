"""
bingo.py: stochastic landscape analysis for multi objective reasoning
(c) 2025 Tim Menseedzies, <timm@ieee.org>. MIT license

Options:
  -h             show help 
  -b     bins    set bins (5)
  -d     dims    set dimensions (5)
  -f     file    file name (../moot/optimize/misc/au
  -p     p       set mankowski coeffecient (2)
  -s     seed    set random number seed (123456781)

"""
import traceback,random,sys

class o:
  __init__= lambda i, **d: i.__dict__.update(**d)
  __repr__= lambda i: str({k:v for k,v in i.__dict__.items() if str(k)[0]!="_"})

the = o(file = "../moot/optimize/misc/auto93.csv",
        p    = 2,
        dims = 5,
        bins = 5,
        seed = 1234567891)

random.seed(the.seed)

#------------------------------------------------------------------------------
def Data(): return o(rows=[], names={}, y={}, hi={},lo={})

def x(data,row):
  for c,use in data.names.items():
    if use and c not in y: 
      v = row[c]
      if v != "?": yield v,c

def y(data,row):
  for c,w in data.y.items():
    return row[c],c,w

#------------------------------------------------------------------------------
def atom(x):
  for what in (int, float):
    try: return what(x)
    except Exception: pass
  x = x.strip()
  y = x.lower()
  return (y == "true") if y in ("true", "false") else x

#------------------------------------------------------------------------------
def eg_h(_): 
  ":        show help"
  print(__doc__)
  for s,fn in globals().items():
    if s.startswith("eg_"):
      print(f"  {s[2:].replace("_","-"):6s} {fn.__doc__[1:]}")

def eg__the(_): 
  ":        show config file"
  print(the)

#------------------------------------------------------------------------------
def run(fn,x=None):
  try: random.seed(the.seed); fn(x)
  except Exception as e:
    return [print(s.strip()) for s in traceback.format_tb(e.__traceback__)]

if __name__ == "__main__":
  for i,s in enumerate(sys.argv):
    if fn := globals().get("eg" + s.replace("-", "_")):
      run(fn, None if i == len(sys.argv) - 1 else atom(sys.argv[i+1]))
