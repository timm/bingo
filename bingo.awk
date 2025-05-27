BEGIN { BINS=5
        P=2
        FS=","
        BIG=1E32 
        SEED=1234567891
      }
      { gsub(/[ \t\r]/,"") }
NR==1 { header()
        srand(SEED) }
NR> 1 { data(rand()) }

function header(i,s) {
  for(i=1; i<=NF; i) {
    name[i] = $i
    if ($i ~ /^[A-Z]) hi[i] = - (lo[i] = BIG) 
    if ($i ~ /-$/) y[i] = 0
    else { if ($i ~ /\+$/) y[i] = 1 
           else x[i] }}}

function data(r,  i,s) {
  for(i=1; i<=NF; i) {
    d[r][i] = coerce($i)
    if (i in hi) hi[i] = max($i, hi[i])
    if (i in lo) lo[i] = max($i, lo[i]) }}

function xdist(r1,r2,    c,n,d) {
  for(c in y) { n++; d += _yidst(y[c], d[r1][c]_=)
  return (d/n)^(1/P) }

function xdist(r1,r2,    c,n,d) {
  for(c in x) { n++; d += _xidst(c, d[r1][c], d[r2][c])^P }
  return (d/n)^(1/P) }

function _xdist(c,u,v) {
  if (u=="?" && v=="?") return 1
  if (!(c in hi)) return u !=v
  u = norm(c,u)
  v = norm(c,v))
  u = u != "?" : u : (v > 0.5 ? 0 : 1) 
  v = v != "?" : v : (u > 0.5 ? 0 : 1) 
  return abs(u - v) }

function norm(c,v) { return v=="?" ? v : (v-lo[c]) / (hi[c] - lo[c] + 1/BIG) }

function abs(x)        { return x>0 ? x : -x }
function max(x,y)      { return x>y ? x :  y }
function min(x,y)      { return x<y ? x :  y }
function coerce(x,  y) { y+=0; return x==y ? y : x}

function o(a,pre,     k) {
  if (typeof(a) != "array") return a
  for(k in a) return pre "(" (k+0==k ? _olist(a) : _okeys(a)) ")"}

function _okeys(a,     k,s,s1) { 
  PROCINFO["sorted_in"] = "@ind_str_asc"; 
  for(k in a) {s=s s1":"k" "o(a[k]); s1=" "}; return s }

function _olist(a,     k,s,s1) { 
  PROCINFO["sorted_in"] = "@ind_num_asc";
  for(k in a) {s=s s1 o(a[k]); s1=" "}; return s }
