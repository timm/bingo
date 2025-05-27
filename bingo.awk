#!/usr/bin/env gawk -f
BEGIN { BINS=5
        P=2
        FS=","
        BIG=1E32 
        SEED=1234567891
      }
      { gsub(/[ \t\r]/,"") }
NR==1 { header();
        srand(SEED) }
NR> 1 { data(rand()) }
END   { 
        print(ok(Hi))
        print(ok(Lo))
        print(ok(Y))
        rogues()
      }

function rogues(  k) {
  for(k in SYMTAB) 
    if (!(k ~ /^[A-Z]/)) print("??", k) }

function header(i,s) {
  for(i=1; i<=NF; i++) {
    Name[i] = $i
    if ($i ~ /^[A-Z]/) Hi[i] = - (Lo[i] = BIG) 
    if (!($i ~ /X$/)) {
      if ($i ~ /-$/) Y[i] = 0
      else { if ($i ~ /\+$/) Y[i] = 1 
             else X[i] }}}}

function data(r,  i,s,v) {
  for(i=1; i<=NF; i++) {
    v = D[r][i] = coerce($i)
    if (v !="?") { 
      if (i in Hi) Hi[i] = max($i, Hi[i])
      if (i in Lo) Lo[i] = min($i, Lo[i]) }}}

function ydist(r1,r2,    c,n,d) {
  for(c in Y) { 
    n++
    d += abs(Y[c] - norm(c,D[r1][c]))^P }
  return (d/n)^(1/P) }

function xdist(r1,r2,    c,n,d) {
  for(c in Name) 
    if (!(c in Y))
       { n++
         d += _xidst(c, D[r1][c], D[r2][c])^P }
  return (d/n)^(1/P) }

function _xdist(c,u,v) {
  if (u=="?" && v=="?") return 1
  if (!(c in Hi)) return u !=v
  u = norm(c,u)
  v = norm(c,v)
  u = u != "?" ? u : (v > 0.5 ? 0 : 1) 
  v = v != "?" ? v : (u > 0.5 ? 0 : 1) 
  return abs(u - v) }

function norm(c,v) { 
  return v=="?" ? v : (v-Lo[c]) / (Hi[c] - Lo[c] + 1/BIG) }

function abs(x)        { return x>0 ? x : -x }
function max(x,y)      { return x>y ? x :  y }
function min(x,y)      { return x<y ? x :  y }
function coerce(x,  y) { y= x+0; return x==y ? y : x}

function oo(a) { print(o(a)) }

function o(a,     k) {
  if (typeof(a) != "array") return a
  for(k in a) return (k+0==k ? ol(a) : ok(a))} 

function ok(a,     k,s,s1) { 
  for(k in a) {s=s s1":"k" "o(a[k]); s1=" "}; return "("s")" }

function ol(a,     k,s,s1) { 
  for(k in a) {s=s s1 o(a[k]); s1=", "}; return "("s")" }
