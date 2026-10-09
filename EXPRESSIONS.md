# Technical Documentation: Expressions for Cn (n < 10)

Catalog of topologically distinct non-intersecting circle arrangements for every figure Cn with 1 ≤ n < 10. Each expression is a canonical nested-parentheses word produced by `generate_rooted_trees(n + 1)`: one pair of parentheses is one circle, factors commute, and the implicit outer root is the plane (equivalently, the equatorial circle used to pass to the sphere).

A flip, as defined by Mathar (arXiv:1603.00077, Section 2.2), starts from a nested expression `A (B)` and ends at `(A) B`. `A` and `B` are well-formed, possibly empty, subexpressions. Operationally: choose one top-level factor, move it to the right (order of the remaining factors is kept), and tear that factor across the back of the sphere.

- `B` is the interior of the chosen factor.
- `A` is the concatenation of the other factors.
- The written form `A (B)` is the parentheses word `A` + `(` + `B` + `)`. Spaces in the paper's `A ( B )` are not part of the word.
- The image `(A) B` is rewritten in canonical factor order. Equal factors make some flips fixed points. Those fixed points are not edges of the EPS graphs.

The two examples in the paper are the n = 3 case:

| source | chosen factor | A | B | A (B) | (A) B |
|--------|---------------|---|---|-------|-------|
| `()()()` | any `()` | `()()` | empty | `()()()` | `(()())` |
| `(())()` | the `()` factor | `(())` | empty | `(())()` | `((()))` |
| `(())()` | the `(())` factor | `()` | `()` | `()(())` | `(())()` (fixed; same as the source) |

Three views are recorded below, in the forms used to check the implementation, for every Cn with n < 10:

- **A** — EPS / DOT generation counts (rooted trees, clusters, nodes, edges)
- **B** — flip-equivalence cluster size summaries
- **C** — cluster membership, each expression with its factor count, and every factor flip written as `A (B)` → `(A) B`

Reproduce the counts with:

```bash
python generate_eps.py 1 2 3 4 5 6 7 8 9
python flip_transforms.py
```

`generate_eps.py` with no arguments still draws C4–C9, the range of the paper figures and their extensions. Passing `1` through `9` is the full n < 10 range. Graphviz (`dot`) is required only for the EPS step. The DOT graphs and the expression tables do not need it.

## Summary

| Cn | rooted trees (A000081, n+1 nodes) | clusters (A000055) | DOT nodes | DOT edges | factor flips |
|----|-----------------------------------:|-------------------:|----------:|----------:|-------------:|
| C1 | 1 | 1 | 1 | 0 | 1 |
| C2 | 2 | 1 | 2 | 1 | 3 |
| C3 | 4 | 2 | 4 | 2 | 7 |
| C4 | 9 | 3 | 9 | 6 | 17 |
| C5 | 20 | 6 | 20 | 14 | 39 |
| C6 | 48 | 11 | 48 | 37 | 96 |
| C7 | 115 | 23 | 115 | 92 | 232 |
| C8 | 286 | 47 | 286 | 239 | 583 |
| C9 | 719 | 106 | 719 | 613 | 1474 |

Rooted-tree counts are OEIS A000081 at index n+1 (the expressions are trees on n+1 nodes). Cluster counts are OEIS A000055 at the same index: the number of flip-equivalence classes, which is the number of distinct embeddings on the sphere.

## A — EPS Diagram Generation

Expected report of `python generate_eps.py 1 2 3 4 5 6 7 8 9`. Node and edge counts are those `generate_dot_file` writes before Graphviz is invoked. `Generated Cn.eps` is the line printed when `dot -Tps` succeeds.

```
EPS Diagram Generator for Circle Topologies
============================================================

Expected counts:
  C1: 1 rooted trees, 1 clusters
  C2: 2 rooted trees, 1 clusters
  C3: 4 rooted trees, 2 clusters
  C4: 9 rooted trees, 3 clusters
  C5: 20 rooted trees, 6 clusters
  C6: 48 rooted trees, 11 clusters
  C7: 115 rooted trees, 23 clusters
  C8: 286 rooted trees, 47 clusters
  C9: 719 rooted trees, 106 clusters

Generating C1...
  Generated C1.dot: 1 nodes, 0 edges
  Generated C1.eps

Generating C2...
  Generated C2.dot: 2 nodes, 1 edges
  Generated C2.eps

Generating C3...
  Generated C3.dot: 4 nodes, 2 edges
  Generated C3.eps

Generating C4...
  Generated C4.dot: 9 nodes, 6 edges
  Generated C4.eps

Generating C5...
  Generated C5.dot: 20 nodes, 14 edges
  Generated C5.eps

Generating C6...
  Generated C6.dot: 48 nodes, 37 edges
  Generated C6.eps

Generating C7...
  Generated C7.dot: 115 nodes, 92 edges
  Generated C7.eps

Generating C8...
  Generated C8.dot: 286 nodes, 239 edges
  Generated C8.eps

Generating C9...
  Generated C9.dot: 719 nodes, 613 edges
  Generated C9.eps

============================================================
Generated 9/9 EPS files
```

Verification of this report:

- Fresh `generate_dot_file` output for C4–C9 is byte-identical to the committed `arXiv-1603.00077v2/C4.dot`–`C9.dot` files. Their edge counts are the numbers above, including the recorded C7–C9 run (115 nodes / 92 edges, 286 / 239, 719 / 613).
- `C1.dot`, `C2.dot`, and `C3.dot` are that same generator's output for the three smaller figures. Those figures already had EPS files; the DOT sources complete the n < 10 set.
- `C1.eps`–`C9.eps` are in `arXiv-1603.00077v2/`. Redrawing an EPS file requires Graphviz. The expression graph (nodes and edges) is fully determined by the DOT file and does not depend on the layout engine.

## B — Cluster Size Summaries

Summary lines from `python flip_transforms.py` for every Cn with n < 10. Cluster sizes are sorted descending. This is the size multiset of the sphere-equivalence classes, not the discovery order used in section C.

```
Flip Transformation Analysis for 1 circles
Total topologies: 1
Number of flip-equivalence clusters: 1
Cluster sizes: [1]

Flip Transformation Analysis for 2 circles
Total topologies: 2
Number of flip-equivalence clusters: 1
Cluster sizes: [2]

Flip Transformation Analysis for 3 circles
Total topologies: 4
Number of flip-equivalence clusters: 2
Cluster sizes: [2, 2]

Flip Transformation Analysis for 4 circles
Total topologies: 9
Number of flip-equivalence clusters: 3
Cluster sizes: [4, 3, 2]

Flip Transformation Analysis for 5 circles
Total topologies: 20
Number of flip-equivalence clusters: 6
Cluster sizes: [5, 4, 4, 3, 2, 2]

Flip Transformation Analysis for 6 circles
Total topologies: 48
Number of flip-equivalence clusters: 11
Cluster sizes: [7, 6, 6, 5, 4, 4, 4, 4, 3, 3, 2]

Flip Transformation Analysis for 7 circles
Total topologies: 115
Number of flip-equivalence clusters: 23
Cluster sizes: [8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 2, 2]

Flip Transformation Analysis for 8 circles
Total topologies: 286
Number of flip-equivalence clusters: 47
Cluster sizes: [9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 3, 2]

Flip Transformation Analysis for 9 circles
Total topologies: 719
Number of flip-equivalence clusters: 106
Cluster sizes: [10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 2]
```

## C — Cluster Membership and Flips of the Form A (B)

Full membership for every Cn with n < 10. Cluster numbers follow discovery order in `find_flip_clusters`: expressions are visited in lexicographic order, and a new cluster starts at the first expression not yet reached by a flip. Inside a cluster, expressions are sorted lexicographically. The bracketed integer is the number of top-level factors.

Each following flip block lists one line per top-level factor. Fields:

- `source` — canonical expression
- `factor` — 1-based index of the chosen top-level factor, in left-to-right order
- `A`, `B` — the paper's subexpressions for that factor
- `form` — the word `A(B)` after the chosen factor is moved to the right
- `image` — canonical `(A) B`
- `fixed` — present when the image is the source (no EPS edge)

```
# source | factor | A | B | form=A(B) | image=(A)B
```

### C1

1 expression, 1 cluster, 0 undirected flip edges, 1 factor flip of the form A (B) → (A) B.

```
Flip Transformation Analysis for 1 circles
============================================================
Total topologies: 1
Number of flip-equivalence clusters: 1
Cluster sizes: [1]

Clusters:
  Cluster 1 (size 1):
    () [1 factors]

Note: Each cluster represents circle topologies that are equivalent when embedded on a sphere surface.
```

Flips of the form `A (B)` → `(A) B`:

```
# source | factor | A | B | form=A(B) | image=(A)B
source=() | factor=1 | A= | B= | form=() | image=() | fixed
```

### C2

2 expressions, 1 cluster, 1 undirected flip edge, 3 factor flips of the form A (B) → (A) B.

```
Flip Transformation Analysis for 2 circles
============================================================
Total topologies: 2
Number of flip-equivalence clusters: 1
Cluster sizes: [2]

Clusters:
  Cluster 1 (size 2):
    (()) [1 factors]
    ()() [2 factors]

Note: Each cluster represents circle topologies that are equivalent when embedded on a sphere surface.
```

Flips of the form `A (B)` → `(A) B`:

```
# source | factor | A | B | form=A(B) | image=(A)B
source=(()) | factor=1 | A= | B=() | form=(()) | image=()()
source=()() | factor=1 | A=() | B= | form=()() | image=(())
source=()() | factor=2 | A=() | B= | form=()() | image=(())
```

### C3

4 expressions, 2 clusters, 2 undirected flip edges, 7 factor flips of the form A (B) → (A) B.

```
Flip Transformation Analysis for 3 circles
============================================================
Total topologies: 4
Number of flip-equivalence clusters: 2
Cluster sizes: [2, 2]

Clusters:
  Cluster 1 (size 2):
    ((())) [1 factors]
    (())() [2 factors]
  Cluster 2 (size 2):
    (()()) [1 factors]
    ()()() [3 factors]

Note: Each cluster represents circle topologies that are equivalent when embedded on a sphere surface.
```

Flips of the form `A (B)` → `(A) B`:

```
# source | factor | A | B | form=A(B) | image=(A)B
source=((())) | factor=1 | A= | B=(()) | form=((())) | image=(())()
source=(()()) | factor=1 | A= | B=()() | form=(()()) | image=()()()
source=(())() | factor=1 | A=() | B=() | form=()(()) | image=(())() | fixed
source=(())() | factor=2 | A=(()) | B= | form=(())() | image=((()))
source=()()() | factor=1 | A=()() | B= | form=()()() | image=(()())
source=()()() | factor=2 | A=()() | B= | form=()()() | image=(()())
source=()()() | factor=3 | A=()() | B= | form=()()() | image=(()())
```

### C4

9 expressions, 3 clusters, 6 undirected flip edges, 17 factor flips of the form A (B) → (A) B.

```
Flip Transformation Analysis for 4 circles
============================================================
Total topologies: 9
Number of flip-equivalence clusters: 3
Cluster sizes: [4, 3, 2]

Clusters:
  Cluster 1 (size 3):
    (((()))) [1 factors]
    ((()))() [2 factors]
    (())(()) [2 factors]
  Cluster 2 (size 4):
    ((()())) [1 factors]
    ((())()) [1 factors]
    (()())() [2 factors]
    (())()() [3 factors]
  Cluster 3 (size 2):
    (()()()) [1 factors]
    ()()()() [4 factors]

Note: Each cluster represents circle topologies that are equivalent when embedded on a sphere surface.
```

Flips of the form `A (B)` → `(A) B`:

```
# source | factor | A | B | form=A(B) | image=(A)B
source=(((()))) | factor=1 | A= | B=((())) | form=(((()))) | image=((()))()
source=((()())) | factor=1 | A= | B=(()()) | form=((()())) | image=(()())()
source=((())()) | factor=1 | A= | B=(())() | form=((())()) | image=(())()()
source=((()))() | factor=1 | A=() | B=(()) | form=()((())) | image=(())(())
source=((()))() | factor=2 | A=((())) | B= | form=((()))() | image=(((())))
source=(()()()) | factor=1 | A= | B=()()() | form=(()()()) | image=()()()()
source=(()())() | factor=1 | A=() | B=()() | form=()(()()) | image=(())()()
source=(()())() | factor=2 | A=(()()) | B= | form=(()())() | image=((()()))
source=(())(()) | factor=1 | A=(()) | B=() | form=(())(()) | image=((()))()
source=(())(()) | factor=2 | A=(()) | B=() | form=(())(()) | image=((()))()
source=(())()() | factor=1 | A=()() | B=() | form=()()(()) | image=(()())()
source=(())()() | factor=2 | A=(())() | B= | form=(())()() | image=((())())
source=(())()() | factor=3 | A=(())() | B= | form=(())()() | image=((())())
source=()()()() | factor=1 | A=()()() | B= | form=()()()() | image=(()()())
source=()()()() | factor=2 | A=()()() | B= | form=()()()() | image=(()()())
source=()()()() | factor=3 | A=()()() | B= | form=()()()() | image=(()()())
source=()()()() | factor=4 | A=()()() | B= | form=()()()() | image=(()()())
```

### C5

20 expressions, 6 clusters, 14 undirected flip edges, 39 factor flips of the form A (B) → (A) B.

```
Flip Transformation Analysis for 5 circles
============================================================
Total topologies: 20
Number of flip-equivalence clusters: 6
Cluster sizes: [5, 4, 4, 3, 2, 2]

Clusters:
  Cluster 1 (size 3):
    ((((())))) [1 factors]
    (((())))() [2 factors]
    (())((())) [2 factors]
  Cluster 2 (size 5):
    (((()()))) [1 factors]
    (((()))()) [1 factors]
    ((()()))() [2 factors]
    ((()))()() [3 factors]
    (()())(()) [2 factors]
  Cluster 3 (size 4):
    (((())())) [1 factors]
    ((())(())) [1 factors]
    ((())())() [2 factors]
    (())(())() [3 factors]
  Cluster 4 (size 4):
    ((()()())) [1 factors]
    ((())()()) [1 factors]
    (()()())() [2 factors]
    (())()()() [4 factors]
  Cluster 5 (size 2):
    ((()())()) [1 factors]
    (()())()() [3 factors]
  Cluster 6 (size 2):
    (()()()()) [1 factors]
    ()()()()() [5 factors]

Note: Each cluster represents circle topologies that are equivalent when embedded on a sphere surface.
```

Flips of the form `A (B)` → `(A) B`:

```
# source | factor | A | B | form=A(B) | image=(A)B
source=((((())))) | factor=1 | A= | B=(((()))) | form=((((())))) | image=(((())))()
source=(((()()))) | factor=1 | A= | B=((()())) | form=(((()()))) | image=((()()))()
source=(((())())) | factor=1 | A= | B=((())()) | form=(((())())) | image=((())())()
source=(((()))()) | factor=1 | A= | B=((()))() | form=(((()))()) | image=((()))()()
source=(((())))() | factor=1 | A=() | B=((())) | form=()(((()))) | image=(())((()))
source=(((())))() | factor=2 | A=(((()))) | B= | form=(((())))() | image=((((()))))
source=((()()())) | factor=1 | A= | B=(()()()) | form=((()()())) | image=(()()())()
source=((()())()) | factor=1 | A= | B=(()())() | form=((()())()) | image=(()())()()
source=((()()))() | factor=1 | A=() | B=(()()) | form=()((()())) | image=(()())(())
source=((()()))() | factor=2 | A=((()())) | B= | form=((()()))() | image=(((()())))
source=((())(())) | factor=1 | A= | B=(())(()) | form=((())(())) | image=(())(())()
source=((())()()) | factor=1 | A= | B=(())()() | form=((())()()) | image=(())()()()
source=((())())() | factor=1 | A=() | B=(())() | form=()((())()) | image=(())(())()
source=((())())() | factor=2 | A=((())()) | B= | form=((())())() | image=(((())()))
source=((()))()() | factor=1 | A=()() | B=(()) | form=()()((())) | image=(()())(())
source=((()))()() | factor=2 | A=((()))() | B= | form=((()))()() | image=(((()))())
source=((()))()() | factor=3 | A=((()))() | B= | form=((()))()() | image=(((()))())
source=(()()()()) | factor=1 | A= | B=()()()() | form=(()()()()) | image=()()()()()
source=(()()())() | factor=1 | A=() | B=()()() | form=()(()()()) | image=(())()()()
source=(()()())() | factor=2 | A=(()()()) | B= | form=(()()())() | image=((()()()))
source=(()())(()) | factor=1 | A=(()) | B=()() | form=(())(()()) | image=((()))()()
source=(()())(()) | factor=2 | A=(()()) | B=() | form=(()())(()) | image=((()()))()
source=(()())()() | factor=1 | A=()() | B=()() | form=()()(()()) | image=(()())()() | fixed
source=(()())()() | factor=2 | A=(()())() | B= | form=(()())()() | image=((()())())
source=(()())()() | factor=3 | A=(()())() | B= | form=(()())()() | image=((()())())
source=(())((())) | factor=1 | A=((())) | B=() | form=((()))(()) | image=(((())))()
source=(())((())) | factor=2 | A=(()) | B=(()) | form=(())((())) | image=(())((())) | fixed
source=(())(())() | factor=1 | A=(())() | B=() | form=(())()(()) | image=((())())()
source=(())(())() | factor=2 | A=(())() | B=() | form=(())()(()) | image=((())())()
source=(())(())() | factor=3 | A=(())(()) | B= | form=(())(())() | image=((())(()))
source=(())()()() | factor=1 | A=()()() | B=() | form=()()()(()) | image=(()()())()
source=(())()()() | factor=2 | A=(())()() | B= | form=(())()()() | image=((())()())
source=(())()()() | factor=3 | A=(())()() | B= | form=(())()()() | image=((())()())
source=(())()()() | factor=4 | A=(())()() | B= | form=(())()()() | image=((())()())
source=()()()()() | factor=1 | A=()()()() | B= | form=()()()()() | image=(()()()())
source=()()()()() | factor=2 | A=()()()() | B= | form=()()()()() | image=(()()()())
source=()()()()() | factor=3 | A=()()()() | B= | form=()()()()() | image=(()()()())
source=()()()()() | factor=4 | A=()()()() | B= | form=()()()()() | image=(()()()())
source=()()()()() | factor=5 | A=()()()() | B= | form=()()()()() | image=(()()()())
```

### C6

48 expressions, 11 clusters, 37 undirected flip edges, 96 factor flips of the form A (B) → (A) B.

```
Flip Transformation Analysis for 6 circles
============================================================
Total topologies: 48
Number of flip-equivalence clusters: 11
Cluster sizes: [7, 6, 6, 5, 4, 4, 4, 4, 3, 3, 2]

Clusters:
  Cluster 1 (size 4):
    (((((()))))) [1 factors]
    ((((()))))() [2 factors]
    ((()))((())) [2 factors]
    (())(((()))) [2 factors]
  Cluster 2 (size 6):
    ((((()())))) [1 factors]
    ((((())))()) [1 factors]
    (((()())))() [2 factors]
    (((())))()() [3 factors]
    (()())((())) [2 factors]
    (())((()())) [2 factors]
  Cluster 3 (size 7):
    ((((())()))) [1 factors]
    ((((()))())) [1 factors]
    (((())()))() [2 factors]
    (((()))())() [2 factors]
    ((())((()))) [1 factors]
    (())((())()) [2 factors]
    (())((()))() [3 factors]
  Cluster 4 (size 5):
    (((()()()))) [1 factors]
    (((()))()()) [1 factors]
    ((()()()))() [2 factors]
    ((()))()()() [4 factors]
    (()()())(()) [2 factors]
  Cluster 5 (size 6):
    (((()())())) [1 factors]
    (((())())()) [1 factors]
    ((()())(())) [1 factors]
    ((()())())() [2 factors]
    ((())())()() [3 factors]
    (()())(())() [3 factors]
  Cluster 6 (size 3):
    (((()()))()) [1 factors]
    ((()()))()() [3 factors]
    (()())(()()) [2 factors]
  Cluster 7 (size 3):
    (((())(()))) [1 factors]
    ((())(()))() [2 factors]
    (())(())(()) [3 factors]
  Cluster 8 (size 4):
    (((())()())) [1 factors]
    ((())(())()) [1 factors]
    ((())()())() [2 factors]
    (())(())()() [4 factors]
  Cluster 9 (size 4):
    ((()()()())) [1 factors]
    ((())()()()) [1 factors]
    (()()()())() [2 factors]
    (())()()()() [5 factors]
  Cluster 10 (size 4):
    ((()()())()) [1 factors]
    ((()())()()) [1 factors]
    (()()())()() [3 factors]
    (()())()()() [4 factors]
  Cluster 11 (size 2):
    (()()()()()) [1 factors]
    ()()()()()() [6 factors]

Note: Each cluster represents circle topologies that are equivalent when embedded on a sphere surface.
```

Flips of the form `A (B)` → `(A) B`:

```
# source | factor | A | B | form=A(B) | image=(A)B
source=(((((()))))) | factor=1 | A= | B=((((())))) | form=(((((()))))) | image=((((()))))()
source=((((()())))) | factor=1 | A= | B=(((()()))) | form=((((()())))) | image=(((()())))()
source=((((())()))) | factor=1 | A= | B=(((())())) | form=((((())()))) | image=(((())()))()
source=((((()))())) | factor=1 | A= | B=(((()))()) | form=((((()))())) | image=(((()))())()
source=((((())))()) | factor=1 | A= | B=(((())))() | form=((((())))()) | image=(((())))()()
source=((((()))))() | factor=1 | A=() | B=(((()))) | form=()((((())))) | image=(())(((())))
source=((((()))))() | factor=2 | A=((((())))) | B= | form=((((()))))() | image=(((((())))))
source=(((()()()))) | factor=1 | A= | B=((()()())) | form=(((()()()))) | image=((()()()))()
source=(((()())())) | factor=1 | A= | B=((()())()) | form=(((()())())) | image=((()())())()
source=(((()()))()) | factor=1 | A= | B=((()()))() | form=(((()()))()) | image=((()()))()()
source=(((()())))() | factor=1 | A=() | B=((()())) | form=()(((()()))) | image=(())((()()))
source=(((()())))() | factor=2 | A=(((()()))) | B= | form=(((()())))() | image=((((()()))))
source=(((())(()))) | factor=1 | A= | B=((())(())) | form=(((())(()))) | image=((())(()))()
source=(((())()())) | factor=1 | A= | B=((())()()) | form=(((())()())) | image=((())()())()
source=(((())())()) | factor=1 | A= | B=((())())() | form=(((())())()) | image=((())())()()
source=(((())()))() | factor=1 | A=() | B=((())()) | form=()(((())())) | image=(())((())())
source=(((())()))() | factor=2 | A=(((())())) | B= | form=(((())()))() | image=((((())())))
source=(((()))()()) | factor=1 | A= | B=((()))()() | form=(((()))()()) | image=((()))()()()
source=(((()))())() | factor=1 | A=() | B=((()))() | form=()(((()))()) | image=(())((()))()
source=(((()))())() | factor=2 | A=(((()))()) | B= | form=(((()))())() | image=((((()))()))
source=(((())))()() | factor=1 | A=()() | B=((())) | form=()()(((()))) | image=(()())((()))
source=(((())))()() | factor=2 | A=(((())))() | B= | form=(((())))()() | image=((((())))())
source=(((())))()() | factor=3 | A=(((())))() | B= | form=(((())))()() | image=((((())))())
source=((()()()())) | factor=1 | A= | B=(()()()()) | form=((()()()())) | image=(()()()())()
source=((()()())()) | factor=1 | A= | B=(()()())() | form=((()()())()) | image=(()()())()()
source=((()()()))() | factor=1 | A=() | B=(()()()) | form=()((()()())) | image=(()()())(())
source=((()()()))() | factor=2 | A=((()()())) | B= | form=((()()()))() | image=(((()()())))
source=((()())(())) | factor=1 | A= | B=(()())(()) | form=((()())(())) | image=(()())(())()
source=((()())()()) | factor=1 | A= | B=(()())()() | form=((()())()()) | image=(()())()()()
source=((()())())() | factor=1 | A=() | B=(()())() | form=()((()())()) | image=(()())(())()
source=((()())())() | factor=2 | A=((()())()) | B= | form=((()())())() | image=(((()())()))
source=((()()))()() | factor=1 | A=()() | B=(()()) | form=()()((()())) | image=(()())(()())
source=((()()))()() | factor=2 | A=((()()))() | B= | form=((()()))()() | image=(((()()))())
source=((()()))()() | factor=3 | A=((()()))() | B= | form=((()()))()() | image=(((()()))())
source=((())((()))) | factor=1 | A= | B=(())((())) | form=((())((()))) | image=(())((()))()
source=((())(())()) | factor=1 | A= | B=(())(())() | form=((())(())()) | image=(())(())()()
source=((())(()))() | factor=1 | A=() | B=(())(()) | form=()((())(())) | image=(())(())(())
source=((())(()))() | factor=2 | A=((())(())) | B= | form=((())(()))() | image=(((())(())))
source=((())()()()) | factor=1 | A= | B=(())()()() | form=((())()()()) | image=(())()()()()
source=((())()())() | factor=1 | A=() | B=(())()() | form=()((())()()) | image=(())(())()()
source=((())()())() | factor=2 | A=((())()()) | B= | form=((())()())() | image=(((())()()))
source=((())())()() | factor=1 | A=()() | B=(())() | form=()()((())()) | image=(()())(())()
source=((())())()() | factor=2 | A=((())())() | B= | form=((())())()() | image=(((())())())
source=((())())()() | factor=3 | A=((())())() | B= | form=((())())()() | image=(((())())())
source=((()))((())) | factor=1 | A=((())) | B=(()) | form=((()))((())) | image=(())(((())))
source=((()))((())) | factor=2 | A=((())) | B=(()) | form=((()))((())) | image=(())(((())))
source=((()))()()() | factor=1 | A=()()() | B=(()) | form=()()()((())) | image=(()()())(())
source=((()))()()() | factor=2 | A=((()))()() | B= | form=((()))()()() | image=(((()))()())
source=((()))()()() | factor=3 | A=((()))()() | B= | form=((()))()()() | image=(((()))()())
source=((()))()()() | factor=4 | A=((()))()() | B= | form=((()))()()() | image=(((()))()())
source=(()()()()()) | factor=1 | A= | B=()()()()() | form=(()()()()()) | image=()()()()()()
source=(()()()())() | factor=1 | A=() | B=()()()() | form=()(()()()()) | image=(())()()()()
source=(()()()())() | factor=2 | A=(()()()()) | B= | form=(()()()())() | image=((()()()()))
source=(()()())(()) | factor=1 | A=(()) | B=()()() | form=(())(()()()) | image=((()))()()()
source=(()()())(()) | factor=2 | A=(()()()) | B=() | form=(()()())(()) | image=((()()()))()
source=(()()())()() | factor=1 | A=()() | B=()()() | form=()()(()()()) | image=(()())()()()
source=(()()())()() | factor=2 | A=(()()())() | B= | form=(()()())()() | image=((()()())())
source=(()()())()() | factor=3 | A=(()()())() | B= | form=(()()())()() | image=((()()())())
source=(()())((())) | factor=1 | A=((())) | B=()() | form=((()))(()()) | image=(((())))()()
source=(()())((())) | factor=2 | A=(()()) | B=(()) | form=(()())((())) | image=(())((()()))
source=(()())(()()) | factor=1 | A=(()()) | B=()() | form=(()())(()()) | image=((()()))()()
source=(()())(()()) | factor=2 | A=(()()) | B=()() | form=(()())(()()) | image=((()()))()()
source=(()())(())() | factor=1 | A=(())() | B=()() | form=(())()(()()) | image=((())())()()
source=(()())(())() | factor=2 | A=(()())() | B=() | form=(()())()(()) | image=((()())())()
source=(()())(())() | factor=3 | A=(()())(()) | B= | form=(()())(())() | image=((()())(()))
source=(()())()()() | factor=1 | A=()()() | B=()() | form=()()()(()()) | image=(()()())()()
source=(()())()()() | factor=2 | A=(()())()() | B= | form=(()())()()() | image=((()())()())
source=(()())()()() | factor=3 | A=(()())()() | B= | form=(()())()()() | image=((()())()())
source=(()())()()() | factor=4 | A=(()())()() | B= | form=(()())()()() | image=((()())()())
source=(())(((()))) | factor=1 | A=(((()))) | B=() | form=(((())))(()) | image=((((()))))()
source=(())(((()))) | factor=2 | A=(()) | B=((())) | form=(())(((()))) | image=((()))((()))
source=(())((()())) | factor=1 | A=((()())) | B=() | form=((()()))(()) | image=(((()())))()
source=(())((()())) | factor=2 | A=(()) | B=(()()) | form=(())((()())) | image=(()())((()))
source=(())((())()) | factor=1 | A=((())()) | B=() | form=((())())(()) | image=(((())()))()
source=(())((())()) | factor=2 | A=(()) | B=(())() | form=(())((())()) | image=(())((()))()
source=(())((()))() | factor=1 | A=((()))() | B=() | form=((()))()(()) | image=(((()))())()
source=(())((()))() | factor=2 | A=(())() | B=(()) | form=(())()((())) | image=(())((())())
source=(())((()))() | factor=3 | A=(())((())) | B= | form=(())((()))() | image=((())((())))
source=(())(())(()) | factor=1 | A=(())(()) | B=() | form=(())(())(()) | image=((())(()))()
source=(())(())(()) | factor=2 | A=(())(()) | B=() | form=(())(())(()) | image=((())(()))()
source=(())(())(()) | factor=3 | A=(())(()) | B=() | form=(())(())(()) | image=((())(()))()
source=(())(())()() | factor=1 | A=(())()() | B=() | form=(())()()(()) | image=((())()())()
source=(())(())()() | factor=2 | A=(())()() | B=() | form=(())()()(()) | image=((())()())()
source=(())(())()() | factor=3 | A=(())(())() | B= | form=(())(())()() | image=((())(())())
source=(())(())()() | factor=4 | A=(())(())() | B= | form=(())(())()() | image=((())(())())
source=(())()()()() | factor=1 | A=()()()() | B=() | form=()()()()(()) | image=(()()()())()
source=(())()()()() | factor=2 | A=(())()()() | B= | form=(())()()()() | image=((())()()())
source=(())()()()() | factor=3 | A=(())()()() | B= | form=(())()()()() | image=((())()()())
source=(())()()()() | factor=4 | A=(())()()() | B= | form=(())()()()() | image=((())()()())
source=(())()()()() | factor=5 | A=(())()()() | B= | form=(())()()()() | image=((())()()())
source=()()()()()() | factor=1 | A=()()()()() | B= | form=()()()()()() | image=(()()()()())
source=()()()()()() | factor=2 | A=()()()()() | B= | form=()()()()()() | image=(()()()()())
source=()()()()()() | factor=3 | A=()()()()() | B= | form=()()()()()() | image=(()()()()())
source=()()()()()() | factor=4 | A=()()()()() | B= | form=()()()()()() | image=(()()()()())
source=()()()()()() | factor=5 | A=()()()()() | B= | form=()()()()()() | image=(()()()()())
source=()()()()()() | factor=6 | A=()()()()() | B= | form=()()()()()() | image=(()()()()())
```

### C7

115 expressions, 23 clusters, 92 undirected flip edges, 232 factor flips of the form A (B) → (A) B.

```
Flip Transformation Analysis for 7 circles
============================================================
Total topologies: 115
Number of flip-equivalence clusters: 23
Cluster sizes: [8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 2, 2]

Clusters:
  Cluster 1 (size 4):
    ((((((())))))) [1 factors]
    (((((())))))() [2 factors]
    ((()))(((()))) [2 factors]
    (())((((())))) [2 factors]
  Cluster 2 (size 7):
    (((((()()))))) [1 factors]
    (((((()))))()) [1 factors]
    ((((()()))))() [2 factors]
    ((((()))))()() [3 factors]
    ((()))((()())) [2 factors]
    (()())(((()))) [2 factors]
    (())(((()()))) [2 factors]
  Cluster 3 (size 8):
    (((((())())))) [1 factors]
    (((((())))())) [1 factors]
    ((((())())))() [2 factors]
    ((((())))())() [2 factors]
    ((())(((())))) [1 factors]
    ((())())((())) [2 factors]
    (())(((())())) [2 factors]
    (())(((())))() [3 factors]
  Cluster 4 (size 5):
    (((((()))()))) [1 factors]
    ((((()))()))() [2 factors]
    (((()))((()))) [1 factors]
    ((()))((()))() [3 factors]
    (())(((()))()) [2 factors]
  Cluster 5 (size 6):
    ((((()()())))) [1 factors]
    ((((())))()()) [1 factors]
    (((()()())))() [2 factors]
    (((())))()()() [4 factors]
    (()()())((())) [2 factors]
    (())((()()())) [2 factors]
  Cluster 6 (size 7):
    ((((()())()))) [1 factors]
    ((((()))())()) [1 factors]
    (((()())()))() [2 factors]
    (((()))())()() [3 factors]
    ((()())((()))) [1 factors]
    (()())((()))() [3 factors]
    (())((()())()) [2 factors]
  Cluster 7 (size 7):
    ((((()()))())) [1 factors]
    ((((())()))()) [1 factors]
    (((()()))())() [2 factors]
    (((())()))()() [3 factors]
    ((())((()()))) [1 factors]
    (()())((())()) [2 factors]
    (())((()()))() [3 factors]
  Cluster 8 (size 3):
    ((((()())))()) [1 factors]
    (((()())))()() [3 factors]
    (()())((()())) [2 factors]
  Cluster 9 (size 6):
    ((((())(())))) [1 factors]
    (((())((())))) [1 factors]
    (((())(())))() [2 factors]
    ((())((())))() [2 factors]
    (())((())(())) [2 factors]
    (())(())((())) [3 factors]
  Cluster 10 (size 7):
    ((((())()()))) [1 factors]
    ((((()))()())) [1 factors]
    (((())()()))() [2 factors]
    (((()))()())() [2 factors]
    ((())((()))()) [1 factors]
    (())((())()()) [2 factors]
    (())((()))()() [4 factors]
  Cluster 11 (size 4):
    ((((())())())) [1 factors]
    (((())())())() [2 factors]
    ((())((())())) [1 factors]
    (())((())())() [3 factors]
  Cluster 12 (size 5):
    (((()()()()))) [1 factors]
    (((()))()()()) [1 factors]
    ((()()()()))() [2 factors]
    ((()))()()()() [5 factors]
    (()()()())(()) [2 factors]
  Cluster 13 (size 6):
    (((()()())())) [1 factors]
    (((())())()()) [1 factors]
    ((()()())(())) [1 factors]
    ((()()())())() [2 factors]
    ((())())()()() [4 factors]
    (()()())(())() [3 factors]
  Cluster 14 (size 5):
    (((()()()))()) [1 factors]
    (((()()))()()) [1 factors]
    ((()()()))()() [3 factors]
    ((()()))()()() [4 factors]
    (()()())(()()) [2 factors]
  Cluster 15 (size 5):
    (((()())(()))) [1 factors]
    (((())(()))()) [1 factors]
    ((()())(()))() [2 factors]
    ((())(()))()() [3 factors]
    (()())(())(()) [3 factors]
  Cluster 16 (size 6):
    (((()())()())) [1 factors]
    (((())()())()) [1 factors]
    ((()())(())()) [1 factors]
    ((()())()())() [2 factors]
    ((())()())()() [3 factors]
    (()())(())()() [4 factors]
  Cluster 17 (size 4):
    (((()())())()) [1 factors]
    ((()())(()())) [1 factors]
    ((()())())()() [3 factors]
    (()())(()())() [3 factors]
  Cluster 18 (size 4):
    (((())(())())) [1 factors]
    ((())(())(())) [1 factors]
    ((())(())())() [2 factors]
    (())(())(())() [4 factors]
  Cluster 19 (size 4):
    (((())()()())) [1 factors]
    ((())(())()()) [1 factors]
    ((())()()())() [2 factors]
    (())(())()()() [5 factors]
  Cluster 20 (size 4):
    ((()()()()())) [1 factors]
    ((())()()()()) [1 factors]
    (()()()()())() [2 factors]
    (())()()()()() [6 factors]
  Cluster 21 (size 4):
    ((()()()())()) [1 factors]
    ((()())()()()) [1 factors]
    (()()()())()() [3 factors]
    (()())()()()() [5 factors]
  Cluster 22 (size 2):
    ((()()())()()) [1 factors]
    (()()())()()() [4 factors]
  Cluster 23 (size 2):
    (()()()()()()) [1 factors]
    ()()()()()()() [7 factors]

Note: Each cluster represents circle topologies that are equivalent when embedded on a sphere surface.
```

Flips of the form `A (B)` → `(A) B`:

```
# source | factor | A | B | form=A(B) | image=(A)B
source=((((((())))))) | factor=1 | A= | B=(((((()))))) | form=((((((())))))) | image=(((((())))))()
source=(((((()()))))) | factor=1 | A= | B=((((()())))) | form=(((((()()))))) | image=((((()()))))()
source=(((((())())))) | factor=1 | A= | B=((((())()))) | form=(((((())())))) | image=((((())())))()
source=(((((()))()))) | factor=1 | A= | B=((((()))())) | form=(((((()))()))) | image=((((()))()))()
source=(((((())))())) | factor=1 | A= | B=((((())))()) | form=(((((())))())) | image=((((())))())()
source=(((((()))))()) | factor=1 | A= | B=((((()))))() | form=(((((()))))()) | image=((((()))))()()
source=(((((())))))() | factor=1 | A=() | B=((((())))) | form=()(((((()))))) | image=(())((((()))))
source=(((((())))))() | factor=2 | A=(((((()))))) | B= | form=(((((())))))() | image=((((((()))))))
source=((((()()())))) | factor=1 | A= | B=(((()()()))) | form=((((()()())))) | image=(((()()())))()
source=((((()())()))) | factor=1 | A= | B=(((()())())) | form=((((()())()))) | image=(((()())()))()
source=((((()()))())) | factor=1 | A= | B=(((()()))()) | form=((((()()))())) | image=(((()()))())()
source=((((()())))()) | factor=1 | A= | B=(((()())))() | form=((((()())))()) | image=(((()())))()()
source=((((()()))))() | factor=1 | A=() | B=(((()()))) | form=()((((()())))) | image=(())(((()())))
source=((((()()))))() | factor=2 | A=((((()())))) | B= | form=((((()()))))() | image=(((((()())))))
source=((((())(())))) | factor=1 | A= | B=(((())(()))) | form=((((())(())))) | image=(((())(())))()
source=((((())()()))) | factor=1 | A= | B=(((())()())) | form=((((())()()))) | image=(((())()()))()
source=((((())())())) | factor=1 | A= | B=(((())())()) | form=((((())())())) | image=(((())())())()
source=((((())()))()) | factor=1 | A= | B=(((())()))() | form=((((())()))()) | image=(((())()))()()
source=((((())())))() | factor=1 | A=() | B=(((())())) | form=()((((())()))) | image=(())(((())()))
source=((((())())))() | factor=2 | A=((((())()))) | B= | form=((((())())))() | image=(((((())()))))
source=((((()))()())) | factor=1 | A= | B=(((()))()()) | form=((((()))()())) | image=(((()))()())()
source=((((()))())()) | factor=1 | A= | B=(((()))())() | form=((((()))())()) | image=(((()))())()()
source=((((()))()))() | factor=1 | A=() | B=(((()))()) | form=()((((()))())) | image=(())(((()))())
source=((((()))()))() | factor=2 | A=((((()))())) | B= | form=((((()))()))() | image=(((((()))())))
source=((((())))()()) | factor=1 | A= | B=(((())))()() | form=((((())))()()) | image=(((())))()()()
source=((((())))())() | factor=1 | A=() | B=(((())))() | form=()((((())))()) | image=(())(((())))()
source=((((())))())() | factor=2 | A=((((())))()) | B= | form=((((())))())() | image=(((((())))()))
source=((((()))))()() | factor=1 | A=()() | B=(((()))) | form=()()((((())))) | image=(()())(((())))
source=((((()))))()() | factor=2 | A=((((()))))() | B= | form=((((()))))()() | image=(((((()))))())
source=((((()))))()() | factor=3 | A=((((()))))() | B= | form=((((()))))()() | image=(((((()))))())
source=(((()()()()))) | factor=1 | A= | B=((()()()())) | form=(((()()()()))) | image=((()()()()))()
source=(((()()())())) | factor=1 | A= | B=((()()())()) | form=(((()()())())) | image=((()()())())()
source=(((()()()))()) | factor=1 | A= | B=((()()()))() | form=(((()()()))()) | image=((()()()))()()
source=(((()()())))() | factor=1 | A=() | B=((()()())) | form=()(((()()()))) | image=(())((()()()))
source=(((()()())))() | factor=2 | A=(((()()()))) | B= | form=(((()()())))() | image=((((()()()))))
source=(((()())(()))) | factor=1 | A= | B=((()())(())) | form=(((()())(()))) | image=((()())(()))()
source=(((()())()())) | factor=1 | A= | B=((()())()()) | form=(((()())()())) | image=((()())()())()
source=(((()())())()) | factor=1 | A= | B=((()())())() | form=(((()())())()) | image=((()())())()()
source=(((()())()))() | factor=1 | A=() | B=((()())()) | form=()(((()())())) | image=(())((()())())
source=(((()())()))() | factor=2 | A=(((()())())) | B= | form=(((()())()))() | image=((((()())())))
source=(((()()))()()) | factor=1 | A= | B=((()()))()() | form=(((()()))()()) | image=((()()))()()()
source=(((()()))())() | factor=1 | A=() | B=((()()))() | form=()(((()()))()) | image=(())((()()))()
source=(((()()))())() | factor=2 | A=(((()()))()) | B= | form=(((()()))())() | image=((((()()))()))
source=(((()())))()() | factor=1 | A=()() | B=((()())) | form=()()(((()()))) | image=(()())((()()))
source=(((()())))()() | factor=2 | A=(((()())))() | B= | form=(((()())))()() | image=((((()())))())
source=(((()())))()() | factor=3 | A=(((()())))() | B= | form=(((()())))()() | image=((((()())))())
source=(((())((())))) | factor=1 | A= | B=((())((()))) | form=(((())((())))) | image=((())((())))()
source=(((())(())())) | factor=1 | A= | B=((())(())()) | form=(((())(())())) | image=((())(())())()
source=(((())(()))()) | factor=1 | A= | B=((())(()))() | form=(((())(()))()) | image=((())(()))()()
source=(((())(())))() | factor=1 | A=() | B=((())(())) | form=()(((())(()))) | image=(())((())(()))
source=(((())(())))() | factor=2 | A=(((())(()))) | B= | form=(((())(())))() | image=((((())(()))))
source=(((())()()())) | factor=1 | A= | B=((())()()()) | form=(((())()()())) | image=((())()()())()
source=(((())()())()) | factor=1 | A= | B=((())()())() | form=(((())()())()) | image=((())()())()()
source=(((())()()))() | factor=1 | A=() | B=((())()()) | form=()(((())()())) | image=(())((())()())
source=(((())()()))() | factor=2 | A=(((())()())) | B= | form=(((())()()))() | image=((((())()())))
source=(((())())()()) | factor=1 | A= | B=((())())()() | form=(((())())()()) | image=((())())()()()
source=(((())())())() | factor=1 | A=() | B=((())())() | form=()(((())())()) | image=(())((())())()
source=(((())())())() | factor=2 | A=(((())())()) | B= | form=(((())())())() | image=((((())())()))
source=(((())()))()() | factor=1 | A=()() | B=((())()) | form=()()(((())())) | image=(()())((())())
source=(((())()))()() | factor=2 | A=(((())()))() | B= | form=(((())()))()() | image=((((())()))())
source=(((())()))()() | factor=3 | A=(((())()))() | B= | form=(((())()))()() | image=((((())()))())
source=(((()))((()))) | factor=1 | A= | B=((()))((())) | form=(((()))((()))) | image=((()))((()))()
source=(((()))()()()) | factor=1 | A= | B=((()))()()() | form=(((()))()()()) | image=((()))()()()()
source=(((()))()())() | factor=1 | A=() | B=((()))()() | form=()(((()))()()) | image=(())((()))()()
source=(((()))()())() | factor=2 | A=(((()))()()) | B= | form=(((()))()())() | image=((((()))()()))
source=(((()))())()() | factor=1 | A=()() | B=((()))() | form=()()(((()))()) | image=(()())((()))()
source=(((()))())()() | factor=2 | A=(((()))())() | B= | form=(((()))())()() | image=((((()))())())
source=(((()))())()() | factor=3 | A=(((()))())() | B= | form=(((()))())()() | image=((((()))())())
source=(((())))()()() | factor=1 | A=()()() | B=((())) | form=()()()(((()))) | image=(()()())((()))
source=(((())))()()() | factor=2 | A=(((())))()() | B= | form=(((())))()()() | image=((((())))()())
source=(((())))()()() | factor=3 | A=(((())))()() | B= | form=(((())))()()() | image=((((())))()())
source=(((())))()()() | factor=4 | A=(((())))()() | B= | form=(((())))()()() | image=((((())))()())
source=((()()()()())) | factor=1 | A= | B=(()()()()()) | form=((()()()()())) | image=(()()()()())()
source=((()()()())()) | factor=1 | A= | B=(()()()())() | form=((()()()())()) | image=(()()()())()()
source=((()()()()))() | factor=1 | A=() | B=(()()()()) | form=()((()()()())) | image=(()()()())(())
source=((()()()()))() | factor=2 | A=((()()()())) | B= | form=((()()()()))() | image=(((()()()())))
source=((()()())(())) | factor=1 | A= | B=(()()())(()) | form=((()()())(())) | image=(()()())(())()
source=((()()())()()) | factor=1 | A= | B=(()()())()() | form=((()()())()()) | image=(()()())()()()
source=((()()())())() | factor=1 | A=() | B=(()()())() | form=()((()()())()) | image=(()()())(())()
source=((()()())())() | factor=2 | A=((()()())()) | B= | form=((()()())())() | image=(((()()())()))
source=((()()()))()() | factor=1 | A=()() | B=(()()()) | form=()()((()()())) | image=(()()())(()())
source=((()()()))()() | factor=2 | A=((()()()))() | B= | form=((()()()))()() | image=(((()()()))())
source=((()()()))()() | factor=3 | A=((()()()))() | B= | form=((()()()))()() | image=(((()()()))())
source=((()())((()))) | factor=1 | A= | B=(()())((())) | form=((()())((()))) | image=(()())((()))()
source=((()())(()())) | factor=1 | A= | B=(()())(()()) | form=((()())(()())) | image=(()())(()())()
source=((()())(())()) | factor=1 | A= | B=(()())(())() | form=((()())(())()) | image=(()())(())()()
source=((()())(()))() | factor=1 | A=() | B=(()())(()) | form=()((()())(())) | image=(()())(())(())
source=((()())(()))() | factor=2 | A=((()())(())) | B= | form=((()())(()))() | image=(((()())(())))
source=((()())()()()) | factor=1 | A= | B=(()())()()() | form=((()())()()()) | image=(()())()()()()
source=((()())()())() | factor=1 | A=() | B=(()())()() | form=()((()())()()) | image=(()())(())()()
source=((()())()())() | factor=2 | A=((()())()()) | B= | form=((()())()())() | image=(((()())()()))
source=((()())())()() | factor=1 | A=()() | B=(()())() | form=()()((()())()) | image=(()())(()())()
source=((()())())()() | factor=2 | A=((()())())() | B= | form=((()())())()() | image=(((()())())())
source=((()())())()() | factor=3 | A=((()())())() | B= | form=((()())())()() | image=(((()())())())
source=((()()))()()() | factor=1 | A=()()() | B=(()()) | form=()()()((()())) | image=(()()())(()())
source=((()()))()()() | factor=2 | A=((()()))()() | B= | form=((()()))()()() | image=(((()()))()())
source=((()()))()()() | factor=3 | A=((()()))()() | B= | form=((()()))()()() | image=(((()()))()())
source=((()()))()()() | factor=4 | A=((()()))()() | B= | form=((()()))()()() | image=(((()()))()())
source=((())(((())))) | factor=1 | A= | B=(())(((()))) | form=((())(((())))) | image=(())(((())))()
source=((())((()()))) | factor=1 | A= | B=(())((()())) | form=((())((()()))) | image=(())((()()))()
source=((())((())())) | factor=1 | A= | B=(())((())()) | form=((())((())())) | image=(())((())())()
source=((())((()))()) | factor=1 | A= | B=(())((()))() | form=((())((()))()) | image=(())((()))()()
source=((())((())))() | factor=1 | A=() | B=(())((())) | form=()((())((()))) | image=(())(())((()))
source=((())((())))() | factor=2 | A=((())((()))) | B= | form=((())((())))() | image=(((())((()))))
source=((())(())(())) | factor=1 | A= | B=(())(())(()) | form=((())(())(())) | image=(())(())(())()
source=((())(())()()) | factor=1 | A= | B=(())(())()() | form=((())(())()()) | image=(())(())()()()
source=((())(())())() | factor=1 | A=() | B=(())(())() | form=()((())(())()) | image=(())(())(())()
source=((())(())())() | factor=2 | A=((())(())()) | B= | form=((())(())())() | image=(((())(())()))
source=((())(()))()() | factor=1 | A=()() | B=(())(()) | form=()()((())(())) | image=(()())(())(())
source=((())(()))()() | factor=2 | A=((())(()))() | B= | form=((())(()))()() | image=(((())(()))())
source=((())(()))()() | factor=3 | A=((())(()))() | B= | form=((())(()))()() | image=(((())(()))())
source=((())()()()()) | factor=1 | A= | B=(())()()()() | form=((())()()()()) | image=(())()()()()()
source=((())()()())() | factor=1 | A=() | B=(())()()() | form=()((())()()()) | image=(())(())()()()
source=((())()()())() | factor=2 | A=((())()()()) | B= | form=((())()()())() | image=(((())()()()))
source=((())()())()() | factor=1 | A=()() | B=(())()() | form=()()((())()()) | image=(()())(())()()
source=((())()())()() | factor=2 | A=((())()())() | B= | form=((())()())()() | image=(((())()())())
source=((())()())()() | factor=3 | A=((())()())() | B= | form=((())()())()() | image=(((())()())())
source=((())())((())) | factor=1 | A=((())) | B=(())() | form=((()))((())()) | image=(())(((())))()
source=((())())((())) | factor=2 | A=((())()) | B=(()) | form=((())())((())) | image=(())(((())()))
source=((())())()()() | factor=1 | A=()()() | B=(())() | form=()()()((())()) | image=(()()())(())()
source=((())())()()() | factor=2 | A=((())())()() | B= | form=((())())()()() | image=(((())())()())
source=((())())()()() | factor=3 | A=((())())()() | B= | form=((())())()()() | image=(((())())()())
source=((())())()()() | factor=4 | A=((())())()() | B= | form=((())())()()() | image=(((())())()())
source=((()))(((()))) | factor=1 | A=(((()))) | B=(()) | form=(((())))((())) | image=(())((((()))))
source=((()))(((()))) | factor=2 | A=((())) | B=((())) | form=((()))(((()))) | image=((()))(((()))) | fixed
source=((()))((()())) | factor=1 | A=((()())) | B=(()) | form=((()()))((())) | image=(())(((()())))
source=((()))((()())) | factor=2 | A=((())) | B=(()()) | form=((()))((()())) | image=(()())(((())))
source=((()))((()))() | factor=1 | A=((()))() | B=(()) | form=((()))()((())) | image=(())(((()))())
source=((()))((()))() | factor=2 | A=((()))() | B=(()) | form=((()))()((())) | image=(())(((()))())
source=((()))((()))() | factor=3 | A=((()))((())) | B= | form=((()))((()))() | image=(((()))((())))
source=((()))()()()() | factor=1 | A=()()()() | B=(()) | form=()()()()((())) | image=(()()()())(())
source=((()))()()()() | factor=2 | A=((()))()()() | B= | form=((()))()()()() | image=(((()))()()())
source=((()))()()()() | factor=3 | A=((()))()()() | B= | form=((()))()()()() | image=(((()))()()())
source=((()))()()()() | factor=4 | A=((()))()()() | B= | form=((()))()()()() | image=(((()))()()())
source=((()))()()()() | factor=5 | A=((()))()()() | B= | form=((()))()()()() | image=(((()))()()())
source=(()()()()()()) | factor=1 | A= | B=()()()()()() | form=(()()()()()()) | image=()()()()()()()
source=(()()()()())() | factor=1 | A=() | B=()()()()() | form=()(()()()()()) | image=(())()()()()()
source=(()()()()())() | factor=2 | A=(()()()()()) | B= | form=(()()()()())() | image=((()()()()()))
source=(()()()())(()) | factor=1 | A=(()) | B=()()()() | form=(())(()()()()) | image=((()))()()()()
source=(()()()())(()) | factor=2 | A=(()()()()) | B=() | form=(()()()())(()) | image=((()()()()))()
source=(()()()())()() | factor=1 | A=()() | B=()()()() | form=()()(()()()()) | image=(()())()()()()
source=(()()()())()() | factor=2 | A=(()()()())() | B= | form=(()()()())()() | image=((()()()())())
source=(()()()())()() | factor=3 | A=(()()()())() | B= | form=(()()()())()() | image=((()()()())())
source=(()()())((())) | factor=1 | A=((())) | B=()()() | form=((()))(()()()) | image=(((())))()()()
source=(()()())((())) | factor=2 | A=(()()()) | B=(()) | form=(()()())((())) | image=(())((()()()))
source=(()()())(()()) | factor=1 | A=(()()) | B=()()() | form=(()())(()()()) | image=((()()))()()()
source=(()()())(()()) | factor=2 | A=(()()()) | B=()() | form=(()()())(()()) | image=((()()()))()()
source=(()()())(())() | factor=1 | A=(())() | B=()()() | form=(())()(()()()) | image=((())())()()()
source=(()()())(())() | factor=2 | A=(()()())() | B=() | form=(()()())()(()) | image=((()()())())()
source=(()()())(())() | factor=3 | A=(()()())(()) | B= | form=(()()())(())() | image=((()()())(()))
source=(()()())()()() | factor=1 | A=()()() | B=()()() | form=()()()(()()()) | image=(()()())()()() | fixed
source=(()()())()()() | factor=2 | A=(()()())()() | B= | form=(()()())()()() | image=((()()())()())
source=(()()())()()() | factor=3 | A=(()()())()() | B= | form=(()()())()()() | image=((()()())()())
source=(()()())()()() | factor=4 | A=(()()())()() | B= | form=(()()())()()() | image=((()()())()())
source=(()())(((()))) | factor=1 | A=(((()))) | B=()() | form=(((())))(()()) | image=((((()))))()()
source=(()())(((()))) | factor=2 | A=(()()) | B=((())) | form=(()())(((()))) | image=((()))((()()))
source=(()())((()())) | factor=1 | A=((()())) | B=()() | form=((()()))(()()) | image=(((()())))()()
source=(()())((()())) | factor=2 | A=(()()) | B=(()()) | form=(()())((()())) | image=(()())((()())) | fixed
source=(()())((())()) | factor=1 | A=((())()) | B=()() | form=((())())(()()) | image=(((())()))()()
source=(()())((())()) | factor=2 | A=(()()) | B=(())() | form=(()())((())()) | image=(())((()()))()
source=(()())((()))() | factor=1 | A=((()))() | B=()() | form=((()))()(()()) | image=(((()))())()()
source=(()())((()))() | factor=2 | A=(()())() | B=(()) | form=(()())()((())) | image=(())((()())())
source=(()())((()))() | factor=3 | A=(()())((())) | B= | form=(()())((()))() | image=((()())((())))
source=(()())(()())() | factor=1 | A=(()())() | B=()() | form=(()())()(()()) | image=((()())())()()
source=(()())(()())() | factor=2 | A=(()())() | B=()() | form=(()())()(()()) | image=((()())())()()
source=(()())(()())() | factor=3 | A=(()())(()()) | B= | form=(()())(()())() | image=((()())(()()))
source=(()())(())(()) | factor=1 | A=(())(()) | B=()() | form=(())(())(()()) | image=((())(()))()()
source=(()())(())(()) | factor=2 | A=(()())(()) | B=() | form=(()())(())(()) | image=((()())(()))()
source=(()())(())(()) | factor=3 | A=(()())(()) | B=() | form=(()())(())(()) | image=((()())(()))()
source=(()())(())()() | factor=1 | A=(())()() | B=()() | form=(())()()(()()) | image=((())()())()()
source=(()())(())()() | factor=2 | A=(()())()() | B=() | form=(()())()()(()) | image=((()())()())()
source=(()())(())()() | factor=3 | A=(()())(())() | B= | form=(()())(())()() | image=((()())(())())
source=(()())(())()() | factor=4 | A=(()())(())() | B= | form=(()())(())()() | image=((()())(())())
source=(()())()()()() | factor=1 | A=()()()() | B=()() | form=()()()()(()()) | image=(()()()())()()
source=(()())()()()() | factor=2 | A=(()())()()() | B= | form=(()())()()()() | image=((()())()()())
source=(()())()()()() | factor=3 | A=(()())()()() | B= | form=(()())()()()() | image=((()())()()())
source=(()())()()()() | factor=4 | A=(()())()()() | B= | form=(()())()()()() | image=((()())()()())
source=(()())()()()() | factor=5 | A=(()())()()() | B= | form=(()())()()()() | image=((()())()()())
source=(())((((())))) | factor=1 | A=((((())))) | B=() | form=((((()))))(()) | image=(((((())))))()
source=(())((((())))) | factor=2 | A=(()) | B=(((()))) | form=(())((((())))) | image=((()))(((())))
source=(())(((()()))) | factor=1 | A=(((()()))) | B=() | form=(((()())))(()) | image=((((()()))))()
source=(())(((()()))) | factor=2 | A=(()) | B=((()())) | form=(())(((()()))) | image=((()))((()()))
source=(())(((())())) | factor=1 | A=(((())())) | B=() | form=(((())()))(()) | image=((((())())))()
source=(())(((())())) | factor=2 | A=(()) | B=((())()) | form=(())(((())())) | image=((())())((()))
source=(())(((()))()) | factor=1 | A=(((()))()) | B=() | form=(((()))())(()) | image=((((()))()))()
source=(())(((()))()) | factor=2 | A=(()) | B=((()))() | form=(())(((()))()) | image=((()))((()))()
source=(())(((())))() | factor=1 | A=(((())))() | B=() | form=(((())))()(()) | image=((((())))())()
source=(())(((())))() | factor=2 | A=(())() | B=((())) | form=(())()(((()))) | image=((())())((()))
source=(())(((())))() | factor=3 | A=(())(((()))) | B= | form=(())(((())))() | image=((())(((()))))
source=(())((()()())) | factor=1 | A=((()()())) | B=() | form=((()()()))(()) | image=(((()()())))()
source=(())((()()())) | factor=2 | A=(()) | B=(()()()) | form=(())((()()())) | image=(()()())((()))
source=(())((()())()) | factor=1 | A=((()())()) | B=() | form=((()())())(()) | image=(((()())()))()
source=(())((()())()) | factor=2 | A=(()) | B=(()())() | form=(())((()())()) | image=(()())((()))()
source=(())((()()))() | factor=1 | A=((()()))() | B=() | form=((()()))()(()) | image=(((()()))())()
source=(())((()()))() | factor=2 | A=(())() | B=(()()) | form=(())()((()())) | image=(()())((())())
source=(())((()()))() | factor=3 | A=(())((()())) | B= | form=(())((()()))() | image=((())((()())))
source=(())((())(())) | factor=1 | A=((())(())) | B=() | form=((())(()))(()) | image=(((())(())))()
source=(())((())(())) | factor=2 | A=(()) | B=(())(()) | form=(())((())(())) | image=(())(())((()))
source=(())((())()()) | factor=1 | A=((())()()) | B=() | form=((())()())(()) | image=(((())()()))()
source=(())((())()()) | factor=2 | A=(()) | B=(())()() | form=(())((())()()) | image=(())((()))()()
source=(())((())())() | factor=1 | A=((())())() | B=() | form=((())())()(()) | image=(((())())())()
source=(())((())())() | factor=2 | A=(())() | B=(())() | form=(())()((())()) | image=(())((())())() | fixed
source=(())((())())() | factor=3 | A=(())((())()) | B= | form=(())((())())() | image=((())((())()))
source=(())((()))()() | factor=1 | A=((()))()() | B=() | form=((()))()()(()) | image=(((()))()())()
source=(())((()))()() | factor=2 | A=(())()() | B=(()) | form=(())()()((())) | image=(())((())()())
source=(())((()))()() | factor=3 | A=(())((()))() | B= | form=(())((()))()() | image=((())((()))())
source=(())((()))()() | factor=4 | A=(())((()))() | B= | form=(())((()))()() | image=((())((()))())
source=(())(())((())) | factor=1 | A=(())((())) | B=() | form=(())((()))(()) | image=((())((())))()
source=(())(())((())) | factor=2 | A=(())((())) | B=() | form=(())((()))(()) | image=((())((())))()
source=(())(())((())) | factor=3 | A=(())(()) | B=(()) | form=(())(())((())) | image=(())((())(()))
source=(())(())(())() | factor=1 | A=(())(())() | B=() | form=(())(())()(()) | image=((())(())())()
source=(())(())(())() | factor=2 | A=(())(())() | B=() | form=(())(())()(()) | image=((())(())())()
source=(())(())(())() | factor=3 | A=(())(())() | B=() | form=(())(())()(()) | image=((())(())())()
source=(())(())(())() | factor=4 | A=(())(())(()) | B= | form=(())(())(())() | image=((())(())(()))
source=(())(())()()() | factor=1 | A=(())()()() | B=() | form=(())()()()(()) | image=((())()()())()
source=(())(())()()() | factor=2 | A=(())()()() | B=() | form=(())()()()(()) | image=((())()()())()
source=(())(())()()() | factor=3 | A=(())(())()() | B= | form=(())(())()()() | image=((())(())()())
source=(())(())()()() | factor=4 | A=(())(())()() | B= | form=(())(())()()() | image=((())(())()())
source=(())(())()()() | factor=5 | A=(())(())()() | B= | form=(())(())()()() | image=((())(())()())
source=(())()()()()() | factor=1 | A=()()()()() | B=() | form=()()()()()(()) | image=(()()()()())()
source=(())()()()()() | factor=2 | A=(())()()()() | B= | form=(())()()()()() | image=((())()()()())
source=(())()()()()() | factor=3 | A=(())()()()() | B= | form=(())()()()()() | image=((())()()()())
source=(())()()()()() | factor=4 | A=(())()()()() | B= | form=(())()()()()() | image=((())()()()())
source=(())()()()()() | factor=5 | A=(())()()()() | B= | form=(())()()()()() | image=((())()()()())
source=(())()()()()() | factor=6 | A=(())()()()() | B= | form=(())()()()()() | image=((())()()()())
source=()()()()()()() | factor=1 | A=()()()()()() | B= | form=()()()()()()() | image=(()()()()()())
source=()()()()()()() | factor=2 | A=()()()()()() | B= | form=()()()()()()() | image=(()()()()()())
source=()()()()()()() | factor=3 | A=()()()()()() | B= | form=()()()()()()() | image=(()()()()()())
source=()()()()()()() | factor=4 | A=()()()()()() | B= | form=()()()()()()() | image=(()()()()()())
source=()()()()()()() | factor=5 | A=()()()()()() | B= | form=()()()()()()() | image=(()()()()()())
source=()()()()()()() | factor=6 | A=()()()()()() | B= | form=()()()()()()() | image=(()()()()()())
source=()()()()()()() | factor=7 | A=()()()()()() | B= | form=()()()()()()() | image=(()()()()()())
```

### C8

286 expressions, 47 clusters, 239 undirected flip edges, 583 factor flips of the form A (B) → (A) B.

```
Flip Transformation Analysis for 8 circles
============================================================
Total topologies: 286
Number of flip-equivalence clusters: 47
Cluster sizes: [9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 3, 2]

Clusters:
  Cluster 1 (size 5):
    (((((((()))))))) [1 factors]
    ((((((()))))))() [2 factors]
    (((())))(((()))) [2 factors]
    ((()))((((())))) [2 factors]
    (())(((((()))))) [2 factors]
  Cluster 2 (size 8):
    ((((((()())))))) [1 factors]
    ((((((())))))()) [1 factors]
    (((((()())))))() [2 factors]
    (((((())))))()() [3 factors]
    ((()()))(((()))) [2 factors]
    ((()))(((()()))) [2 factors]
    (()())((((())))) [2 factors]
    (())((((()())))) [2 factors]
  Cluster 3 (size 9):
    ((((((())()))))) [1 factors]
    ((((((()))))())) [1 factors]
    (((((())()))))() [2 factors]
    (((((()))))())() [2 factors]
    ((())((((()))))) [1 factors]
    ((())())(((()))) [2 factors]
    ((()))(((())())) [2 factors]
    (())((((())()))) [2 factors]
    (())((((()))))() [3 factors]
  Cluster 4 (size 9):
    ((((((()))())))) [1 factors]
    ((((((())))()))) [1 factors]
    (((((()))())))() [2 factors]
    (((((())))()))() [2 factors]
    (((()))(((())))) [1 factors]
    ((()))(((()))()) [2 factors]
    ((()))(((())))() [3 factors]
    (())((((()))())) [2 factors]
    (())((((())))()) [2 factors]
  Cluster 5 (size 7):
    (((((()()()))))) [1 factors]
    (((((()))))()()) [1 factors]
    ((((()()()))))() [2 factors]
    ((((()))))()()() [4 factors]
    ((()))((()()())) [2 factors]
    (()()())(((()))) [2 factors]
    (())(((()()()))) [2 factors]
  Cluster 6 (size 8):
    (((((()())())))) [1 factors]
    (((((())))())()) [1 factors]
    ((((()())())))() [2 factors]
    ((((())))())()() [3 factors]
    ((()())(((())))) [1 factors]
    ((()))((()())()) [2 factors]
    (()())(((())))() [3 factors]
    (())(((()())())) [2 factors]
  Cluster 7 (size 8):
    (((((()()))()))) [1 factors]
    (((((()))()))()) [1 factors]
    ((((()()))()))() [2 factors]
    ((((()))()))()() [3 factors]
    (((()))((()()))) [1 factors]
    ((()))((()()))() [3 factors]
    (()())(((()))()) [2 factors]
    (())(((()()))()) [2 factors]
  Cluster 8 (size 8):
    (((((()())))())) [1 factors]
    (((((())())))()) [1 factors]
    ((((()())))())() [2 factors]
    ((((())())))()() [3 factors]
    ((())(((()())))) [1 factors]
    ((())())((()())) [2 factors]
    (()())(((())())) [2 factors]
    (())(((()())))() [3 factors]
  Cluster 9 (size 4):
    (((((()()))))()) [1 factors]
    ((((()()))))()() [3 factors]
    ((()()))((()())) [2 factors]
    (()())(((()()))) [2 factors]
  Cluster 10 (size 7):
    (((((())(()))))) [1 factors]
    ((((())(()))))() [2 factors]
    (((())(((()))))) [1 factors]
    ((())(((()))))() [2 factors]
    ((())(()))((())) [2 factors]
    (())(((())(()))) [2 factors]
    (())(())(((()))) [3 factors]
  Cluster 11 (size 8):
    (((((())()())))) [1 factors]
    (((((())))()())) [1 factors]
    ((((())()())))() [2 factors]
    ((((())))()())() [2 factors]
    ((())(((())))()) [1 factors]
    ((())()())((())) [2 factors]
    (())(((())()())) [2 factors]
    (())(((())))()() [4 factors]
  Cluster 12 (size 9):
    (((((())())()))) [1 factors]
    (((((()))())())) [1 factors]
    ((((())())()))() [2 factors]
    ((((()))())())() [2 factors]
    (((())())((()))) [1 factors]
    ((())(((()))())) [1 factors]
    ((())())((()))() [3 factors]
    (())(((())())()) [2 factors]
    (())(((()))())() [3 factors]
  Cluster 13 (size 5):
    (((((())()))())) [1 factors]
    ((((())()))())() [2 factors]
    ((())(((())()))) [1 factors]
    ((())())((())()) [2 factors]
    (())(((())()))() [3 factors]
  Cluster 14 (size 5):
    (((((()))()()))) [1 factors]
    ((((()))()()))() [2 factors]
    (((()))((()))()) [1 factors]
    ((()))((()))()() [4 factors]
    (())(((()))()()) [2 factors]
  Cluster 15 (size 6):
    ((((()()()())))) [1 factors]
    ((((())))()()()) [1 factors]
    (((()()()())))() [2 factors]
    (((())))()()()() [5 factors]
    (()()()())((())) [2 factors]
    (())((()()()())) [2 factors]
  Cluster 16 (size 7):
    ((((()()())()))) [1 factors]
    ((((()))())()()) [1 factors]
    (((()()())()))() [2 factors]
    (((()))())()()() [4 factors]
    ((()()())((()))) [1 factors]
    (()()())((()))() [3 factors]
    (())((()()())()) [2 factors]
  Cluster 17 (size 7):
    ((((()()()))())) [1 factors]
    ((((())()))()()) [1 factors]
    (((()()()))())() [2 factors]
    (((())()))()()() [4 factors]
    ((())((()()()))) [1 factors]
    (()()())((())()) [2 factors]
    (())((()()()))() [3 factors]
  Cluster 18 (size 6):
    ((((()()())))()) [1 factors]
    ((((()())))()()) [1 factors]
    (((()()())))()() [3 factors]
    (((()())))()()() [4 factors]
    (()()())((()())) [2 factors]
    (()())((()()())) [2 factors]
  Cluster 19 (size 8):
    ((((()())(())))) [1 factors]
    (((()())((())))) [1 factors]
    (((()())(())))() [2 factors]
    (((())((())))()) [1 factors]
    ((()())((())))() [2 factors]
    ((())((())))()() [3 factors]
    (()())(())((())) [3 factors]
    (())((()())(())) [2 factors]
  Cluster 20 (size 7):
    ((((()())()()))) [1 factors]
    ((((()))()())()) [1 factors]
    (((()())()()))() [2 factors]
    (((()))()())()() [3 factors]
    ((()())((()))()) [1 factors]
    (()())((()))()() [4 factors]
    (())((()())()()) [2 factors]
  Cluster 21 (size 8):
    ((((()())())())) [1 factors]
    ((((())())())()) [1 factors]
    (((()())())())() [2 factors]
    (((())())())()() [3 factors]
    ((()())((())())) [1 factors]
    ((())((()())())) [1 factors]
    (()())((())())() [3 factors]
    (())((()())())() [3 factors]
  Cluster 22 (size 7):
    ((((()())()))()) [1 factors]
    ((((()()))())()) [1 factors]
    (((()())()))()() [3 factors]
    (((()()))())()() [3 factors]
    ((()())((()()))) [1 factors]
    (()())((()())()) [2 factors]
    (()())((()()))() [3 factors]
  Cluster 23 (size 7):
    ((((()()))()())) [1 factors]
    ((((())()()))()) [1 factors]
    (((()()))()())() [2 factors]
    (((())()()))()() [3 factors]
    ((())((()()))()) [1 factors]
    (()())((())()()) [2 factors]
    (())((()()))()() [4 factors]
  Cluster 24 (size 6):
    ((((())((()))))) [1 factors]
    ((((()))((())))) [1 factors]
    (((())((()))))() [2 factors]
    (((()))((())))() [2 factors]
    (())((())((()))) [2 factors]
    (())((()))((())) [3 factors]
  Cluster 25 (size 7):
    ((((())(())()))) [1 factors]
    (((())((()))())) [1 factors]
    (((())(())()))() [2 factors]
    ((())((()))())() [2 factors]
    ((())(())((()))) [1 factors]
    (())((())(())()) [2 factors]
    (())(())((()))() [4 factors]
  Cluster 26 (size 7):
    ((((())(()))())) [1 factors]
    (((())((())()))) [1 factors]
    (((())(()))())() [2 factors]
    ((())((())(()))) [1 factors]
    ((())((())()))() [2 factors]
    (())((())(()))() [3 factors]
    (())(())((())()) [3 factors]
  Cluster 27 (size 6):
    ((((())(())))()) [1 factors]
    (((())((()())))) [1 factors]
    (((())(())))()() [3 factors]
    ((())((()())))() [2 factors]
    (()())((())(())) [2 factors]
    (())(())((()())) [3 factors]
  Cluster 28 (size 7):
    ((((())()()()))) [1 factors]
    ((((()))()()())) [1 factors]
    (((())()()()))() [2 factors]
    (((()))()()())() [2 factors]
    ((())((()))()()) [1 factors]
    (())((())()()()) [2 factors]
    (())((()))()()() [5 factors]
  Cluster 29 (size 8):
    ((((())()())())) [1 factors]
    ((((())())()())) [1 factors]
    (((())()())())() [2 factors]
    (((())())()())() [2 factors]
    ((())((())()())) [1 factors]
    ((())((())())()) [1 factors]
    (())((())()())() [3 factors]
    (())((())())()() [4 factors]
  Cluster 30 (size 5):
    (((()()()()()))) [1 factors]
    (((()))()()()()) [1 factors]
    ((()()()()()))() [2 factors]
    ((()))()()()()() [6 factors]
    (()()()()())(()) [2 factors]
  Cluster 31 (size 6):
    (((()()()())())) [1 factors]
    (((())())()()()) [1 factors]
    ((()()()())(())) [1 factors]
    ((()()()())())() [2 factors]
    ((())())()()()() [5 factors]
    (()()()())(())() [3 factors]
  Cluster 32 (size 5):
    (((()()()()))()) [1 factors]
    (((()()))()()()) [1 factors]
    ((()()()()))()() [3 factors]
    ((()()))()()()() [5 factors]
    (()()()())(()()) [2 factors]
  Cluster 33 (size 5):
    (((()()())(()))) [1 factors]
    (((())(()))()()) [1 factors]
    ((()()())(()))() [2 factors]
    ((())(()))()()() [4 factors]
    (()()())(())(()) [3 factors]
  Cluster 34 (size 6):
    (((()()())()())) [1 factors]
    (((())()())()()) [1 factors]
    ((()()())(())()) [1 factors]
    ((()()())()())() [2 factors]
    ((())()())()()() [4 factors]
    (()()())(())()() [4 factors]
  Cluster 35 (size 6):
    (((()()())())()) [1 factors]
    (((()())())()()) [1 factors]
    ((()()())(()())) [1 factors]
    ((()()())())()() [3 factors]
    ((()())())()()() [4 factors]
    (()()())(()())() [3 factors]
  Cluster 36 (size 3):
    (((()()()))()()) [1 factors]
    ((()()()))()()() [4 factors]
    (()()())(()()()) [2 factors]
  Cluster 37 (size 5):
    (((()())(()()))) [1 factors]
    (((()())(()))()) [1 factors]
    ((()())(()()))() [2 factors]
    ((()())(()))()() [3 factors]
    (()())(()())(()) [3 factors]
  Cluster 38 (size 6):
    (((()())(())())) [1 factors]
    (((())(())())()) [1 factors]
    ((()())(())(())) [1 factors]
    ((()())(())())() [2 factors]
    ((())(())())()() [3 factors]
    (()())(())(())() [4 factors]
  Cluster 39 (size 6):
    (((()())()()())) [1 factors]
    (((())()()())()) [1 factors]
    ((()())(())()()) [1 factors]
    ((()())()()())() [2 factors]
    ((())()()())()() [3 factors]
    (()())(())()()() [5 factors]
  Cluster 40 (size 4):
    (((()())()())()) [1 factors]
    ((()())(()())()) [1 factors]
    ((()())()())()() [3 factors]
    (()())(()())()() [4 factors]
  Cluster 41 (size 3):
    (((())(())(()))) [1 factors]
    ((())(())(()))() [2 factors]
    (())(())(())(()) [4 factors]
  Cluster 42 (size 4):
    (((())(())()())) [1 factors]
    ((())(())(())()) [1 factors]
    ((())(())()())() [2 factors]
    (())(())(())()() [5 factors]
  Cluster 43 (size 4):
    (((())()()()())) [1 factors]
    ((())(())()()()) [1 factors]
    ((())()()()())() [2 factors]
    (())(())()()()() [6 factors]
  Cluster 44 (size 4):
    ((()()()()()())) [1 factors]
    ((())()()()()()) [1 factors]
    (()()()()()())() [2 factors]
    (())()()()()()() [7 factors]
  Cluster 45 (size 4):
    ((()()()()())()) [1 factors]
    ((()())()()()()) [1 factors]
    (()()()()())()() [3 factors]
    (()())()()()()() [6 factors]
  Cluster 46 (size 4):
    ((()()()())()()) [1 factors]
    ((()()())()()()) [1 factors]
    (()()()())()()() [4 factors]
    (()()())()()()() [5 factors]
  Cluster 47 (size 2):
    (()()()()()()()) [1 factors]
    ()()()()()()()() [8 factors]

Note: Each cluster represents circle topologies that are equivalent when embedded on a sphere surface.
```

Flips of the form `A (B)` → `(A) B`:

```
# source | factor | A | B | form=A(B) | image=(A)B
source=(((((((()))))))) | factor=1 | A= | B=((((((())))))) | form=(((((((()))))))) | image=((((((()))))))()
source=((((((()())))))) | factor=1 | A= | B=(((((()()))))) | form=((((((()())))))) | image=(((((()())))))()
source=((((((())()))))) | factor=1 | A= | B=(((((())())))) | form=((((((())()))))) | image=(((((())()))))()
source=((((((()))())))) | factor=1 | A= | B=(((((()))()))) | form=((((((()))())))) | image=(((((()))())))()
source=((((((())))()))) | factor=1 | A= | B=(((((())))())) | form=((((((())))()))) | image=(((((())))()))()
source=((((((()))))())) | factor=1 | A= | B=(((((()))))()) | form=((((((()))))())) | image=(((((()))))())()
source=((((((())))))()) | factor=1 | A= | B=(((((())))))() | form=((((((())))))()) | image=(((((())))))()()
source=((((((()))))))() | factor=1 | A=() | B=(((((()))))) | form=()((((((())))))) | image=(())(((((())))))
source=((((((()))))))() | factor=2 | A=((((((())))))) | B= | form=((((((()))))))() | image=(((((((())))))))
source=(((((()()()))))) | factor=1 | A= | B=((((()()())))) | form=(((((()()()))))) | image=((((()()()))))()
source=(((((()())())))) | factor=1 | A= | B=((((()())()))) | form=(((((()())())))) | image=((((()())())))()
source=(((((()()))()))) | factor=1 | A= | B=((((()()))())) | form=(((((()()))()))) | image=((((()()))()))()
source=(((((()())))())) | factor=1 | A= | B=((((()())))()) | form=(((((()())))())) | image=((((()())))())()
source=(((((()()))))()) | factor=1 | A= | B=((((()()))))() | form=(((((()()))))()) | image=((((()()))))()()
source=(((((()())))))() | factor=1 | A=() | B=((((()())))) | form=()(((((()()))))) | image=(())((((()()))))
source=(((((()())))))() | factor=2 | A=(((((()()))))) | B= | form=(((((()())))))() | image=((((((()()))))))
source=(((((())(()))))) | factor=1 | A= | B=((((())(())))) | form=(((((())(()))))) | image=((((())(()))))()
source=(((((())()())))) | factor=1 | A= | B=((((())()()))) | form=(((((())()())))) | image=((((())()())))()
source=(((((())())()))) | factor=1 | A= | B=((((())())())) | form=(((((())())()))) | image=((((())())()))()
source=(((((())()))())) | factor=1 | A= | B=((((())()))()) | form=(((((())()))())) | image=((((())()))())()
source=(((((())())))()) | factor=1 | A= | B=((((())())))() | form=(((((())())))()) | image=((((())())))()()
source=(((((())()))))() | factor=1 | A=() | B=((((())()))) | form=()(((((())())))) | image=(())((((())())))
source=(((((())()))))() | factor=2 | A=(((((())())))) | B= | form=(((((())()))))() | image=((((((())())))))
source=(((((()))()()))) | factor=1 | A= | B=((((()))()())) | form=(((((()))()()))) | image=((((()))()()))()
source=(((((()))())())) | factor=1 | A= | B=((((()))())()) | form=(((((()))())())) | image=((((()))())())()
source=(((((()))()))()) | factor=1 | A= | B=((((()))()))() | form=(((((()))()))()) | image=((((()))()))()()
source=(((((()))())))() | factor=1 | A=() | B=((((()))())) | form=()(((((()))()))) | image=(())((((()))()))
source=(((((()))())))() | factor=2 | A=(((((()))()))) | B= | form=(((((()))())))() | image=((((((()))()))))
source=(((((())))()())) | factor=1 | A= | B=((((())))()()) | form=(((((())))()())) | image=((((())))()())()
source=(((((())))())()) | factor=1 | A= | B=((((())))())() | form=(((((())))())()) | image=((((())))())()()
source=(((((())))()))() | factor=1 | A=() | B=((((())))()) | form=()(((((())))())) | image=(())((((())))())
source=(((((())))()))() | factor=2 | A=(((((())))())) | B= | form=(((((())))()))() | image=((((((())))())))
source=(((((()))))()()) | factor=1 | A= | B=((((()))))()() | form=(((((()))))()()) | image=((((()))))()()()
source=(((((()))))())() | factor=1 | A=() | B=((((()))))() | form=()(((((()))))()) | image=(())((((()))))()
source=(((((()))))())() | factor=2 | A=(((((()))))()) | B= | form=(((((()))))())() | image=((((((()))))()))
source=(((((())))))()() | factor=1 | A=()() | B=((((())))) | form=()()(((((()))))) | image=(()())((((()))))
source=(((((())))))()() | factor=2 | A=(((((())))))() | B= | form=(((((())))))()() | image=((((((())))))())
source=(((((())))))()() | factor=3 | A=(((((())))))() | B= | form=(((((())))))()() | image=((((((())))))())
source=((((()()()())))) | factor=1 | A= | B=(((()()()()))) | form=((((()()()())))) | image=(((()()()())))()
source=((((()()())()))) | factor=1 | A= | B=(((()()())())) | form=((((()()())()))) | image=(((()()())()))()
source=((((()()()))())) | factor=1 | A= | B=(((()()()))()) | form=((((()()()))())) | image=(((()()()))())()
source=((((()()())))()) | factor=1 | A= | B=(((()()())))() | form=((((()()())))()) | image=(((()()())))()()
source=((((()()()))))() | factor=1 | A=() | B=(((()()()))) | form=()((((()()())))) | image=(())(((()()())))
source=((((()()()))))() | factor=2 | A=((((()()())))) | B= | form=((((()()()))))() | image=(((((()()())))))
source=((((()())(())))) | factor=1 | A= | B=(((()())(()))) | form=((((()())(())))) | image=(((()())(())))()
source=((((()())()()))) | factor=1 | A= | B=(((()())()())) | form=((((()())()()))) | image=(((()())()()))()
source=((((()())())())) | factor=1 | A= | B=(((()())())()) | form=((((()())())())) | image=(((()())())())()
source=((((()())()))()) | factor=1 | A= | B=(((()())()))() | form=((((()())()))()) | image=(((()())()))()()
source=((((()())())))() | factor=1 | A=() | B=(((()())())) | form=()((((()())()))) | image=(())(((()())()))
source=((((()())())))() | factor=2 | A=((((()())()))) | B= | form=((((()())())))() | image=(((((()())()))))
source=((((()()))()())) | factor=1 | A= | B=(((()()))()()) | form=((((()()))()())) | image=(((()()))()())()
source=((((()()))())()) | factor=1 | A= | B=(((()()))())() | form=((((()()))())()) | image=(((()()))())()()
source=((((()()))()))() | factor=1 | A=() | B=(((()()))()) | form=()((((()()))())) | image=(())(((()()))())
source=((((()()))()))() | factor=2 | A=((((()()))())) | B= | form=((((()()))()))() | image=(((((()()))())))
source=((((()())))()()) | factor=1 | A= | B=(((()())))()() | form=((((()())))()()) | image=(((()())))()()()
source=((((()())))())() | factor=1 | A=() | B=(((()())))() | form=()((((()())))()) | image=(())(((()())))()
source=((((()())))())() | factor=2 | A=((((()())))()) | B= | form=((((()())))())() | image=(((((()())))()))
source=((((()()))))()() | factor=1 | A=()() | B=(((()()))) | form=()()((((()())))) | image=(()())(((()())))
source=((((()()))))()() | factor=2 | A=((((()()))))() | B= | form=((((()()))))()() | image=(((((()()))))())
source=((((()()))))()() | factor=3 | A=((((()()))))() | B= | form=((((()()))))()() | image=(((((()()))))())
source=((((())((()))))) | factor=1 | A= | B=(((())((())))) | form=((((())((()))))) | image=(((())((()))))()
source=((((())(())()))) | factor=1 | A= | B=(((())(())())) | form=((((())(())()))) | image=(((())(())()))()
source=((((())(()))())) | factor=1 | A= | B=(((())(()))()) | form=((((())(()))())) | image=(((())(()))())()
source=((((())(())))()) | factor=1 | A= | B=(((())(())))() | form=((((())(())))()) | image=(((())(())))()()
source=((((())(()))))() | factor=1 | A=() | B=(((())(()))) | form=()((((())(())))) | image=(())(((())(())))
source=((((())(()))))() | factor=2 | A=((((())(())))) | B= | form=((((())(()))))() | image=(((((())(())))))
source=((((())()()()))) | factor=1 | A= | B=(((())()()())) | form=((((())()()()))) | image=(((())()()()))()
source=((((())()())())) | factor=1 | A= | B=(((())()())()) | form=((((())()())())) | image=(((())()())())()
source=((((())()()))()) | factor=1 | A= | B=(((())()()))() | form=((((())()()))()) | image=(((())()()))()()
source=((((())()())))() | factor=1 | A=() | B=(((())()())) | form=()((((())()()))) | image=(())(((())()()))
source=((((())()())))() | factor=2 | A=((((())()()))) | B= | form=((((())()())))() | image=(((((())()()))))
source=((((())())()())) | factor=1 | A= | B=(((())())()()) | form=((((())())()())) | image=(((())())()())()
source=((((())())())()) | factor=1 | A= | B=(((())())())() | form=((((())())())()) | image=(((())())())()()
source=((((())())()))() | factor=1 | A=() | B=(((())())()) | form=()((((())())())) | image=(())(((())())())
source=((((())())()))() | factor=2 | A=((((())())())) | B= | form=((((())())()))() | image=(((((())())())))
source=((((())()))()()) | factor=1 | A= | B=(((())()))()() | form=((((())()))()()) | image=(((())()))()()()
source=((((())()))())() | factor=1 | A=() | B=(((())()))() | form=()((((())()))()) | image=(())(((())()))()
source=((((())()))())() | factor=2 | A=((((())()))()) | B= | form=((((())()))())() | image=(((((())()))()))
source=((((())())))()() | factor=1 | A=()() | B=(((())())) | form=()()((((())()))) | image=(()())(((())()))
source=((((())())))()() | factor=2 | A=((((())())))() | B= | form=((((())())))()() | image=(((((())())))())
source=((((())())))()() | factor=3 | A=((((())())))() | B= | form=((((())())))()() | image=(((((())())))())
source=((((()))((())))) | factor=1 | A= | B=(((()))((()))) | form=((((()))((())))) | image=(((()))((())))()
source=((((()))()()())) | factor=1 | A= | B=(((()))()()()) | form=((((()))()()())) | image=(((()))()()())()
source=((((()))()())()) | factor=1 | A= | B=(((()))()())() | form=((((()))()())()) | image=(((()))()())()()
source=((((()))()()))() | factor=1 | A=() | B=(((()))()()) | form=()((((()))()())) | image=(())(((()))()())
source=((((()))()()))() | factor=2 | A=((((()))()())) | B= | form=((((()))()()))() | image=(((((()))()())))
source=((((()))())()()) | factor=1 | A= | B=(((()))())()() | form=((((()))())()()) | image=(((()))())()()()
source=((((()))())())() | factor=1 | A=() | B=(((()))())() | form=()((((()))())()) | image=(())(((()))())()
source=((((()))())())() | factor=2 | A=((((()))())()) | B= | form=((((()))())())() | image=(((((()))())()))
source=((((()))()))()() | factor=1 | A=()() | B=(((()))()) | form=()()((((()))())) | image=(()())(((()))())
source=((((()))()))()() | factor=2 | A=((((()))()))() | B= | form=((((()))()))()() | image=(((((()))()))())
source=((((()))()))()() | factor=3 | A=((((()))()))() | B= | form=((((()))()))()() | image=(((((()))()))())
source=((((())))()()()) | factor=1 | A= | B=(((())))()()() | form=((((())))()()()) | image=(((())))()()()()
source=((((())))()())() | factor=1 | A=() | B=(((())))()() | form=()((((())))()()) | image=(())(((())))()()
source=((((())))()())() | factor=2 | A=((((())))()()) | B= | form=((((())))()())() | image=(((((())))()()))
source=((((())))())()() | factor=1 | A=()() | B=(((())))() | form=()()((((())))()) | image=(()())(((())))()
source=((((())))())()() | factor=2 | A=((((())))())() | B= | form=((((())))())()() | image=(((((())))())())
source=((((())))())()() | factor=3 | A=((((())))())() | B= | form=((((())))())()() | image=(((((())))())())
source=((((()))))()()() | factor=1 | A=()()() | B=(((()))) | form=()()()((((())))) | image=(()()())(((())))
source=((((()))))()()() | factor=2 | A=((((()))))()() | B= | form=((((()))))()()() | image=(((((()))))()())
source=((((()))))()()() | factor=3 | A=((((()))))()() | B= | form=((((()))))()()() | image=(((((()))))()())
source=((((()))))()()() | factor=4 | A=((((()))))()() | B= | form=((((()))))()()() | image=(((((()))))()())
source=(((()()()()()))) | factor=1 | A= | B=((()()()()())) | form=(((()()()()()))) | image=((()()()()()))()
source=(((()()()())())) | factor=1 | A= | B=((()()()())()) | form=(((()()()())())) | image=((()()()())())()
source=(((()()()()))()) | factor=1 | A= | B=((()()()()))() | form=(((()()()()))()) | image=((()()()()))()()
source=(((()()()())))() | factor=1 | A=() | B=((()()()())) | form=()(((()()()()))) | image=(())((()()()()))
source=(((()()()())))() | factor=2 | A=(((()()()()))) | B= | form=(((()()()())))() | image=((((()()()()))))
source=(((()()())(()))) | factor=1 | A= | B=((()()())(())) | form=(((()()())(()))) | image=((()()())(()))()
source=(((()()())()())) | factor=1 | A= | B=((()()())()()) | form=(((()()())()())) | image=((()()())()())()
source=(((()()())())()) | factor=1 | A= | B=((()()())())() | form=(((()()())())()) | image=((()()())())()()
source=(((()()())()))() | factor=1 | A=() | B=((()()())()) | form=()(((()()())())) | image=(())((()()())())
source=(((()()())()))() | factor=2 | A=(((()()())())) | B= | form=(((()()())()))() | image=((((()()())())))
source=(((()()()))()()) | factor=1 | A= | B=((()()()))()() | form=(((()()()))()()) | image=((()()()))()()()
source=(((()()()))())() | factor=1 | A=() | B=((()()()))() | form=()(((()()()))()) | image=(())((()()()))()
source=(((()()()))())() | factor=2 | A=(((()()()))()) | B= | form=(((()()()))())() | image=((((()()()))()))
source=(((()()())))()() | factor=1 | A=()() | B=((()()())) | form=()()(((()()()))) | image=(()())((()()()))
source=(((()()())))()() | factor=2 | A=(((()()())))() | B= | form=(((()()())))()() | image=((((()()())))())
source=(((()()())))()() | factor=3 | A=(((()()())))() | B= | form=(((()()())))()() | image=((((()()())))())
source=(((()())((())))) | factor=1 | A= | B=((()())((()))) | form=(((()())((())))) | image=((()())((())))()
source=(((()())(()()))) | factor=1 | A= | B=((()())(()())) | form=(((()())(()()))) | image=((()())(()()))()
source=(((()())(())())) | factor=1 | A= | B=((()())(())()) | form=(((()())(())())) | image=((()())(())())()
source=(((()())(()))()) | factor=1 | A= | B=((()())(()))() | form=(((()())(()))()) | image=((()())(()))()()
source=(((()())(())))() | factor=1 | A=() | B=((()())(())) | form=()(((()())(()))) | image=(())((()())(()))
source=(((()())(())))() | factor=2 | A=(((()())(()))) | B= | form=(((()())(())))() | image=((((()())(()))))
source=(((()())()()())) | factor=1 | A= | B=((()())()()()) | form=(((()())()()())) | image=((()())()()())()
source=(((()())()())()) | factor=1 | A= | B=((()())()())() | form=(((()())()())()) | image=((()())()())()()
source=(((()())()()))() | factor=1 | A=() | B=((()())()()) | form=()(((()())()())) | image=(())((()())()())
source=(((()())()()))() | factor=2 | A=(((()())()())) | B= | form=(((()())()()))() | image=((((()())()())))
source=(((()())())()()) | factor=1 | A= | B=((()())())()() | form=(((()())())()()) | image=((()())())()()()
source=(((()())())())() | factor=1 | A=() | B=((()())())() | form=()(((()())())()) | image=(())((()())())()
source=(((()())())())() | factor=2 | A=(((()())())()) | B= | form=(((()())())())() | image=((((()())())()))
source=(((()())()))()() | factor=1 | A=()() | B=((()())()) | form=()()(((()())())) | image=(()())((()())())
source=(((()())()))()() | factor=2 | A=(((()())()))() | B= | form=(((()())()))()() | image=((((()())()))())
source=(((()())()))()() | factor=3 | A=(((()())()))() | B= | form=(((()())()))()() | image=((((()())()))())
source=(((()()))()()()) | factor=1 | A= | B=((()()))()()() | form=(((()()))()()()) | image=((()()))()()()()
source=(((()()))()())() | factor=1 | A=() | B=((()()))()() | form=()(((()()))()()) | image=(())((()()))()()
source=(((()()))()())() | factor=2 | A=(((()()))()()) | B= | form=(((()()))()())() | image=((((()()))()()))
source=(((()()))())()() | factor=1 | A=()() | B=((()()))() | form=()()(((()()))()) | image=(()())((()()))()
source=(((()()))())()() | factor=2 | A=(((()()))())() | B= | form=(((()()))())()() | image=((((()()))())())
source=(((()()))())()() | factor=3 | A=(((()()))())() | B= | form=(((()()))())()() | image=((((()()))())())
source=(((()())))()()() | factor=1 | A=()()() | B=((()())) | form=()()()(((()()))) | image=(()()())((()()))
source=(((()())))()()() | factor=2 | A=(((()())))()() | B= | form=(((()())))()()() | image=((((()())))()())
source=(((()())))()()() | factor=3 | A=(((()())))()() | B= | form=(((()())))()()() | image=((((()())))()())
source=(((()())))()()() | factor=4 | A=(((()())))()() | B= | form=(((()())))()()() | image=((((()())))()())
source=(((())(((()))))) | factor=1 | A= | B=((())(((())))) | form=(((())(((()))))) | image=((())(((()))))()
source=(((())((()())))) | factor=1 | A= | B=((())((()()))) | form=(((())((()())))) | image=((())((()())))()
source=(((())((())()))) | factor=1 | A= | B=((())((())())) | form=(((())((())()))) | image=((())((())()))()
source=(((())((()))())) | factor=1 | A= | B=((())((()))()) | form=(((())((()))())) | image=((())((()))())()
source=(((())((())))()) | factor=1 | A= | B=((())((())))() | form=(((())((())))()) | image=((())((())))()()
source=(((())((()))))() | factor=1 | A=() | B=((())((()))) | form=()(((())((())))) | image=(())((())((())))
source=(((())((()))))() | factor=2 | A=(((())((())))) | B= | form=(((())((()))))() | image=((((())((())))))
source=(((())(())(()))) | factor=1 | A= | B=((())(())(())) | form=(((())(())(()))) | image=((())(())(()))()
source=(((())(())()())) | factor=1 | A= | B=((())(())()()) | form=(((())(())()())) | image=((())(())()())()
source=(((())(())())()) | factor=1 | A= | B=((())(())())() | form=(((())(())())()) | image=((())(())())()()
source=(((())(())()))() | factor=1 | A=() | B=((())(())()) | form=()(((())(())())) | image=(())((())(())())
source=(((())(())()))() | factor=2 | A=(((())(())())) | B= | form=(((())(())()))() | image=((((())(())())))
source=(((())(()))()()) | factor=1 | A= | B=((())(()))()() | form=(((())(()))()()) | image=((())(()))()()()
source=(((())(()))())() | factor=1 | A=() | B=((())(()))() | form=()(((())(()))()) | image=(())((())(()))()
source=(((())(()))())() | factor=2 | A=(((())(()))()) | B= | form=(((())(()))())() | image=((((())(()))()))
source=(((())(())))()() | factor=1 | A=()() | B=((())(())) | form=()()(((())(()))) | image=(()())((())(()))
source=(((())(())))()() | factor=2 | A=(((())(())))() | B= | form=(((())(())))()() | image=((((())(())))())
source=(((())(())))()() | factor=3 | A=(((())(())))() | B= | form=(((())(())))()() | image=((((())(())))())
source=(((())()()()())) | factor=1 | A= | B=((())()()()()) | form=(((())()()()())) | image=((())()()()())()
source=(((())()()())()) | factor=1 | A= | B=((())()()())() | form=(((())()()())()) | image=((())()()())()()
source=(((())()()()))() | factor=1 | A=() | B=((())()()()) | form=()(((())()()())) | image=(())((())()()())
source=(((())()()()))() | factor=2 | A=(((())()()())) | B= | form=(((())()()()))() | image=((((())()()())))
source=(((())()())()()) | factor=1 | A= | B=((())()())()() | form=(((())()())()()) | image=((())()())()()()
source=(((())()())())() | factor=1 | A=() | B=((())()())() | form=()(((())()())()) | image=(())((())()())()
source=(((())()())())() | factor=2 | A=(((())()())()) | B= | form=(((())()())())() | image=((((())()())()))
source=(((())()()))()() | factor=1 | A=()() | B=((())()()) | form=()()(((())()())) | image=(()())((())()())
source=(((())()()))()() | factor=2 | A=(((())()()))() | B= | form=(((())()()))()() | image=((((())()()))())
source=(((())()()))()() | factor=3 | A=(((())()()))() | B= | form=(((())()()))()() | image=((((())()()))())
source=(((())())((()))) | factor=1 | A= | B=((())())((())) | form=(((())())((()))) | image=((())())((()))()
source=(((())())()()()) | factor=1 | A= | B=((())())()()() | form=(((())())()()()) | image=((())())()()()()
source=(((())())()())() | factor=1 | A=() | B=((())())()() | form=()(((())())()()) | image=(())((())())()()
source=(((())())()())() | factor=2 | A=(((())())()()) | B= | form=(((())())()())() | image=((((())())()()))
source=(((())())())()() | factor=1 | A=()() | B=((())())() | form=()()(((())())()) | image=(()())((())())()
source=(((())())())()() | factor=2 | A=(((())())())() | B= | form=(((())())())()() | image=((((())())())())
source=(((())())())()() | factor=3 | A=(((())())())() | B= | form=(((())())())()() | image=((((())())())())
source=(((())()))()()() | factor=1 | A=()()() | B=((())()) | form=()()()(((())())) | image=(()()())((())())
source=(((())()))()()() | factor=2 | A=(((())()))()() | B= | form=(((())()))()()() | image=((((())()))()())
source=(((())()))()()() | factor=3 | A=(((())()))()() | B= | form=(((())()))()()() | image=((((())()))()())
source=(((())()))()()() | factor=4 | A=(((())()))()() | B= | form=(((())()))()()() | image=((((())()))()())
source=(((()))(((())))) | factor=1 | A= | B=((()))(((()))) | form=(((()))(((())))) | image=((()))(((())))()
source=(((()))((()()))) | factor=1 | A= | B=((()))((()())) | form=(((()))((()()))) | image=((()))((()()))()
source=(((()))((()))()) | factor=1 | A= | B=((()))((()))() | form=(((()))((()))()) | image=((()))((()))()()
source=(((()))((())))() | factor=1 | A=() | B=((()))((())) | form=()(((()))((()))) | image=(())((()))((()))
source=(((()))((())))() | factor=2 | A=(((()))((()))) | B= | form=(((()))((())))() | image=((((()))((()))))
source=(((()))()()()()) | factor=1 | A= | B=((()))()()()() | form=(((()))()()()()) | image=((()))()()()()()
source=(((()))()()())() | factor=1 | A=() | B=((()))()()() | form=()(((()))()()()) | image=(())((()))()()()
source=(((()))()()())() | factor=2 | A=(((()))()()()) | B= | form=(((()))()()())() | image=((((()))()()()))
source=(((()))()())()() | factor=1 | A=()() | B=((()))()() | form=()()(((()))()()) | image=(()())((()))()()
source=(((()))()())()() | factor=2 | A=(((()))()())() | B= | form=(((()))()())()() | image=((((()))()())())
source=(((()))()())()() | factor=3 | A=(((()))()())() | B= | form=(((()))()())()() | image=((((()))()())())
source=(((()))())()()() | factor=1 | A=()()() | B=((()))() | form=()()()(((()))()) | image=(()()())((()))()
source=(((()))())()()() | factor=2 | A=(((()))())()() | B= | form=(((()))())()()() | image=((((()))())()())
source=(((()))())()()() | factor=3 | A=(((()))())()() | B= | form=(((()))())()()() | image=((((()))())()())
source=(((()))())()()() | factor=4 | A=(((()))())()() | B= | form=(((()))())()()() | image=((((()))())()())
source=(((())))(((()))) | factor=1 | A=(((()))) | B=((())) | form=(((())))(((()))) | image=((()))((((()))))
source=(((())))(((()))) | factor=2 | A=(((()))) | B=((())) | form=(((())))(((()))) | image=((()))((((()))))
source=(((())))()()()() | factor=1 | A=()()()() | B=((())) | form=()()()()(((()))) | image=(()()()())((()))
source=(((())))()()()() | factor=2 | A=(((())))()()() | B= | form=(((())))()()()() | image=((((())))()()())
source=(((())))()()()() | factor=3 | A=(((())))()()() | B= | form=(((())))()()()() | image=((((())))()()())
source=(((())))()()()() | factor=4 | A=(((())))()()() | B= | form=(((())))()()()() | image=((((())))()()())
source=(((())))()()()() | factor=5 | A=(((())))()()() | B= | form=(((())))()()()() | image=((((())))()()())
source=((()()()()()())) | factor=1 | A= | B=(()()()()()()) | form=((()()()()()())) | image=(()()()()()())()
source=((()()()()())()) | factor=1 | A= | B=(()()()()())() | form=((()()()()())()) | image=(()()()()())()()
source=((()()()()()))() | factor=1 | A=() | B=(()()()()()) | form=()((()()()()())) | image=(()()()()())(())
source=((()()()()()))() | factor=2 | A=((()()()()())) | B= | form=((()()()()()))() | image=(((()()()()())))
source=((()()()())(())) | factor=1 | A= | B=(()()()())(()) | form=((()()()())(())) | image=(()()()())(())()
source=((()()()())()()) | factor=1 | A= | B=(()()()())()() | form=((()()()())()()) | image=(()()()())()()()
source=((()()()())())() | factor=1 | A=() | B=(()()()())() | form=()((()()()())()) | image=(()()()())(())()
source=((()()()())())() | factor=2 | A=((()()()())()) | B= | form=((()()()())())() | image=(((()()()())()))
source=((()()()()))()() | factor=1 | A=()() | B=(()()()()) | form=()()((()()()())) | image=(()()()())(()())
source=((()()()()))()() | factor=2 | A=((()()()()))() | B= | form=((()()()()))()() | image=(((()()()()))())
source=((()()()()))()() | factor=3 | A=((()()()()))() | B= | form=((()()()()))()() | image=(((()()()()))())
source=((()()())((()))) | factor=1 | A= | B=(()()())((())) | form=((()()())((()))) | image=(()()())((()))()
source=((()()())(()())) | factor=1 | A= | B=(()()())(()()) | form=((()()())(()())) | image=(()()())(()())()
source=((()()())(())()) | factor=1 | A= | B=(()()())(())() | form=((()()())(())()) | image=(()()())(())()()
source=((()()())(()))() | factor=1 | A=() | B=(()()())(()) | form=()((()()())(())) | image=(()()())(())(())
source=((()()())(()))() | factor=2 | A=((()()())(())) | B= | form=((()()())(()))() | image=(((()()())(())))
source=((()()())()()()) | factor=1 | A= | B=(()()())()()() | form=((()()())()()()) | image=(()()())()()()()
source=((()()())()())() | factor=1 | A=() | B=(()()())()() | form=()((()()())()()) | image=(()()())(())()()
source=((()()())()())() | factor=2 | A=((()()())()()) | B= | form=((()()())()())() | image=(((()()())()()))
source=((()()())())()() | factor=1 | A=()() | B=(()()())() | form=()()((()()())()) | image=(()()())(()())()
source=((()()())())()() | factor=2 | A=((()()())())() | B= | form=((()()())())()() | image=(((()()())())())
source=((()()())())()() | factor=3 | A=((()()())())() | B= | form=((()()())())()() | image=(((()()())())())
source=((()()()))()()() | factor=1 | A=()()() | B=(()()()) | form=()()()((()()())) | image=(()()())(()()())
source=((()()()))()()() | factor=2 | A=((()()()))()() | B= | form=((()()()))()()() | image=(((()()()))()())
source=((()()()))()()() | factor=3 | A=((()()()))()() | B= | form=((()()()))()()() | image=(((()()()))()())
source=((()()()))()()() | factor=4 | A=((()()()))()() | B= | form=((()()()))()()() | image=(((()()()))()())
source=((()())(((())))) | factor=1 | A= | B=(()())(((()))) | form=((()())(((())))) | image=(()())(((())))()
source=((()())((()()))) | factor=1 | A= | B=(()())((()())) | form=((()())((()()))) | image=(()())((()()))()
source=((()())((())())) | factor=1 | A= | B=(()())((())()) | form=((()())((())())) | image=(()())((())())()
source=((()())((()))()) | factor=1 | A= | B=(()())((()))() | form=((()())((()))()) | image=(()())((()))()()
source=((()())((())))() | factor=1 | A=() | B=(()())((())) | form=()((()())((()))) | image=(()())(())((()))
source=((()())((())))() | factor=2 | A=((()())((()))) | B= | form=((()())((())))() | image=(((()())((()))))
source=((()())(()())()) | factor=1 | A= | B=(()())(()())() | form=((()())(()())()) | image=(()())(()())()()
source=((()())(()()))() | factor=1 | A=() | B=(()())(()()) | form=()((()())(()())) | image=(()())(()())(())
source=((()())(()()))() | factor=2 | A=((()())(()())) | B= | form=((()())(()()))() | image=(((()())(()())))
source=((()())(())(())) | factor=1 | A= | B=(()())(())(()) | form=((()())(())(())) | image=(()())(())(())()
source=((()())(())()()) | factor=1 | A= | B=(()())(())()() | form=((()())(())()()) | image=(()())(())()()()
source=((()())(())())() | factor=1 | A=() | B=(()())(())() | form=()((()())(())()) | image=(()())(())(())()
source=((()())(())())() | factor=2 | A=((()())(())()) | B= | form=((()())(())())() | image=(((()())(())()))
source=((()())(()))()() | factor=1 | A=()() | B=(()())(()) | form=()()((()())(())) | image=(()())(()())(())
source=((()())(()))()() | factor=2 | A=((()())(()))() | B= | form=((()())(()))()() | image=(((()())(()))())
source=((()())(()))()() | factor=3 | A=((()())(()))() | B= | form=((()())(()))()() | image=(((()())(()))())
source=((()())()()()()) | factor=1 | A= | B=(()())()()()() | form=((()())()()()()) | image=(()())()()()()()
source=((()())()()())() | factor=1 | A=() | B=(()())()()() | form=()((()())()()()) | image=(()())(())()()()
source=((()())()()())() | factor=2 | A=((()())()()()) | B= | form=((()())()()())() | image=(((()())()()()))
source=((()())()())()() | factor=1 | A=()() | B=(()())()() | form=()()((()())()()) | image=(()())(()())()()
source=((()())()())()() | factor=2 | A=((()())()())() | B= | form=((()())()())()() | image=(((()())()())())
source=((()())()())()() | factor=3 | A=((()())()())() | B= | form=((()())()())()() | image=(((()())()())())
source=((()())())()()() | factor=1 | A=()()() | B=(()())() | form=()()()((()())()) | image=(()()())(()())()
source=((()())())()()() | factor=2 | A=((()())())()() | B= | form=((()())())()()() | image=(((()())())()())
source=((()())())()()() | factor=3 | A=((()())())()() | B= | form=((()())())()()() | image=(((()())())()())
source=((()())())()()() | factor=4 | A=((()())())()() | B= | form=((()())())()()() | image=(((()())())()())
source=((()()))(((()))) | factor=1 | A=(((()))) | B=(()()) | form=(((())))((()())) | image=(()())((((()))))
source=((()()))(((()))) | factor=2 | A=((()())) | B=((())) | form=((()()))(((()))) | image=((()))(((()())))
source=((()()))((()())) | factor=1 | A=((()())) | B=(()()) | form=((()()))((()())) | image=(()())(((()())))
source=((()()))((()())) | factor=2 | A=((()())) | B=(()()) | form=((()()))((()())) | image=(()())(((()())))
source=((()()))()()()() | factor=1 | A=()()()() | B=(()()) | form=()()()()((()())) | image=(()()()())(()())
source=((()()))()()()() | factor=2 | A=((()()))()()() | B= | form=((()()))()()()() | image=(((()()))()()())
source=((()()))()()()() | factor=3 | A=((()()))()()() | B= | form=((()()))()()()() | image=(((()()))()()())
source=((()()))()()()() | factor=4 | A=((()()))()()() | B= | form=((()()))()()()() | image=(((()()))()()())
source=((()()))()()()() | factor=5 | A=((()()))()()() | B= | form=((()()))()()()() | image=(((()()))()()())
source=((())((((()))))) | factor=1 | A= | B=(())((((())))) | form=((())((((()))))) | image=(())((((()))))()
source=((())(((()())))) | factor=1 | A= | B=(())(((()()))) | form=((())(((()())))) | image=(())(((()())))()
source=((())(((())()))) | factor=1 | A= | B=(())(((())())) | form=((())(((())()))) | image=(())(((())()))()
source=((())(((()))())) | factor=1 | A= | B=(())(((()))()) | form=((())(((()))())) | image=(())(((()))())()
source=((())(((())))()) | factor=1 | A= | B=(())(((())))() | form=((())(((())))()) | image=(())(((())))()()
source=((())(((()))))() | factor=1 | A=() | B=(())(((()))) | form=()((())(((())))) | image=(())(())(((())))
source=((())(((()))))() | factor=2 | A=((())(((())))) | B= | form=((())(((()))))() | image=(((())(((())))))
source=((())((()()()))) | factor=1 | A= | B=(())((()()())) | form=((())((()()()))) | image=(())((()()()))()
source=((())((()())())) | factor=1 | A= | B=(())((()())()) | form=((())((()())())) | image=(())((()())())()
source=((())((()()))()) | factor=1 | A= | B=(())((()()))() | form=((())((()()))()) | image=(())((()()))()()
source=((())((()())))() | factor=1 | A=() | B=(())((()())) | form=()((())((()()))) | image=(())(())((()()))
source=((())((()())))() | factor=2 | A=((())((()()))) | B= | form=((())((()())))() | image=(((())((()()))))
source=((())((())(()))) | factor=1 | A= | B=(())((())(())) | form=((())((())(()))) | image=(())((())(()))()
source=((())((())()())) | factor=1 | A= | B=(())((())()()) | form=((())((())()())) | image=(())((())()())()
source=((())((())())()) | factor=1 | A= | B=(())((())())() | form=((())((())())()) | image=(())((())())()()
source=((())((())()))() | factor=1 | A=() | B=(())((())()) | form=()((())((())())) | image=(())(())((())())
source=((())((())()))() | factor=2 | A=((())((())())) | B= | form=((())((())()))() | image=(((())((())())))
source=((())((()))()()) | factor=1 | A= | B=(())((()))()() | form=((())((()))()()) | image=(())((()))()()()
source=((())((()))())() | factor=1 | A=() | B=(())((()))() | form=()((())((()))()) | image=(())(())((()))()
source=((())((()))())() | factor=2 | A=((())((()))()) | B= | form=((())((()))())() | image=(((())((()))()))
source=((())((())))()() | factor=1 | A=()() | B=(())((())) | form=()()((())((()))) | image=(()())(())((()))
source=((())((())))()() | factor=2 | A=((())((())))() | B= | form=((())((())))()() | image=(((())((())))())
source=((())((())))()() | factor=3 | A=((())((())))() | B= | form=((())((())))()() | image=(((())((())))())
source=((())(())((()))) | factor=1 | A= | B=(())(())((())) | form=((())(())((()))) | image=(())(())((()))()
source=((())(())(())()) | factor=1 | A= | B=(())(())(())() | form=((())(())(())()) | image=(())(())(())()()
source=((())(())(()))() | factor=1 | A=() | B=(())(())(()) | form=()((())(())(())) | image=(())(())(())(())
source=((())(())(()))() | factor=2 | A=((())(())(())) | B= | form=((())(())(()))() | image=(((())(())(())))
source=((())(())()()()) | factor=1 | A= | B=(())(())()()() | form=((())(())()()()) | image=(())(())()()()()
source=((())(())()())() | factor=1 | A=() | B=(())(())()() | form=()((())(())()()) | image=(())(())(())()()
source=((())(())()())() | factor=2 | A=((())(())()()) | B= | form=((())(())()())() | image=(((())(())()()))
source=((())(())())()() | factor=1 | A=()() | B=(())(())() | form=()()((())(())()) | image=(()())(())(())()
source=((())(())())()() | factor=2 | A=((())(())())() | B= | form=((())(())())()() | image=(((())(())())())
source=((())(())())()() | factor=3 | A=((())(())())() | B= | form=((())(())())()() | image=(((())(())())())
source=((())(()))((())) | factor=1 | A=((())) | B=(())(()) | form=((()))((())(())) | image=(())(())(((())))
source=((())(()))((())) | factor=2 | A=((())(())) | B=(()) | form=((())(()))((())) | image=(())(((())(())))
source=((())(()))()()() | factor=1 | A=()()() | B=(())(()) | form=()()()((())(())) | image=(()()())(())(())
source=((())(()))()()() | factor=2 | A=((())(()))()() | B= | form=((())(()))()()() | image=(((())(()))()())
source=((())(()))()()() | factor=3 | A=((())(()))()() | B= | form=((())(()))()()() | image=(((())(()))()())
source=((())(()))()()() | factor=4 | A=((())(()))()() | B= | form=((())(()))()()() | image=(((())(()))()())
source=((())()()()()()) | factor=1 | A= | B=(())()()()()() | form=((())()()()()()) | image=(())()()()()()()
source=((())()()()())() | factor=1 | A=() | B=(())()()()() | form=()((())()()()()) | image=(())(())()()()()
source=((())()()()())() | factor=2 | A=((())()()()()) | B= | form=((())()()()())() | image=(((())()()()()))
source=((())()()())()() | factor=1 | A=()() | B=(())()()() | form=()()((())()()()) | image=(()())(())()()()
source=((())()()())()() | factor=2 | A=((())()()())() | B= | form=((())()()())()() | image=(((())()()())())
source=((())()()())()() | factor=3 | A=((())()()())() | B= | form=((())()()())()() | image=(((())()()())())
source=((())()())((())) | factor=1 | A=((())) | B=(())()() | form=((()))((())()()) | image=(())(((())))()()
source=((())()())((())) | factor=2 | A=((())()()) | B=(()) | form=((())()())((())) | image=(())(((())()()))
source=((())()())()()() | factor=1 | A=()()() | B=(())()() | form=()()()((())()()) | image=(()()())(())()()
source=((())()())()()() | factor=2 | A=((())()())()() | B= | form=((())()())()()() | image=(((())()())()())
source=((())()())()()() | factor=3 | A=((())()())()() | B= | form=((())()())()()() | image=(((())()())()())
source=((())()())()()() | factor=4 | A=((())()())()() | B= | form=((())()())()()() | image=(((())()())()())
source=((())())(((()))) | factor=1 | A=(((()))) | B=(())() | form=(((())))((())()) | image=(())((((()))))()
source=((())())(((()))) | factor=2 | A=((())()) | B=((())) | form=((())())(((()))) | image=((()))(((())()))
source=((())())((()())) | factor=1 | A=((()())) | B=(())() | form=((()()))((())()) | image=(())(((()())))()
source=((())())((()())) | factor=2 | A=((())()) | B=(()()) | form=((())())((()())) | image=(()())(((())()))
source=((())())((())()) | factor=1 | A=((())()) | B=(())() | form=((())())((())()) | image=(())(((())()))()
source=((())())((())()) | factor=2 | A=((())()) | B=(())() | form=((())())((())()) | image=(())(((())()))()
source=((())())((()))() | factor=1 | A=((()))() | B=(())() | form=((()))()((())()) | image=(())(((()))())()
source=((())())((()))() | factor=2 | A=((())())() | B=(()) | form=((())())()((())) | image=(())(((())())())
source=((())())((()))() | factor=3 | A=((())())((())) | B= | form=((())())((()))() | image=(((())())((())))
source=((())())()()()() | factor=1 | A=()()()() | B=(())() | form=()()()()((())()) | image=(()()()())(())()
source=((())())()()()() | factor=2 | A=((())())()()() | B= | form=((())())()()()() | image=(((())())()()())
source=((())())()()()() | factor=3 | A=((())())()()() | B= | form=((())())()()()() | image=(((())())()()())
source=((())())()()()() | factor=4 | A=((())())()()() | B= | form=((())())()()()() | image=(((())())()()())
source=((())())()()()() | factor=5 | A=((())())()()() | B= | form=((())())()()()() | image=(((())())()()())
source=((()))((((())))) | factor=1 | A=((((())))) | B=(()) | form=((((()))))((())) | image=(())(((((())))))
source=((()))((((())))) | factor=2 | A=((())) | B=(((()))) | form=((()))((((())))) | image=(((())))(((())))
source=((()))(((()()))) | factor=1 | A=(((()()))) | B=(()) | form=(((()())))((())) | image=(())((((()()))))
source=((()))(((()()))) | factor=2 | A=((())) | B=((()())) | form=((()))(((()()))) | image=((()()))(((())))
source=((()))(((())())) | factor=1 | A=(((())())) | B=(()) | form=(((())()))((())) | image=(())((((())())))
source=((()))(((())())) | factor=2 | A=((())) | B=((())()) | form=((()))(((())())) | image=((())())(((())))
source=((()))(((()))()) | factor=1 | A=(((()))()) | B=(()) | form=(((()))())((())) | image=(())((((()))()))
source=((()))(((()))()) | factor=2 | A=((())) | B=((()))() | form=((()))(((()))()) | image=((()))(((())))()
source=((()))(((())))() | factor=1 | A=(((())))() | B=(()) | form=(((())))()((())) | image=(())((((())))())
source=((()))(((())))() | factor=2 | A=((()))() | B=((())) | form=((()))()(((()))) | image=((()))(((()))())
source=((()))(((())))() | factor=3 | A=((()))(((()))) | B= | form=((()))(((())))() | image=(((()))(((()))))
source=((()))((()()())) | factor=1 | A=((()()())) | B=(()) | form=((()()()))((())) | image=(())(((()()())))
source=((()))((()()())) | factor=2 | A=((())) | B=(()()()) | form=((()))((()()())) | image=(()()())(((())))
source=((()))((()())()) | factor=1 | A=((()())()) | B=(()) | form=((()())())((())) | image=(())(((()())()))
source=((()))((()())()) | factor=2 | A=((())) | B=(()())() | form=((()))((()())()) | image=(()())(((())))()
source=((()))((()()))() | factor=1 | A=((()()))() | B=(()) | form=((()()))()((())) | image=(())(((()()))())
source=((()))((()()))() | factor=2 | A=((()))() | B=(()()) | form=((()))()((()())) | image=(()())(((()))())
source=((()))((()()))() | factor=3 | A=((()))((()())) | B= | form=((()))((()()))() | image=(((()))((()())))
source=((()))((()))()() | factor=1 | A=((()))()() | B=(()) | form=((()))()()((())) | image=(())(((()))()())
source=((()))((()))()() | factor=2 | A=((()))()() | B=(()) | form=((()))()()((())) | image=(())(((()))()())
source=((()))((()))()() | factor=3 | A=((()))((()))() | B= | form=((()))((()))()() | image=(((()))((()))())
source=((()))((()))()() | factor=4 | A=((()))((()))() | B= | form=((()))((()))()() | image=(((()))((()))())
source=((()))()()()()() | factor=1 | A=()()()()() | B=(()) | form=()()()()()((())) | image=(()()()()())(())
source=((()))()()()()() | factor=2 | A=((()))()()()() | B= | form=((()))()()()()() | image=(((()))()()()())
source=((()))()()()()() | factor=3 | A=((()))()()()() | B= | form=((()))()()()()() | image=(((()))()()()())
source=((()))()()()()() | factor=4 | A=((()))()()()() | B= | form=((()))()()()()() | image=(((()))()()()())
source=((()))()()()()() | factor=5 | A=((()))()()()() | B= | form=((()))()()()()() | image=(((()))()()()())
source=((()))()()()()() | factor=6 | A=((()))()()()() | B= | form=((()))()()()()() | image=(((()))()()()())
source=(()()()()()()()) | factor=1 | A= | B=()()()()()()() | form=(()()()()()()()) | image=()()()()()()()()
source=(()()()()()())() | factor=1 | A=() | B=()()()()()() | form=()(()()()()()()) | image=(())()()()()()()
source=(()()()()()())() | factor=2 | A=(()()()()()()) | B= | form=(()()()()()())() | image=((()()()()()()))
source=(()()()()())(()) | factor=1 | A=(()) | B=()()()()() | form=(())(()()()()()) | image=((()))()()()()()
source=(()()()()())(()) | factor=2 | A=(()()()()()) | B=() | form=(()()()()())(()) | image=((()()()()()))()
source=(()()()()())()() | factor=1 | A=()() | B=()()()()() | form=()()(()()()()()) | image=(()())()()()()()
source=(()()()()())()() | factor=2 | A=(()()()()())() | B= | form=(()()()()())()() | image=((()()()()())())
source=(()()()()())()() | factor=3 | A=(()()()()())() | B= | form=(()()()()())()() | image=((()()()()())())
source=(()()()())((())) | factor=1 | A=((())) | B=()()()() | form=((()))(()()()()) | image=(((())))()()()()
source=(()()()())((())) | factor=2 | A=(()()()()) | B=(()) | form=(()()()())((())) | image=(())((()()()()))
source=(()()()())(()()) | factor=1 | A=(()()) | B=()()()() | form=(()())(()()()()) | image=((()()))()()()()
source=(()()()())(()()) | factor=2 | A=(()()()()) | B=()() | form=(()()()())(()()) | image=((()()()()))()()
source=(()()()())(())() | factor=1 | A=(())() | B=()()()() | form=(())()(()()()()) | image=((())())()()()()
source=(()()()())(())() | factor=2 | A=(()()()())() | B=() | form=(()()()())()(()) | image=((()()()())())()
source=(()()()())(())() | factor=3 | A=(()()()())(()) | B= | form=(()()()())(())() | image=((()()()())(()))
source=(()()()())()()() | factor=1 | A=()()() | B=()()()() | form=()()()(()()()()) | image=(()()())()()()()
source=(()()()())()()() | factor=2 | A=(()()()())()() | B= | form=(()()()())()()() | image=((()()()())()())
source=(()()()())()()() | factor=3 | A=(()()()())()() | B= | form=(()()()())()()() | image=((()()()())()())
source=(()()()())()()() | factor=4 | A=(()()()())()() | B= | form=(()()()())()()() | image=((()()()())()())
source=(()()())(((()))) | factor=1 | A=(((()))) | B=()()() | form=(((())))(()()()) | image=((((()))))()()()
source=(()()())(((()))) | factor=2 | A=(()()()) | B=((())) | form=(()()())(((()))) | image=((()))((()()()))
source=(()()())((()())) | factor=1 | A=((()())) | B=()()() | form=((()()))(()()()) | image=(((()())))()()()
source=(()()())((()())) | factor=2 | A=(()()()) | B=(()()) | form=(()()())((()())) | image=(()())((()()()))
source=(()()())((())()) | factor=1 | A=((())()) | B=()()() | form=((())())(()()()) | image=(((())()))()()()
source=(()()())((())()) | factor=2 | A=(()()()) | B=(())() | form=(()()())((())()) | image=(())((()()()))()
source=(()()())((()))() | factor=1 | A=((()))() | B=()()() | form=((()))()(()()()) | image=(((()))())()()()
source=(()()())((()))() | factor=2 | A=(()()())() | B=(()) | form=(()()())()((())) | image=(())((()()())())
source=(()()())((()))() | factor=3 | A=(()()())((())) | B= | form=(()()())((()))() | image=((()()())((())))
source=(()()())(()()()) | factor=1 | A=(()()()) | B=()()() | form=(()()())(()()()) | image=((()()()))()()()
source=(()()())(()()()) | factor=2 | A=(()()()) | B=()()() | form=(()()())(()()()) | image=((()()()))()()()
source=(()()())(()())() | factor=1 | A=(()())() | B=()()() | form=(()())()(()()()) | image=((()())())()()()
source=(()()())(()())() | factor=2 | A=(()()())() | B=()() | form=(()()())()(()()) | image=((()()())())()()
source=(()()())(()())() | factor=3 | A=(()()())(()()) | B= | form=(()()())(()())() | image=((()()())(()()))
source=(()()())(())(()) | factor=1 | A=(())(()) | B=()()() | form=(())(())(()()()) | image=((())(()))()()()
source=(()()())(())(()) | factor=2 | A=(()()())(()) | B=() | form=(()()())(())(()) | image=((()()())(()))()
source=(()()())(())(()) | factor=3 | A=(()()())(()) | B=() | form=(()()())(())(()) | image=((()()())(()))()
source=(()()())(())()() | factor=1 | A=(())()() | B=()()() | form=(())()()(()()()) | image=((())()())()()()
source=(()()())(())()() | factor=2 | A=(()()())()() | B=() | form=(()()())()()(()) | image=((()()())()())()
source=(()()())(())()() | factor=3 | A=(()()())(())() | B= | form=(()()())(())()() | image=((()()())(())())
source=(()()())(())()() | factor=4 | A=(()()())(())() | B= | form=(()()())(())()() | image=((()()())(())())
source=(()()())()()()() | factor=1 | A=()()()() | B=()()() | form=()()()()(()()()) | image=(()()()())()()()
source=(()()())()()()() | factor=2 | A=(()()())()()() | B= | form=(()()())()()()() | image=((()()())()()())
source=(()()())()()()() | factor=3 | A=(()()())()()() | B= | form=(()()())()()()() | image=((()()())()()())
source=(()()())()()()() | factor=4 | A=(()()())()()() | B= | form=(()()())()()()() | image=((()()())()()())
source=(()()())()()()() | factor=5 | A=(()()())()()() | B= | form=(()()())()()()() | image=((()()())()()())
source=(()())((((())))) | factor=1 | A=((((())))) | B=()() | form=((((()))))(()()) | image=(((((())))))()()
source=(()())((((())))) | factor=2 | A=(()()) | B=(((()))) | form=(()())((((())))) | image=((()()))(((())))
source=(()())(((()()))) | factor=1 | A=(((()()))) | B=()() | form=(((()())))(()()) | image=((((()()))))()()
source=(()())(((()()))) | factor=2 | A=(()()) | B=((()())) | form=(()())(((()()))) | image=((()()))((()()))
source=(()())(((())())) | factor=1 | A=(((())())) | B=()() | form=(((())()))(()()) | image=((((())())))()()
source=(()())(((())())) | factor=2 | A=(()()) | B=((())()) | form=(()())(((())())) | image=((())())((()()))
source=(()())(((()))()) | factor=1 | A=(((()))()) | B=()() | form=(((()))())(()()) | image=((((()))()))()()
source=(()())(((()))()) | factor=2 | A=(()()) | B=((()))() | form=(()())(((()))()) | image=((()))((()()))()
source=(()())(((())))() | factor=1 | A=(((())))() | B=()() | form=(((())))()(()()) | image=((((())))())()()
source=(()())(((())))() | factor=2 | A=(()())() | B=((())) | form=(()())()(((()))) | image=((()))((()())())
source=(()())(((())))() | factor=3 | A=(()())(((()))) | B= | form=(()())(((())))() | image=((()())(((()))))
source=(()())((()()())) | factor=1 | A=((()()())) | B=()() | form=((()()()))(()()) | image=(((()()())))()()
source=(()())((()()())) | factor=2 | A=(()()) | B=(()()()) | form=(()())((()()())) | image=(()()())((()()))
source=(()())((()())()) | factor=1 | A=((()())()) | B=()() | form=((()())())(()()) | image=(((()())()))()()
source=(()())((()())()) | factor=2 | A=(()()) | B=(()())() | form=(()())((()())()) | image=(()())((()()))()
source=(()())((()()))() | factor=1 | A=((()()))() | B=()() | form=((()()))()(()()) | image=(((()()))())()()
source=(()())((()()))() | factor=2 | A=(()())() | B=(()()) | form=(()())()((()())) | image=(()())((()())())
source=(()())((()()))() | factor=3 | A=(()())((()())) | B= | form=(()())((()()))() | image=((()())((()())))
source=(()())((())(())) | factor=1 | A=((())(())) | B=()() | form=((())(()))(()()) | image=(((())(())))()()
source=(()())((())(())) | factor=2 | A=(()()) | B=(())(()) | form=(()())((())(())) | image=(())(())((()()))
source=(()())((())()()) | factor=1 | A=((())()()) | B=()() | form=((())()())(()()) | image=(((())()()))()()
source=(()())((())()()) | factor=2 | A=(()()) | B=(())()() | form=(()())((())()()) | image=(())((()()))()()
source=(()())((())())() | factor=1 | A=((())())() | B=()() | form=((())())()(()()) | image=(((())())())()()
source=(()())((())())() | factor=2 | A=(()())() | B=(())() | form=(()())()((())()) | image=(())((()())())()
source=(()())((())())() | factor=3 | A=(()())((())()) | B= | form=(()())((())())() | image=((()())((())()))
source=(()())((()))()() | factor=1 | A=((()))()() | B=()() | form=((()))()()(()()) | image=(((()))()())()()
source=(()())((()))()() | factor=2 | A=(()())()() | B=(()) | form=(()())()()((())) | image=(())((()())()())
source=(()())((()))()() | factor=3 | A=(()())((()))() | B= | form=(()())((()))()() | image=((()())((()))())
source=(()())((()))()() | factor=4 | A=(()())((()))() | B= | form=(()())((()))()() | image=((()())((()))())
source=(()())(()())(()) | factor=1 | A=(()())(()) | B=()() | form=(()())(())(()()) | image=((()())(()))()()
source=(()())(()())(()) | factor=2 | A=(()())(()) | B=()() | form=(()())(())(()()) | image=((()())(()))()()
source=(()())(()())(()) | factor=3 | A=(()())(()()) | B=() | form=(()())(()())(()) | image=((()())(()()))()
source=(()())(()())()() | factor=1 | A=(()())()() | B=()() | form=(()())()()(()()) | image=((()())()())()()
source=(()())(()())()() | factor=2 | A=(()())()() | B=()() | form=(()())()()(()()) | image=((()())()())()()
source=(()())(()())()() | factor=3 | A=(()())(()())() | B= | form=(()())(()())()() | image=((()())(()())())
source=(()())(()())()() | factor=4 | A=(()())(()())() | B= | form=(()())(()())()() | image=((()())(()())())
source=(()())(())((())) | factor=1 | A=(())((())) | B=()() | form=(())((()))(()()) | image=((())((())))()()
source=(()())(())((())) | factor=2 | A=(()())((())) | B=() | form=(()())((()))(()) | image=((()())((())))()
source=(()())(())((())) | factor=3 | A=(()())(()) | B=(()) | form=(()())(())((())) | image=(())((()())(()))
source=(()())(())(())() | factor=1 | A=(())(())() | B=()() | form=(())(())()(()()) | image=((())(())())()()
source=(()())(())(())() | factor=2 | A=(()())(())() | B=() | form=(()())(())()(()) | image=((()())(())())()
source=(()())(())(())() | factor=3 | A=(()())(())() | B=() | form=(()())(())()(()) | image=((()())(())())()
source=(()())(())(())() | factor=4 | A=(()())(())(()) | B= | form=(()())(())(())() | image=((()())(())(()))
source=(()())(())()()() | factor=1 | A=(())()()() | B=()() | form=(())()()()(()()) | image=((())()()())()()
source=(()())(())()()() | factor=2 | A=(()())()()() | B=() | form=(()())()()()(()) | image=((()())()()())()
source=(()())(())()()() | factor=3 | A=(()())(())()() | B= | form=(()())(())()()() | image=((()())(())()())
source=(()())(())()()() | factor=4 | A=(()())(())()() | B= | form=(()())(())()()() | image=((()())(())()())
source=(()())(())()()() | factor=5 | A=(()())(())()() | B= | form=(()())(())()()() | image=((()())(())()())
source=(()())()()()()() | factor=1 | A=()()()()() | B=()() | form=()()()()()(()()) | image=(()()()()())()()
source=(()())()()()()() | factor=2 | A=(()())()()()() | B= | form=(()())()()()()() | image=((()())()()()())
source=(()())()()()()() | factor=3 | A=(()())()()()() | B= | form=(()())()()()()() | image=((()())()()()())
source=(()())()()()()() | factor=4 | A=(()())()()()() | B= | form=(()())()()()()() | image=((()())()()()())
source=(()())()()()()() | factor=5 | A=(()())()()()() | B= | form=(()())()()()()() | image=((()())()()()())
source=(()())()()()()() | factor=6 | A=(()())()()()() | B= | form=(()())()()()()() | image=((()())()()()())
source=(())(((((()))))) | factor=1 | A=(((((()))))) | B=() | form=(((((())))))(()) | image=((((((()))))))()
source=(())(((((()))))) | factor=2 | A=(()) | B=((((())))) | form=(())(((((()))))) | image=((()))((((()))))
source=(())((((()())))) | factor=1 | A=((((()())))) | B=() | form=((((()()))))(()) | image=(((((()())))))()
source=(())((((()())))) | factor=2 | A=(()) | B=(((()()))) | form=(())((((()())))) | image=((()))(((()())))
source=(())((((())()))) | factor=1 | A=((((())()))) | B=() | form=((((())())))(()) | image=(((((())()))))()
source=(())((((())()))) | factor=2 | A=(()) | B=(((())())) | form=(())((((())()))) | image=((()))(((())()))
source=(())((((()))())) | factor=1 | A=((((()))())) | B=() | form=((((()))()))(()) | image=(((((()))())))()
source=(())((((()))())) | factor=2 | A=(()) | B=(((()))()) | form=(())((((()))())) | image=((()))(((()))())
source=(())((((())))()) | factor=1 | A=((((())))()) | B=() | form=((((())))())(()) | image=(((((())))()))()
source=(())((((())))()) | factor=2 | A=(()) | B=(((())))() | form=(())((((())))()) | image=((()))(((())))()
source=(())((((()))))() | factor=1 | A=((((()))))() | B=() | form=((((()))))()(()) | image=(((((()))))())()
source=(())((((()))))() | factor=2 | A=(())() | B=(((()))) | form=(())()((((())))) | image=((())())(((())))
source=(())((((()))))() | factor=3 | A=(())((((())))) | B= | form=(())((((()))))() | image=((())((((())))))
source=(())(((()()()))) | factor=1 | A=(((()()()))) | B=() | form=(((()()())))(()) | image=((((()()()))))()
source=(())(((()()()))) | factor=2 | A=(()) | B=((()()())) | form=(())(((()()()))) | image=((()))((()()()))
source=(())(((()())())) | factor=1 | A=(((()())())) | B=() | form=(((()())()))(()) | image=((((()())())))()
source=(())(((()())())) | factor=2 | A=(()) | B=((()())()) | form=(())(((()())())) | image=((()))((()())())
source=(())(((()()))()) | factor=1 | A=(((()()))()) | B=() | form=(((()()))())(()) | image=((((()()))()))()
source=(())(((()()))()) | factor=2 | A=(()) | B=((()()))() | form=(())(((()()))()) | image=((()))((()()))()
source=(())(((()())))() | factor=1 | A=(((()())))() | B=() | form=(((()())))()(()) | image=((((()())))())()
source=(())(((()())))() | factor=2 | A=(())() | B=((()())) | form=(())()(((()()))) | image=((())())((()()))
source=(())(((()())))() | factor=3 | A=(())(((()()))) | B= | form=(())(((()())))() | image=((())(((()()))))
source=(())(((())(()))) | factor=1 | A=(((())(()))) | B=() | form=(((())(())))(()) | image=((((())(()))))()
source=(())(((())(()))) | factor=2 | A=(()) | B=((())(())) | form=(())(((())(()))) | image=((())(()))((()))
source=(())(((())()())) | factor=1 | A=(((())()())) | B=() | form=(((())()()))(()) | image=((((())()())))()
source=(())(((())()())) | factor=2 | A=(()) | B=((())()()) | form=(())(((())()())) | image=((())()())((()))
source=(())(((())())()) | factor=1 | A=(((())())()) | B=() | form=(((())())())(()) | image=((((())())()))()
source=(())(((())())()) | factor=2 | A=(()) | B=((())())() | form=(())(((())())()) | image=((())())((()))()
source=(())(((())()))() | factor=1 | A=(((())()))() | B=() | form=(((())()))()(()) | image=((((())()))())()
source=(())(((())()))() | factor=2 | A=(())() | B=((())()) | form=(())()(((())())) | image=((())())((())())
source=(())(((())()))() | factor=3 | A=(())(((())())) | B= | form=(())(((())()))() | image=((())(((())())))
source=(())(((()))()()) | factor=1 | A=(((()))()()) | B=() | form=(((()))()())(()) | image=((((()))()()))()
source=(())(((()))()()) | factor=2 | A=(()) | B=((()))()() | form=(())(((()))()()) | image=((()))((()))()()
source=(())(((()))())() | factor=1 | A=(((()))())() | B=() | form=(((()))())()(()) | image=((((()))())())()
source=(())(((()))())() | factor=2 | A=(())() | B=((()))() | form=(())()(((()))()) | image=((())())((()))()
source=(())(((()))())() | factor=3 | A=(())(((()))()) | B= | form=(())(((()))())() | image=((())(((()))()))
source=(())(((())))()() | factor=1 | A=(((())))()() | B=() | form=(((())))()()(()) | image=((((())))()())()
source=(())(((())))()() | factor=2 | A=(())()() | B=((())) | form=(())()()(((()))) | image=((())()())((()))
source=(())(((())))()() | factor=3 | A=(())(((())))() | B= | form=(())(((())))()() | image=((())(((())))())
source=(())(((())))()() | factor=4 | A=(())(((())))() | B= | form=(())(((())))()() | image=((())(((())))())
source=(())((()()()())) | factor=1 | A=((()()()())) | B=() | form=((()()()()))(()) | image=(((()()()())))()
source=(())((()()()())) | factor=2 | A=(()) | B=(()()()()) | form=(())((()()()())) | image=(()()()())((()))
source=(())((()()())()) | factor=1 | A=((()()())()) | B=() | form=((()()())())(()) | image=(((()()())()))()
source=(())((()()())()) | factor=2 | A=(()) | B=(()()())() | form=(())((()()())()) | image=(()()())((()))()
source=(())((()()()))() | factor=1 | A=((()()()))() | B=() | form=((()()()))()(()) | image=(((()()()))())()
source=(())((()()()))() | factor=2 | A=(())() | B=(()()()) | form=(())()((()()())) | image=(()()())((())())
source=(())((()()()))() | factor=3 | A=(())((()()())) | B= | form=(())((()()()))() | image=((())((()()())))
source=(())((()())(())) | factor=1 | A=((()())(())) | B=() | form=((()())(()))(()) | image=(((()())(())))()
source=(())((()())(())) | factor=2 | A=(()) | B=(()())(()) | form=(())((()())(())) | image=(()())(())((()))
source=(())((()())()()) | factor=1 | A=((()())()()) | B=() | form=((()())()())(()) | image=(((()())()()))()
source=(())((()())()()) | factor=2 | A=(()) | B=(()())()() | form=(())((()())()()) | image=(()())((()))()()
source=(())((()())())() | factor=1 | A=((()())())() | B=() | form=((()())())()(()) | image=(((()())())())()
source=(())((()())())() | factor=2 | A=(())() | B=(()())() | form=(())()((()())()) | image=(()())((())())()
source=(())((()())())() | factor=3 | A=(())((()())()) | B= | form=(())((()())())() | image=((())((()())()))
source=(())((()()))()() | factor=1 | A=((()()))()() | B=() | form=((()()))()()(()) | image=(((()()))()())()
source=(())((()()))()() | factor=2 | A=(())()() | B=(()()) | form=(())()()((()())) | image=(()())((())()())
source=(())((()()))()() | factor=3 | A=(())((()()))() | B= | form=(())((()()))()() | image=((())((()()))())
source=(())((()()))()() | factor=4 | A=(())((()()))() | B= | form=(())((()()))()() | image=((())((()()))())
source=(())((())((()))) | factor=1 | A=((())((()))) | B=() | form=((())((())))(()) | image=(((())((()))))()
source=(())((())((()))) | factor=2 | A=(()) | B=(())((())) | form=(())((())((()))) | image=(())((()))((()))
source=(())((())(())()) | factor=1 | A=((())(())()) | B=() | form=((())(())())(()) | image=(((())(())()))()
source=(())((())(())()) | factor=2 | A=(()) | B=(())(())() | form=(())((())(())()) | image=(())(())((()))()
source=(())((())(()))() | factor=1 | A=((())(()))() | B=() | form=((())(()))()(()) | image=(((())(()))())()
source=(())((())(()))() | factor=2 | A=(())() | B=(())(()) | form=(())()((())(())) | image=(())(())((())())
source=(())((())(()))() | factor=3 | A=(())((())(())) | B= | form=(())((())(()))() | image=((())((())(())))
source=(())((())()()()) | factor=1 | A=((())()()()) | B=() | form=((())()()())(()) | image=(((())()()()))()
source=(())((())()()()) | factor=2 | A=(()) | B=(())()()() | form=(())((())()()()) | image=(())((()))()()()
source=(())((())()())() | factor=1 | A=((())()())() | B=() | form=((())()())()(()) | image=(((())()())())()
source=(())((())()())() | factor=2 | A=(())() | B=(())()() | form=(())()((())()()) | image=(())((())())()()
source=(())((())()())() | factor=3 | A=(())((())()()) | B= | form=(())((())()())() | image=((())((())()()))
source=(())((())())()() | factor=1 | A=((())())()() | B=() | form=((())())()()(()) | image=(((())())()())()
source=(())((())())()() | factor=2 | A=(())()() | B=(())() | form=(())()()((())()) | image=(())((())()())()
source=(())((())())()() | factor=3 | A=(())((())())() | B= | form=(())((())())()() | image=((())((())())())
source=(())((())())()() | factor=4 | A=(())((())())() | B= | form=(())((())())()() | image=((())((())())())
source=(())((()))((())) | factor=1 | A=((()))((())) | B=() | form=((()))((()))(()) | image=(((()))((())))()
source=(())((()))((())) | factor=2 | A=(())((())) | B=(()) | form=(())((()))((())) | image=(())((())((())))
source=(())((()))((())) | factor=3 | A=(())((())) | B=(()) | form=(())((()))((())) | image=(())((())((())))
source=(())((()))()()() | factor=1 | A=((()))()()() | B=() | form=((()))()()()(()) | image=(((()))()()())()
source=(())((()))()()() | factor=2 | A=(())()()() | B=(()) | form=(())()()()((())) | image=(())((())()()())
source=(())((()))()()() | factor=3 | A=(())((()))()() | B= | form=(())((()))()()() | image=((())((()))()())
source=(())((()))()()() | factor=4 | A=(())((()))()() | B= | form=(())((()))()()() | image=((())((()))()())
source=(())((()))()()() | factor=5 | A=(())((()))()() | B= | form=(())((()))()()() | image=((())((()))()())
source=(())(())(((()))) | factor=1 | A=(())(((()))) | B=() | form=(())(((())))(()) | image=((())(((()))))()
source=(())(())(((()))) | factor=2 | A=(())(((()))) | B=() | form=(())(((())))(()) | image=((())(((()))))()
source=(())(())(((()))) | factor=3 | A=(())(()) | B=((())) | form=(())(())(((()))) | image=((())(()))((()))
source=(())(())((()())) | factor=1 | A=(())((()())) | B=() | form=(())((()()))(()) | image=((())((()())))()
source=(())(())((()())) | factor=2 | A=(())((()())) | B=() | form=(())((()()))(()) | image=((())((()())))()
source=(())(())((()())) | factor=3 | A=(())(()) | B=(()()) | form=(())(())((()())) | image=(()())((())(()))
source=(())(())((())()) | factor=1 | A=(())((())()) | B=() | form=(())((())())(()) | image=((())((())()))()
source=(())(())((())()) | factor=2 | A=(())((())()) | B=() | form=(())((())())(()) | image=((())((())()))()
source=(())(())((())()) | factor=3 | A=(())(()) | B=(())() | form=(())(())((())()) | image=(())((())(()))()
source=(())(())((()))() | factor=1 | A=(())((()))() | B=() | form=(())((()))()(()) | image=((())((()))())()
source=(())(())((()))() | factor=2 | A=(())((()))() | B=() | form=(())((()))()(()) | image=((())((()))())()
source=(())(())((()))() | factor=3 | A=(())(())() | B=(()) | form=(())(())()((())) | image=(())((())(())())
source=(())(())((()))() | factor=4 | A=(())(())((())) | B= | form=(())(())((()))() | image=((())(())((())))
source=(())(())(())(()) | factor=1 | A=(())(())(()) | B=() | form=(())(())(())(()) | image=((())(())(()))()
source=(())(())(())(()) | factor=2 | A=(())(())(()) | B=() | form=(())(())(())(()) | image=((())(())(()))()
source=(())(())(())(()) | factor=3 | A=(())(())(()) | B=() | form=(())(())(())(()) | image=((())(())(()))()
source=(())(())(())(()) | factor=4 | A=(())(())(()) | B=() | form=(())(())(())(()) | image=((())(())(()))()
source=(())(())(())()() | factor=1 | A=(())(())()() | B=() | form=(())(())()()(()) | image=((())(())()())()
source=(())(())(())()() | factor=2 | A=(())(())()() | B=() | form=(())(())()()(()) | image=((())(())()())()
source=(())(())(())()() | factor=3 | A=(())(())()() | B=() | form=(())(())()()(()) | image=((())(())()())()
source=(())(())(())()() | factor=4 | A=(())(())(())() | B= | form=(())(())(())()() | image=((())(())(())())
source=(())(())(())()() | factor=5 | A=(())(())(())() | B= | form=(())(())(())()() | image=((())(())(())())
source=(())(())()()()() | factor=1 | A=(())()()()() | B=() | form=(())()()()()(()) | image=((())()()()())()
source=(())(())()()()() | factor=2 | A=(())()()()() | B=() | form=(())()()()()(()) | image=((())()()()())()
source=(())(())()()()() | factor=3 | A=(())(())()()() | B= | form=(())(())()()()() | image=((())(())()()())
source=(())(())()()()() | factor=4 | A=(())(())()()() | B= | form=(())(())()()()() | image=((())(())()()())
source=(())(())()()()() | factor=5 | A=(())(())()()() | B= | form=(())(())()()()() | image=((())(())()()())
source=(())(())()()()() | factor=6 | A=(())(())()()() | B= | form=(())(())()()()() | image=((())(())()()())
source=(())()()()()()() | factor=1 | A=()()()()()() | B=() | form=()()()()()()(()) | image=(()()()()()())()
source=(())()()()()()() | factor=2 | A=(())()()()()() | B= | form=(())()()()()()() | image=((())()()()()())
source=(())()()()()()() | factor=3 | A=(())()()()()() | B= | form=(())()()()()()() | image=((())()()()()())
source=(())()()()()()() | factor=4 | A=(())()()()()() | B= | form=(())()()()()()() | image=((())()()()()())
source=(())()()()()()() | factor=5 | A=(())()()()()() | B= | form=(())()()()()()() | image=((())()()()()())
source=(())()()()()()() | factor=6 | A=(())()()()()() | B= | form=(())()()()()()() | image=((())()()()()())
source=(())()()()()()() | factor=7 | A=(())()()()()() | B= | form=(())()()()()()() | image=((())()()()()())
source=()()()()()()()() | factor=1 | A=()()()()()()() | B= | form=()()()()()()()() | image=(()()()()()()())
source=()()()()()()()() | factor=2 | A=()()()()()()() | B= | form=()()()()()()()() | image=(()()()()()()())
source=()()()()()()()() | factor=3 | A=()()()()()()() | B= | form=()()()()()()()() | image=(()()()()()()())
source=()()()()()()()() | factor=4 | A=()()()()()()() | B= | form=()()()()()()()() | image=(()()()()()()())
source=()()()()()()()() | factor=5 | A=()()()()()()() | B= | form=()()()()()()()() | image=(()()()()()()())
source=()()()()()()()() | factor=6 | A=()()()()()()() | B= | form=()()()()()()()() | image=(()()()()()()())
source=()()()()()()()() | factor=7 | A=()()()()()()() | B= | form=()()()()()()()() | image=(()()()()()()())
source=()()()()()()()() | factor=8 | A=()()()()()()() | B= | form=()()()()()()()() | image=(()()()()()()())
```

### C9

719 expressions, 106 clusters, 613 undirected flip edges, 1474 factor flips of the form A (B) → (A) B.

```
Flip Transformation Analysis for 9 circles
============================================================
Total topologies: 719
Number of flip-equivalence clusters: 106
Cluster sizes: [10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 2]

Clusters:
  Cluster 1 (size 5):
    ((((((((())))))))) [1 factors]
    (((((((())))))))() [2 factors]
    (((())))((((())))) [2 factors]
    ((()))(((((()))))) [2 factors]
    (())((((((())))))) [2 factors]
  Cluster 2 (size 9):
    (((((((()()))))))) [1 factors]
    (((((((()))))))()) [1 factors]
    ((((((()()))))))() [2 factors]
    ((((((()))))))()() [3 factors]
    (((())))(((()()))) [2 factors]
    ((()()))((((())))) [2 factors]
    ((()))((((()())))) [2 factors]
    (()())(((((()))))) [2 factors]
    (())(((((()()))))) [2 factors]
  Cluster 3 (size 10):
    (((((((())())))))) [1 factors]
    (((((((())))))())) [1 factors]
    ((((((())())))))() [2 factors]
    ((((((())))))())() [2 factors]
    (((())))(((())())) [2 factors]
    ((())(((((())))))) [1 factors]
    ((())())((((())))) [2 factors]
    ((()))((((())()))) [2 factors]
    (())(((((())())))) [2 factors]
    (())(((((())))))() [3 factors]
  Cluster 4 (size 10):
    (((((((()))()))))) [1 factors]
    (((((((()))))()))) [1 factors]
    ((((((()))()))))() [2 factors]
    ((((((()))))()))() [2 factors]
    (((()))((((()))))) [1 factors]
    (((()))())(((()))) [2 factors]
    ((()))((((()))())) [2 factors]
    ((()))((((()))))() [3 factors]
    (())(((((()))()))) [2 factors]
    (())(((((()))))()) [2 factors]
  Cluster 5 (size 6):
    (((((((())))())))) [1 factors]
    ((((((())))())))() [2 factors]
    ((((())))(((())))) [1 factors]
    (((())))(((())))() [3 factors]
    ((()))((((())))()) [2 factors]
    (())(((((())))())) [2 factors]
  Cluster 6 (size 8):
    ((((((()()())))))) [1 factors]
    ((((((())))))()()) [1 factors]
    (((((()()())))))() [2 factors]
    (((((())))))()()() [4 factors]
    ((()()()))(((()))) [2 factors]
    ((()))(((()()()))) [2 factors]
    (()()())((((())))) [2 factors]
    (())((((()()())))) [2 factors]
  Cluster 7 (size 9):
    ((((((()())()))))) [1 factors]
    ((((((()))))())()) [1 factors]
    (((((()())()))))() [2 factors]
    (((((()))))())()() [3 factors]
    ((()())((((()))))) [1 factors]
    ((()())())(((()))) [2 factors]
    ((()))(((()())())) [2 factors]
    (()())((((()))))() [3 factors]
    (())((((()())()))) [2 factors]
  Cluster 8 (size 9):
    ((((((()()))())))) [1 factors]
    ((((((())))()))()) [1 factors]
    (((((()()))())))() [2 factors]
    (((((())))()))()() [3 factors]
    (((()()))(((())))) [1 factors]
    ((()()))(((())))() [3 factors]
    ((()))(((()()))()) [2 factors]
    (()())((((())))()) [2 factors]
    (())((((()()))())) [2 factors]
  Cluster 9 (size 9):
    ((((((()())))()))) [1 factors]
    ((((((()))())))()) [1 factors]
    (((((()())))()))() [2 factors]
    (((((()))())))()() [3 factors]
    (((()))(((()())))) [1 factors]
    ((()()))(((()))()) [2 factors]
    ((()))(((()())))() [3 factors]
    (()())((((()))())) [2 factors]
    (())((((()())))()) [2 factors]
  Cluster 10 (size 9):
    ((((((()()))))())) [1 factors]
    ((((((())()))))()) [1 factors]
    (((((()()))))())() [2 factors]
    (((((())()))))()() [3 factors]
    ((()()))(((())())) [2 factors]
    ((())((((()()))))) [1 factors]
    ((())())(((()()))) [2 factors]
    (()())((((())()))) [2 factors]
    (())((((()()))))() [3 factors]
  Cluster 11 (size 4):
    ((((((()())))))()) [1 factors]
    (((((()())))))()() [3 factors]
    ((()()))(((()()))) [2 factors]
    (()())((((()())))) [2 factors]
  Cluster 12 (size 8):
    ((((((())(())))))) [1 factors]
    (((((())(())))))() [2 factors]
    (((())((((())))))) [1 factors]
    ((())((((())))))() [2 factors]
    ((())(()))(((()))) [2 factors]
    ((()))(((())(()))) [2 factors]
    (())((((())(())))) [2 factors]
    (())(())((((())))) [3 factors]
  Cluster 13 (size 9):
    ((((((())()()))))) [1 factors]
    ((((((()))))()())) [1 factors]
    (((((())()()))))() [2 factors]
    (((((()))))()())() [2 factors]
    ((())((((()))))()) [1 factors]
    ((())()())(((()))) [2 factors]
    ((()))(((())()())) [2 factors]
    (())((((())()()))) [2 factors]
    (())((((()))))()() [4 factors]
  Cluster 14 (size 10):
    ((((((())())())))) [1 factors]
    ((((((())))())())) [1 factors]
    (((((())())())))() [2 factors]
    (((((())))())())() [2 factors]
    (((())())(((())))) [1 factors]
    ((())((((())))())) [1 factors]
    ((())())(((())))() [3 factors]
    ((()))(((())())()) [2 factors]
    (())((((())())())) [2 factors]
    (())((((())))())() [3 factors]
  Cluster 15 (size 10):
    ((((((())()))()))) [1 factors]
    ((((((()))()))())) [1 factors]
    (((((())()))()))() [2 factors]
    (((((()))()))())() [2 factors]
    (((()))(((())()))) [1 factors]
    ((())((((()))()))) [1 factors]
    ((())())(((()))()) [2 factors]
    ((()))(((())()))() [3 factors]
    (())((((())()))()) [2 factors]
    (())((((()))()))() [3 factors]
  Cluster 16 (size 5):
    ((((((())())))())) [1 factors]
    (((((())())))())() [2 factors]
    ((())((((())())))) [1 factors]
    ((())())(((())())) [2 factors]
    (())((((())())))() [3 factors]
  Cluster 17 (size 9):
    ((((((()))()())))) [1 factors]
    ((((((())))()()))) [1 factors]
    (((((()))()())))() [2 factors]
    (((((())))()()))() [2 factors]
    (((()))(((())))()) [1 factors]
    ((()))(((()))()()) [2 factors]
    ((()))(((())))()() [4 factors]
    (())((((()))()())) [2 factors]
    (())((((())))()()) [2 factors]
  Cluster 18 (size 5):
    ((((((()))())()))) [1 factors]
    (((((()))())()))() [2 factors]
    (((()))(((()))())) [1 factors]
    ((()))(((()))())() [3 factors]
    (())((((()))())()) [2 factors]
  Cluster 19 (size 7):
    (((((()()()()))))) [1 factors]
    (((((()))))()()()) [1 factors]
    ((((()()()()))))() [2 factors]
    ((((()))))()()()() [5 factors]
    ((()))((()()()())) [2 factors]
    (()()()())(((()))) [2 factors]
    (())(((()()()()))) [2 factors]
  Cluster 20 (size 8):
    (((((()()())())))) [1 factors]
    (((((())))())()()) [1 factors]
    ((((()()())())))() [2 factors]
    ((((())))())()()() [4 factors]
    ((()()())(((())))) [1 factors]
    ((()))((()()())()) [2 factors]
    (()()())(((())))() [3 factors]
    (())(((()()())())) [2 factors]
  Cluster 21 (size 8):
    (((((()()()))()))) [1 factors]
    (((((()))()))()()) [1 factors]
    ((((()()()))()))() [2 factors]
    ((((()))()))()()() [4 factors]
    (((()))((()()()))) [1 factors]
    ((()))((()()()))() [3 factors]
    (()()())(((()))()) [2 factors]
    (())(((()()()))()) [2 factors]
  Cluster 22 (size 8):
    (((((()()())))())) [1 factors]
    (((((())())))()()) [1 factors]
    ((((()()())))())() [2 factors]
    ((((())())))()()() [4 factors]
    ((())(((()()())))) [1 factors]
    ((())())((()()())) [2 factors]
    (()()())(((())())) [2 factors]
    (())(((()()())))() [3 factors]
  Cluster 23 (size 7):
    (((((()()()))))()) [1 factors]
    (((((()()))))()()) [1 factors]
    ((((()()()))))()() [3 factors]
    ((((()()))))()()() [4 factors]
    ((()()))((()()())) [2 factors]
    (()()())(((()()))) [2 factors]
    (()())(((()()()))) [2 factors]
  Cluster 24 (size 9):
    (((((()())(()))))) [1 factors]
    ((((()())(()))))() [2 factors]
    (((()())(((()))))) [1 factors]
    (((())(((()))))()) [1 factors]
    ((()())(((()))))() [2 factors]
    ((())(((()))))()() [3 factors]
    ((()))((()())(())) [2 factors]
    (()())(())(((()))) [3 factors]
    (())(((()())(()))) [2 factors]
  Cluster 25 (size 8):
    (((((()())()())))) [1 factors]
    (((((())))()())()) [1 factors]
    ((((()())()())))() [2 factors]
    ((((())))()())()() [3 factors]
    ((()())(((())))()) [1 factors]
    ((()))((()())()()) [2 factors]
    (()())(((())))()() [4 factors]
    (())(((()())()())) [2 factors]
  Cluster 26 (size 9):
    (((((()())())()))) [1 factors]
    (((((()))())())()) [1 factors]
    ((((()())())()))() [2 factors]
    ((((()))())())()() [3 factors]
    (((()))((()())())) [1 factors]
    ((()())(((()))())) [1 factors]
    ((()))((()())())() [3 factors]
    (()())(((()))())() [3 factors]
    (())(((()())())()) [2 factors]
  Cluster 27 (size 9):
    (((((()())()))())) [1 factors]
    (((((())()))())()) [1 factors]
    ((((()())()))())() [2 factors]
    ((((())()))())()() [3 factors]
    ((()())(((())()))) [1 factors]
    ((())(((()())()))) [1 factors]
    ((())())((()())()) [2 factors]
    (()())(((())()))() [3 factors]
    (())(((()())()))() [3 factors]
  Cluster 28 (size 8):
    (((((()())())))()) [1 factors]
    (((((()())))())()) [1 factors]
    ((((()())())))()() [3 factors]
    ((((()())))())()() [3 factors]
    ((()())(((()())))) [1 factors]
    ((()())())((()())) [2 factors]
    (()())(((()())())) [2 factors]
    (()())(((()())))() [3 factors]
  Cluster 29 (size 8):
    (((((()()))()()))) [1 factors]
    (((((()))()()))()) [1 factors]
    ((((()()))()()))() [2 factors]
    ((((()))()()))()() [3 factors]
    (((()))((()()))()) [1 factors]
    ((()))((()()))()() [4 factors]
    (()())(((()))()()) [2 factors]
    (())(((()()))()()) [2 factors]
  Cluster 30 (size 9):
    (((((()()))())())) [1 factors]
    (((((())())()))()) [1 factors]
    ((((()()))())())() [2 factors]
    ((((())())()))()() [3 factors]
    (((())())((()()))) [1 factors]
    ((())(((()()))())) [1 factors]
    ((())())((()()))() [3 factors]
    (()())(((())())()) [2 factors]
    (())(((()()))())() [3 factors]
  Cluster 31 (size 5):
    (((((()()))()))()) [1 factors]
    ((((()()))()))()() [3 factors]
    (((()()))((()()))) [1 factors]
    ((()()))((()()))() [3 factors]
    (()())(((()()))()) [2 factors]
  Cluster 32 (size 8):
    (((((()())))()())) [1 factors]
    (((((())()())))()) [1 factors]
    ((((()())))()())() [2 factors]
    ((((())()())))()() [3 factors]
    ((())(((()())))()) [1 factors]
    ((())()())((()())) [2 factors]
    (()())(((())()())) [2 factors]
    (())(((()())))()() [4 factors]
  Cluster 33 (size 10):
    (((((())((())))))) [1 factors]
    ((((())(((())))))) [1 factors]
    ((((())((())))))() [2 factors]
    ((((()))(((()))))) [1 factors]
    (((())(((())))))() [2 factors]
    (((()))(((()))))() [2 factors]
    ((())((())))((())) [2 factors]
    (())(((())((())))) [2 factors]
    (())((())(((())))) [2 factors]
    (())((()))(((()))) [3 factors]
  Cluster 34 (size 8):
    (((((())(())())))) [1 factors]
    ((((())(())())))() [2 factors]
    (((())(((())))())) [1 factors]
    ((())(((())))())() [2 factors]
    ((())(())(((())))) [1 factors]
    ((())(())())((())) [2 factors]
    (())(((())(())())) [2 factors]
    (())(())(((())))() [4 factors]
  Cluster 35 (size 8):
    (((((())(()))()))) [1 factors]
    ((((())(()))()))() [2 factors]
    (((())(((()))()))) [1 factors]
    (((())(()))((()))) [1 factors]
    ((())(((()))()))() [2 factors]
    ((())(()))((()))() [3 factors]
    (())(((())(()))()) [2 factors]
    (())(())(((()))()) [3 factors]
  Cluster 36 (size 8):
    (((((())(())))())) [1 factors]
    ((((())(())))())() [2 factors]
    (((())(((())())))) [1 factors]
    ((())(((())(())))) [1 factors]
    ((())(((())())))() [2 factors]
    ((())())((())(())) [2 factors]
    (())(((())(())))() [3 factors]
    (())(())(((())())) [3 factors]
  Cluster 37 (size 7):
    (((((())(()))))()) [1 factors]
    ((((())(()))))()() [3 factors]
    (((())(((()()))))) [1 factors]
    ((())(((()()))))() [2 factors]
    ((())(()))((()())) [2 factors]
    (()())(((())(()))) [2 factors]
    (())(())(((()()))) [3 factors]
  Cluster 38 (size 8):
    (((((())()()())))) [1 factors]
    (((((())))()()())) [1 factors]
    ((((())()()())))() [2 factors]
    ((((())))()()())() [2 factors]
    ((())(((())))()()) [1 factors]
    ((())()()())((())) [2 factors]
    (())(((())()()())) [2 factors]
    (())(((())))()()() [5 factors]
  Cluster 39 (size 9):
    (((((())()())()))) [1 factors]
    (((((()))())()())) [1 factors]
    ((((())()())()))() [2 factors]
    ((((()))())()())() [2 factors]
    (((())()())((()))) [1 factors]
    ((())(((()))())()) [1 factors]
    ((())()())((()))() [3 factors]
    (())(((())()())()) [2 factors]
    (())(((()))())()() [4 factors]
  Cluster 40 (size 9):
    (((((())()()))())) [1 factors]
    (((((())()))()())) [1 factors]
    ((((())()()))())() [2 factors]
    ((((())()))()())() [2 factors]
    ((())(((())()()))) [1 factors]
    ((())(((())()))()) [1 factors]
    ((())()())((())()) [2 factors]
    (())(((())()()))() [3 factors]
    (())(((())()))()() [4 factors]
  Cluster 41 (size 9):
    (((((())())()()))) [1 factors]
    (((((()))()())())) [1 factors]
    ((((())())()()))() [2 factors]
    ((((()))()())())() [2 factors]
    (((())())((()))()) [1 factors]
    ((())(((()))()())) [1 factors]
    ((())())((()))()() [4 factors]
    (())(((())())()()) [2 factors]
    (())(((()))()())() [3 factors]
  Cluster 42 (size 6):
    (((((())())())())) [1 factors]
    ((((())())())())() [2 factors]
    (((())())((())())) [1 factors]
    ((())(((())())())) [1 factors]
    ((())())((())())() [3 factors]
    (())(((())())())() [3 factors]
  Cluster 43 (size 4):
    (((((()))((()))))) [1 factors]
    ((((()))((()))))() [2 factors]
    ((()))((()))((())) [3 factors]
    (())(((()))((()))) [2 factors]
  Cluster 44 (size 5):
    (((((()))()()()))) [1 factors]
    ((((()))()()()))() [2 factors]
    (((()))((()))()()) [1 factors]
    ((()))((()))()()() [5 factors]
    (())(((()))()()()) [2 factors]
  Cluster 45 (size 6):
    ((((()()()()())))) [1 factors]
    ((((())))()()()()) [1 factors]
    (((()()()()())))() [2 factors]
    (((())))()()()()() [6 factors]
    (()()()()())((())) [2 factors]
    (())((()()()()())) [2 factors]
  Cluster 46 (size 7):
    ((((()()()())()))) [1 factors]
    ((((()))())()()()) [1 factors]
    (((()()()())()))() [2 factors]
    (((()))())()()()() [5 factors]
    ((()()()())((()))) [1 factors]
    (()()()())((()))() [3 factors]
    (())((()()()())()) [2 factors]
  Cluster 47 (size 7):
    ((((()()()()))())) [1 factors]
    ((((())()))()()()) [1 factors]
    (((()()()()))())() [2 factors]
    (((())()))()()()() [5 factors]
    ((())((()()()()))) [1 factors]
    (()()()())((())()) [2 factors]
    (())((()()()()))() [3 factors]
  Cluster 48 (size 6):
    ((((()()()())))()) [1 factors]
    ((((()())))()()()) [1 factors]
    (((()()()())))()() [3 factors]
    (((()())))()()()() [5 factors]
    (()()()())((()())) [2 factors]
    (()())((()()()())) [2 factors]
  Cluster 49 (size 8):
    ((((()()())(())))) [1 factors]
    (((()()())((())))) [1 factors]
    (((()()())(())))() [2 factors]
    (((())((())))()()) [1 factors]
    ((()()())((())))() [2 factors]
    ((())((())))()()() [4 factors]
    (()()())(())((())) [3 factors]
    (())((()()())(())) [2 factors]
  Cluster 50 (size 7):
    ((((()()())()()))) [1 factors]
    ((((()))()())()()) [1 factors]
    (((()()())()()))() [2 factors]
    (((()))()())()()() [4 factors]
    ((()()())((()))()) [1 factors]
    (()()())((()))()() [4 factors]
    (())((()()())()()) [2 factors]
  Cluster 51 (size 8):
    ((((()()())())())) [1 factors]
    ((((())())())()()) [1 factors]
    (((()()())())())() [2 factors]
    (((())())())()()() [4 factors]
    ((()()())((())())) [1 factors]
    ((())((()()())())) [1 factors]
    (()()())((())())() [3 factors]
    (())((()()())())() [3 factors]
  Cluster 52 (size 7):
    ((((()()())()))()) [1 factors]
    ((((()()))())()()) [1 factors]
    (((()()())()))()() [3 factors]
    (((()()))())()()() [4 factors]
    ((()()())((()()))) [1 factors]
    (()()())((()()))() [3 factors]
    (()())((()()())()) [2 factors]
  Cluster 53 (size 7):
    ((((()()()))()())) [1 factors]
    ((((())()()))()()) [1 factors]
    (((()()()))()())() [2 factors]
    (((())()()))()()() [4 factors]
    ((())((()()()))()) [1 factors]
    (()()())((())()()) [2 factors]
    (())((()()()))()() [4 factors]
  Cluster 54 (size 7):
    ((((()()()))())()) [1 factors]
    ((((()())()))()()) [1 factors]
    (((()()()))())()() [3 factors]
    (((()())()))()()() [4 factors]
    ((()())((()()()))) [1 factors]
    (()()())((()())()) [2 factors]
    (()())((()()()))() [3 factors]
  Cluster 55 (size 3):
    ((((()()())))()()) [1 factors]
    (((()()())))()()() [4 factors]
    (()()())((()()())) [2 factors]
  Cluster 56 (size 6):
    ((((()())((()))))) [1 factors]
    ((((()))((())))()) [1 factors]
    (((()())((()))))() [2 factors]
    (((()))((())))()() [3 factors]
    (()())((()))((())) [3 factors]
    (())((()())((()))) [2 factors]
  Cluster 57 (size 6):
    ((((()())(()())))) [1 factors]
    (((()())((())))()) [1 factors]
    (((()())(()())))() [2 factors]
    ((()())((())))()() [3 factors]
    (()())(()())((())) [3 factors]
    (())((()())(()())) [2 factors]
  Cluster 58 (size 9):
    ((((()())(())()))) [1 factors]
    (((()())((()))())) [1 factors]
    (((()())(())()))() [2 factors]
    (((())((()))())()) [1 factors]
    ((()())((()))())() [2 factors]
    ((()())(())((()))) [1 factors]
    ((())((()))())()() [3 factors]
    (()())(())((()))() [4 factors]
    (())((()())(())()) [2 factors]
  Cluster 59 (size 9):
    ((((()())(()))())) [1 factors]
    (((()())((())()))) [1 factors]
    (((()())(()))())() [2 factors]
    (((())((())()))()) [1 factors]
    ((()())((())()))() [2 factors]
    ((())((()())(()))) [1 factors]
    ((())((())()))()() [3 factors]
    (()())(())((())()) [3 factors]
    (())((()())(()))() [3 factors]
  Cluster 60 (size 8):
    ((((()())(())))()) [1 factors]
    (((()())((()())))) [1 factors]
    (((()())(())))()() [3 factors]
    (((())((()())))()) [1 factors]
    ((()())((()())))() [2 factors]
    ((())((()())))()() [3 factors]
    (()())((()())(())) [2 factors]
    (()())(())((()())) [3 factors]
  Cluster 61 (size 7):
    ((((()())()()()))) [1 factors]
    ((((()))()()())()) [1 factors]
    (((()())()()()))() [2 factors]
    (((()))()()())()() [3 factors]
    ((()())((()))()()) [1 factors]
    (()())((()))()()() [5 factors]
    (())((()())()()()) [2 factors]
  Cluster 62 (size 8):
    ((((()())()())())) [1 factors]
    ((((())())()())()) [1 factors]
    (((()())()())())() [2 factors]
    (((())())()())()() [3 factors]
    ((()())((())())()) [1 factors]
    ((())((()())()())) [1 factors]
    (()())((())())()() [4 factors]
    (())((()())()())() [3 factors]
  Cluster 63 (size 7):
    ((((()())()()))()) [1 factors]
    ((((()()))()())()) [1 factors]
    (((()())()()))()() [3 factors]
    (((()()))()())()() [3 factors]
    ((()())((()()))()) [1 factors]
    (()())((()())()()) [2 factors]
    (()())((()()))()() [4 factors]
  Cluster 64 (size 8):
    ((((()())())()())) [1 factors]
    ((((())()())())()) [1 factors]
    (((()())())()())() [2 factors]
    (((())()())())()() [3 factors]
    ((()())((())()())) [1 factors]
    ((())((()())())()) [1 factors]
    (()())((())()())() [3 factors]
    (())((()())())()() [4 factors]
  Cluster 65 (size 4):
    ((((()())())())()) [1 factors]
    (((()())())())()() [3 factors]
    ((()())((()())())) [1 factors]
    (()())((()())())() [3 factors]
  Cluster 66 (size 7):
    ((((()()))()()())) [1 factors]
    ((((())()()()))()) [1 factors]
    (((()()))()()())() [2 factors]
    (((())()()()))()() [3 factors]
    ((())((()()))()()) [1 factors]
    (()())((())()()()) [2 factors]
    (())((()()))()()() [5 factors]
  Cluster 67 (size 9):
    ((((())((()()))))) [1 factors]
    ((((())((()))))()) [1 factors]
    ((((()))((()())))) [1 factors]
    (((())((()()))))() [2 factors]
    (((())((()))))()() [3 factors]
    (((()))((()())))() [2 factors]
    (()())((())((()))) [2 factors]
    (())((())((()()))) [2 factors]
    (())((()))((()())) [3 factors]
  Cluster 68 (size 10):
    ((((())((())())))) [1 factors]
    ((((())((())))())) [1 factors]
    ((((())())((())))) [1 factors]
    (((())((())())))() [2 factors]
    (((())((())))())() [2 factors]
    (((())())((())))() [2 factors]
    ((())((())((())))) [1 factors]
    (())((())((())())) [2 factors]
    (())((())((())))() [3 factors]
    (())((())())((())) [3 factors]
  Cluster 69 (size 7):
    ((((())((()))()))) [1 factors]
    ((((()))((()))())) [1 factors]
    (((())((()))()))() [2 factors]
    (((()))((()))())() [2 factors]
    ((())((()))((()))) [1 factors]
    (())((())((()))()) [2 factors]
    (())((()))((()))() [4 factors]
  Cluster 70 (size 6):
    ((((())(())(())))) [1 factors]
    (((())(())((())))) [1 factors]
    (((())(())(())))() [2 factors]
    ((())(())((())))() [2 factors]
    (())((())(())(())) [2 factors]
    (())(())(())((())) [4 factors]
  Cluster 71 (size 7):
    ((((())(())()()))) [1 factors]
    (((())((()))()())) [1 factors]
    (((())(())()()))() [2 factors]
    ((())((()))()())() [2 factors]
    ((())(())((()))()) [1 factors]
    (())((())(())()()) [2 factors]
    (())(())((()))()() [5 factors]
  Cluster 72 (size 8):
    ((((())(())())())) [1 factors]
    (((())((())())())) [1 factors]
    (((())(())())())() [2 factors]
    ((())((())(())())) [1 factors]
    ((())((())())())() [2 factors]
    ((())(())((())())) [1 factors]
    (())((())(())())() [3 factors]
    (())(())((())())() [4 factors]
  Cluster 73 (size 7):
    ((((())(())()))()) [1 factors]
    (((())((()()))())) [1 factors]
    (((())(())()))()() [3 factors]
    ((())((()()))())() [2 factors]
    ((())(())((()()))) [1 factors]
    (()())((())(())()) [2 factors]
    (())(())((()()))() [4 factors]
  Cluster 74 (size 7):
    ((((())(()))()())) [1 factors]
    (((())((())()()))) [1 factors]
    (((())(()))()())() [2 factors]
    ((())((())(()))()) [1 factors]
    ((())((())()()))() [2 factors]
    (())((())(()))()() [4 factors]
    (())(())((())()()) [3 factors]
  Cluster 75 (size 7):
    ((((())(()))())()) [1 factors]
    (((())((()())()))) [1 factors]
    (((())(()))())()() [3 factors]
    ((()())((())(()))) [1 factors]
    ((())((()())()))() [2 factors]
    (()())((())(()))() [3 factors]
    (())(())((()())()) [3 factors]
  Cluster 76 (size 6):
    ((((())(())))()()) [1 factors]
    (((())((()()())))) [1 factors]
    (((())(())))()()() [4 factors]
    ((())((()()())))() [2 factors]
    (()()())((())(())) [2 factors]
    (())(())((()()())) [3 factors]
  Cluster 77 (size 7):
    ((((())()()()()))) [1 factors]
    ((((()))()()()())) [1 factors]
    (((())()()()()))() [2 factors]
    (((()))()()()())() [2 factors]
    ((())((()))()()()) [1 factors]
    (())((())()()()()) [2 factors]
    (())((()))()()()() [6 factors]
  Cluster 78 (size 8):
    ((((())()()())())) [1 factors]
    ((((())())()()())) [1 factors]
    (((())()()())())() [2 factors]
    (((())())()()())() [2 factors]
    ((())((())()()())) [1 factors]
    ((())((())())()()) [1 factors]
    (())((())()()())() [3 factors]
    (())((())())()()() [5 factors]
  Cluster 79 (size 4):
    ((((())()())()())) [1 factors]
    (((())()())()())() [2 factors]
    ((())((())()())()) [1 factors]
    (())((())()())()() [4 factors]
  Cluster 80 (size 5):
    (((()()()()()()))) [1 factors]
    (((()))()()()()()) [1 factors]
    ((()()()()()()))() [2 factors]
    ((()))()()()()()() [7 factors]
    (()()()()()())(()) [2 factors]
  Cluster 81 (size 6):
    (((()()()()())())) [1 factors]
    (((())())()()()()) [1 factors]
    ((()()()()())(())) [1 factors]
    ((()()()()())())() [2 factors]
    ((())())()()()()() [6 factors]
    (()()()()())(())() [3 factors]
  Cluster 82 (size 5):
    (((()()()()()))()) [1 factors]
    (((()()))()()()()) [1 factors]
    ((()()()()()))()() [3 factors]
    ((()()))()()()()() [6 factors]
    (()()()()())(()()) [2 factors]
  Cluster 83 (size 5):
    (((()()()())(()))) [1 factors]
    (((())(()))()()()) [1 factors]
    ((()()()())(()))() [2 factors]
    ((())(()))()()()() [5 factors]
    (()()()())(())(()) [3 factors]
  Cluster 84 (size 6):
    (((()()()())()())) [1 factors]
    (((())()())()()()) [1 factors]
    ((()()()())(())()) [1 factors]
    ((()()()())()())() [2 factors]
    ((())()())()()()() [5 factors]
    (()()()())(())()() [4 factors]
  Cluster 85 (size 6):
    (((()()()())())()) [1 factors]
    (((()())())()()()) [1 factors]
    ((()()()())(()())) [1 factors]
    ((()()()())())()() [3 factors]
    ((()())())()()()() [5 factors]
    (()()()())(()())() [3 factors]
  Cluster 86 (size 5):
    (((()()()()))()()) [1 factors]
    (((()()()))()()()) [1 factors]
    ((()()()()))()()() [4 factors]
    ((()()()))()()()() [5 factors]
    (()()()())(()()()) [2 factors]
  Cluster 87 (size 7):
    (((()()())(()()))) [1 factors]
    (((()()())(()))()) [1 factors]
    (((()())(()))()()) [1 factors]
    ((()()())(()()))() [2 factors]
    ((()()())(()))()() [3 factors]
    ((()())(()))()()() [4 factors]
    (()()())(()())(()) [3 factors]
  Cluster 88 (size 6):
    (((()()())(())())) [1 factors]
    (((())(())())()()) [1 factors]
    ((()()())(())(())) [1 factors]
    ((()()())(())())() [2 factors]
    ((())(())())()()() [4 factors]
    (()()())(())(())() [4 factors]
  Cluster 89 (size 6):
    (((()()())()()())) [1 factors]
    (((())()()())()()) [1 factors]
    ((()()())(())()()) [1 factors]
    ((()()())()()())() [2 factors]
    ((())()()())()()() [4 factors]
    (()()())(())()()() [5 factors]
  Cluster 90 (size 6):
    (((()()())()())()) [1 factors]
    (((()())()())()()) [1 factors]
    ((()()())(()())()) [1 factors]
    ((()()())()())()() [3 factors]
    ((()())()())()()() [4 factors]
    (()()())(()())()() [4 factors]
  Cluster 91 (size 4):
    (((()()())())()()) [1 factors]
    ((()()())(()()())) [1 factors]
    ((()()())())()()() [4 factors]
    (()()())(()()())() [3 factors]
  Cluster 92 (size 6):
    (((()())(()())())) [1 factors]
    (((()())(())())()) [1 factors]
    ((()())(()())(())) [1 factors]
    ((()())(()())())() [2 factors]
    ((()())(())())()() [3 factors]
    (()())(()())(())() [4 factors]
  Cluster 93 (size 3):
    (((()())(()()))()) [1 factors]
    ((()())(()()))()() [3 factors]
    (()())(()())(()()) [3 factors]
  Cluster 94 (size 5):
    (((()())(())(()))) [1 factors]
    (((())(())(()))()) [1 factors]
    ((()())(())(()))() [2 factors]
    ((())(())(()))()() [3 factors]
    (()())(())(())(()) [4 factors]
  Cluster 95 (size 6):
    (((()())(())()())) [1 factors]
    (((())(())()())()) [1 factors]
    ((()())(())(())()) [1 factors]
    ((()())(())()())() [2 factors]
    ((())(())()())()() [3 factors]
    (()())(())(())()() [5 factors]
  Cluster 96 (size 6):
    (((()())()()()())) [1 factors]
    (((())()()()())()) [1 factors]
    ((()())(())()()()) [1 factors]
    ((()())()()()())() [2 factors]
    ((())()()()())()() [3 factors]
    (()())(())()()()() [6 factors]
  Cluster 97 (size 4):
    (((()())()()())()) [1 factors]
    ((()())(()())()()) [1 factors]
    ((()())()()())()() [3 factors]
    (()())(()())()()() [5 factors]
  Cluster 98 (size 3):
    (((())((())(())))) [1 factors]
    ((())((())(())))() [2 factors]
    (())(())((())(())) [3 factors]
  Cluster 99 (size 4):
    (((())(())(())())) [1 factors]
    ((())(())(())(())) [1 factors]
    ((())(())(())())() [2 factors]
    (())(())(())(())() [5 factors]
  Cluster 100 (size 4):
    (((())(())()()())) [1 factors]
    ((())(())(())()()) [1 factors]
    ((())(())()()())() [2 factors]
    (())(())(())()()() [6 factors]
  Cluster 101 (size 4):
    (((())()()()()())) [1 factors]
    ((())(())()()()()) [1 factors]
    ((())()()()()())() [2 factors]
    (())(())()()()()() [7 factors]
  Cluster 102 (size 4):
    ((()()()()()()())) [1 factors]
    ((())()()()()()()) [1 factors]
    (()()()()()()())() [2 factors]
    (())()()()()()()() [8 factors]
  Cluster 103 (size 4):
    ((()()()()()())()) [1 factors]
    ((()())()()()()()) [1 factors]
    (()()()()()())()() [3 factors]
    (()())()()()()()() [7 factors]
  Cluster 104 (size 4):
    ((()()()()())()()) [1 factors]
    ((()()())()()()()) [1 factors]
    (()()()()())()()() [4 factors]
    (()()())()()()()() [6 factors]
  Cluster 105 (size 2):
    ((()()()())()()()) [1 factors]
    (()()()())()()()() [5 factors]
  Cluster 106 (size 2):
    (()()()()()()()()) [1 factors]
    ()()()()()()()()() [9 factors]

Note: Each cluster represents circle topologies that are equivalent when embedded on a sphere surface.
```

Flips of the form `A (B)` → `(A) B`:

```
# source | factor | A | B | form=A(B) | image=(A)B
source=((((((((())))))))) | factor=1 | A= | B=(((((((()))))))) | form=((((((((())))))))) | image=(((((((())))))))()
source=(((((((()()))))))) | factor=1 | A= | B=((((((()())))))) | form=(((((((()()))))))) | image=((((((()()))))))()
source=(((((((())())))))) | factor=1 | A= | B=((((((())()))))) | form=(((((((())())))))) | image=((((((())())))))()
source=(((((((()))()))))) | factor=1 | A= | B=((((((()))())))) | form=(((((((()))()))))) | image=((((((()))()))))()
source=(((((((())))())))) | factor=1 | A= | B=((((((())))()))) | form=(((((((())))())))) | image=((((((())))())))()
source=(((((((()))))()))) | factor=1 | A= | B=((((((()))))())) | form=(((((((()))))()))) | image=((((((()))))()))()
source=(((((((())))))())) | factor=1 | A= | B=((((((())))))()) | form=(((((((())))))())) | image=((((((())))))())()
source=(((((((()))))))()) | factor=1 | A= | B=((((((()))))))() | form=(((((((()))))))()) | image=((((((()))))))()()
source=(((((((())))))))() | factor=1 | A=() | B=((((((())))))) | form=()(((((((()))))))) | image=(())((((((()))))))
source=(((((((())))))))() | factor=2 | A=(((((((()))))))) | B= | form=(((((((())))))))() | image=((((((((()))))))))
source=((((((()()())))))) | factor=1 | A= | B=(((((()()()))))) | form=((((((()()())))))) | image=(((((()()())))))()
source=((((((()())()))))) | factor=1 | A= | B=(((((()())())))) | form=((((((()())()))))) | image=(((((()())()))))()
source=((((((()()))())))) | factor=1 | A= | B=(((((()()))()))) | form=((((((()()))())))) | image=(((((()()))())))()
source=((((((()())))()))) | factor=1 | A= | B=(((((()())))())) | form=((((((()())))()))) | image=(((((()())))()))()
source=((((((()()))))())) | factor=1 | A= | B=(((((()()))))()) | form=((((((()()))))())) | image=(((((()()))))())()
source=((((((()())))))()) | factor=1 | A= | B=(((((()())))))() | form=((((((()())))))()) | image=(((((()())))))()()
source=((((((()()))))))() | factor=1 | A=() | B=(((((()()))))) | form=()((((((()())))))) | image=(())(((((()())))))
source=((((((()()))))))() | factor=2 | A=((((((()())))))) | B= | form=((((((()()))))))() | image=(((((((()())))))))
source=((((((())(())))))) | factor=1 | A= | B=(((((())(()))))) | form=((((((())(())))))) | image=(((((())(())))))()
source=((((((())()()))))) | factor=1 | A= | B=(((((())()())))) | form=((((((())()()))))) | image=(((((())()()))))()
source=((((((())())())))) | factor=1 | A= | B=(((((())())()))) | form=((((((())())())))) | image=(((((())())())))()
source=((((((())()))()))) | factor=1 | A= | B=(((((())()))())) | form=((((((())()))()))) | image=(((((())()))()))()
source=((((((())())))())) | factor=1 | A= | B=(((((())())))()) | form=((((((())())))())) | image=(((((())())))())()
source=((((((())()))))()) | factor=1 | A= | B=(((((())()))))() | form=((((((())()))))()) | image=(((((())()))))()()
source=((((((())())))))() | factor=1 | A=() | B=(((((())())))) | form=()((((((())()))))) | image=(())(((((())()))))
source=((((((())())))))() | factor=2 | A=((((((())()))))) | B= | form=((((((())())))))() | image=(((((((())()))))))
source=((((((()))()())))) | factor=1 | A= | B=(((((()))()()))) | form=((((((()))()())))) | image=(((((()))()())))()
source=((((((()))())()))) | factor=1 | A= | B=(((((()))())())) | form=((((((()))())()))) | image=(((((()))())()))()
source=((((((()))()))())) | factor=1 | A= | B=(((((()))()))()) | form=((((((()))()))())) | image=(((((()))()))())()
source=((((((()))())))()) | factor=1 | A= | B=(((((()))())))() | form=((((((()))())))()) | image=(((((()))())))()()
source=((((((()))()))))() | factor=1 | A=() | B=(((((()))()))) | form=()((((((()))())))) | image=(())(((((()))())))
source=((((((()))()))))() | factor=2 | A=((((((()))())))) | B= | form=((((((()))()))))() | image=(((((((()))())))))
source=((((((())))()()))) | factor=1 | A= | B=(((((())))()())) | form=((((((())))()()))) | image=(((((())))()()))()
source=((((((())))())())) | factor=1 | A= | B=(((((())))())()) | form=((((((())))())())) | image=(((((())))())())()
source=((((((())))()))()) | factor=1 | A= | B=(((((())))()))() | form=((((((())))()))()) | image=(((((())))()))()()
source=((((((())))())))() | factor=1 | A=() | B=(((((())))())) | form=()((((((())))()))) | image=(())(((((())))()))
source=((((((())))())))() | factor=2 | A=((((((())))()))) | B= | form=((((((())))())))() | image=(((((((())))()))))
source=((((((()))))()())) | factor=1 | A= | B=(((((()))))()()) | form=((((((()))))()())) | image=(((((()))))()())()
source=((((((()))))())()) | factor=1 | A= | B=(((((()))))())() | form=((((((()))))())()) | image=(((((()))))())()()
source=((((((()))))()))() | factor=1 | A=() | B=(((((()))))()) | form=()((((((()))))())) | image=(())(((((()))))())
source=((((((()))))()))() | factor=2 | A=((((((()))))())) | B= | form=((((((()))))()))() | image=(((((((()))))())))
source=((((((())))))()()) | factor=1 | A= | B=(((((())))))()() | form=((((((())))))()()) | image=(((((())))))()()()
source=((((((())))))())() | factor=1 | A=() | B=(((((())))))() | form=()((((((())))))()) | image=(())(((((())))))()
source=((((((())))))())() | factor=2 | A=((((((())))))()) | B= | form=((((((())))))())() | image=(((((((())))))()))
source=((((((()))))))()() | factor=1 | A=()() | B=(((((()))))) | form=()()((((((())))))) | image=(()())(((((())))))
source=((((((()))))))()() | factor=2 | A=((((((()))))))() | B= | form=((((((()))))))()() | image=(((((((()))))))())
source=((((((()))))))()() | factor=3 | A=((((((()))))))() | B= | form=((((((()))))))()() | image=(((((((()))))))())
source=(((((()()()()))))) | factor=1 | A= | B=((((()()()())))) | form=(((((()()()()))))) | image=((((()()()()))))()
source=(((((()()())())))) | factor=1 | A= | B=((((()()())()))) | form=(((((()()())())))) | image=((((()()())())))()
source=(((((()()()))()))) | factor=1 | A= | B=((((()()()))())) | form=(((((()()()))()))) | image=((((()()()))()))()
source=(((((()()())))())) | factor=1 | A= | B=((((()()())))()) | form=(((((()()())))())) | image=((((()()())))())()
source=(((((()()()))))()) | factor=1 | A= | B=((((()()()))))() | form=(((((()()()))))()) | image=((((()()()))))()()
source=(((((()()())))))() | factor=1 | A=() | B=((((()()())))) | form=()(((((()()()))))) | image=(())((((()()()))))
source=(((((()()())))))() | factor=2 | A=(((((()()()))))) | B= | form=(((((()()())))))() | image=((((((()()()))))))
source=(((((()())(()))))) | factor=1 | A= | B=((((()())(())))) | form=(((((()())(()))))) | image=((((()())(()))))()
source=(((((()())()())))) | factor=1 | A= | B=((((()())()()))) | form=(((((()())()())))) | image=((((()())()())))()
source=(((((()())())()))) | factor=1 | A= | B=((((()())())())) | form=(((((()())())()))) | image=((((()())())()))()
source=(((((()())()))())) | factor=1 | A= | B=((((()())()))()) | form=(((((()())()))())) | image=((((()())()))())()
source=(((((()())())))()) | factor=1 | A= | B=((((()())())))() | form=(((((()())())))()) | image=((((()())())))()()
source=(((((()())()))))() | factor=1 | A=() | B=((((()())()))) | form=()(((((()())())))) | image=(())((((()())())))
source=(((((()())()))))() | factor=2 | A=(((((()())())))) | B= | form=(((((()())()))))() | image=((((((()())())))))
source=(((((()()))()()))) | factor=1 | A= | B=((((()()))()())) | form=(((((()()))()()))) | image=((((()()))()()))()
source=(((((()()))())())) | factor=1 | A= | B=((((()()))())()) | form=(((((()()))())())) | image=((((()()))())())()
source=(((((()()))()))()) | factor=1 | A= | B=((((()()))()))() | form=(((((()()))()))()) | image=((((()()))()))()()
source=(((((()()))())))() | factor=1 | A=() | B=((((()()))())) | form=()(((((()()))()))) | image=(())((((()()))()))
source=(((((()()))())))() | factor=2 | A=(((((()()))()))) | B= | form=(((((()()))())))() | image=((((((()()))()))))
source=(((((()())))()())) | factor=1 | A= | B=((((()())))()()) | form=(((((()())))()())) | image=((((()())))()())()
source=(((((()())))())()) | factor=1 | A= | B=((((()())))())() | form=(((((()())))())()) | image=((((()())))())()()
source=(((((()())))()))() | factor=1 | A=() | B=((((()())))()) | form=()(((((()())))())) | image=(())((((()())))())
source=(((((()())))()))() | factor=2 | A=(((((()())))())) | B= | form=(((((()())))()))() | image=((((((()())))())))
source=(((((()()))))()()) | factor=1 | A= | B=((((()()))))()() | form=(((((()()))))()()) | image=((((()()))))()()()
source=(((((()()))))())() | factor=1 | A=() | B=((((()()))))() | form=()(((((()()))))()) | image=(())((((()()))))()
source=(((((()()))))())() | factor=2 | A=(((((()()))))()) | B= | form=(((((()()))))())() | image=((((((()()))))()))
source=(((((()())))))()() | factor=1 | A=()() | B=((((()())))) | form=()()(((((()()))))) | image=(()())((((()()))))
source=(((((()())))))()() | factor=2 | A=(((((()())))))() | B= | form=(((((()())))))()() | image=((((((()())))))())
source=(((((()())))))()() | factor=3 | A=(((((()())))))() | B= | form=(((((()())))))()() | image=((((((()())))))())
source=(((((())((())))))) | factor=1 | A= | B=((((())((()))))) | form=(((((())((())))))) | image=((((())((())))))()
source=(((((())(())())))) | factor=1 | A= | B=((((())(())()))) | form=(((((())(())())))) | image=((((())(())())))()
source=(((((())(()))()))) | factor=1 | A= | B=((((())(()))())) | form=(((((())(()))()))) | image=((((())(()))()))()
source=(((((())(())))())) | factor=1 | A= | B=((((())(())))()) | form=(((((())(())))())) | image=((((())(())))())()
source=(((((())(()))))()) | factor=1 | A= | B=((((())(()))))() | form=(((((())(()))))()) | image=((((())(()))))()()
source=(((((())(())))))() | factor=1 | A=() | B=((((())(())))) | form=()(((((())(()))))) | image=(())((((())(()))))
source=(((((())(())))))() | factor=2 | A=(((((())(()))))) | B= | form=(((((())(())))))() | image=((((((())(()))))))
source=(((((())()()())))) | factor=1 | A= | B=((((())()()()))) | form=(((((())()()())))) | image=((((())()()())))()
source=(((((())()())()))) | factor=1 | A= | B=((((())()())())) | form=(((((())()())()))) | image=((((())()())()))()
source=(((((())()()))())) | factor=1 | A= | B=((((())()()))()) | form=(((((())()()))())) | image=((((())()()))())()
source=(((((())()())))()) | factor=1 | A= | B=((((())()())))() | form=(((((())()())))()) | image=((((())()())))()()
source=(((((())()()))))() | factor=1 | A=() | B=((((())()()))) | form=()(((((())()())))) | image=(())((((())()())))
source=(((((())()()))))() | factor=2 | A=(((((())()())))) | B= | form=(((((())()()))))() | image=((((((())()())))))
source=(((((())())()()))) | factor=1 | A= | B=((((())())()())) | form=(((((())())()()))) | image=((((())())()()))()
source=(((((())())())())) | factor=1 | A= | B=((((())())())()) | form=(((((())())())())) | image=((((())())())())()
source=(((((())())()))()) | factor=1 | A= | B=((((())())()))() | form=(((((())())()))()) | image=((((())())()))()()
source=(((((())())())))() | factor=1 | A=() | B=((((())())())) | form=()(((((())())()))) | image=(())((((())())()))
source=(((((())())())))() | factor=2 | A=(((((())())()))) | B= | form=(((((())())())))() | image=((((((())())()))))
source=(((((())()))()())) | factor=1 | A= | B=((((())()))()()) | form=(((((())()))()())) | image=((((())()))()())()
source=(((((())()))())()) | factor=1 | A= | B=((((())()))())() | form=(((((())()))())()) | image=((((())()))())()()
source=(((((())()))()))() | factor=1 | A=() | B=((((())()))()) | form=()(((((())()))())) | image=(())((((())()))())
source=(((((())()))()))() | factor=2 | A=(((((())()))())) | B= | form=(((((())()))()))() | image=((((((())()))())))
source=(((((())())))()()) | factor=1 | A= | B=((((())())))()() | form=(((((())())))()()) | image=((((())())))()()()
source=(((((())())))())() | factor=1 | A=() | B=((((())())))() | form=()(((((())())))()) | image=(())((((())())))()
source=(((((())())))())() | factor=2 | A=(((((())())))()) | B= | form=(((((())())))())() | image=((((((())())))()))
source=(((((())()))))()() | factor=1 | A=()() | B=((((())()))) | form=()()(((((())())))) | image=(()())((((())())))
source=(((((())()))))()() | factor=2 | A=(((((())()))))() | B= | form=(((((())()))))()() | image=((((((())()))))())
source=(((((())()))))()() | factor=3 | A=(((((())()))))() | B= | form=(((((())()))))()() | image=((((((())()))))())
source=(((((()))((()))))) | factor=1 | A= | B=((((()))((())))) | form=(((((()))((()))))) | image=((((()))((()))))()
source=(((((()))()()()))) | factor=1 | A= | B=((((()))()()())) | form=(((((()))()()()))) | image=((((()))()()()))()
source=(((((()))()())())) | factor=1 | A= | B=((((()))()())()) | form=(((((()))()())())) | image=((((()))()())())()
source=(((((()))()()))()) | factor=1 | A= | B=((((()))()()))() | form=(((((()))()()))()) | image=((((()))()()))()()
source=(((((()))()())))() | factor=1 | A=() | B=((((()))()())) | form=()(((((()))()()))) | image=(())((((()))()()))
source=(((((()))()())))() | factor=2 | A=(((((()))()()))) | B= | form=(((((()))()())))() | image=((((((()))()()))))
source=(((((()))())()())) | factor=1 | A= | B=((((()))())()()) | form=(((((()))())()())) | image=((((()))())()())()
source=(((((()))())())()) | factor=1 | A= | B=((((()))())())() | form=(((((()))())())()) | image=((((()))())())()()
source=(((((()))())()))() | factor=1 | A=() | B=((((()))())()) | form=()(((((()))())())) | image=(())((((()))())())
source=(((((()))())()))() | factor=2 | A=(((((()))())())) | B= | form=(((((()))())()))() | image=((((((()))())())))
source=(((((()))()))()()) | factor=1 | A= | B=((((()))()))()() | form=(((((()))()))()()) | image=((((()))()))()()()
source=(((((()))()))())() | factor=1 | A=() | B=((((()))()))() | form=()(((((()))()))()) | image=(())((((()))()))()
source=(((((()))()))())() | factor=2 | A=(((((()))()))()) | B= | form=(((((()))()))())() | image=((((((()))()))()))
source=(((((()))())))()() | factor=1 | A=()() | B=((((()))())) | form=()()(((((()))()))) | image=(()())((((()))()))
source=(((((()))())))()() | factor=2 | A=(((((()))())))() | B= | form=(((((()))())))()() | image=((((((()))())))())
source=(((((()))())))()() | factor=3 | A=(((((()))())))() | B= | form=(((((()))())))()() | image=((((((()))())))())
source=(((((())))()()())) | factor=1 | A= | B=((((())))()()()) | form=(((((())))()()())) | image=((((())))()()())()
source=(((((())))()())()) | factor=1 | A= | B=((((())))()())() | form=(((((())))()())()) | image=((((())))()())()()
source=(((((())))()()))() | factor=1 | A=() | B=((((())))()()) | form=()(((((())))()())) | image=(())((((())))()())
source=(((((())))()()))() | factor=2 | A=(((((())))()())) | B= | form=(((((())))()()))() | image=((((((())))()())))
source=(((((())))())()()) | factor=1 | A= | B=((((())))())()() | form=(((((())))())()()) | image=((((())))())()()()
source=(((((())))())())() | factor=1 | A=() | B=((((())))())() | form=()(((((())))())()) | image=(())((((())))())()
source=(((((())))())())() | factor=2 | A=(((((())))())()) | B= | form=(((((())))())())() | image=((((((())))())()))
source=(((((())))()))()() | factor=1 | A=()() | B=((((())))()) | form=()()(((((())))())) | image=(()())((((())))())
source=(((((())))()))()() | factor=2 | A=(((((())))()))() | B= | form=(((((())))()))()() | image=((((((())))()))())
source=(((((())))()))()() | factor=3 | A=(((((())))()))() | B= | form=(((((())))()))()() | image=((((((())))()))())
source=(((((()))))()()()) | factor=1 | A= | B=((((()))))()()() | form=(((((()))))()()()) | image=((((()))))()()()()
source=(((((()))))()())() | factor=1 | A=() | B=((((()))))()() | form=()(((((()))))()()) | image=(())((((()))))()()
source=(((((()))))()())() | factor=2 | A=(((((()))))()()) | B= | form=(((((()))))()())() | image=((((((()))))()()))
source=(((((()))))())()() | factor=1 | A=()() | B=((((()))))() | form=()()(((((()))))()) | image=(()())((((()))))()
source=(((((()))))())()() | factor=2 | A=(((((()))))())() | B= | form=(((((()))))())()() | image=((((((()))))())())
source=(((((()))))())()() | factor=3 | A=(((((()))))())() | B= | form=(((((()))))())()() | image=((((((()))))())())
source=(((((())))))()()() | factor=1 | A=()()() | B=((((())))) | form=()()()(((((()))))) | image=(()()())((((()))))
source=(((((())))))()()() | factor=2 | A=(((((())))))()() | B= | form=(((((())))))()()() | image=((((((())))))()())
source=(((((())))))()()() | factor=3 | A=(((((())))))()() | B= | form=(((((())))))()()() | image=((((((())))))()())
source=(((((())))))()()() | factor=4 | A=(((((())))))()() | B= | form=(((((())))))()()() | image=((((((())))))()())
source=((((()()()()())))) | factor=1 | A= | B=(((()()()()()))) | form=((((()()()()())))) | image=(((()()()()())))()
source=((((()()()())()))) | factor=1 | A= | B=(((()()()())())) | form=((((()()()())()))) | image=(((()()()())()))()
source=((((()()()()))())) | factor=1 | A= | B=(((()()()()))()) | form=((((()()()()))())) | image=(((()()()()))())()
source=((((()()()())))()) | factor=1 | A= | B=(((()()()())))() | form=((((()()()())))()) | image=(((()()()())))()()
source=((((()()()()))))() | factor=1 | A=() | B=(((()()()()))) | form=()((((()()()())))) | image=(())(((()()()())))
source=((((()()()()))))() | factor=2 | A=((((()()()())))) | B= | form=((((()()()()))))() | image=(((((()()()())))))
source=((((()()())(())))) | factor=1 | A= | B=(((()()())(()))) | form=((((()()())(())))) | image=(((()()())(())))()
source=((((()()())()()))) | factor=1 | A= | B=(((()()())()())) | form=((((()()())()()))) | image=(((()()())()()))()
source=((((()()())())())) | factor=1 | A= | B=(((()()())())()) | form=((((()()())())())) | image=(((()()())())())()
source=((((()()())()))()) | factor=1 | A= | B=(((()()())()))() | form=((((()()())()))()) | image=(((()()())()))()()
source=((((()()())())))() | factor=1 | A=() | B=(((()()())())) | form=()((((()()())()))) | image=(())(((()()())()))
source=((((()()())())))() | factor=2 | A=((((()()())()))) | B= | form=((((()()())())))() | image=(((((()()())()))))
source=((((()()()))()())) | factor=1 | A= | B=(((()()()))()()) | form=((((()()()))()())) | image=(((()()()))()())()
source=((((()()()))())()) | factor=1 | A= | B=(((()()()))())() | form=((((()()()))())()) | image=(((()()()))())()()
source=((((()()()))()))() | factor=1 | A=() | B=(((()()()))()) | form=()((((()()()))())) | image=(())(((()()()))())
source=((((()()()))()))() | factor=2 | A=((((()()()))())) | B= | form=((((()()()))()))() | image=(((((()()()))())))
source=((((()()())))()()) | factor=1 | A= | B=(((()()())))()() | form=((((()()())))()()) | image=(((()()())))()()()
source=((((()()())))())() | factor=1 | A=() | B=(((()()())))() | form=()((((()()())))()) | image=(())(((()()())))()
source=((((()()())))())() | factor=2 | A=((((()()())))()) | B= | form=((((()()())))())() | image=(((((()()())))()))
source=((((()()()))))()() | factor=1 | A=()() | B=(((()()()))) | form=()()((((()()())))) | image=(()())(((()()())))
source=((((()()()))))()() | factor=2 | A=((((()()()))))() | B= | form=((((()()()))))()() | image=(((((()()()))))())
source=((((()()()))))()() | factor=3 | A=((((()()()))))() | B= | form=((((()()()))))()() | image=(((((()()()))))())
source=((((()())((()))))) | factor=1 | A= | B=(((()())((())))) | form=((((()())((()))))) | image=(((()())((()))))()
source=((((()())(()())))) | factor=1 | A= | B=(((()())(()()))) | form=((((()())(()())))) | image=(((()())(()())))()
source=((((()())(())()))) | factor=1 | A= | B=(((()())(())())) | form=((((()())(())()))) | image=(((()())(())()))()
source=((((()())(()))())) | factor=1 | A= | B=(((()())(()))()) | form=((((()())(()))())) | image=(((()())(()))())()
source=((((()())(())))()) | factor=1 | A= | B=(((()())(())))() | form=((((()())(())))()) | image=(((()())(())))()()
source=((((()())(()))))() | factor=1 | A=() | B=(((()())(()))) | form=()((((()())(())))) | image=(())(((()())(())))
source=((((()())(()))))() | factor=2 | A=((((()())(())))) | B= | form=((((()())(()))))() | image=(((((()())(())))))
source=((((()())()()()))) | factor=1 | A= | B=(((()())()()())) | form=((((()())()()()))) | image=(((()())()()()))()
source=((((()())()())())) | factor=1 | A= | B=(((()())()())()) | form=((((()())()())())) | image=(((()())()())())()
source=((((()())()()))()) | factor=1 | A= | B=(((()())()()))() | form=((((()())()()))()) | image=(((()())()()))()()
source=((((()())()())))() | factor=1 | A=() | B=(((()())()())) | form=()((((()())()()))) | image=(())(((()())()()))
source=((((()())()())))() | factor=2 | A=((((()())()()))) | B= | form=((((()())()())))() | image=(((((()())()()))))
source=((((()())())()())) | factor=1 | A= | B=(((()())())()()) | form=((((()())())()())) | image=(((()())())()())()
source=((((()())())())()) | factor=1 | A= | B=(((()())())())() | form=((((()())())())()) | image=(((()())())())()()
source=((((()())())()))() | factor=1 | A=() | B=(((()())())()) | form=()((((()())())())) | image=(())(((()())())())
source=((((()())())()))() | factor=2 | A=((((()())())())) | B= | form=((((()())())()))() | image=(((((()())())())))
source=((((()())()))()()) | factor=1 | A= | B=(((()())()))()() | form=((((()())()))()()) | image=(((()())()))()()()
source=((((()())()))())() | factor=1 | A=() | B=(((()())()))() | form=()((((()())()))()) | image=(())(((()())()))()
source=((((()())()))())() | factor=2 | A=((((()())()))()) | B= | form=((((()())()))())() | image=(((((()())()))()))
source=((((()())())))()() | factor=1 | A=()() | B=(((()())())) | form=()()((((()())()))) | image=(()())(((()())()))
source=((((()())())))()() | factor=2 | A=((((()())())))() | B= | form=((((()())())))()() | image=(((((()())())))())
source=((((()())())))()() | factor=3 | A=((((()())())))() | B= | form=((((()())())))()() | image=(((((()())())))())
source=((((()()))()()())) | factor=1 | A= | B=(((()()))()()()) | form=((((()()))()()())) | image=(((()()))()()())()
source=((((()()))()())()) | factor=1 | A= | B=(((()()))()())() | form=((((()()))()())()) | image=(((()()))()())()()
source=((((()()))()()))() | factor=1 | A=() | B=(((()()))()()) | form=()((((()()))()())) | image=(())(((()()))()())
source=((((()()))()()))() | factor=2 | A=((((()()))()())) | B= | form=((((()()))()()))() | image=(((((()()))()())))
source=((((()()))())()()) | factor=1 | A= | B=(((()()))())()() | form=((((()()))())()()) | image=(((()()))())()()()
source=((((()()))())())() | factor=1 | A=() | B=(((()()))())() | form=()((((()()))())()) | image=(())(((()()))())()
source=((((()()))())())() | factor=2 | A=((((()()))())()) | B= | form=((((()()))())())() | image=(((((()()))())()))
source=((((()()))()))()() | factor=1 | A=()() | B=(((()()))()) | form=()()((((()()))())) | image=(()())(((()()))())
source=((((()()))()))()() | factor=2 | A=((((()()))()))() | B= | form=((((()()))()))()() | image=(((((()()))()))())
source=((((()()))()))()() | factor=3 | A=((((()()))()))() | B= | form=((((()()))()))()() | image=(((((()()))()))())
source=((((()())))()()()) | factor=1 | A= | B=(((()())))()()() | form=((((()())))()()()) | image=(((()())))()()()()
source=((((()())))()())() | factor=1 | A=() | B=(((()())))()() | form=()((((()())))()()) | image=(())(((()())))()()
source=((((()())))()())() | factor=2 | A=((((()())))()()) | B= | form=((((()())))()())() | image=(((((()())))()()))
source=((((()())))())()() | factor=1 | A=()() | B=(((()())))() | form=()()((((()())))()) | image=(()())(((()())))()
source=((((()())))())()() | factor=2 | A=((((()())))())() | B= | form=((((()())))())()() | image=(((((()())))())())
source=((((()())))())()() | factor=3 | A=((((()())))())() | B= | form=((((()())))())()() | image=(((((()())))())())
source=((((()()))))()()() | factor=1 | A=()()() | B=(((()()))) | form=()()()((((()())))) | image=(()()())(((()())))
source=((((()()))))()()() | factor=2 | A=((((()()))))()() | B= | form=((((()()))))()()() | image=(((((()()))))()())
source=((((()()))))()()() | factor=3 | A=((((()()))))()() | B= | form=((((()()))))()()() | image=(((((()()))))()())
source=((((()()))))()()() | factor=4 | A=((((()()))))()() | B= | form=((((()()))))()()() | image=(((((()()))))()())
source=((((())(((())))))) | factor=1 | A= | B=(((())(((()))))) | form=((((())(((())))))) | image=(((())(((())))))()
source=((((())((()()))))) | factor=1 | A= | B=(((())((()())))) | form=((((())((()()))))) | image=(((())((()()))))()
source=((((())((())())))) | factor=1 | A= | B=(((())((())()))) | form=((((())((())())))) | image=(((())((())())))()
source=((((())((()))()))) | factor=1 | A= | B=(((())((()))())) | form=((((())((()))()))) | image=(((())((()))()))()
source=((((())((())))())) | factor=1 | A= | B=(((())((())))()) | form=((((())((())))())) | image=(((())((())))())()
source=((((())((()))))()) | factor=1 | A= | B=(((())((()))))() | form=((((())((()))))()) | image=(((())((()))))()()
source=((((())((())))))() | factor=1 | A=() | B=(((())((())))) | form=()((((())((()))))) | image=(())(((())((()))))
source=((((())((())))))() | factor=2 | A=((((())((()))))) | B= | form=((((())((())))))() | image=(((((())((()))))))
source=((((())(())(())))) | factor=1 | A= | B=(((())(())(()))) | form=((((())(())(())))) | image=(((())(())(())))()
source=((((())(())()()))) | factor=1 | A= | B=(((())(())()())) | form=((((())(())()()))) | image=(((())(())()()))()
source=((((())(())())())) | factor=1 | A= | B=(((())(())())()) | form=((((())(())())())) | image=(((())(())())())()
source=((((())(())()))()) | factor=1 | A= | B=(((())(())()))() | form=((((())(())()))()) | image=(((())(())()))()()
source=((((())(())())))() | factor=1 | A=() | B=(((())(())())) | form=()((((())(())()))) | image=(())(((())(())()))
source=((((())(())())))() | factor=2 | A=((((())(())()))) | B= | form=((((())(())())))() | image=(((((())(())()))))
source=((((())(()))()())) | factor=1 | A= | B=(((())(()))()()) | form=((((())(()))()())) | image=(((())(()))()())()
source=((((())(()))())()) | factor=1 | A= | B=(((())(()))())() | form=((((())(()))())()) | image=(((())(()))())()()
source=((((())(()))()))() | factor=1 | A=() | B=(((())(()))()) | form=()((((())(()))())) | image=(())(((())(()))())
source=((((())(()))()))() | factor=2 | A=((((())(()))())) | B= | form=((((())(()))()))() | image=(((((())(()))())))
source=((((())(())))()()) | factor=1 | A= | B=(((())(())))()() | form=((((())(())))()()) | image=(((())(())))()()()
source=((((())(())))())() | factor=1 | A=() | B=(((())(())))() | form=()((((())(())))()) | image=(())(((())(())))()
source=((((())(())))())() | factor=2 | A=((((())(())))()) | B= | form=((((())(())))())() | image=(((((())(())))()))
source=((((())(()))))()() | factor=1 | A=()() | B=(((())(()))) | form=()()((((())(())))) | image=(()())(((())(())))
source=((((())(()))))()() | factor=2 | A=((((())(()))))() | B= | form=((((())(()))))()() | image=(((((())(()))))())
source=((((())(()))))()() | factor=3 | A=((((())(()))))() | B= | form=((((())(()))))()() | image=(((((())(()))))())
source=((((())()()()()))) | factor=1 | A= | B=(((())()()()())) | form=((((())()()()()))) | image=(((())()()()()))()
source=((((())()()())())) | factor=1 | A= | B=(((())()()())()) | form=((((())()()())())) | image=(((())()()())())()
source=((((())()()()))()) | factor=1 | A= | B=(((())()()()))() | form=((((())()()()))()) | image=(((())()()()))()()
source=((((())()()())))() | factor=1 | A=() | B=(((())()()())) | form=()((((())()()()))) | image=(())(((())()()()))
source=((((())()()())))() | factor=2 | A=((((())()()()))) | B= | form=((((())()()())))() | image=(((((())()()()))))
source=((((())()())()())) | factor=1 | A= | B=(((())()())()()) | form=((((())()())()())) | image=(((())()())()())()
source=((((())()())())()) | factor=1 | A= | B=(((())()())())() | form=((((())()())())()) | image=(((())()())())()()
source=((((())()())()))() | factor=1 | A=() | B=(((())()())()) | form=()((((())()())())) | image=(())(((())()())())
source=((((())()())()))() | factor=2 | A=((((())()())())) | B= | form=((((())()())()))() | image=(((((())()())())))
source=((((())()()))()()) | factor=1 | A= | B=(((())()()))()() | form=((((())()()))()()) | image=(((())()()))()()()
source=((((())()()))())() | factor=1 | A=() | B=(((())()()))() | form=()((((())()()))()) | image=(())(((())()()))()
source=((((())()()))())() | factor=2 | A=((((())()()))()) | B= | form=((((())()()))())() | image=(((((())()()))()))
source=((((())()())))()() | factor=1 | A=()() | B=(((())()())) | form=()()((((())()()))) | image=(()())(((())()()))
source=((((())()())))()() | factor=2 | A=((((())()())))() | B= | form=((((())()())))()() | image=(((((())()())))())
source=((((())()())))()() | factor=3 | A=((((())()())))() | B= | form=((((())()())))()() | image=(((((())()())))())
source=((((())())((())))) | factor=1 | A= | B=(((())())((()))) | form=((((())())((())))) | image=(((())())((())))()
source=((((())())()()())) | factor=1 | A= | B=(((())())()()()) | form=((((())())()()())) | image=(((())())()()())()
source=((((())())()())()) | factor=1 | A= | B=(((())())()())() | form=((((())())()())()) | image=(((())())()())()()
source=((((())())()()))() | factor=1 | A=() | B=(((())())()()) | form=()((((())())()())) | image=(())(((())())()())
source=((((())())()()))() | factor=2 | A=((((())())()())) | B= | form=((((())())()()))() | image=(((((())())()())))
source=((((())())())()()) | factor=1 | A= | B=(((())())())()() | form=((((())())())()()) | image=(((())())())()()()
source=((((())())())())() | factor=1 | A=() | B=(((())())())() | form=()((((())())())()) | image=(())(((())())())()
source=((((())())())())() | factor=2 | A=((((())())())()) | B= | form=((((())())())())() | image=(((((())())())()))
source=((((())())()))()() | factor=1 | A=()() | B=(((())())()) | form=()()((((())())())) | image=(()())(((())())())
source=((((())())()))()() | factor=2 | A=((((())())()))() | B= | form=((((())())()))()() | image=(((((())())()))())
source=((((())())()))()() | factor=3 | A=((((())())()))() | B= | form=((((())())()))()() | image=(((((())())()))())
source=((((())()))()()()) | factor=1 | A= | B=(((())()))()()() | form=((((())()))()()()) | image=(((())()))()()()()
source=((((())()))()())() | factor=1 | A=() | B=(((())()))()() | form=()((((())()))()()) | image=(())(((())()))()()
source=((((())()))()())() | factor=2 | A=((((())()))()()) | B= | form=((((())()))()())() | image=(((((())()))()()))
source=((((())()))())()() | factor=1 | A=()() | B=(((())()))() | form=()()((((())()))()) | image=(()())(((())()))()
source=((((())()))())()() | factor=2 | A=((((())()))())() | B= | form=((((())()))())()() | image=(((((())()))())())
source=((((())()))())()() | factor=3 | A=((((())()))())() | B= | form=((((())()))())()() | image=(((((())()))())())
source=((((())())))()()() | factor=1 | A=()()() | B=(((())())) | form=()()()((((())()))) | image=(()()())(((())()))
source=((((())())))()()() | factor=2 | A=((((())())))()() | B= | form=((((())())))()()() | image=(((((())())))()())
source=((((())())))()()() | factor=3 | A=((((())())))()() | B= | form=((((())())))()()() | image=(((((())())))()())
source=((((())())))()()() | factor=4 | A=((((())())))()() | B= | form=((((())())))()()() | image=(((((())())))()())
source=((((()))(((()))))) | factor=1 | A= | B=(((()))(((())))) | form=((((()))(((()))))) | image=(((()))(((()))))()
source=((((()))((()())))) | factor=1 | A= | B=(((()))((()()))) | form=((((()))((()())))) | image=(((()))((()())))()
source=((((()))((()))())) | factor=1 | A= | B=(((()))((()))()) | form=((((()))((()))())) | image=(((()))((()))())()
source=((((()))((())))()) | factor=1 | A= | B=(((()))((())))() | form=((((()))((())))()) | image=(((()))((())))()()
source=((((()))((()))))() | factor=1 | A=() | B=(((()))((()))) | form=()((((()))((())))) | image=(())(((()))((())))
source=((((()))((()))))() | factor=2 | A=((((()))((())))) | B= | form=((((()))((()))))() | image=(((((()))((())))))
source=((((()))()()()())) | factor=1 | A= | B=(((()))()()()()) | form=((((()))()()()())) | image=(((()))()()()())()
source=((((()))()()())()) | factor=1 | A= | B=(((()))()()())() | form=((((()))()()())()) | image=(((()))()()())()()
source=((((()))()()()))() | factor=1 | A=() | B=(((()))()()()) | form=()((((()))()()())) | image=(())(((()))()()())
source=((((()))()()()))() | factor=2 | A=((((()))()()())) | B= | form=((((()))()()()))() | image=(((((()))()()())))
source=((((()))()())()()) | factor=1 | A= | B=(((()))()())()() | form=((((()))()())()()) | image=(((()))()())()()()
source=((((()))()())())() | factor=1 | A=() | B=(((()))()())() | form=()((((()))()())()) | image=(())(((()))()())()
source=((((()))()())())() | factor=2 | A=((((()))()())()) | B= | form=((((()))()())())() | image=(((((()))()())()))
source=((((()))()()))()() | factor=1 | A=()() | B=(((()))()()) | form=()()((((()))()())) | image=(()())(((()))()())
source=((((()))()()))()() | factor=2 | A=((((()))()()))() | B= | form=((((()))()()))()() | image=(((((()))()()))())
source=((((()))()()))()() | factor=3 | A=((((()))()()))() | B= | form=((((()))()()))()() | image=(((((()))()()))())
source=((((()))())()()()) | factor=1 | A= | B=(((()))())()()() | form=((((()))())()()()) | image=(((()))())()()()()
source=((((()))())()())() | factor=1 | A=() | B=(((()))())()() | form=()((((()))())()()) | image=(())(((()))())()()
source=((((()))())()())() | factor=2 | A=((((()))())()()) | B= | form=((((()))())()())() | image=(((((()))())()()))
source=((((()))())())()() | factor=1 | A=()() | B=(((()))())() | form=()()((((()))())()) | image=(()())(((()))())()
source=((((()))())())()() | factor=2 | A=((((()))())())() | B= | form=((((()))())())()() | image=(((((()))())())())
source=((((()))())())()() | factor=3 | A=((((()))())())() | B= | form=((((()))())())()() | image=(((((()))())())())
source=((((()))()))()()() | factor=1 | A=()()() | B=(((()))()) | form=()()()((((()))())) | image=(()()())(((()))())
source=((((()))()))()()() | factor=2 | A=((((()))()))()() | B= | form=((((()))()))()()() | image=(((((()))()))()())
source=((((()))()))()()() | factor=3 | A=((((()))()))()() | B= | form=((((()))()))()()() | image=(((((()))()))()())
source=((((()))()))()()() | factor=4 | A=((((()))()))()() | B= | form=((((()))()))()()() | image=(((((()))()))()())
source=((((())))(((())))) | factor=1 | A= | B=(((())))(((()))) | form=((((())))(((())))) | image=(((())))(((())))()
source=((((())))()()()()) | factor=1 | A= | B=(((())))()()()() | form=((((())))()()()()) | image=(((())))()()()()()
source=((((())))()()())() | factor=1 | A=() | B=(((())))()()() | form=()((((())))()()()) | image=(())(((())))()()()
source=((((())))()()())() | factor=2 | A=((((())))()()()) | B= | form=((((())))()()())() | image=(((((())))()()()))
source=((((())))()())()() | factor=1 | A=()() | B=(((())))()() | form=()()((((())))()()) | image=(()())(((())))()()
source=((((())))()())()() | factor=2 | A=((((())))()())() | B= | form=((((())))()())()() | image=(((((())))()())())
source=((((())))()())()() | factor=3 | A=((((())))()())() | B= | form=((((())))()())()() | image=(((((())))()())())
source=((((())))())()()() | factor=1 | A=()()() | B=(((())))() | form=()()()((((())))()) | image=(()()())(((())))()
source=((((())))())()()() | factor=2 | A=((((())))())()() | B= | form=((((())))())()()() | image=(((((())))())()())
source=((((())))())()()() | factor=3 | A=((((())))())()() | B= | form=((((())))())()()() | image=(((((())))())()())
source=((((())))())()()() | factor=4 | A=((((())))())()() | B= | form=((((())))())()()() | image=(((((())))())()())
source=((((()))))()()()() | factor=1 | A=()()()() | B=(((()))) | form=()()()()((((())))) | image=(()()()())(((())))
source=((((()))))()()()() | factor=2 | A=((((()))))()()() | B= | form=((((()))))()()()() | image=(((((()))))()()())
source=((((()))))()()()() | factor=3 | A=((((()))))()()() | B= | form=((((()))))()()()() | image=(((((()))))()()())
source=((((()))))()()()() | factor=4 | A=((((()))))()()() | B= | form=((((()))))()()()() | image=(((((()))))()()())
source=((((()))))()()()() | factor=5 | A=((((()))))()()() | B= | form=((((()))))()()()() | image=(((((()))))()()())
source=(((()()()()()()))) | factor=1 | A= | B=((()()()()()())) | form=(((()()()()()()))) | image=((()()()()()()))()
source=(((()()()()())())) | factor=1 | A= | B=((()()()()())()) | form=(((()()()()())())) | image=((()()()()())())()
source=(((()()()()()))()) | factor=1 | A= | B=((()()()()()))() | form=(((()()()()()))()) | image=((()()()()()))()()
source=(((()()()()())))() | factor=1 | A=() | B=((()()()()())) | form=()(((()()()()()))) | image=(())((()()()()()))
source=(((()()()()())))() | factor=2 | A=(((()()()()()))) | B= | form=(((()()()()())))() | image=((((()()()()()))))
source=(((()()()())(()))) | factor=1 | A= | B=((()()()())(())) | form=(((()()()())(()))) | image=((()()()())(()))()
source=(((()()()())()())) | factor=1 | A= | B=((()()()())()()) | form=(((()()()())()())) | image=((()()()())()())()
source=(((()()()())())()) | factor=1 | A= | B=((()()()())())() | form=(((()()()())())()) | image=((()()()())())()()
source=(((()()()())()))() | factor=1 | A=() | B=((()()()())()) | form=()(((()()()())())) | image=(())((()()()())())
source=(((()()()())()))() | factor=2 | A=(((()()()())())) | B= | form=(((()()()())()))() | image=((((()()()())())))
source=(((()()()()))()()) | factor=1 | A= | B=((()()()()))()() | form=(((()()()()))()()) | image=((()()()()))()()()
source=(((()()()()))())() | factor=1 | A=() | B=((()()()()))() | form=()(((()()()()))()) | image=(())((()()()()))()
source=(((()()()()))())() | factor=2 | A=(((()()()()))()) | B= | form=(((()()()()))())() | image=((((()()()()))()))
source=(((()()()())))()() | factor=1 | A=()() | B=((()()()())) | form=()()(((()()()()))) | image=(()())((()()()()))
source=(((()()()())))()() | factor=2 | A=(((()()()())))() | B= | form=(((()()()())))()() | image=((((()()()())))())
source=(((()()()())))()() | factor=3 | A=(((()()()())))() | B= | form=(((()()()())))()() | image=((((()()()())))())
source=(((()()())((())))) | factor=1 | A= | B=((()()())((()))) | form=(((()()())((())))) | image=((()()())((())))()
source=(((()()())(()()))) | factor=1 | A= | B=((()()())(()())) | form=(((()()())(()()))) | image=((()()())(()()))()
source=(((()()())(())())) | factor=1 | A= | B=((()()())(())()) | form=(((()()())(())())) | image=((()()())(())())()
source=(((()()())(()))()) | factor=1 | A= | B=((()()())(()))() | form=(((()()())(()))()) | image=((()()())(()))()()
source=(((()()())(())))() | factor=1 | A=() | B=((()()())(())) | form=()(((()()())(()))) | image=(())((()()())(()))
source=(((()()())(())))() | factor=2 | A=(((()()())(()))) | B= | form=(((()()())(())))() | image=((((()()())(()))))
source=(((()()())()()())) | factor=1 | A= | B=((()()())()()()) | form=(((()()())()()())) | image=((()()())()()())()
source=(((()()())()())()) | factor=1 | A= | B=((()()())()())() | form=(((()()())()())()) | image=((()()())()())()()
source=(((()()())()()))() | factor=1 | A=() | B=((()()())()()) | form=()(((()()())()())) | image=(())((()()())()())
source=(((()()())()()))() | factor=2 | A=(((()()())()())) | B= | form=(((()()())()()))() | image=((((()()())()())))
source=(((()()())())()()) | factor=1 | A= | B=((()()())())()() | form=(((()()())())()()) | image=((()()())())()()()
source=(((()()())())())() | factor=1 | A=() | B=((()()())())() | form=()(((()()())())()) | image=(())((()()())())()
source=(((()()())())())() | factor=2 | A=(((()()())())()) | B= | form=(((()()())())())() | image=((((()()())())()))
source=(((()()())()))()() | factor=1 | A=()() | B=((()()())()) | form=()()(((()()())())) | image=(()())((()()())())
source=(((()()())()))()() | factor=2 | A=(((()()())()))() | B= | form=(((()()())()))()() | image=((((()()())()))())
source=(((()()())()))()() | factor=3 | A=(((()()())()))() | B= | form=(((()()())()))()() | image=((((()()())()))())
source=(((()()()))()()()) | factor=1 | A= | B=((()()()))()()() | form=(((()()()))()()()) | image=((()()()))()()()()
source=(((()()()))()())() | factor=1 | A=() | B=((()()()))()() | form=()(((()()()))()()) | image=(())((()()()))()()
source=(((()()()))()())() | factor=2 | A=(((()()()))()()) | B= | form=(((()()()))()())() | image=((((()()()))()()))
source=(((()()()))())()() | factor=1 | A=()() | B=((()()()))() | form=()()(((()()()))()) | image=(()())((()()()))()
source=(((()()()))())()() | factor=2 | A=(((()()()))())() | B= | form=(((()()()))())()() | image=((((()()()))())())
source=(((()()()))())()() | factor=3 | A=(((()()()))())() | B= | form=(((()()()))())()() | image=((((()()()))())())
source=(((()()())))()()() | factor=1 | A=()()() | B=((()()())) | form=()()()(((()()()))) | image=(()()())((()()()))
source=(((()()())))()()() | factor=2 | A=(((()()())))()() | B= | form=(((()()())))()()() | image=((((()()())))()())
source=(((()()())))()()() | factor=3 | A=(((()()())))()() | B= | form=(((()()())))()()() | image=((((()()())))()())
source=(((()()())))()()() | factor=4 | A=(((()()())))()() | B= | form=(((()()())))()()() | image=((((()()())))()())
source=(((()())(((()))))) | factor=1 | A= | B=((()())(((())))) | form=(((()())(((()))))) | image=((()())(((()))))()
source=(((()())((()())))) | factor=1 | A= | B=((()())((()()))) | form=(((()())((()())))) | image=((()())((()())))()
source=(((()())((())()))) | factor=1 | A= | B=((()())((())())) | form=(((()())((())()))) | image=((()())((())()))()
source=(((()())((()))())) | factor=1 | A= | B=((()())((()))()) | form=(((()())((()))())) | image=((()())((()))())()
source=(((()())((())))()) | factor=1 | A= | B=((()())((())))() | form=(((()())((())))()) | image=((()())((())))()()
source=(((()())((()))))() | factor=1 | A=() | B=((()())((()))) | form=()(((()())((())))) | image=(())((()())((())))
source=(((()())((()))))() | factor=2 | A=(((()())((())))) | B= | form=(((()())((()))))() | image=((((()())((())))))
source=(((()())(()())())) | factor=1 | A= | B=((()())(()())()) | form=(((()())(()())())) | image=((()())(()())())()
source=(((()())(()()))()) | factor=1 | A= | B=((()())(()()))() | form=(((()())(()()))()) | image=((()())(()()))()()
source=(((()())(()())))() | factor=1 | A=() | B=((()())(()())) | form=()(((()())(()()))) | image=(())((()())(()()))
source=(((()())(()())))() | factor=2 | A=(((()())(()()))) | B= | form=(((()())(()())))() | image=((((()())(()()))))
source=(((()())(())(()))) | factor=1 | A= | B=((()())(())(())) | form=(((()())(())(()))) | image=((()())(())(()))()
source=(((()())(())()())) | factor=1 | A= | B=((()())(())()()) | form=(((()())(())()())) | image=((()())(())()())()
source=(((()())(())())()) | factor=1 | A= | B=((()())(())())() | form=(((()())(())())()) | image=((()())(())())()()
source=(((()())(())()))() | factor=1 | A=() | B=((()())(())()) | form=()(((()())(())())) | image=(())((()())(())())
source=(((()())(())()))() | factor=2 | A=(((()())(())())) | B= | form=(((()())(())()))() | image=((((()())(())())))
source=(((()())(()))()()) | factor=1 | A= | B=((()())(()))()() | form=(((()())(()))()()) | image=((()())(()))()()()
source=(((()())(()))())() | factor=1 | A=() | B=((()())(()))() | form=()(((()())(()))()) | image=(())((()())(()))()
source=(((()())(()))())() | factor=2 | A=(((()())(()))()) | B= | form=(((()())(()))())() | image=((((()())(()))()))
source=(((()())(())))()() | factor=1 | A=()() | B=((()())(())) | form=()()(((()())(()))) | image=(()())((()())(()))
source=(((()())(())))()() | factor=2 | A=(((()())(())))() | B= | form=(((()())(())))()() | image=((((()())(())))())
source=(((()())(())))()() | factor=3 | A=(((()())(())))() | B= | form=(((()())(())))()() | image=((((()())(())))())
source=(((()())()()()())) | factor=1 | A= | B=((()())()()()()) | form=(((()())()()()())) | image=((()())()()()())()
source=(((()())()()())()) | factor=1 | A= | B=((()())()()())() | form=(((()())()()())()) | image=((()())()()())()()
source=(((()())()()()))() | factor=1 | A=() | B=((()())()()()) | form=()(((()())()()())) | image=(())((()())()()())
source=(((()())()()()))() | factor=2 | A=(((()())()()())) | B= | form=(((()())()()()))() | image=((((()())()()())))
source=(((()())()())()()) | factor=1 | A= | B=((()())()())()() | form=(((()())()())()()) | image=((()())()())()()()
source=(((()())()())())() | factor=1 | A=() | B=((()())()())() | form=()(((()())()())()) | image=(())((()())()())()
source=(((()())()())())() | factor=2 | A=(((()())()())()) | B= | form=(((()())()())())() | image=((((()())()())()))
source=(((()())()()))()() | factor=1 | A=()() | B=((()())()()) | form=()()(((()())()())) | image=(()())((()())()())
source=(((()())()()))()() | factor=2 | A=(((()())()()))() | B= | form=(((()())()()))()() | image=((((()())()()))())
source=(((()())()()))()() | factor=3 | A=(((()())()()))() | B= | form=(((()())()()))()() | image=((((()())()()))())
source=(((()())())()()()) | factor=1 | A= | B=((()())())()()() | form=(((()())())()()()) | image=((()())())()()()()
source=(((()())())()())() | factor=1 | A=() | B=((()())())()() | form=()(((()())())()()) | image=(())((()())())()()
source=(((()())())()())() | factor=2 | A=(((()())())()()) | B= | form=(((()())())()())() | image=((((()())())()()))
source=(((()())())())()() | factor=1 | A=()() | B=((()())())() | form=()()(((()())())()) | image=(()())((()())())()
source=(((()())())())()() | factor=2 | A=(((()())())())() | B= | form=(((()())())())()() | image=((((()())())())())
source=(((()())())())()() | factor=3 | A=(((()())())())() | B= | form=(((()())())())()() | image=((((()())())())())
source=(((()())()))()()() | factor=1 | A=()()() | B=((()())()) | form=()()()(((()())())) | image=(()()())((()())())
source=(((()())()))()()() | factor=2 | A=(((()())()))()() | B= | form=(((()())()))()()() | image=((((()())()))()())
source=(((()())()))()()() | factor=3 | A=(((()())()))()() | B= | form=(((()())()))()()() | image=((((()())()))()())
source=(((()())()))()()() | factor=4 | A=(((()())()))()() | B= | form=(((()())()))()()() | image=((((()())()))()())
source=(((()()))(((())))) | factor=1 | A= | B=((()()))(((()))) | form=(((()()))(((())))) | image=((()()))(((())))()
source=(((()()))((()()))) | factor=1 | A= | B=((()()))((()())) | form=(((()()))((()()))) | image=((()()))((()()))()
source=(((()()))()()()()) | factor=1 | A= | B=((()()))()()()() | form=(((()()))()()()()) | image=((()()))()()()()()
source=(((()()))()()())() | factor=1 | A=() | B=((()()))()()() | form=()(((()()))()()()) | image=(())((()()))()()()
source=(((()()))()()())() | factor=2 | A=(((()()))()()()) | B= | form=(((()()))()()())() | image=((((()()))()()()))
source=(((()()))()())()() | factor=1 | A=()() | B=((()()))()() | form=()()(((()()))()()) | image=(()())((()()))()()
source=(((()()))()())()() | factor=2 | A=(((()()))()())() | B= | form=(((()()))()())()() | image=((((()()))()())())
source=(((()()))()())()() | factor=3 | A=(((()()))()())() | B= | form=(((()()))()())()() | image=((((()()))()())())
source=(((()()))())()()() | factor=1 | A=()()() | B=((()()))() | form=()()()(((()()))()) | image=(()()())((()()))()
source=(((()()))())()()() | factor=2 | A=(((()()))())()() | B= | form=(((()()))())()()() | image=((((()()))())()())
source=(((()()))())()()() | factor=3 | A=(((()()))())()() | B= | form=(((()()))())()()() | image=((((()()))())()())
source=(((()()))())()()() | factor=4 | A=(((()()))())()() | B= | form=(((()()))())()()() | image=((((()()))())()())
source=(((()())))()()()() | factor=1 | A=()()()() | B=((()())) | form=()()()()(((()()))) | image=(()()()())((()()))
source=(((()())))()()()() | factor=2 | A=(((()())))()()() | B= | form=(((()())))()()()() | image=((((()())))()()())
source=(((()())))()()()() | factor=3 | A=(((()())))()()() | B= | form=(((()())))()()()() | image=((((()())))()()())
source=(((()())))()()()() | factor=4 | A=(((()())))()()() | B= | form=(((()())))()()()() | image=((((()())))()()())
source=(((()())))()()()() | factor=5 | A=(((()())))()()() | B= | form=(((()())))()()()() | image=((((()())))()()())
source=(((())((((())))))) | factor=1 | A= | B=((())((((()))))) | form=(((())((((())))))) | image=((())((((())))))()
source=(((())(((()()))))) | factor=1 | A= | B=((())(((()())))) | form=(((())(((()()))))) | image=((())(((()()))))()
source=(((())(((())())))) | factor=1 | A= | B=((())(((())()))) | form=(((())(((())())))) | image=((())(((())())))()
source=(((())(((()))()))) | factor=1 | A= | B=((())(((()))())) | form=(((())(((()))()))) | image=((())(((()))()))()
source=(((())(((())))())) | factor=1 | A= | B=((())(((())))()) | form=(((())(((())))())) | image=((())(((())))())()
source=(((())(((()))))()) | factor=1 | A= | B=((())(((()))))() | form=(((())(((()))))()) | image=((())(((()))))()()
source=(((())(((())))))() | factor=1 | A=() | B=((())(((())))) | form=()(((())(((()))))) | image=(())((())(((()))))
source=(((())(((())))))() | factor=2 | A=(((())(((()))))) | B= | form=(((())(((())))))() | image=((((())(((()))))))
source=(((())((()()())))) | factor=1 | A= | B=((())((()()()))) | form=(((())((()()())))) | image=((())((()()())))()
source=(((())((()())()))) | factor=1 | A= | B=((())((()())())) | form=(((())((()())()))) | image=((())((()())()))()
source=(((())((()()))())) | factor=1 | A= | B=((())((()()))()) | form=(((())((()()))())) | image=((())((()()))())()
source=(((())((()())))()) | factor=1 | A= | B=((())((()())))() | form=(((())((()())))()) | image=((())((()())))()()
source=(((())((()()))))() | factor=1 | A=() | B=((())((()()))) | form=()(((())((()())))) | image=(())((())((()())))
source=(((())((()()))))() | factor=2 | A=(((())((()())))) | B= | form=(((())((()()))))() | image=((((())((()())))))
source=(((())((())(())))) | factor=1 | A= | B=((())((())(()))) | form=(((())((())(())))) | image=((())((())(())))()
source=(((())((())()()))) | factor=1 | A= | B=((())((())()())) | form=(((())((())()()))) | image=((())((())()()))()
source=(((())((())())())) | factor=1 | A= | B=((())((())())()) | form=(((())((())())())) | image=((())((())())())()
source=(((())((())()))()) | factor=1 | A= | B=((())((())()))() | form=(((())((())()))()) | image=((())((())()))()()
source=(((())((())())))() | factor=1 | A=() | B=((())((())())) | form=()(((())((())()))) | image=(())((())((())()))
source=(((())((())())))() | factor=2 | A=(((())((())()))) | B= | form=(((())((())())))() | image=((((())((())()))))
source=(((())((()))()())) | factor=1 | A= | B=((())((()))()()) | form=(((())((()))()())) | image=((())((()))()())()
source=(((())((()))())()) | factor=1 | A= | B=((())((()))())() | form=(((())((()))())()) | image=((())((()))())()()
source=(((())((()))()))() | factor=1 | A=() | B=((())((()))()) | form=()(((())((()))())) | image=(())((())((()))())
source=(((())((()))()))() | factor=2 | A=(((())((()))())) | B= | form=(((())((()))()))() | image=((((())((()))())))
source=(((())((())))()()) | factor=1 | A= | B=((())((())))()() | form=(((())((())))()()) | image=((())((())))()()()
source=(((())((())))())() | factor=1 | A=() | B=((())((())))() | form=()(((())((())))()) | image=(())((())((())))()
source=(((())((())))())() | factor=2 | A=(((())((())))()) | B= | form=(((())((())))())() | image=((((())((())))()))
source=(((())((()))))()() | factor=1 | A=()() | B=((())((()))) | form=()()(((())((())))) | image=(()())((())((())))
source=(((())((()))))()() | factor=2 | A=(((())((()))))() | B= | form=(((())((()))))()() | image=((((())((()))))())
source=(((())((()))))()() | factor=3 | A=(((())((()))))() | B= | form=(((())((()))))()() | image=((((())((()))))())
source=(((())(())((())))) | factor=1 | A= | B=((())(())((()))) | form=(((())(())((())))) | image=((())(())((())))()
source=(((())(())(())())) | factor=1 | A= | B=((())(())(())()) | form=(((())(())(())())) | image=((())(())(())())()
source=(((())(())(()))()) | factor=1 | A= | B=((())(())(()))() | form=(((())(())(()))()) | image=((())(())(()))()()
source=(((())(())(())))() | factor=1 | A=() | B=((())(())(())) | form=()(((())(())(()))) | image=(())((())(())(()))
source=(((())(())(())))() | factor=2 | A=(((())(())(()))) | B= | form=(((())(())(())))() | image=((((())(())(()))))
source=(((())(())()()())) | factor=1 | A= | B=((())(())()()()) | form=(((())(())()()())) | image=((())(())()()())()
source=(((())(())()())()) | factor=1 | A= | B=((())(())()())() | form=(((())(())()())()) | image=((())(())()())()()
source=(((())(())()()))() | factor=1 | A=() | B=((())(())()()) | form=()(((())(())()())) | image=(())((())(())()())
source=(((())(())()()))() | factor=2 | A=(((())(())()())) | B= | form=(((())(())()()))() | image=((((())(())()())))
source=(((())(())())()()) | factor=1 | A= | B=((())(())())()() | form=(((())(())())()()) | image=((())(())())()()()
source=(((())(())())())() | factor=1 | A=() | B=((())(())())() | form=()(((())(())())()) | image=(())((())(())())()
source=(((())(())())())() | factor=2 | A=(((())(())())()) | B= | form=(((())(())())())() | image=((((())(())())()))
source=(((())(())()))()() | factor=1 | A=()() | B=((())(())()) | form=()()(((())(())())) | image=(()())((())(())())
source=(((())(())()))()() | factor=2 | A=(((())(())()))() | B= | form=(((())(())()))()() | image=((((())(())()))())
source=(((())(())()))()() | factor=3 | A=(((())(())()))() | B= | form=(((())(())()))()() | image=((((())(())()))())
source=(((())(()))((()))) | factor=1 | A= | B=((())(()))((())) | form=(((())(()))((()))) | image=((())(()))((()))()
source=(((())(()))()()()) | factor=1 | A= | B=((())(()))()()() | form=(((())(()))()()()) | image=((())(()))()()()()
source=(((())(()))()())() | factor=1 | A=() | B=((())(()))()() | form=()(((())(()))()()) | image=(())((())(()))()()
source=(((())(()))()())() | factor=2 | A=(((())(()))()()) | B= | form=(((())(()))()())() | image=((((())(()))()()))
source=(((())(()))())()() | factor=1 | A=()() | B=((())(()))() | form=()()(((())(()))()) | image=(()())((())(()))()
source=(((())(()))())()() | factor=2 | A=(((())(()))())() | B= | form=(((())(()))())()() | image=((((())(()))())())
source=(((())(()))())()() | factor=3 | A=(((())(()))())() | B= | form=(((())(()))())()() | image=((((())(()))())())
source=(((())(())))()()() | factor=1 | A=()()() | B=((())(())) | form=()()()(((())(()))) | image=(()()())((())(()))
source=(((())(())))()()() | factor=2 | A=(((())(())))()() | B= | form=(((())(())))()()() | image=((((())(())))()())
source=(((())(())))()()() | factor=3 | A=(((())(())))()() | B= | form=(((())(())))()()() | image=((((())(())))()())
source=(((())(())))()()() | factor=4 | A=(((())(())))()() | B= | form=(((())(())))()()() | image=((((())(())))()())
source=(((())()()()()())) | factor=1 | A= | B=((())()()()()()) | form=(((())()()()()())) | image=((())()()()()())()
source=(((())()()()())()) | factor=1 | A= | B=((())()()()())() | form=(((())()()()())()) | image=((())()()()())()()
source=(((())()()()()))() | factor=1 | A=() | B=((())()()()()) | form=()(((())()()()())) | image=(())((())()()()())
source=(((())()()()()))() | factor=2 | A=(((())()()()())) | B= | form=(((())()()()()))() | image=((((())()()()())))
source=(((())()()())()()) | factor=1 | A= | B=((())()()())()() | form=(((())()()())()()) | image=((())()()())()()()
source=(((())()()())())() | factor=1 | A=() | B=((())()()())() | form=()(((())()()())()) | image=(())((())()()())()
source=(((())()()())())() | factor=2 | A=(((())()()())()) | B= | form=(((())()()())())() | image=((((())()()())()))
source=(((())()()()))()() | factor=1 | A=()() | B=((())()()()) | form=()()(((())()()())) | image=(()())((())()()())
source=(((())()()()))()() | factor=2 | A=(((())()()()))() | B= | form=(((())()()()))()() | image=((((())()()()))())
source=(((())()()()))()() | factor=3 | A=(((())()()()))() | B= | form=(((())()()()))()() | image=((((())()()()))())
source=(((())()())((()))) | factor=1 | A= | B=((())()())((())) | form=(((())()())((()))) | image=((())()())((()))()
source=(((())()())()()()) | factor=1 | A= | B=((())()())()()() | form=(((())()())()()()) | image=((())()())()()()()
source=(((())()())()())() | factor=1 | A=() | B=((())()())()() | form=()(((())()())()()) | image=(())((())()())()()
source=(((())()())()())() | factor=2 | A=(((())()())()()) | B= | form=(((())()())()())() | image=((((())()())()()))
source=(((())()())())()() | factor=1 | A=()() | B=((())()())() | form=()()(((())()())()) | image=(()())((())()())()
source=(((())()())())()() | factor=2 | A=(((())()())())() | B= | form=(((())()())())()() | image=((((())()())())())
source=(((())()())())()() | factor=3 | A=(((())()())())() | B= | form=(((())()())())()() | image=((((())()())())())
source=(((())()()))()()() | factor=1 | A=()()() | B=((())()()) | form=()()()(((())()())) | image=(()()())((())()())
source=(((())()()))()()() | factor=2 | A=(((())()()))()() | B= | form=(((())()()))()()() | image=((((())()()))()())
source=(((())()()))()()() | factor=3 | A=(((())()()))()() | B= | form=(((())()()))()()() | image=((((())()()))()())
source=(((())()()))()()() | factor=4 | A=(((())()()))()() | B= | form=(((())()()))()()() | image=((((())()()))()())
source=(((())())(((())))) | factor=1 | A= | B=((())())(((()))) | form=(((())())(((())))) | image=((())())(((())))()
source=(((())())((()()))) | factor=1 | A= | B=((())())((()())) | form=(((())())((()()))) | image=((())())((()()))()
source=(((())())((())())) | factor=1 | A= | B=((())())((())()) | form=(((())())((())())) | image=((())())((())())()
source=(((())())((()))()) | factor=1 | A= | B=((())())((()))() | form=(((())())((()))()) | image=((())())((()))()()
source=(((())())((())))() | factor=1 | A=() | B=((())())((())) | form=()(((())())((()))) | image=(())((())())((()))
source=(((())())((())))() | factor=2 | A=(((())())((()))) | B= | form=(((())())((())))() | image=((((())())((()))))
source=(((())())()()()()) | factor=1 | A= | B=((())())()()()() | form=(((())())()()()()) | image=((())())()()()()()
source=(((())())()()())() | factor=1 | A=() | B=((())())()()() | form=()(((())())()()()) | image=(())((())())()()()
source=(((())())()()())() | factor=2 | A=(((())())()()()) | B= | form=(((())())()()())() | image=((((())())()()()))
source=(((())())()())()() | factor=1 | A=()() | B=((())())()() | form=()()(((())())()()) | image=(()())((())())()()
source=(((())())()())()() | factor=2 | A=(((())())()())() | B= | form=(((())())()())()() | image=((((())())()())())
source=(((())())()())()() | factor=3 | A=(((())())()())() | B= | form=(((())())()())()() | image=((((())())()())())
source=(((())())())()()() | factor=1 | A=()()() | B=((())())() | form=()()()(((())())()) | image=(()()())((())())()
source=(((())())())()()() | factor=2 | A=(((())())())()() | B= | form=(((())())())()()() | image=((((())())())()())
source=(((())())())()()() | factor=3 | A=(((())())())()() | B= | form=(((())())())()()() | image=((((())())())()())
source=(((())())())()()() | factor=4 | A=(((())())())()() | B= | form=(((())())())()()() | image=((((())())())()())
source=(((())()))()()()() | factor=1 | A=()()()() | B=((())()) | form=()()()()(((())())) | image=(()()()())((())())
source=(((())()))()()()() | factor=2 | A=(((())()))()()() | B= | form=(((())()))()()()() | image=((((())()))()()())
source=(((())()))()()()() | factor=3 | A=(((())()))()()() | B= | form=(((())()))()()()() | image=((((())()))()()())
source=(((())()))()()()() | factor=4 | A=(((())()))()()() | B= | form=(((())()))()()()() | image=((((())()))()()())
source=(((())()))()()()() | factor=5 | A=(((())()))()()() | B= | form=(((())()))()()()() | image=((((())()))()()())
source=(((()))((((()))))) | factor=1 | A= | B=((()))((((())))) | form=(((()))((((()))))) | image=((()))((((()))))()
source=(((()))(((()())))) | factor=1 | A= | B=((()))(((()()))) | form=(((()))(((()())))) | image=((()))(((()())))()
source=(((()))(((())()))) | factor=1 | A= | B=((()))(((())())) | form=(((()))(((())()))) | image=((()))(((())()))()
source=(((()))(((()))())) | factor=1 | A= | B=((()))(((()))()) | form=(((()))(((()))())) | image=((()))(((()))())()
source=(((()))(((())))()) | factor=1 | A= | B=((()))(((())))() | form=(((()))(((())))()) | image=((()))(((())))()()
source=(((()))(((()))))() | factor=1 | A=() | B=((()))(((()))) | form=()(((()))(((())))) | image=(())((()))(((())))
source=(((()))(((()))))() | factor=2 | A=(((()))(((())))) | B= | form=(((()))(((()))))() | image=((((()))(((())))))
source=(((()))((()()()))) | factor=1 | A= | B=((()))((()()())) | form=(((()))((()()()))) | image=((()))((()()()))()
source=(((()))((()())())) | factor=1 | A= | B=((()))((()())()) | form=(((()))((()())())) | image=((()))((()())())()
source=(((()))((()()))()) | factor=1 | A= | B=((()))((()()))() | form=(((()))((()()))()) | image=((()))((()()))()()
source=(((()))((()())))() | factor=1 | A=() | B=((()))((()())) | form=()(((()))((()()))) | image=(())((()))((()()))
source=(((()))((()())))() | factor=2 | A=(((()))((()()))) | B= | form=(((()))((()())))() | image=((((()))((()()))))
source=(((()))((()))()()) | factor=1 | A= | B=((()))((()))()() | form=(((()))((()))()()) | image=((()))((()))()()()
source=(((()))((()))())() | factor=1 | A=() | B=((()))((()))() | form=()(((()))((()))()) | image=(())((()))((()))()
source=(((()))((()))())() | factor=2 | A=(((()))((()))()) | B= | form=(((()))((()))())() | image=((((()))((()))()))
source=(((()))((())))()() | factor=1 | A=()() | B=((()))((())) | form=()()(((()))((()))) | image=(()())((()))((()))
source=(((()))((())))()() | factor=2 | A=(((()))((())))() | B= | form=(((()))((())))()() | image=((((()))((())))())
source=(((()))((())))()() | factor=3 | A=(((()))((())))() | B= | form=(((()))((())))()() | image=((((()))((())))())
source=(((()))()()()()()) | factor=1 | A= | B=((()))()()()()() | form=(((()))()()()()()) | image=((()))()()()()()()
source=(((()))()()()())() | factor=1 | A=() | B=((()))()()()() | form=()(((()))()()()()) | image=(())((()))()()()()
source=(((()))()()()())() | factor=2 | A=(((()))()()()()) | B= | form=(((()))()()()())() | image=((((()))()()()()))
source=(((()))()()())()() | factor=1 | A=()() | B=((()))()()() | form=()()(((()))()()()) | image=(()())((()))()()()
source=(((()))()()())()() | factor=2 | A=(((()))()()())() | B= | form=(((()))()()())()() | image=((((()))()()())())
source=(((()))()()())()() | factor=3 | A=(((()))()()())() | B= | form=(((()))()()())()() | image=((((()))()()())())
source=(((()))()())()()() | factor=1 | A=()()() | B=((()))()() | form=()()()(((()))()()) | image=(()()())((()))()()
source=(((()))()())()()() | factor=2 | A=(((()))()())()() | B= | form=(((()))()())()()() | image=((((()))()())()())
source=(((()))()())()()() | factor=3 | A=(((()))()())()() | B= | form=(((()))()())()()() | image=((((()))()())()())
source=(((()))()())()()() | factor=4 | A=(((()))()())()() | B= | form=(((()))()())()()() | image=((((()))()())()())
source=(((()))())(((()))) | factor=1 | A=(((()))) | B=((()))() | form=(((())))(((()))()) | image=((()))((((()))))()
source=(((()))())(((()))) | factor=2 | A=(((()))()) | B=((())) | form=(((()))())(((()))) | image=((()))((((()))()))
source=(((()))())()()()() | factor=1 | A=()()()() | B=((()))() | form=()()()()(((()))()) | image=(()()()())((()))()
source=(((()))())()()()() | factor=2 | A=(((()))())()()() | B= | form=(((()))())()()()() | image=((((()))())()()())
source=(((()))())()()()() | factor=3 | A=(((()))())()()() | B= | form=(((()))())()()()() | image=((((()))())()()())
source=(((()))())()()()() | factor=4 | A=(((()))())()()() | B= | form=(((()))())()()()() | image=((((()))())()()())
source=(((()))())()()()() | factor=5 | A=(((()))())()()() | B= | form=(((()))())()()()() | image=((((()))())()()())
source=(((())))((((())))) | factor=1 | A=((((())))) | B=((())) | form=((((()))))(((()))) | image=((()))(((((())))))
source=(((())))((((())))) | factor=2 | A=(((()))) | B=(((()))) | form=(((())))((((())))) | image=(((())))((((())))) | fixed
source=(((())))(((()()))) | factor=1 | A=(((()()))) | B=((())) | form=(((()())))(((()))) | image=((()))((((()()))))
source=(((())))(((()()))) | factor=2 | A=(((()))) | B=((()())) | form=(((())))(((()()))) | image=((()()))((((()))))
source=(((())))(((())())) | factor=1 | A=(((())())) | B=((())) | form=(((())()))(((()))) | image=((()))((((())())))
source=(((())))(((())())) | factor=2 | A=(((()))) | B=((())()) | form=(((())))(((())())) | image=((())())((((()))))
source=(((())))(((())))() | factor=1 | A=(((())))() | B=((())) | form=(((())))()(((()))) | image=((()))((((())))())
source=(((())))(((())))() | factor=2 | A=(((())))() | B=((())) | form=(((())))()(((()))) | image=((()))((((())))())
source=(((())))(((())))() | factor=3 | A=(((())))(((()))) | B= | form=(((())))(((())))() | image=((((())))(((()))))
source=(((())))()()()()() | factor=1 | A=()()()()() | B=((())) | form=()()()()()(((()))) | image=(()()()()())((()))
source=(((())))()()()()() | factor=2 | A=(((())))()()()() | B= | form=(((())))()()()()() | image=((((())))()()()())
source=(((())))()()()()() | factor=3 | A=(((())))()()()() | B= | form=(((())))()()()()() | image=((((())))()()()())
source=(((())))()()()()() | factor=4 | A=(((())))()()()() | B= | form=(((())))()()()()() | image=((((())))()()()())
source=(((())))()()()()() | factor=5 | A=(((())))()()()() | B= | form=(((())))()()()()() | image=((((())))()()()())
source=(((())))()()()()() | factor=6 | A=(((())))()()()() | B= | form=(((())))()()()()() | image=((((())))()()()())
source=((()()()()()()())) | factor=1 | A= | B=(()()()()()()()) | form=((()()()()()()())) | image=(()()()()()()())()
source=((()()()()()())()) | factor=1 | A= | B=(()()()()()())() | form=((()()()()()())()) | image=(()()()()()())()()
source=((()()()()()()))() | factor=1 | A=() | B=(()()()()()()) | form=()((()()()()()())) | image=(()()()()()())(())
source=((()()()()()()))() | factor=2 | A=((()()()()()())) | B= | form=((()()()()()()))() | image=(((()()()()()())))
source=((()()()()())(())) | factor=1 | A= | B=(()()()()())(()) | form=((()()()()())(())) | image=(()()()()())(())()
source=((()()()()())()()) | factor=1 | A= | B=(()()()()())()() | form=((()()()()())()()) | image=(()()()()())()()()
source=((()()()()())())() | factor=1 | A=() | B=(()()()()())() | form=()((()()()()())()) | image=(()()()()())(())()
source=((()()()()())())() | factor=2 | A=((()()()()())()) | B= | form=((()()()()())())() | image=(((()()()()())()))
source=((()()()()()))()() | factor=1 | A=()() | B=(()()()()()) | form=()()((()()()()())) | image=(()()()()())(()())
source=((()()()()()))()() | factor=2 | A=((()()()()()))() | B= | form=((()()()()()))()() | image=(((()()()()()))())
source=((()()()()()))()() | factor=3 | A=((()()()()()))() | B= | form=((()()()()()))()() | image=(((()()()()()))())
source=((()()()())((()))) | factor=1 | A= | B=(()()()())((())) | form=((()()()())((()))) | image=(()()()())((()))()
source=((()()()())(()())) | factor=1 | A= | B=(()()()())(()()) | form=((()()()())(()())) | image=(()()()())(()())()
source=((()()()())(())()) | factor=1 | A= | B=(()()()())(())() | form=((()()()())(())()) | image=(()()()())(())()()
source=((()()()())(()))() | factor=1 | A=() | B=(()()()())(()) | form=()((()()()())(())) | image=(()()()())(())(())
source=((()()()())(()))() | factor=2 | A=((()()()())(())) | B= | form=((()()()())(()))() | image=(((()()()())(())))
source=((()()()())()()()) | factor=1 | A= | B=(()()()())()()() | form=((()()()())()()()) | image=(()()()())()()()()
source=((()()()())()())() | factor=1 | A=() | B=(()()()())()() | form=()((()()()())()()) | image=(()()()())(())()()
source=((()()()())()())() | factor=2 | A=((()()()())()()) | B= | form=((()()()())()())() | image=(((()()()())()()))
source=((()()()())())()() | factor=1 | A=()() | B=(()()()())() | form=()()((()()()())()) | image=(()()()())(()())()
source=((()()()())())()() | factor=2 | A=((()()()())())() | B= | form=((()()()())())()() | image=(((()()()())())())
source=((()()()())())()() | factor=3 | A=((()()()())())() | B= | form=((()()()())())()() | image=(((()()()())())())
source=((()()()()))()()() | factor=1 | A=()()() | B=(()()()()) | form=()()()((()()()())) | image=(()()()())(()()())
source=((()()()()))()()() | factor=2 | A=((()()()()))()() | B= | form=((()()()()))()()() | image=(((()()()()))()())
source=((()()()()))()()() | factor=3 | A=((()()()()))()() | B= | form=((()()()()))()()() | image=(((()()()()))()())
source=((()()()()))()()() | factor=4 | A=((()()()()))()() | B= | form=((()()()()))()()() | image=(((()()()()))()())
source=((()()())(((())))) | factor=1 | A= | B=(()()())(((()))) | form=((()()())(((())))) | image=(()()())(((())))()
source=((()()())((()()))) | factor=1 | A= | B=(()()())((()())) | form=((()()())((()()))) | image=(()()())((()()))()
source=((()()())((())())) | factor=1 | A= | B=(()()())((())()) | form=((()()())((())())) | image=(()()())((())())()
source=((()()())((()))()) | factor=1 | A= | B=(()()())((()))() | form=((()()())((()))()) | image=(()()())((()))()()
source=((()()())((())))() | factor=1 | A=() | B=(()()())((())) | form=()((()()())((()))) | image=(()()())(())((()))
source=((()()())((())))() | factor=2 | A=((()()())((()))) | B= | form=((()()())((())))() | image=(((()()())((()))))
source=((()()())(()()())) | factor=1 | A= | B=(()()())(()()()) | form=((()()())(()()())) | image=(()()())(()()())()
source=((()()())(()())()) | factor=1 | A= | B=(()()())(()())() | form=((()()())(()())()) | image=(()()())(()())()()
source=((()()())(()()))() | factor=1 | A=() | B=(()()())(()()) | form=()((()()())(()())) | image=(()()())(()())(())
source=((()()())(()()))() | factor=2 | A=((()()())(()())) | B= | form=((()()())(()()))() | image=(((()()())(()())))
source=((()()())(())(())) | factor=1 | A= | B=(()()())(())(()) | form=((()()())(())(())) | image=(()()())(())(())()
source=((()()())(())()()) | factor=1 | A= | B=(()()())(())()() | form=((()()())(())()()) | image=(()()())(())()()()
source=((()()())(())())() | factor=1 | A=() | B=(()()())(())() | form=()((()()())(())()) | image=(()()())(())(())()
source=((()()())(())())() | factor=2 | A=((()()())(())()) | B= | form=((()()())(())())() | image=(((()()())(())()))
source=((()()())(()))()() | factor=1 | A=()() | B=(()()())(()) | form=()()((()()())(())) | image=(()()())(()())(())
source=((()()())(()))()() | factor=2 | A=((()()())(()))() | B= | form=((()()())(()))()() | image=(((()()())(()))())
source=((()()())(()))()() | factor=3 | A=((()()())(()))() | B= | form=((()()())(()))()() | image=(((()()())(()))())
source=((()()())()()()()) | factor=1 | A= | B=(()()())()()()() | form=((()()())()()()()) | image=(()()())()()()()()
source=((()()())()()())() | factor=1 | A=() | B=(()()())()()() | form=()((()()())()()()) | image=(()()())(())()()()
source=((()()())()()())() | factor=2 | A=((()()())()()()) | B= | form=((()()())()()())() | image=(((()()())()()()))
source=((()()())()())()() | factor=1 | A=()() | B=(()()())()() | form=()()((()()())()()) | image=(()()())(()())()()
source=((()()())()())()() | factor=2 | A=((()()())()())() | B= | form=((()()())()())()() | image=(((()()())()())())
source=((()()())()())()() | factor=3 | A=((()()())()())() | B= | form=((()()())()())()() | image=(((()()())()())())
source=((()()())())()()() | factor=1 | A=()()() | B=(()()())() | form=()()()((()()())()) | image=(()()())(()()())()
source=((()()())())()()() | factor=2 | A=((()()())())()() | B= | form=((()()())())()()() | image=(((()()())())()())
source=((()()())())()()() | factor=3 | A=((()()())())()() | B= | form=((()()())())()()() | image=(((()()())())()())
source=((()()())())()()() | factor=4 | A=((()()())())()() | B= | form=((()()())())()()() | image=(((()()())())()())
source=((()()()))(((()))) | factor=1 | A=(((()))) | B=(()()()) | form=(((())))((()()())) | image=(()()())((((()))))
source=((()()()))(((()))) | factor=2 | A=((()()())) | B=((())) | form=((()()()))(((()))) | image=((()))(((()()())))
source=((()()()))()()()() | factor=1 | A=()()()() | B=(()()()) | form=()()()()((()()())) | image=(()()()())(()()())
source=((()()()))()()()() | factor=2 | A=((()()()))()()() | B= | form=((()()()))()()()() | image=(((()()()))()()())
source=((()()()))()()()() | factor=3 | A=((()()()))()()() | B= | form=((()()()))()()()() | image=(((()()()))()()())
source=((()()()))()()()() | factor=4 | A=((()()()))()()() | B= | form=((()()()))()()()() | image=(((()()()))()()())
source=((()()()))()()()() | factor=5 | A=((()()()))()()() | B= | form=((()()()))()()()() | image=(((()()()))()()())
source=((()())((((()))))) | factor=1 | A= | B=(()())((((())))) | form=((()())((((()))))) | image=(()())((((()))))()
source=((()())(((()())))) | factor=1 | A= | B=(()())(((()()))) | form=((()())(((()())))) | image=(()())(((()())))()
source=((()())(((())()))) | factor=1 | A= | B=(()())(((())())) | form=((()())(((())()))) | image=(()())(((())()))()
source=((()())(((()))())) | factor=1 | A= | B=(()())(((()))()) | form=((()())(((()))())) | image=(()())(((()))())()
source=((()())(((())))()) | factor=1 | A= | B=(()())(((())))() | form=((()())(((())))()) | image=(()())(((())))()()
source=((()())(((()))))() | factor=1 | A=() | B=(()())(((()))) | form=()((()())(((())))) | image=(()())(())(((())))
source=((()())(((()))))() | factor=2 | A=((()())(((())))) | B= | form=((()())(((()))))() | image=(((()())(((())))))
source=((()())((()()()))) | factor=1 | A= | B=(()())((()()())) | form=((()())((()()()))) | image=(()())((()()()))()
source=((()())((()())())) | factor=1 | A= | B=(()())((()())()) | form=((()())((()())())) | image=(()())((()())())()
source=((()())((()()))()) | factor=1 | A= | B=(()())((()()))() | form=((()())((()()))()) | image=(()())((()()))()()
source=((()())((()())))() | factor=1 | A=() | B=(()())((()())) | form=()((()())((()()))) | image=(()())(())((()()))
source=((()())((()())))() | factor=2 | A=((()())((()()))) | B= | form=((()())((()())))() | image=(((()())((()()))))
source=((()())((())(()))) | factor=1 | A= | B=(()())((())(())) | form=((()())((())(()))) | image=(()())((())(()))()
source=((()())((())()())) | factor=1 | A= | B=(()())((())()()) | form=((()())((())()())) | image=(()())((())()())()
source=((()())((())())()) | factor=1 | A= | B=(()())((())())() | form=((()())((())())()) | image=(()())((())())()()
source=((()())((())()))() | factor=1 | A=() | B=(()())((())()) | form=()((()())((())())) | image=(()())(())((())())
source=((()())((())()))() | factor=2 | A=((()())((())())) | B= | form=((()())((())()))() | image=(((()())((())())))
source=((()())((()))()()) | factor=1 | A= | B=(()())((()))()() | form=((()())((()))()()) | image=(()())((()))()()()
source=((()())((()))())() | factor=1 | A=() | B=(()())((()))() | form=()((()())((()))()) | image=(()())(())((()))()
source=((()())((()))())() | factor=2 | A=((()())((()))()) | B= | form=((()())((()))())() | image=(((()())((()))()))
source=((()())((())))()() | factor=1 | A=()() | B=(()())((())) | form=()()((()())((()))) | image=(()())(()())((()))
source=((()())((())))()() | factor=2 | A=((()())((())))() | B= | form=((()())((())))()() | image=(((()())((())))())
source=((()())((())))()() | factor=3 | A=((()())((())))() | B= | form=((()())((())))()() | image=(((()())((())))())
source=((()())(()())(())) | factor=1 | A= | B=(()())(()())(()) | form=((()())(()())(())) | image=(()())(()())(())()
source=((()())(()())()()) | factor=1 | A= | B=(()())(()())()() | form=((()())(()())()()) | image=(()())(()())()()()
source=((()())(()())())() | factor=1 | A=() | B=(()())(()())() | form=()((()())(()())()) | image=(()())(()())(())()
source=((()())(()())())() | factor=2 | A=((()())(()())()) | B= | form=((()())(()())())() | image=(((()())(()())()))
source=((()())(()()))()() | factor=1 | A=()() | B=(()())(()()) | form=()()((()())(()())) | image=(()())(()())(()())
source=((()())(()()))()() | factor=2 | A=((()())(()()))() | B= | form=((()())(()()))()() | image=(((()())(()()))())
source=((()())(()()))()() | factor=3 | A=((()())(()()))() | B= | form=((()())(()()))()() | image=(((()())(()()))())
source=((()())(())((()))) | factor=1 | A= | B=(()())(())((())) | form=((()())(())((()))) | image=(()())(())((()))()
source=((()())(())(())()) | factor=1 | A= | B=(()())(())(())() | form=((()())(())(())()) | image=(()())(())(())()()
source=((()())(())(()))() | factor=1 | A=() | B=(()())(())(()) | form=()((()())(())(())) | image=(()())(())(())(())
source=((()())(())(()))() | factor=2 | A=((()())(())(())) | B= | form=((()())(())(()))() | image=(((()())(())(())))
source=((()())(())()()()) | factor=1 | A= | B=(()())(())()()() | form=((()())(())()()()) | image=(()())(())()()()()
source=((()())(())()())() | factor=1 | A=() | B=(()())(())()() | form=()((()())(())()()) | image=(()())(())(())()()
source=((()())(())()())() | factor=2 | A=((()())(())()()) | B= | form=((()())(())()())() | image=(((()())(())()()))
source=((()())(())())()() | factor=1 | A=()() | B=(()())(())() | form=()()((()())(())()) | image=(()())(()())(())()
source=((()())(())())()() | factor=2 | A=((()())(())())() | B= | form=((()())(())())()() | image=(((()())(())())())
source=((()())(())())()() | factor=3 | A=((()())(())())() | B= | form=((()())(())())()() | image=(((()())(())())())
source=((()())(()))()()() | factor=1 | A=()()() | B=(()())(()) | form=()()()((()())(())) | image=(()()())(()())(())
source=((()())(()))()()() | factor=2 | A=((()())(()))()() | B= | form=((()())(()))()()() | image=(((()())(()))()())
source=((()())(()))()()() | factor=3 | A=((()())(()))()() | B= | form=((()())(()))()()() | image=(((()())(()))()())
source=((()())(()))()()() | factor=4 | A=((()())(()))()() | B= | form=((()())(()))()()() | image=(((()())(()))()())
source=((()())()()()()()) | factor=1 | A= | B=(()())()()()()() | form=((()())()()()()()) | image=(()())()()()()()()
source=((()())()()()())() | factor=1 | A=() | B=(()())()()()() | form=()((()())()()()()) | image=(()())(())()()()()
source=((()())()()()())() | factor=2 | A=((()())()()()()) | B= | form=((()())()()()())() | image=(((()())()()()()))
source=((()())()()())()() | factor=1 | A=()() | B=(()())()()() | form=()()((()())()()()) | image=(()())(()())()()()
source=((()())()()())()() | factor=2 | A=((()())()()())() | B= | form=((()())()()())()() | image=(((()())()()())())
source=((()())()()())()() | factor=3 | A=((()())()()())() | B= | form=((()())()()())()() | image=(((()())()()())())
source=((()())()())()()() | factor=1 | A=()()() | B=(()())()() | form=()()()((()())()()) | image=(()()())(()())()()
source=((()())()())()()() | factor=2 | A=((()())()())()() | B= | form=((()())()())()()() | image=(((()())()())()())
source=((()())()())()()() | factor=3 | A=((()())()())()() | B= | form=((()())()())()()() | image=(((()())()())()())
source=((()())()())()()() | factor=4 | A=((()())()())()() | B= | form=((()())()())()()() | image=(((()())()())()())
source=((()())())(((()))) | factor=1 | A=(((()))) | B=(()())() | form=(((())))((()())()) | image=(()())((((()))))()
source=((()())())(((()))) | factor=2 | A=((()())()) | B=((())) | form=((()())())(((()))) | image=((()))(((()())()))
source=((()())())((()())) | factor=1 | A=((()())) | B=(()())() | form=((()()))((()())()) | image=(()())(((()())))()
source=((()())())((()())) | factor=2 | A=((()())()) | B=(()()) | form=((()())())((()())) | image=(()())(((()())()))
source=((()())())()()()() | factor=1 | A=()()()() | B=(()())() | form=()()()()((()())()) | image=(()()()())(()())()
source=((()())())()()()() | factor=2 | A=((()())())()()() | B= | form=((()())())()()()() | image=(((()())())()()())
source=((()())())()()()() | factor=3 | A=((()())())()()() | B= | form=((()())())()()()() | image=(((()())())()()())
source=((()())())()()()() | factor=4 | A=((()())())()()() | B= | form=((()())())()()()() | image=(((()())())()()())
source=((()())())()()()() | factor=5 | A=((()())())()()() | B= | form=((()())())()()()() | image=(((()())())()()())
source=((()()))((((())))) | factor=1 | A=((((())))) | B=(()()) | form=((((()))))((()())) | image=(()())(((((())))))
source=((()()))((((())))) | factor=2 | A=((()())) | B=(((()))) | form=((()()))((((())))) | image=(((())))(((()())))
source=((()()))(((()()))) | factor=1 | A=(((()()))) | B=(()()) | form=(((()())))((()())) | image=(()())((((()()))))
source=((()()))(((()()))) | factor=2 | A=((()())) | B=((()())) | form=((()()))(((()()))) | image=((()()))(((()()))) | fixed
source=((()()))(((())())) | factor=1 | A=(((())())) | B=(()()) | form=(((())()))((()())) | image=(()())((((())())))
source=((()()))(((())())) | factor=2 | A=((()())) | B=((())()) | form=((()()))(((())())) | image=((())())(((()())))
source=((()()))(((()))()) | factor=1 | A=(((()))()) | B=(()()) | form=(((()))())((()())) | image=(()())((((()))()))
source=((()()))(((()))()) | factor=2 | A=((()())) | B=((()))() | form=((()()))(((()))()) | image=((()))(((()())))()
source=((()()))(((())))() | factor=1 | A=(((())))() | B=(()()) | form=(((())))()((()())) | image=(()())((((())))())
source=((()()))(((())))() | factor=2 | A=((()()))() | B=((())) | form=((()()))()(((()))) | image=((()))(((()()))())
source=((()()))(((())))() | factor=3 | A=((()()))(((()))) | B= | form=((()()))(((())))() | image=(((()()))(((()))))
source=((()()))((()()())) | factor=1 | A=((()()())) | B=(()()) | form=((()()()))((()())) | image=(()())(((()()())))
source=((()()))((()()())) | factor=2 | A=((()())) | B=(()()()) | form=((()()))((()()())) | image=(()()())(((()())))
source=((()()))((()()))() | factor=1 | A=((()()))() | B=(()()) | form=((()()))()((()())) | image=(()())(((()()))())
source=((()()))((()()))() | factor=2 | A=((()()))() | B=(()()) | form=((()()))()((()())) | image=(()())(((()()))())
source=((()()))((()()))() | factor=3 | A=((()()))((()())) | B= | form=((()()))((()()))() | image=(((()()))((()())))
source=((()()))()()()()() | factor=1 | A=()()()()() | B=(()()) | form=()()()()()((()())) | image=(()()()()())(()())
source=((()()))()()()()() | factor=2 | A=((()()))()()()() | B= | form=((()()))()()()()() | image=(((()()))()()()())
source=((()()))()()()()() | factor=3 | A=((()()))()()()() | B= | form=((()()))()()()()() | image=(((()()))()()()())
source=((()()))()()()()() | factor=4 | A=((()()))()()()() | B= | form=((()()))()()()()() | image=(((()()))()()()())
source=((()()))()()()()() | factor=5 | A=((()()))()()()() | B= | form=((()()))()()()()() | image=(((()()))()()()())
source=((()()))()()()()() | factor=6 | A=((()()))()()()() | B= | form=((()()))()()()()() | image=(((()()))()()()())
source=((())(((((())))))) | factor=1 | A= | B=(())(((((()))))) | form=((())(((((())))))) | image=(())(((((())))))()
source=((())((((()()))))) | factor=1 | A= | B=(())((((()())))) | form=((())((((()()))))) | image=(())((((()()))))()
source=((())((((())())))) | factor=1 | A= | B=(())((((())()))) | form=((())((((())())))) | image=(())((((())())))()
source=((())((((()))()))) | factor=1 | A= | B=(())((((()))())) | form=((())((((()))()))) | image=(())((((()))()))()
source=((())((((())))())) | factor=1 | A= | B=(())((((())))()) | form=((())((((())))())) | image=(())((((())))())()
source=((())((((()))))()) | factor=1 | A= | B=(())((((()))))() | form=((())((((()))))()) | image=(())((((()))))()()
source=((())((((())))))() | factor=1 | A=() | B=(())((((())))) | form=()((())((((()))))) | image=(())(())((((()))))
source=((())((((())))))() | factor=2 | A=((())((((()))))) | B= | form=((())((((())))))() | image=(((())((((()))))))
source=((())(((()()())))) | factor=1 | A= | B=(())(((()()()))) | form=((())(((()()())))) | image=(())(((()()())))()
source=((())(((()())()))) | factor=1 | A= | B=(())(((()())())) | form=((())(((()())()))) | image=(())(((()())()))()
source=((())(((()()))())) | factor=1 | A= | B=(())(((()()))()) | form=((())(((()()))())) | image=(())(((()()))())()
source=((())(((()())))()) | factor=1 | A= | B=(())(((()())))() | form=((())(((()())))()) | image=(())(((()())))()()
source=((())(((()()))))() | factor=1 | A=() | B=(())(((()()))) | form=()((())(((()())))) | image=(())(())(((()())))
source=((())(((()()))))() | factor=2 | A=((())(((()())))) | B= | form=((())(((()()))))() | image=(((())(((()())))))
source=((())(((())(())))) | factor=1 | A= | B=(())(((())(()))) | form=((())(((())(())))) | image=(())(((())(())))()
source=((())(((())()()))) | factor=1 | A= | B=(())(((())()())) | form=((())(((())()()))) | image=(())(((())()()))()
source=((())(((())())())) | factor=1 | A= | B=(())(((())())()) | form=((())(((())())())) | image=(())(((())())())()
source=((())(((())()))()) | factor=1 | A= | B=(())(((())()))() | form=((())(((())()))()) | image=(())(((())()))()()
source=((())(((())())))() | factor=1 | A=() | B=(())(((())())) | form=()((())(((())()))) | image=(())(())(((())()))
source=((())(((())())))() | factor=2 | A=((())(((())()))) | B= | form=((())(((())())))() | image=(((())(((())()))))
source=((())(((()))()())) | factor=1 | A= | B=(())(((()))()()) | form=((())(((()))()())) | image=(())(((()))()())()
source=((())(((()))())()) | factor=1 | A= | B=(())(((()))())() | form=((())(((()))())()) | image=(())(((()))())()()
source=((())(((()))()))() | factor=1 | A=() | B=(())(((()))()) | form=()((())(((()))())) | image=(())(())(((()))())
source=((())(((()))()))() | factor=2 | A=((())(((()))())) | B= | form=((())(((()))()))() | image=(((())(((()))())))
source=((())(((())))()()) | factor=1 | A= | B=(())(((())))()() | form=((())(((())))()()) | image=(())(((())))()()()
source=((())(((())))())() | factor=1 | A=() | B=(())(((())))() | form=()((())(((())))()) | image=(())(())(((())))()
source=((())(((())))())() | factor=2 | A=((())(((())))()) | B= | form=((())(((())))())() | image=(((())(((())))()))
source=((())(((()))))()() | factor=1 | A=()() | B=(())(((()))) | form=()()((())(((())))) | image=(()())(())(((())))
source=((())(((()))))()() | factor=2 | A=((())(((()))))() | B= | form=((())(((()))))()() | image=(((())(((()))))())
source=((())(((()))))()() | factor=3 | A=((())(((()))))() | B= | form=((())(((()))))()() | image=(((())(((()))))())
source=((())((()()()()))) | factor=1 | A= | B=(())((()()()())) | form=((())((()()()()))) | image=(())((()()()()))()
source=((())((()()())())) | factor=1 | A= | B=(())((()()())()) | form=((())((()()())())) | image=(())((()()())())()
source=((())((()()()))()) | factor=1 | A= | B=(())((()()()))() | form=((())((()()()))()) | image=(())((()()()))()()
source=((())((()()())))() | factor=1 | A=() | B=(())((()()())) | form=()((())((()()()))) | image=(())(())((()()()))
source=((())((()()())))() | factor=2 | A=((())((()()()))) | B= | form=((())((()()())))() | image=(((())((()()()))))
source=((())((()())(()))) | factor=1 | A= | B=(())((()())(())) | form=((())((()())(()))) | image=(())((()())(()))()
source=((())((()())()())) | factor=1 | A= | B=(())((()())()()) | form=((())((()())()())) | image=(())((()())()())()
source=((())((()())())()) | factor=1 | A= | B=(())((()())())() | form=((())((()())())()) | image=(())((()())())()()
source=((())((()())()))() | factor=1 | A=() | B=(())((()())()) | form=()((())((()())())) | image=(())(())((()())())
source=((())((()())()))() | factor=2 | A=((())((()())())) | B= | form=((())((()())()))() | image=(((())((()())())))
source=((())((()()))()()) | factor=1 | A= | B=(())((()()))()() | form=((())((()()))()()) | image=(())((()()))()()()
source=((())((()()))())() | factor=1 | A=() | B=(())((()()))() | form=()((())((()()))()) | image=(())(())((()()))()
source=((())((()()))())() | factor=2 | A=((())((()()))()) | B= | form=((())((()()))())() | image=(((())((()()))()))
source=((())((()())))()() | factor=1 | A=()() | B=(())((()())) | form=()()((())((()()))) | image=(()())(())((()()))
source=((())((()())))()() | factor=2 | A=((())((()())))() | B= | form=((())((()())))()() | image=(((())((()())))())
source=((())((()())))()() | factor=3 | A=((())((()())))() | B= | form=((())((()())))()() | image=(((())((()())))())
source=((())((())((())))) | factor=1 | A= | B=(())((())((()))) | form=((())((())((())))) | image=(())((())((())))()
source=((())((())(())())) | factor=1 | A= | B=(())((())(())()) | form=((())((())(())())) | image=(())((())(())())()
source=((())((())(()))()) | factor=1 | A= | B=(())((())(()))() | form=((())((())(()))()) | image=(())((())(()))()()
source=((())((())(())))() | factor=1 | A=() | B=(())((())(())) | form=()((())((())(()))) | image=(())(())((())(()))
source=((())((())(())))() | factor=2 | A=((())((())(()))) | B= | form=((())((())(())))() | image=(((())((())(()))))
source=((())((())()()())) | factor=1 | A= | B=(())((())()()()) | form=((())((())()()())) | image=(())((())()()())()
source=((())((())()())()) | factor=1 | A= | B=(())((())()())() | form=((())((())()())()) | image=(())((())()())()()
source=((())((())()()))() | factor=1 | A=() | B=(())((())()()) | form=()((())((())()())) | image=(())(())((())()())
source=((())((())()()))() | factor=2 | A=((())((())()())) | B= | form=((())((())()()))() | image=(((())((())()())))
source=((())((())())()()) | factor=1 | A= | B=(())((())())()() | form=((())((())())()()) | image=(())((())())()()()
source=((())((())())())() | factor=1 | A=() | B=(())((())())() | form=()((())((())())()) | image=(())(())((())())()
source=((())((())())())() | factor=2 | A=((())((())())()) | B= | form=((())((())())())() | image=(((())((())())()))
source=((())((())()))()() | factor=1 | A=()() | B=(())((())()) | form=()()((())((())())) | image=(()())(())((())())
source=((())((())()))()() | factor=2 | A=((())((())()))() | B= | form=((())((())()))()() | image=(((())((())()))())
source=((())((())()))()() | factor=3 | A=((())((())()))() | B= | form=((())((())()))()() | image=(((())((())()))())
source=((())((()))((()))) | factor=1 | A= | B=(())((()))((())) | form=((())((()))((()))) | image=(())((()))((()))()
source=((())((()))()()()) | factor=1 | A= | B=(())((()))()()() | form=((())((()))()()()) | image=(())((()))()()()()
source=((())((()))()())() | factor=1 | A=() | B=(())((()))()() | form=()((())((()))()()) | image=(())(())((()))()()
source=((())((()))()())() | factor=2 | A=((())((()))()()) | B= | form=((())((()))()())() | image=(((())((()))()()))
source=((())((()))())()() | factor=1 | A=()() | B=(())((()))() | form=()()((())((()))()) | image=(()())(())((()))()
source=((())((()))())()() | factor=2 | A=((())((()))())() | B= | form=((())((()))())()() | image=(((())((()))())())
source=((())((()))())()() | factor=3 | A=((())((()))())() | B= | form=((())((()))())()() | image=(((())((()))())())
source=((())((())))((())) | factor=1 | A=((())) | B=(())((())) | form=((()))((())((()))) | image=(())((()))(((())))
source=((())((())))((())) | factor=2 | A=((())((()))) | B=(()) | form=((())((())))((())) | image=(())(((())((()))))
source=((())((())))()()() | factor=1 | A=()()() | B=(())((())) | form=()()()((())((()))) | image=(()()())(())((()))
source=((())((())))()()() | factor=2 | A=((())((())))()() | B= | form=((())((())))()()() | image=(((())((())))()())
source=((())((())))()()() | factor=3 | A=((())((())))()() | B= | form=((())((())))()()() | image=(((())((())))()())
source=((())((())))()()() | factor=4 | A=((())((())))()() | B= | form=((())((())))()()() | image=(((())((())))()())
source=((())(())(((())))) | factor=1 | A= | B=(())(())(((()))) | form=((())(())(((())))) | image=(())(())(((())))()
source=((())(())((()()))) | factor=1 | A= | B=(())(())((()())) | form=((())(())((()()))) | image=(())(())((()()))()
source=((())(())((())())) | factor=1 | A= | B=(())(())((())()) | form=((())(())((())())) | image=(())(())((())())()
source=((())(())((()))()) | factor=1 | A= | B=(())(())((()))() | form=((())(())((()))()) | image=(())(())((()))()()
source=((())(())((())))() | factor=1 | A=() | B=(())(())((())) | form=()((())(())((()))) | image=(())(())(())((()))
source=((())(())((())))() | factor=2 | A=((())(())((()))) | B= | form=((())(())((())))() | image=(((())(())((()))))
source=((())(())(())(())) | factor=1 | A= | B=(())(())(())(()) | form=((())(())(())(())) | image=(())(())(())(())()
source=((())(())(())()()) | factor=1 | A= | B=(())(())(())()() | form=((())(())(())()()) | image=(())(())(())()()()
source=((())(())(())())() | factor=1 | A=() | B=(())(())(())() | form=()((())(())(())()) | image=(())(())(())(())()
source=((())(())(())())() | factor=2 | A=((())(())(())()) | B= | form=((())(())(())())() | image=(((())(())(())()))
source=((())(())(()))()() | factor=1 | A=()() | B=(())(())(()) | form=()()((())(())(())) | image=(()())(())(())(())
source=((())(())(()))()() | factor=2 | A=((())(())(()))() | B= | form=((())(())(()))()() | image=(((())(())(()))())
source=((())(())(()))()() | factor=3 | A=((())(())(()))() | B= | form=((())(())(()))()() | image=(((())(())(()))())
source=((())(())()()()()) | factor=1 | A= | B=(())(())()()()() | form=((())(())()()()()) | image=(())(())()()()()()
source=((())(())()()())() | factor=1 | A=() | B=(())(())()()() | form=()((())(())()()()) | image=(())(())(())()()()
source=((())(())()()())() | factor=2 | A=((())(())()()()) | B= | form=((())(())()()())() | image=(((())(())()()()))
source=((())(())()())()() | factor=1 | A=()() | B=(())(())()() | form=()()((())(())()()) | image=(()())(())(())()()
source=((())(())()())()() | factor=2 | A=((())(())()())() | B= | form=((())(())()())()() | image=(((())(())()())())
source=((())(())()())()() | factor=3 | A=((())(())()())() | B= | form=((())(())()())()() | image=(((())(())()())())
source=((())(())())((())) | factor=1 | A=((())) | B=(())(())() | form=((()))((())(())()) | image=(())(())(((())))()
source=((())(())())((())) | factor=2 | A=((())(())()) | B=(()) | form=((())(())())((())) | image=(())(((())(())()))
source=((())(())())()()() | factor=1 | A=()()() | B=(())(())() | form=()()()((())(())()) | image=(()()())(())(())()
source=((())(())())()()() | factor=2 | A=((())(())())()() | B= | form=((())(())())()()() | image=(((())(())())()())
source=((())(())())()()() | factor=3 | A=((())(())())()() | B= | form=((())(())())()()() | image=(((())(())())()())
source=((())(())())()()() | factor=4 | A=((())(())())()() | B= | form=((())(())())()()() | image=(((())(())())()())
source=((())(()))(((()))) | factor=1 | A=(((()))) | B=(())(()) | form=(((())))((())(())) | image=(())(())((((()))))
source=((())(()))(((()))) | factor=2 | A=((())(())) | B=((())) | form=((())(()))(((()))) | image=((()))(((())(())))
source=((())(()))((()())) | factor=1 | A=((()())) | B=(())(()) | form=((()()))((())(())) | image=(())(())(((()())))
source=((())(()))((()())) | factor=2 | A=((())(())) | B=(()()) | form=((())(()))((()())) | image=(()())(((())(())))
source=((())(()))((()))() | factor=1 | A=((()))() | B=(())(()) | form=((()))()((())(())) | image=(())(())(((()))())
source=((())(()))((()))() | factor=2 | A=((())(()))() | B=(()) | form=((())(()))()((())) | image=(())(((())(()))())
source=((())(()))((()))() | factor=3 | A=((())(()))((())) | B= | form=((())(()))((()))() | image=(((())(()))((())))
source=((())(()))()()()() | factor=1 | A=()()()() | B=(())(()) | form=()()()()((())(())) | image=(()()()())(())(())
source=((())(()))()()()() | factor=2 | A=((())(()))()()() | B= | form=((())(()))()()()() | image=(((())(()))()()())
source=((())(()))()()()() | factor=3 | A=((())(()))()()() | B= | form=((())(()))()()()() | image=(((())(()))()()())
source=((())(()))()()()() | factor=4 | A=((())(()))()()() | B= | form=((())(()))()()()() | image=(((())(()))()()())
source=((())(()))()()()() | factor=5 | A=((())(()))()()() | B= | form=((())(()))()()()() | image=(((())(()))()()())
source=((())()()()()()()) | factor=1 | A= | B=(())()()()()()() | form=((())()()()()()()) | image=(())()()()()()()()
source=((())()()()()())() | factor=1 | A=() | B=(())()()()()() | form=()((())()()()()()) | image=(())(())()()()()()
source=((())()()()()())() | factor=2 | A=((())()()()()()) | B= | form=((())()()()()())() | image=(((())()()()()()))
source=((())()()()())()() | factor=1 | A=()() | B=(())()()()() | form=()()((())()()()()) | image=(()())(())()()()()
source=((())()()()())()() | factor=2 | A=((())()()()())() | B= | form=((())()()()())()() | image=(((())()()()())())
source=((())()()()())()() | factor=3 | A=((())()()()())() | B= | form=((())()()()())()() | image=(((())()()()())())
source=((())()()())((())) | factor=1 | A=((())) | B=(())()()() | form=((()))((())()()()) | image=(())(((())))()()()
source=((())()()())((())) | factor=2 | A=((())()()()) | B=(()) | form=((())()()())((())) | image=(())(((())()()()))
source=((())()()())()()() | factor=1 | A=()()() | B=(())()()() | form=()()()((())()()()) | image=(()()())(())()()()
source=((())()()())()()() | factor=2 | A=((())()()())()() | B= | form=((())()()())()()() | image=(((())()()())()())
source=((())()()())()()() | factor=3 | A=((())()()())()() | B= | form=((())()()())()()() | image=(((())()()())()())
source=((())()()())()()() | factor=4 | A=((())()()())()() | B= | form=((())()()())()()() | image=(((())()()())()())
source=((())()())(((()))) | factor=1 | A=(((()))) | B=(())()() | form=(((())))((())()()) | image=(())((((()))))()()
source=((())()())(((()))) | factor=2 | A=((())()()) | B=((())) | form=((())()())(((()))) | image=((()))(((())()()))
source=((())()())((()())) | factor=1 | A=((()())) | B=(())()() | form=((()()))((())()()) | image=(())(((()())))()()
source=((())()())((()())) | factor=2 | A=((())()()) | B=(()()) | form=((())()())((()())) | image=(()())(((())()()))
source=((())()())((())()) | factor=1 | A=((())()) | B=(())()() | form=((())())((())()()) | image=(())(((())()))()()
source=((())()())((())()) | factor=2 | A=((())()()) | B=(())() | form=((())()())((())()) | image=(())(((())()()))()
source=((())()())((()))() | factor=1 | A=((()))() | B=(())()() | form=((()))()((())()()) | image=(())(((()))())()()
source=((())()())((()))() | factor=2 | A=((())()())() | B=(()) | form=((())()())()((())) | image=(())(((())()())())
source=((())()())((()))() | factor=3 | A=((())()())((())) | B= | form=((())()())((()))() | image=(((())()())((())))
source=((())()())()()()() | factor=1 | A=()()()() | B=(())()() | form=()()()()((())()()) | image=(()()()())(())()()
source=((())()())()()()() | factor=2 | A=((())()())()()() | B= | form=((())()())()()()() | image=(((())()())()()())
source=((())()())()()()() | factor=3 | A=((())()())()()() | B= | form=((())()())()()()() | image=(((())()())()()())
source=((())()())()()()() | factor=4 | A=((())()())()()() | B= | form=((())()())()()()() | image=(((())()())()()())
source=((())()())()()()() | factor=5 | A=((())()())()()() | B= | form=((())()())()()()() | image=(((())()())()()())
source=((())())((((())))) | factor=1 | A=((((())))) | B=(())() | form=((((()))))((())()) | image=(())(((((())))))()
source=((())())((((())))) | factor=2 | A=((())()) | B=(((()))) | form=((())())((((())))) | image=(((())))(((())()))
source=((())())(((()()))) | factor=1 | A=(((()()))) | B=(())() | form=(((()())))((())()) | image=(())((((()()))))()
source=((())())(((()()))) | factor=2 | A=((())()) | B=((()())) | form=((())())(((()()))) | image=((()()))(((())()))
source=((())())(((())())) | factor=1 | A=(((())())) | B=(())() | form=(((())()))((())()) | image=(())((((())())))()
source=((())())(((())())) | factor=2 | A=((())()) | B=((())()) | form=((())())(((())())) | image=((())())(((())())) | fixed
source=((())())(((()))()) | factor=1 | A=(((()))()) | B=(())() | form=(((()))())((())()) | image=(())((((()))()))()
source=((())())(((()))()) | factor=2 | A=((())()) | B=((()))() | form=((())())(((()))()) | image=((()))(((())()))()
source=((())())(((())))() | factor=1 | A=(((())))() | B=(())() | form=(((())))()((())()) | image=(())((((())))())()
source=((())())(((())))() | factor=2 | A=((())())() | B=((())) | form=((())())()(((()))) | image=((()))(((())())())
source=((())())(((())))() | factor=3 | A=((())())(((()))) | B= | form=((())())(((())))() | image=(((())())(((()))))
source=((())())((()()())) | factor=1 | A=((()()())) | B=(())() | form=((()()()))((())()) | image=(())(((()()())))()
source=((())())((()()())) | factor=2 | A=((())()) | B=(()()()) | form=((())())((()()())) | image=(()()())(((())()))
source=((())())((()())()) | factor=1 | A=((()())()) | B=(())() | form=((()())())((())()) | image=(())(((()())()))()
source=((())())((()())()) | factor=2 | A=((())()) | B=(()())() | form=((())())((()())()) | image=(()())(((())()))()
source=((())())((()()))() | factor=1 | A=((()()))() | B=(())() | form=((()()))()((())()) | image=(())(((()()))())()
source=((())())((()()))() | factor=2 | A=((())())() | B=(()()) | form=((())())()((()())) | image=(()())(((())())())
source=((())())((()()))() | factor=3 | A=((())())((()())) | B= | form=((())())((()()))() | image=(((())())((()())))
source=((())())((())(())) | factor=1 | A=((())(())) | B=(())() | form=((())(()))((())()) | image=(())(((())(())))()
source=((())())((())(())) | factor=2 | A=((())()) | B=(())(()) | form=((())())((())(())) | image=(())(())(((())()))
source=((())())((())())() | factor=1 | A=((())())() | B=(())() | form=((())())()((())()) | image=(())(((())())())()
source=((())())((())())() | factor=2 | A=((())())() | B=(())() | form=((())())()((())()) | image=(())(((())())())()
source=((())())((())())() | factor=3 | A=((())())((())()) | B= | form=((())())((())())() | image=(((())())((())()))
source=((())())((()))()() | factor=1 | A=((()))()() | B=(())() | form=((()))()()((())()) | image=(())(((()))()())()
source=((())())((()))()() | factor=2 | A=((())())()() | B=(()) | form=((())())()()((())) | image=(())(((())())()())
source=((())())((()))()() | factor=3 | A=((())())((()))() | B= | form=((())())((()))()() | image=(((())())((()))())
source=((())())((()))()() | factor=4 | A=((())())((()))() | B= | form=((())())((()))()() | image=(((())())((()))())
source=((())())()()()()() | factor=1 | A=()()()()() | B=(())() | form=()()()()()((())()) | image=(()()()()())(())()
source=((())())()()()()() | factor=2 | A=((())())()()()() | B= | form=((())())()()()()() | image=(((())())()()()())
source=((())())()()()()() | factor=3 | A=((())())()()()() | B= | form=((())())()()()()() | image=(((())())()()()())
source=((())())()()()()() | factor=4 | A=((())())()()()() | B= | form=((())())()()()()() | image=(((())())()()()())
source=((())())()()()()() | factor=5 | A=((())())()()()() | B= | form=((())())()()()()() | image=(((())())()()()())
source=((())())()()()()() | factor=6 | A=((())())()()()() | B= | form=((())())()()()()() | image=(((())())()()()())
source=((()))(((((()))))) | factor=1 | A=(((((()))))) | B=(()) | form=(((((())))))((())) | image=(())((((((()))))))
source=((()))(((((()))))) | factor=2 | A=((())) | B=((((())))) | form=((()))(((((()))))) | image=(((())))((((()))))
source=((()))((((()())))) | factor=1 | A=((((()())))) | B=(()) | form=((((()()))))((())) | image=(())(((((()())))))
source=((()))((((()())))) | factor=2 | A=((())) | B=(((()()))) | form=((()))((((()())))) | image=(((())))(((()())))
source=((()))((((())()))) | factor=1 | A=((((())()))) | B=(()) | form=((((())())))((())) | image=(())(((((())()))))
source=((()))((((())()))) | factor=2 | A=((())) | B=(((())())) | form=((()))((((())()))) | image=(((())))(((())()))
source=((()))((((()))())) | factor=1 | A=((((()))())) | B=(()) | form=((((()))()))((())) | image=(())(((((()))())))
source=((()))((((()))())) | factor=2 | A=((())) | B=(((()))()) | form=((()))((((()))())) | image=(((()))())(((())))
source=((()))((((())))()) | factor=1 | A=((((())))()) | B=(()) | form=((((())))())((())) | image=(())(((((())))()))
source=((()))((((())))()) | factor=2 | A=((())) | B=(((())))() | form=((()))((((())))()) | image=(((())))(((())))()
source=((()))((((()))))() | factor=1 | A=((((()))))() | B=(()) | form=((((()))))()((())) | image=(())(((((()))))())
source=((()))((((()))))() | factor=2 | A=((()))() | B=(((()))) | form=((()))()((((())))) | image=(((()))())(((())))
source=((()))((((()))))() | factor=3 | A=((()))((((())))) | B= | form=((()))((((()))))() | image=(((()))((((())))))
source=((()))(((()()()))) | factor=1 | A=(((()()()))) | B=(()) | form=(((()()())))((())) | image=(())((((()()()))))
source=((()))(((()()()))) | factor=2 | A=((())) | B=((()()())) | form=((()))(((()()()))) | image=((()()()))(((())))
source=((()))(((()())())) | factor=1 | A=(((()())())) | B=(()) | form=(((()())()))((())) | image=(())((((()())())))
source=((()))(((()())())) | factor=2 | A=((())) | B=((()())()) | form=((()))(((()())())) | image=((()())())(((())))
source=((()))(((()()))()) | factor=1 | A=(((()()))()) | B=(()) | form=(((()()))())((())) | image=(())((((()()))()))
source=((()))(((()()))()) | factor=2 | A=((())) | B=((()()))() | form=((()))(((()()))()) | image=((()()))(((())))()
source=((()))(((()())))() | factor=1 | A=(((()())))() | B=(()) | form=(((()())))()((())) | image=(())((((()())))())
source=((()))(((()())))() | factor=2 | A=((()))() | B=((()())) | form=((()))()(((()()))) | image=((()()))(((()))())
source=((()))(((()())))() | factor=3 | A=((()))(((()()))) | B= | form=((()))(((()())))() | image=(((()))(((()()))))
source=((()))(((())(()))) | factor=1 | A=(((())(()))) | B=(()) | form=(((())(())))((())) | image=(())((((())(()))))
source=((()))(((())(()))) | factor=2 | A=((())) | B=((())(())) | form=((()))(((())(()))) | image=((())(()))(((())))
source=((()))(((())()())) | factor=1 | A=(((())()())) | B=(()) | form=(((())()()))((())) | image=(())((((())()())))
source=((()))(((())()())) | factor=2 | A=((())) | B=((())()()) | form=((()))(((())()())) | image=((())()())(((())))
source=((()))(((())())()) | factor=1 | A=(((())())()) | B=(()) | form=(((())())())((())) | image=(())((((())())()))
source=((()))(((())())()) | factor=2 | A=((())) | B=((())())() | form=((()))(((())())()) | image=((())())(((())))()
source=((()))(((())()))() | factor=1 | A=(((())()))() | B=(()) | form=(((())()))()((())) | image=(())((((())()))())
source=((()))(((())()))() | factor=2 | A=((()))() | B=((())()) | form=((()))()(((())())) | image=((())())(((()))())
source=((()))(((())()))() | factor=3 | A=((()))(((())())) | B= | form=((()))(((())()))() | image=(((()))(((())())))
source=((()))(((()))()()) | factor=1 | A=(((()))()()) | B=(()) | form=(((()))()())((())) | image=(())((((()))()()))
source=((()))(((()))()()) | factor=2 | A=((())) | B=((()))()() | form=((()))(((()))()()) | image=((()))(((())))()()
source=((()))(((()))())() | factor=1 | A=(((()))())() | B=(()) | form=(((()))())()((())) | image=(())((((()))())())
source=((()))(((()))())() | factor=2 | A=((()))() | B=((()))() | form=((()))()(((()))()) | image=((()))(((()))())() | fixed
source=((()))(((()))())() | factor=3 | A=((()))(((()))()) | B= | form=((()))(((()))())() | image=(((()))(((()))()))
source=((()))(((())))()() | factor=1 | A=(((())))()() | B=(()) | form=(((())))()()((())) | image=(())((((())))()())
source=((()))(((())))()() | factor=2 | A=((()))()() | B=((())) | form=((()))()()(((()))) | image=((()))(((()))()())
source=((()))(((())))()() | factor=3 | A=((()))(((())))() | B= | form=((()))(((())))()() | image=(((()))(((())))())
source=((()))(((())))()() | factor=4 | A=((()))(((())))() | B= | form=((()))(((())))()() | image=(((()))(((())))())
source=((()))((()()()())) | factor=1 | A=((()()()())) | B=(()) | form=((()()()()))((())) | image=(())(((()()()())))
source=((()))((()()()())) | factor=2 | A=((())) | B=(()()()()) | form=((()))((()()()())) | image=(()()()())(((())))
source=((()))((()()())()) | factor=1 | A=((()()())()) | B=(()) | form=((()()())())((())) | image=(())(((()()())()))
source=((()))((()()())()) | factor=2 | A=((())) | B=(()()())() | form=((()))((()()())()) | image=(()()())(((())))()
source=((()))((()()()))() | factor=1 | A=((()()()))() | B=(()) | form=((()()()))()((())) | image=(())(((()()()))())
source=((()))((()()()))() | factor=2 | A=((()))() | B=(()()()) | form=((()))()((()()())) | image=(()()())(((()))())
source=((()))((()()()))() | factor=3 | A=((()))((()()())) | B= | form=((()))((()()()))() | image=(((()))((()()())))
source=((()))((()())(())) | factor=1 | A=((()())(())) | B=(()) | form=((()())(()))((())) | image=(())(((()())(())))
source=((()))((()())(())) | factor=2 | A=((())) | B=(()())(()) | form=((()))((()())(())) | image=(()())(())(((())))
source=((()))((()())()()) | factor=1 | A=((()())()()) | B=(()) | form=((()())()())((())) | image=(())(((()())()()))
source=((()))((()())()()) | factor=2 | A=((())) | B=(()())()() | form=((()))((()())()()) | image=(()())(((())))()()
source=((()))((()())())() | factor=1 | A=((()())())() | B=(()) | form=((()())())()((())) | image=(())(((()())())())
source=((()))((()())())() | factor=2 | A=((()))() | B=(()())() | form=((()))()((()())()) | image=(()())(((()))())()
source=((()))((()())())() | factor=3 | A=((()))((()())()) | B= | form=((()))((()())())() | image=(((()))((()())()))
source=((()))((()()))()() | factor=1 | A=((()()))()() | B=(()) | form=((()()))()()((())) | image=(())(((()()))()())
source=((()))((()()))()() | factor=2 | A=((()))()() | B=(()()) | form=((()))()()((()())) | image=(()())(((()))()())
source=((()))((()()))()() | factor=3 | A=((()))((()()))() | B= | form=((()))((()()))()() | image=(((()))((()()))())
source=((()))((()()))()() | factor=4 | A=((()))((()()))() | B= | form=((()))((()()))()() | image=(((()))((()()))())
source=((()))((()))((())) | factor=1 | A=((()))((())) | B=(()) | form=((()))((()))((())) | image=(())(((()))((())))
source=((()))((()))((())) | factor=2 | A=((()))((())) | B=(()) | form=((()))((()))((())) | image=(())(((()))((())))
source=((()))((()))((())) | factor=3 | A=((()))((())) | B=(()) | form=((()))((()))((())) | image=(())(((()))((())))
source=((()))((()))()()() | factor=1 | A=((()))()()() | B=(()) | form=((()))()()()((())) | image=(())(((()))()()())
source=((()))((()))()()() | factor=2 | A=((()))()()() | B=(()) | form=((()))()()()((())) | image=(())(((()))()()())
source=((()))((()))()()() | factor=3 | A=((()))((()))()() | B= | form=((()))((()))()()() | image=(((()))((()))()())
source=((()))((()))()()() | factor=4 | A=((()))((()))()() | B= | form=((()))((()))()()() | image=(((()))((()))()())
source=((()))((()))()()() | factor=5 | A=((()))((()))()() | B= | form=((()))((()))()()() | image=(((()))((()))()())
source=((()))()()()()()() | factor=1 | A=()()()()()() | B=(()) | form=()()()()()()((())) | image=(()()()()()())(())
source=((()))()()()()()() | factor=2 | A=((()))()()()()() | B= | form=((()))()()()()()() | image=(((()))()()()()())
source=((()))()()()()()() | factor=3 | A=((()))()()()()() | B= | form=((()))()()()()()() | image=(((()))()()()()())
source=((()))()()()()()() | factor=4 | A=((()))()()()()() | B= | form=((()))()()()()()() | image=(((()))()()()()())
source=((()))()()()()()() | factor=5 | A=((()))()()()()() | B= | form=((()))()()()()()() | image=(((()))()()()()())
source=((()))()()()()()() | factor=6 | A=((()))()()()()() | B= | form=((()))()()()()()() | image=(((()))()()()()())
source=((()))()()()()()() | factor=7 | A=((()))()()()()() | B= | form=((()))()()()()()() | image=(((()))()()()()())
source=(()()()()()()()()) | factor=1 | A= | B=()()()()()()()() | form=(()()()()()()()()) | image=()()()()()()()()()
source=(()()()()()()())() | factor=1 | A=() | B=()()()()()()() | form=()(()()()()()()()) | image=(())()()()()()()()
source=(()()()()()()())() | factor=2 | A=(()()()()()()()) | B= | form=(()()()()()()())() | image=((()()()()()()()))
source=(()()()()()())(()) | factor=1 | A=(()) | B=()()()()()() | form=(())(()()()()()()) | image=((()))()()()()()()
source=(()()()()()())(()) | factor=2 | A=(()()()()()()) | B=() | form=(()()()()()())(()) | image=((()()()()()()))()
source=(()()()()()())()() | factor=1 | A=()() | B=()()()()()() | form=()()(()()()()()()) | image=(()())()()()()()()
source=(()()()()()())()() | factor=2 | A=(()()()()()())() | B= | form=(()()()()()())()() | image=((()()()()()())())
source=(()()()()()())()() | factor=3 | A=(()()()()()())() | B= | form=(()()()()()())()() | image=((()()()()()())())
source=(()()()()())((())) | factor=1 | A=((())) | B=()()()()() | form=((()))(()()()()()) | image=(((())))()()()()()
source=(()()()()())((())) | factor=2 | A=(()()()()()) | B=(()) | form=(()()()()())((())) | image=(())((()()()()()))
source=(()()()()())(()()) | factor=1 | A=(()()) | B=()()()()() | form=(()())(()()()()()) | image=((()()))()()()()()
source=(()()()()())(()()) | factor=2 | A=(()()()()()) | B=()() | form=(()()()()())(()()) | image=((()()()()()))()()
source=(()()()()())(())() | factor=1 | A=(())() | B=()()()()() | form=(())()(()()()()()) | image=((())())()()()()()
source=(()()()()())(())() | factor=2 | A=(()()()()())() | B=() | form=(()()()()())()(()) | image=((()()()()())())()
source=(()()()()())(())() | factor=3 | A=(()()()()())(()) | B= | form=(()()()()())(())() | image=((()()()()())(()))
source=(()()()()())()()() | factor=1 | A=()()() | B=()()()()() | form=()()()(()()()()()) | image=(()()())()()()()()
source=(()()()()())()()() | factor=2 | A=(()()()()())()() | B= | form=(()()()()())()()() | image=((()()()()())()())
source=(()()()()())()()() | factor=3 | A=(()()()()())()() | B= | form=(()()()()())()()() | image=((()()()()())()())
source=(()()()()())()()() | factor=4 | A=(()()()()())()() | B= | form=(()()()()())()()() | image=((()()()()())()())
source=(()()()())(((()))) | factor=1 | A=(((()))) | B=()()()() | form=(((())))(()()()()) | image=((((()))))()()()()
source=(()()()())(((()))) | factor=2 | A=(()()()()) | B=((())) | form=(()()()())(((()))) | image=((()))((()()()()))
source=(()()()())((()())) | factor=1 | A=((()())) | B=()()()() | form=((()()))(()()()()) | image=(((()())))()()()()
source=(()()()())((()())) | factor=2 | A=(()()()()) | B=(()()) | form=(()()()())((()())) | image=(()())((()()()()))
source=(()()()())((())()) | factor=1 | A=((())()) | B=()()()() | form=((())())(()()()()) | image=(((())()))()()()()
source=(()()()())((())()) | factor=2 | A=(()()()()) | B=(())() | form=(()()()())((())()) | image=(())((()()()()))()
source=(()()()())((()))() | factor=1 | A=((()))() | B=()()()() | form=((()))()(()()()()) | image=(((()))())()()()()
source=(()()()())((()))() | factor=2 | A=(()()()())() | B=(()) | form=(()()()())()((())) | image=(())((()()()())())
source=(()()()())((()))() | factor=3 | A=(()()()())((())) | B= | form=(()()()())((()))() | image=((()()()())((())))
source=(()()()())(()()()) | factor=1 | A=(()()()) | B=()()()() | form=(()()())(()()()()) | image=((()()()))()()()()
source=(()()()())(()()()) | factor=2 | A=(()()()()) | B=()()() | form=(()()()())(()()()) | image=((()()()()))()()()
source=(()()()())(()())() | factor=1 | A=(()())() | B=()()()() | form=(()())()(()()()()) | image=((()())())()()()()
source=(()()()())(()())() | factor=2 | A=(()()()())() | B=()() | form=(()()()())()(()()) | image=((()()()())())()()
source=(()()()())(()())() | factor=3 | A=(()()()())(()()) | B= | form=(()()()())(()())() | image=((()()()())(()()))
source=(()()()())(())(()) | factor=1 | A=(())(()) | B=()()()() | form=(())(())(()()()()) | image=((())(()))()()()()
source=(()()()())(())(()) | factor=2 | A=(()()()())(()) | B=() | form=(()()()())(())(()) | image=((()()()())(()))()
source=(()()()())(())(()) | factor=3 | A=(()()()())(()) | B=() | form=(()()()())(())(()) | image=((()()()())(()))()
source=(()()()())(())()() | factor=1 | A=(())()() | B=()()()() | form=(())()()(()()()()) | image=((())()())()()()()
source=(()()()())(())()() | factor=2 | A=(()()()())()() | B=() | form=(()()()())()()(()) | image=((()()()())()())()
source=(()()()())(())()() | factor=3 | A=(()()()())(())() | B= | form=(()()()())(())()() | image=((()()()())(())())
source=(()()()())(())()() | factor=4 | A=(()()()())(())() | B= | form=(()()()())(())()() | image=((()()()())(())())
source=(()()()())()()()() | factor=1 | A=()()()() | B=()()()() | form=()()()()(()()()()) | image=(()()()())()()()() | fixed
source=(()()()())()()()() | factor=2 | A=(()()()())()()() | B= | form=(()()()())()()()() | image=((()()()())()()())
source=(()()()())()()()() | factor=3 | A=(()()()())()()() | B= | form=(()()()())()()()() | image=((()()()())()()())
source=(()()()())()()()() | factor=4 | A=(()()()())()()() | B= | form=(()()()())()()()() | image=((()()()())()()())
source=(()()()())()()()() | factor=5 | A=(()()()())()()() | B= | form=(()()()())()()()() | image=((()()()())()()())
source=(()()())((((())))) | factor=1 | A=((((())))) | B=()()() | form=((((()))))(()()()) | image=(((((())))))()()()
source=(()()())((((())))) | factor=2 | A=(()()()) | B=(((()))) | form=(()()())((((())))) | image=((()()()))(((())))
source=(()()())(((()()))) | factor=1 | A=(((()()))) | B=()()() | form=(((()())))(()()()) | image=((((()()))))()()()
source=(()()())(((()()))) | factor=2 | A=(()()()) | B=((()())) | form=(()()())(((()()))) | image=((()()))((()()()))
source=(()()())(((())())) | factor=1 | A=(((())())) | B=()()() | form=(((())()))(()()()) | image=((((())())))()()()
source=(()()())(((())())) | factor=2 | A=(()()()) | B=((())()) | form=(()()())(((())())) | image=((())())((()()()))
source=(()()())(((()))()) | factor=1 | A=(((()))()) | B=()()() | form=(((()))())(()()()) | image=((((()))()))()()()
source=(()()())(((()))()) | factor=2 | A=(()()()) | B=((()))() | form=(()()())(((()))()) | image=((()))((()()()))()
source=(()()())(((())))() | factor=1 | A=(((())))() | B=()()() | form=(((())))()(()()()) | image=((((())))())()()()
source=(()()())(((())))() | factor=2 | A=(()()())() | B=((())) | form=(()()())()(((()))) | image=((()))((()()())())
source=(()()())(((())))() | factor=3 | A=(()()())(((()))) | B= | form=(()()())(((())))() | image=((()()())(((()))))
source=(()()())((()()())) | factor=1 | A=((()()())) | B=()()() | form=((()()()))(()()()) | image=(((()()())))()()()
source=(()()())((()()())) | factor=2 | A=(()()()) | B=(()()()) | form=(()()())((()()())) | image=(()()())((()()())) | fixed
source=(()()())((()())()) | factor=1 | A=((()())()) | B=()()() | form=((()())())(()()()) | image=(((()())()))()()()
source=(()()())((()())()) | factor=2 | A=(()()()) | B=(()())() | form=(()()())((()())()) | image=(()())((()()()))()
source=(()()())((()()))() | factor=1 | A=((()()))() | B=()()() | form=((()()))()(()()()) | image=(((()()))())()()()
source=(()()())((()()))() | factor=2 | A=(()()())() | B=(()()) | form=(()()())()((()())) | image=(()())((()()())())
source=(()()())((()()))() | factor=3 | A=(()()())((()())) | B= | form=(()()())((()()))() | image=((()()())((()())))
source=(()()())((())(())) | factor=1 | A=((())(())) | B=()()() | form=((())(()))(()()()) | image=(((())(())))()()()
source=(()()())((())(())) | factor=2 | A=(()()()) | B=(())(()) | form=(()()())((())(())) | image=(())(())((()()()))
source=(()()())((())()()) | factor=1 | A=((())()()) | B=()()() | form=((())()())(()()()) | image=(((())()()))()()()
source=(()()())((())()()) | factor=2 | A=(()()()) | B=(())()() | form=(()()())((())()()) | image=(())((()()()))()()
source=(()()())((())())() | factor=1 | A=((())())() | B=()()() | form=((())())()(()()()) | image=(((())())())()()()
source=(()()())((())())() | factor=2 | A=(()()())() | B=(())() | form=(()()())()((())()) | image=(())((()()())())()
source=(()()())((())())() | factor=3 | A=(()()())((())()) | B= | form=(()()())((())())() | image=((()()())((())()))
source=(()()())((()))()() | factor=1 | A=((()))()() | B=()()() | form=((()))()()(()()()) | image=(((()))()())()()()
source=(()()())((()))()() | factor=2 | A=(()()())()() | B=(()) | form=(()()())()()((())) | image=(())((()()())()())
source=(()()())((()))()() | factor=3 | A=(()()())((()))() | B= | form=(()()())((()))()() | image=((()()())((()))())
source=(()()())((()))()() | factor=4 | A=(()()())((()))() | B= | form=(()()())((()))()() | image=((()()())((()))())
source=(()()())(()()())() | factor=1 | A=(()()())() | B=()()() | form=(()()())()(()()()) | image=((()()())())()()()
source=(()()())(()()())() | factor=2 | A=(()()())() | B=()()() | form=(()()())()(()()()) | image=((()()())())()()()
source=(()()())(()()())() | factor=3 | A=(()()())(()()()) | B= | form=(()()())(()()())() | image=((()()())(()()()))
source=(()()())(()())(()) | factor=1 | A=(()())(()) | B=()()() | form=(()())(())(()()()) | image=((()())(()))()()()
source=(()()())(()())(()) | factor=2 | A=(()()())(()) | B=()() | form=(()()())(())(()()) | image=((()()())(()))()()
source=(()()())(()())(()) | factor=3 | A=(()()())(()()) | B=() | form=(()()())(()())(()) | image=((()()())(()()))()
source=(()()())(()())()() | factor=1 | A=(()())()() | B=()()() | form=(()())()()(()()()) | image=((()())()())()()()
source=(()()())(()())()() | factor=2 | A=(()()())()() | B=()() | form=(()()())()()(()()) | image=((()()())()())()()
source=(()()())(()())()() | factor=3 | A=(()()())(()())() | B= | form=(()()())(()())()() | image=((()()())(()())())
source=(()()())(()())()() | factor=4 | A=(()()())(()())() | B= | form=(()()())(()())()() | image=((()()())(()())())
source=(()()())(())((())) | factor=1 | A=(())((())) | B=()()() | form=(())((()))(()()()) | image=((())((())))()()()
source=(()()())(())((())) | factor=2 | A=(()()())((())) | B=() | form=(()()())((()))(()) | image=((()()())((())))()
source=(()()())(())((())) | factor=3 | A=(()()())(()) | B=(()) | form=(()()())(())((())) | image=(())((()()())(()))
source=(()()())(())(())() | factor=1 | A=(())(())() | B=()()() | form=(())(())()(()()()) | image=((())(())())()()()
source=(()()())(())(())() | factor=2 | A=(()()())(())() | B=() | form=(()()())(())()(()) | image=((()()())(())())()
source=(()()())(())(())() | factor=3 | A=(()()())(())() | B=() | form=(()()())(())()(()) | image=((()()())(())())()
source=(()()())(())(())() | factor=4 | A=(()()())(())(()) | B= | form=(()()())(())(())() | image=((()()())(())(()))
source=(()()())(())()()() | factor=1 | A=(())()()() | B=()()() | form=(())()()()(()()()) | image=((())()()())()()()
source=(()()())(())()()() | factor=2 | A=(()()())()()() | B=() | form=(()()())()()()(()) | image=((()()())()()())()
source=(()()())(())()()() | factor=3 | A=(()()())(())()() | B= | form=(()()())(())()()() | image=((()()())(())()())
source=(()()())(())()()() | factor=4 | A=(()()())(())()() | B= | form=(()()())(())()()() | image=((()()())(())()())
source=(()()())(())()()() | factor=5 | A=(()()())(())()() | B= | form=(()()())(())()()() | image=((()()())(())()())
source=(()()())()()()()() | factor=1 | A=()()()()() | B=()()() | form=()()()()()(()()()) | image=(()()()()())()()()
source=(()()())()()()()() | factor=2 | A=(()()())()()()() | B= | form=(()()())()()()()() | image=((()()())()()()())
source=(()()())()()()()() | factor=3 | A=(()()())()()()() | B= | form=(()()())()()()()() | image=((()()())()()()())
source=(()()())()()()()() | factor=4 | A=(()()())()()()() | B= | form=(()()())()()()()() | image=((()()())()()()())
source=(()()())()()()()() | factor=5 | A=(()()())()()()() | B= | form=(()()())()()()()() | image=((()()())()()()())
source=(()()())()()()()() | factor=6 | A=(()()())()()()() | B= | form=(()()())()()()()() | image=((()()())()()()())
source=(()())(((((()))))) | factor=1 | A=(((((()))))) | B=()() | form=(((((())))))(()()) | image=((((((()))))))()()
source=(()())(((((()))))) | factor=2 | A=(()()) | B=((((())))) | form=(()())(((((()))))) | image=((()()))((((()))))
source=(()())((((()())))) | factor=1 | A=((((()())))) | B=()() | form=((((()()))))(()()) | image=(((((()())))))()()
source=(()())((((()())))) | factor=2 | A=(()()) | B=(((()()))) | form=(()())((((()())))) | image=((()()))(((()())))
source=(()())((((())()))) | factor=1 | A=((((())()))) | B=()() | form=((((())())))(()()) | image=(((((())()))))()()
source=(()())((((())()))) | factor=2 | A=(()()) | B=(((())())) | form=(()())((((())()))) | image=((()()))(((())()))
source=(()())((((()))())) | factor=1 | A=((((()))())) | B=()() | form=((((()))()))(()()) | image=(((((()))())))()()
source=(()())((((()))())) | factor=2 | A=(()()) | B=(((()))()) | form=(()())((((()))())) | image=((()()))(((()))())
source=(()())((((())))()) | factor=1 | A=((((())))()) | B=()() | form=((((())))())(()()) | image=(((((())))()))()()
source=(()())((((())))()) | factor=2 | A=(()()) | B=(((())))() | form=(()())((((())))()) | image=((()()))(((())))()
source=(()())((((()))))() | factor=1 | A=((((()))))() | B=()() | form=((((()))))()(()()) | image=(((((()))))())()()
source=(()())((((()))))() | factor=2 | A=(()())() | B=(((()))) | form=(()())()((((())))) | image=((()())())(((())))
source=(()())((((()))))() | factor=3 | A=(()())((((())))) | B= | form=(()())((((()))))() | image=((()())((((())))))
source=(()())(((()()()))) | factor=1 | A=(((()()()))) | B=()() | form=(((()()())))(()()) | image=((((()()()))))()()
source=(()())(((()()()))) | factor=2 | A=(()()) | B=((()()())) | form=(()())(((()()()))) | image=((()()))((()()()))
source=(()())(((()())())) | factor=1 | A=(((()())())) | B=()() | form=(((()())()))(()()) | image=((((()())())))()()
source=(()())(((()())())) | factor=2 | A=(()()) | B=((()())()) | form=(()())(((()())())) | image=((()())())((()()))
source=(()())(((()()))()) | factor=1 | A=(((()()))()) | B=()() | form=(((()()))())(()()) | image=((((()()))()))()()
source=(()())(((()()))()) | factor=2 | A=(()()) | B=((()()))() | form=(()())(((()()))()) | image=((()()))((()()))()
source=(()())(((()())))() | factor=1 | A=(((()())))() | B=()() | form=(((()())))()(()()) | image=((((()())))())()()
source=(()())(((()())))() | factor=2 | A=(()())() | B=((()())) | form=(()())()(((()()))) | image=((()())())((()()))
source=(()())(((()())))() | factor=3 | A=(()())(((()()))) | B= | form=(()())(((()())))() | image=((()())(((()()))))
source=(()())(((())(()))) | factor=1 | A=(((())(()))) | B=()() | form=(((())(())))(()()) | image=((((())(()))))()()
source=(()())(((())(()))) | factor=2 | A=(()()) | B=((())(())) | form=(()())(((())(()))) | image=((())(()))((()()))
source=(()())(((())()())) | factor=1 | A=(((())()())) | B=()() | form=(((())()()))(()()) | image=((((())()())))()()
source=(()())(((())()())) | factor=2 | A=(()()) | B=((())()()) | form=(()())(((())()())) | image=((())()())((()()))
source=(()())(((())())()) | factor=1 | A=(((())())()) | B=()() | form=(((())())())(()()) | image=((((())())()))()()
source=(()())(((())())()) | factor=2 | A=(()()) | B=((())())() | form=(()())(((())())()) | image=((())())((()()))()
source=(()())(((())()))() | factor=1 | A=(((())()))() | B=()() | form=(((())()))()(()()) | image=((((())()))())()()
source=(()())(((())()))() | factor=2 | A=(()())() | B=((())()) | form=(()())()(((())())) | image=((())())((()())())
source=(()())(((())()))() | factor=3 | A=(()())(((())())) | B= | form=(()())(((())()))() | image=((()())(((())())))
source=(()())(((()))()()) | factor=1 | A=(((()))()()) | B=()() | form=(((()))()())(()()) | image=((((()))()()))()()
source=(()())(((()))()()) | factor=2 | A=(()()) | B=((()))()() | form=(()())(((()))()()) | image=((()))((()()))()()
source=(()())(((()))())() | factor=1 | A=(((()))())() | B=()() | form=(((()))())()(()()) | image=((((()))())())()()
source=(()())(((()))())() | factor=2 | A=(()())() | B=((()))() | form=(()())()(((()))()) | image=((()))((()())())()
source=(()())(((()))())() | factor=3 | A=(()())(((()))()) | B= | form=(()())(((()))())() | image=((()())(((()))()))
source=(()())(((())))()() | factor=1 | A=(((())))()() | B=()() | form=(((())))()()(()()) | image=((((())))()())()()
source=(()())(((())))()() | factor=2 | A=(()())()() | B=((())) | form=(()())()()(((()))) | image=((()))((()())()())
source=(()())(((())))()() | factor=3 | A=(()())(((())))() | B= | form=(()())(((())))()() | image=((()())(((())))())
source=(()())(((())))()() | factor=4 | A=(()())(((())))() | B= | form=(()())(((())))()() | image=((()())(((())))())
source=(()())((()()()())) | factor=1 | A=((()()()())) | B=()() | form=((()()()()))(()()) | image=(((()()()())))()()
source=(()())((()()()())) | factor=2 | A=(()()) | B=(()()()()) | form=(()())((()()()())) | image=(()()()())((()()))
source=(()())((()()())()) | factor=1 | A=((()()())()) | B=()() | form=((()()())())(()()) | image=(((()()())()))()()
source=(()())((()()())()) | factor=2 | A=(()()) | B=(()()())() | form=(()())((()()())()) | image=(()()())((()()))()
source=(()())((()()()))() | factor=1 | A=((()()()))() | B=()() | form=((()()()))()(()()) | image=(((()()()))())()()
source=(()())((()()()))() | factor=2 | A=(()())() | B=(()()()) | form=(()())()((()()())) | image=(()()())((()())())
source=(()())((()()()))() | factor=3 | A=(()())((()()())) | B= | form=(()())((()()()))() | image=((()())((()()())))
source=(()())((()())(())) | factor=1 | A=((()())(())) | B=()() | form=((()())(()))(()()) | image=(((()())(())))()()
source=(()())((()())(())) | factor=2 | A=(()()) | B=(()())(()) | form=(()())((()())(())) | image=(()())(())((()()))
source=(()())((()())()()) | factor=1 | A=((()())()()) | B=()() | form=((()())()())(()()) | image=(((()())()()))()()
source=(()())((()())()()) | factor=2 | A=(()()) | B=(()())()() | form=(()())((()())()()) | image=(()())((()()))()()
source=(()())((()())())() | factor=1 | A=((()())())() | B=()() | form=((()())())()(()()) | image=(((()())())())()()
source=(()())((()())())() | factor=2 | A=(()())() | B=(()())() | form=(()())()((()())()) | image=(()())((()())())() | fixed
source=(()())((()())())() | factor=3 | A=(()())((()())()) | B= | form=(()())((()())())() | image=((()())((()())()))
source=(()())((()()))()() | factor=1 | A=((()()))()() | B=()() | form=((()()))()()(()()) | image=(((()()))()())()()
source=(()())((()()))()() | factor=2 | A=(()())()() | B=(()()) | form=(()())()()((()())) | image=(()())((()())()())
source=(()())((()()))()() | factor=3 | A=(()())((()()))() | B= | form=(()())((()()))()() | image=((()())((()()))())
source=(()())((()()))()() | factor=4 | A=(()())((()()))() | B= | form=(()())((()()))()() | image=((()())((()()))())
source=(()())((())((()))) | factor=1 | A=((())((()))) | B=()() | form=((())((())))(()()) | image=(((())((()))))()()
source=(()())((())((()))) | factor=2 | A=(()()) | B=(())((())) | form=(()())((())((()))) | image=(())((()))((()()))
source=(()())((())(())()) | factor=1 | A=((())(())()) | B=()() | form=((())(())())(()()) | image=(((())(())()))()()
source=(()())((())(())()) | factor=2 | A=(()()) | B=(())(())() | form=(()())((())(())()) | image=(())(())((()()))()
source=(()())((())(()))() | factor=1 | A=((())(()))() | B=()() | form=((())(()))()(()()) | image=(((())(()))())()()
source=(()())((())(()))() | factor=2 | A=(()())() | B=(())(()) | form=(()())()((())(())) | image=(())(())((()())())
source=(()())((())(()))() | factor=3 | A=(()())((())(())) | B= | form=(()())((())(()))() | image=((()())((())(())))
source=(()())((())()()()) | factor=1 | A=((())()()()) | B=()() | form=((())()()())(()()) | image=(((())()()()))()()
source=(()())((())()()()) | factor=2 | A=(()()) | B=(())()()() | form=(()())((())()()()) | image=(())((()()))()()()
source=(()())((())()())() | factor=1 | A=((())()())() | B=()() | form=((())()())()(()()) | image=(((())()())())()()
source=(()())((())()())() | factor=2 | A=(()())() | B=(())()() | form=(()())()((())()()) | image=(())((()())())()()
source=(()())((())()())() | factor=3 | A=(()())((())()()) | B= | form=(()())((())()())() | image=((()())((())()()))
source=(()())((())())()() | factor=1 | A=((())())()() | B=()() | form=((())())()()(()()) | image=(((())())()())()()
source=(()())((())())()() | factor=2 | A=(()())()() | B=(())() | form=(()())()()((())()) | image=(())((()())()())()
source=(()())((())())()() | factor=3 | A=(()())((())())() | B= | form=(()())((())())()() | image=((()())((())())())
source=(()())((())())()() | factor=4 | A=(()())((())())() | B= | form=(()())((())())()() | image=((()())((())())())
source=(()())((()))((())) | factor=1 | A=((()))((())) | B=()() | form=((()))((()))(()()) | image=(((()))((())))()()
source=(()())((()))((())) | factor=2 | A=(()())((())) | B=(()) | form=(()())((()))((())) | image=(())((()())((())))
source=(()())((()))((())) | factor=3 | A=(()())((())) | B=(()) | form=(()())((()))((())) | image=(())((()())((())))
source=(()())((()))()()() | factor=1 | A=((()))()()() | B=()() | form=((()))()()()(()()) | image=(((()))()()())()()
source=(()())((()))()()() | factor=2 | A=(()())()()() | B=(()) | form=(()())()()()((())) | image=(())((()())()()())
source=(()())((()))()()() | factor=3 | A=(()())((()))()() | B= | form=(()())((()))()()() | image=((()())((()))()())
source=(()())((()))()()() | factor=4 | A=(()())((()))()() | B= | form=(()())((()))()()() | image=((()())((()))()())
source=(()())((()))()()() | factor=5 | A=(()())((()))()() | B= | form=(()())((()))()()() | image=((()())((()))()())
source=(()())(()())((())) | factor=1 | A=(()())((())) | B=()() | form=(()())((()))(()()) | image=((()())((())))()()
source=(()())(()())((())) | factor=2 | A=(()())((())) | B=()() | form=(()())((()))(()()) | image=((()())((())))()()
source=(()())(()())((())) | factor=3 | A=(()())(()()) | B=(()) | form=(()())(()())((())) | image=(())((()())(()()))
source=(()())(()())(()()) | factor=1 | A=(()())(()()) | B=()() | form=(()())(()())(()()) | image=((()())(()()))()()
source=(()())(()())(()()) | factor=2 | A=(()())(()()) | B=()() | form=(()())(()())(()()) | image=((()())(()()))()()
source=(()())(()())(()()) | factor=3 | A=(()())(()()) | B=()() | form=(()())(()())(()()) | image=((()())(()()))()()
source=(()())(()())(())() | factor=1 | A=(()())(())() | B=()() | form=(()())(())()(()()) | image=((()())(())())()()
source=(()())(()())(())() | factor=2 | A=(()())(())() | B=()() | form=(()())(())()(()()) | image=((()())(())())()()
source=(()())(()())(())() | factor=3 | A=(()())(()())() | B=() | form=(()())(()())()(()) | image=((()())(()())())()
source=(()())(()())(())() | factor=4 | A=(()())(()())(()) | B= | form=(()())(()())(())() | image=((()())(()())(()))
source=(()())(()())()()() | factor=1 | A=(()())()()() | B=()() | form=(()())()()()(()()) | image=((()())()()())()()
source=(()())(()())()()() | factor=2 | A=(()())()()() | B=()() | form=(()())()()()(()()) | image=((()())()()())()()
source=(()())(()())()()() | factor=3 | A=(()())(()())()() | B= | form=(()())(()())()()() | image=((()())(()())()())
source=(()())(()())()()() | factor=4 | A=(()())(()())()() | B= | form=(()())(()())()()() | image=((()())(()())()())
source=(()())(()())()()() | factor=5 | A=(()())(()())()() | B= | form=(()())(()())()()() | image=((()())(()())()())
source=(()())(())(((()))) | factor=1 | A=(())(((()))) | B=()() | form=(())(((())))(()()) | image=((())(((()))))()()
source=(()())(())(((()))) | factor=2 | A=(()())(((()))) | B=() | form=(()())(((())))(()) | image=((()())(((()))))()
source=(()())(())(((()))) | factor=3 | A=(()())(()) | B=((())) | form=(()())(())(((()))) | image=((()))((()())(()))
source=(()())(())((()())) | factor=1 | A=(())((()())) | B=()() | form=(())((()()))(()()) | image=((())((()())))()()
source=(()())(())((()())) | factor=2 | A=(()())((()())) | B=() | form=(()())((()()))(()) | image=((()())((()())))()
source=(()())(())((()())) | factor=3 | A=(()())(()) | B=(()()) | form=(()())(())((()())) | image=(()())((()())(()))
source=(()())(())((())()) | factor=1 | A=(())((())()) | B=()() | form=(())((())())(()()) | image=((())((())()))()()
source=(()())(())((())()) | factor=2 | A=(()())((())()) | B=() | form=(()())((())())(()) | image=((()())((())()))()
source=(()())(())((())()) | factor=3 | A=(()())(()) | B=(())() | form=(()())(())((())()) | image=(())((()())(()))()
source=(()())(())((()))() | factor=1 | A=(())((()))() | B=()() | form=(())((()))()(()()) | image=((())((()))())()()
source=(()())(())((()))() | factor=2 | A=(()())((()))() | B=() | form=(()())((()))()(()) | image=((()())((()))())()
source=(()())(())((()))() | factor=3 | A=(()())(())() | B=(()) | form=(()())(())()((())) | image=(())((()())(())())
source=(()())(())((()))() | factor=4 | A=(()())(())((())) | B= | form=(()())(())((()))() | image=((()())(())((())))
source=(()())(())(())(()) | factor=1 | A=(())(())(()) | B=()() | form=(())(())(())(()()) | image=((())(())(()))()()
source=(()())(())(())(()) | factor=2 | A=(()())(())(()) | B=() | form=(()())(())(())(()) | image=((()())(())(()))()
source=(()())(())(())(()) | factor=3 | A=(()())(())(()) | B=() | form=(()())(())(())(()) | image=((()())(())(()))()
source=(()())(())(())(()) | factor=4 | A=(()())(())(()) | B=() | form=(()())(())(())(()) | image=((()())(())(()))()
source=(()())(())(())()() | factor=1 | A=(())(())()() | B=()() | form=(())(())()()(()()) | image=((())(())()())()()
source=(()())(())(())()() | factor=2 | A=(()())(())()() | B=() | form=(()())(())()()(()) | image=((()())(())()())()
source=(()())(())(())()() | factor=3 | A=(()())(())()() | B=() | form=(()())(())()()(()) | image=((()())(())()())()
source=(()())(())(())()() | factor=4 | A=(()())(())(())() | B= | form=(()())(())(())()() | image=((()())(())(())())
source=(()())(())(())()() | factor=5 | A=(()())(())(())() | B= | form=(()())(())(())()() | image=((()())(())(())())
source=(()())(())()()()() | factor=1 | A=(())()()()() | B=()() | form=(())()()()()(()()) | image=((())()()()())()()
source=(()())(())()()()() | factor=2 | A=(()())()()()() | B=() | form=(()())()()()()(()) | image=((()())()()()())()
source=(()())(())()()()() | factor=3 | A=(()())(())()()() | B= | form=(()())(())()()()() | image=((()())(())()()())
source=(()())(())()()()() | factor=4 | A=(()())(())()()() | B= | form=(()())(())()()()() | image=((()())(())()()())
source=(()())(())()()()() | factor=5 | A=(()())(())()()() | B= | form=(()())(())()()()() | image=((()())(())()()())
source=(()())(())()()()() | factor=6 | A=(()())(())()()() | B= | form=(()())(())()()()() | image=((()())(())()()())
source=(()())()()()()()() | factor=1 | A=()()()()()() | B=()() | form=()()()()()()(()()) | image=(()()()()()())()()
source=(()())()()()()()() | factor=2 | A=(()())()()()()() | B= | form=(()())()()()()()() | image=((()())()()()()())
source=(()())()()()()()() | factor=3 | A=(()())()()()()() | B= | form=(()())()()()()()() | image=((()())()()()()())
source=(()())()()()()()() | factor=4 | A=(()())()()()()() | B= | form=(()())()()()()()() | image=((()())()()()()())
source=(()())()()()()()() | factor=5 | A=(()())()()()()() | B= | form=(()())()()()()()() | image=((()())()()()()())
source=(()())()()()()()() | factor=6 | A=(()())()()()()() | B= | form=(()())()()()()()() | image=((()())()()()()())
source=(()())()()()()()() | factor=7 | A=(()())()()()()() | B= | form=(()())()()()()()() | image=((()())()()()()())
source=(())((((((())))))) | factor=1 | A=((((((())))))) | B=() | form=((((((()))))))(()) | image=(((((((())))))))()
source=(())((((((())))))) | factor=2 | A=(()) | B=(((((()))))) | form=(())((((((())))))) | image=((()))(((((())))))
source=(())(((((()()))))) | factor=1 | A=(((((()()))))) | B=() | form=(((((()())))))(()) | image=((((((()()))))))()
source=(())(((((()()))))) | factor=2 | A=(()) | B=((((()())))) | form=(())(((((()()))))) | image=((()))((((()()))))
source=(())(((((())())))) | factor=1 | A=(((((())())))) | B=() | form=(((((())()))))(()) | image=((((((())())))))()
source=(())(((((())())))) | factor=2 | A=(()) | B=((((())()))) | form=(())(((((())())))) | image=((()))((((())())))
source=(())(((((()))()))) | factor=1 | A=(((((()))()))) | B=() | form=(((((()))())))(()) | image=((((((()))()))))()
source=(())(((((()))()))) | factor=2 | A=(()) | B=((((()))())) | form=(())(((((()))()))) | image=((()))((((()))()))
source=(())(((((())))())) | factor=1 | A=(((((())))())) | B=() | form=(((((())))()))(()) | image=((((((())))())))()
source=(())(((((())))())) | factor=2 | A=(()) | B=((((())))()) | form=(())(((((())))())) | image=((()))((((())))())
source=(())(((((()))))()) | factor=1 | A=(((((()))))()) | B=() | form=(((((()))))())(()) | image=((((((()))))()))()
source=(())(((((()))))()) | factor=2 | A=(()) | B=((((()))))() | form=(())(((((()))))()) | image=((()))((((()))))()
source=(())(((((())))))() | factor=1 | A=(((((())))))() | B=() | form=(((((())))))()(()) | image=((((((())))))())()
source=(())(((((())))))() | factor=2 | A=(())() | B=((((())))) | form=(())()(((((()))))) | image=((())())((((()))))
source=(())(((((())))))() | factor=3 | A=(())(((((()))))) | B= | form=(())(((((())))))() | image=((())(((((()))))))
source=(())((((()()())))) | factor=1 | A=((((()()())))) | B=() | form=((((()()()))))(()) | image=(((((()()())))))()
source=(())((((()()())))) | factor=2 | A=(()) | B=(((()()()))) | form=(())((((()()())))) | image=((()))(((()()())))
source=(())((((()())()))) | factor=1 | A=((((()())()))) | B=() | form=((((()())())))(()) | image=(((((()())()))))()
source=(())((((()())()))) | factor=2 | A=(()) | B=(((()())())) | form=(())((((()())()))) | image=((()))(((()())()))
source=(())((((()()))())) | factor=1 | A=((((()()))())) | B=() | form=((((()()))()))(()) | image=(((((()()))())))()
source=(())((((()()))())) | factor=2 | A=(()) | B=(((()()))()) | form=(())((((()()))())) | image=((()))(((()()))())
source=(())((((()())))()) | factor=1 | A=((((()())))()) | B=() | form=((((()())))())(()) | image=(((((()())))()))()
source=(())((((()())))()) | factor=2 | A=(()) | B=(((()())))() | form=(())((((()())))()) | image=((()))(((()())))()
source=(())((((()()))))() | factor=1 | A=((((()()))))() | B=() | form=((((()()))))()(()) | image=(((((()()))))())()
source=(())((((()()))))() | factor=2 | A=(())() | B=(((()()))) | form=(())()((((()())))) | image=((())())(((()())))
source=(())((((()()))))() | factor=3 | A=(())((((()())))) | B= | form=(())((((()()))))() | image=((())((((()())))))
source=(())((((())(())))) | factor=1 | A=((((())(())))) | B=() | form=((((())(()))))(()) | image=(((((())(())))))()
source=(())((((())(())))) | factor=2 | A=(()) | B=(((())(()))) | form=(())((((())(())))) | image=((()))(((())(())))
source=(())((((())()()))) | factor=1 | A=((((())()()))) | B=() | form=((((())()())))(()) | image=(((((())()()))))()
source=(())((((())()()))) | factor=2 | A=(()) | B=(((())()())) | form=(())((((())()()))) | image=((()))(((())()()))
source=(())((((())())())) | factor=1 | A=((((())())())) | B=() | form=((((())())()))(()) | image=(((((())())())))()
source=(())((((())())())) | factor=2 | A=(()) | B=(((())())()) | form=(())((((())())())) | image=((()))(((())())())
source=(())((((())()))()) | factor=1 | A=((((())()))()) | B=() | form=((((())()))())(()) | image=(((((())()))()))()
source=(())((((())()))()) | factor=2 | A=(()) | B=(((())()))() | form=(())((((())()))()) | image=((()))(((())()))()
source=(())((((())())))() | factor=1 | A=((((())())))() | B=() | form=((((())())))()(()) | image=(((((())())))())()
source=(())((((())())))() | factor=2 | A=(())() | B=(((())())) | form=(())()((((())()))) | image=((())())(((())()))
source=(())((((())())))() | factor=3 | A=(())((((())()))) | B= | form=(())((((())())))() | image=((())((((())()))))
source=(())((((()))()())) | factor=1 | A=((((()))()())) | B=() | form=((((()))()()))(()) | image=(((((()))()())))()
source=(())((((()))()())) | factor=2 | A=(()) | B=(((()))()()) | form=(())((((()))()())) | image=((()))(((()))()())
source=(())((((()))())()) | factor=1 | A=((((()))())()) | B=() | form=((((()))())())(()) | image=(((((()))())()))()
source=(())((((()))())()) | factor=2 | A=(()) | B=(((()))())() | form=(())((((()))())()) | image=((()))(((()))())()
source=(())((((()))()))() | factor=1 | A=((((()))()))() | B=() | form=((((()))()))()(()) | image=(((((()))()))())()
source=(())((((()))()))() | factor=2 | A=(())() | B=(((()))()) | form=(())()((((()))())) | image=((())())(((()))())
source=(())((((()))()))() | factor=3 | A=(())((((()))())) | B= | form=(())((((()))()))() | image=((())((((()))())))
source=(())((((())))()()) | factor=1 | A=((((())))()()) | B=() | form=((((())))()())(()) | image=(((((())))()()))()
source=(())((((())))()()) | factor=2 | A=(()) | B=(((())))()() | form=(())((((())))()()) | image=((()))(((())))()()
source=(())((((())))())() | factor=1 | A=((((())))())() | B=() | form=((((())))())()(()) | image=(((((())))())())()
source=(())((((())))())() | factor=2 | A=(())() | B=(((())))() | form=(())()((((())))()) | image=((())())(((())))()
source=(())((((())))())() | factor=3 | A=(())((((())))()) | B= | form=(())((((())))())() | image=((())((((())))()))
source=(())((((()))))()() | factor=1 | A=((((()))))()() | B=() | form=((((()))))()()(()) | image=(((((()))))()())()
source=(())((((()))))()() | factor=2 | A=(())()() | B=(((()))) | form=(())()()((((())))) | image=((())()())(((())))
source=(())((((()))))()() | factor=3 | A=(())((((()))))() | B= | form=(())((((()))))()() | image=((())((((()))))())
source=(())((((()))))()() | factor=4 | A=(())((((()))))() | B= | form=(())((((()))))()() | image=((())((((()))))())
source=(())(((()()()()))) | factor=1 | A=(((()()()()))) | B=() | form=(((()()()())))(()) | image=((((()()()()))))()
source=(())(((()()()()))) | factor=2 | A=(()) | B=((()()()())) | form=(())(((()()()()))) | image=((()))((()()()()))
source=(())(((()()())())) | factor=1 | A=(((()()())())) | B=() | form=(((()()())()))(()) | image=((((()()())())))()
source=(())(((()()())())) | factor=2 | A=(()) | B=((()()())()) | form=(())(((()()())())) | image=((()))((()()())())
source=(())(((()()()))()) | factor=1 | A=(((()()()))()) | B=() | form=(((()()()))())(()) | image=((((()()()))()))()
source=(())(((()()()))()) | factor=2 | A=(()) | B=((()()()))() | form=(())(((()()()))()) | image=((()))((()()()))()
source=(())(((()()())))() | factor=1 | A=(((()()())))() | B=() | form=(((()()())))()(()) | image=((((()()())))())()
source=(())(((()()())))() | factor=2 | A=(())() | B=((()()())) | form=(())()(((()()()))) | image=((())())((()()()))
source=(())(((()()())))() | factor=3 | A=(())(((()()()))) | B= | form=(())(((()()())))() | image=((())(((()()()))))
source=(())(((()())(()))) | factor=1 | A=(((()())(()))) | B=() | form=(((()())(())))(()) | image=((((()())(()))))()
source=(())(((()())(()))) | factor=2 | A=(()) | B=((()())(())) | form=(())(((()())(()))) | image=((()))((()())(()))
source=(())(((()())()())) | factor=1 | A=(((()())()())) | B=() | form=(((()())()()))(()) | image=((((()())()())))()
source=(())(((()())()())) | factor=2 | A=(()) | B=((()())()()) | form=(())(((()())()())) | image=((()))((()())()())
source=(())(((()())())()) | factor=1 | A=(((()())())()) | B=() | form=(((()())())())(()) | image=((((()())())()))()
source=(())(((()())())()) | factor=2 | A=(()) | B=((()())())() | form=(())(((()())())()) | image=((()))((()())())()
source=(())(((()())()))() | factor=1 | A=(((()())()))() | B=() | form=(((()())()))()(()) | image=((((()())()))())()
source=(())(((()())()))() | factor=2 | A=(())() | B=((()())()) | form=(())()(((()())())) | image=((())())((()())())
source=(())(((()())()))() | factor=3 | A=(())(((()())())) | B= | form=(())(((()())()))() | image=((())(((()())())))
source=(())(((()()))()()) | factor=1 | A=(((()()))()()) | B=() | form=(((()()))()())(()) | image=((((()()))()()))()
source=(())(((()()))()()) | factor=2 | A=(()) | B=((()()))()() | form=(())(((()()))()()) | image=((()))((()()))()()
source=(())(((()()))())() | factor=1 | A=(((()()))())() | B=() | form=(((()()))())()(()) | image=((((()()))())())()
source=(())(((()()))())() | factor=2 | A=(())() | B=((()()))() | form=(())()(((()()))()) | image=((())())((()()))()
source=(())(((()()))())() | factor=3 | A=(())(((()()))()) | B= | form=(())(((()()))())() | image=((())(((()()))()))
source=(())(((()())))()() | factor=1 | A=(((()())))()() | B=() | form=(((()())))()()(()) | image=((((()())))()())()
source=(())(((()())))()() | factor=2 | A=(())()() | B=((()())) | form=(())()()(((()()))) | image=((())()())((()()))
source=(())(((()())))()() | factor=3 | A=(())(((()())))() | B= | form=(())(((()())))()() | image=((())(((()())))())
source=(())(((()())))()() | factor=4 | A=(())(((()())))() | B= | form=(())(((()())))()() | image=((())(((()())))())
source=(())(((())((())))) | factor=1 | A=(((())((())))) | B=() | form=(((())((()))))(()) | image=((((())((())))))()
source=(())(((())((())))) | factor=2 | A=(()) | B=((())((()))) | form=(())(((())((())))) | image=((())((())))((()))
source=(())(((())(())())) | factor=1 | A=(((())(())())) | B=() | form=(((())(())()))(()) | image=((((())(())())))()
source=(())(((())(())())) | factor=2 | A=(()) | B=((())(())()) | form=(())(((())(())())) | image=((())(())())((()))
source=(())(((())(()))()) | factor=1 | A=(((())(()))()) | B=() | form=(((())(()))())(()) | image=((((())(()))()))()
source=(())(((())(()))()) | factor=2 | A=(()) | B=((())(()))() | form=(())(((())(()))()) | image=((())(()))((()))()
source=(())(((())(())))() | factor=1 | A=(((())(())))() | B=() | form=(((())(())))()(()) | image=((((())(())))())()
source=(())(((())(())))() | factor=2 | A=(())() | B=((())(())) | form=(())()(((())(()))) | image=((())())((())(()))
source=(())(((())(())))() | factor=3 | A=(())(((())(()))) | B= | form=(())(((())(())))() | image=((())(((())(()))))
source=(())(((())()()())) | factor=1 | A=(((())()()())) | B=() | form=(((())()()()))(()) | image=((((())()()())))()
source=(())(((())()()())) | factor=2 | A=(()) | B=((())()()()) | form=(())(((())()()())) | image=((())()()())((()))
source=(())(((())()())()) | factor=1 | A=(((())()())()) | B=() | form=(((())()())())(()) | image=((((())()())()))()
source=(())(((())()())()) | factor=2 | A=(()) | B=((())()())() | form=(())(((())()())()) | image=((())()())((()))()
source=(())(((())()()))() | factor=1 | A=(((())()()))() | B=() | form=(((())()()))()(()) | image=((((())()()))())()
source=(())(((())()()))() | factor=2 | A=(())() | B=((())()()) | form=(())()(((())()())) | image=((())()())((())())
source=(())(((())()()))() | factor=3 | A=(())(((())()())) | B= | form=(())(((())()()))() | image=((())(((())()())))
source=(())(((())())()()) | factor=1 | A=(((())())()()) | B=() | form=(((())())()())(()) | image=((((())())()()))()
source=(())(((())())()()) | factor=2 | A=(()) | B=((())())()() | form=(())(((())())()()) | image=((())())((()))()()
source=(())(((())())())() | factor=1 | A=(((())())())() | B=() | form=(((())())())()(()) | image=((((())())())())()
source=(())(((())())())() | factor=2 | A=(())() | B=((())())() | form=(())()(((())())()) | image=((())())((())())()
source=(())(((())())())() | factor=3 | A=(())(((())())()) | B= | form=(())(((())())())() | image=((())(((())())()))
source=(())(((())()))()() | factor=1 | A=(((())()))()() | B=() | form=(((())()))()()(()) | image=((((())()))()())()
source=(())(((())()))()() | factor=2 | A=(())()() | B=((())()) | form=(())()()(((())())) | image=((())()())((())())
source=(())(((())()))()() | factor=3 | A=(())(((())()))() | B= | form=(())(((())()))()() | image=((())(((())()))())
source=(())(((())()))()() | factor=4 | A=(())(((())()))() | B= | form=(())(((())()))()() | image=((())(((())()))())
source=(())(((()))((()))) | factor=1 | A=(((()))((()))) | B=() | form=(((()))((())))(()) | image=((((()))((()))))()
source=(())(((()))((()))) | factor=2 | A=(()) | B=((()))((())) | form=(())(((()))((()))) | image=((()))((()))((()))
source=(())(((()))()()()) | factor=1 | A=(((()))()()()) | B=() | form=(((()))()()())(()) | image=((((()))()()()))()
source=(())(((()))()()()) | factor=2 | A=(()) | B=((()))()()() | form=(())(((()))()()()) | image=((()))((()))()()()
source=(())(((()))()())() | factor=1 | A=(((()))()())() | B=() | form=(((()))()())()(()) | image=((((()))()())())()
source=(())(((()))()())() | factor=2 | A=(())() | B=((()))()() | form=(())()(((()))()()) | image=((())())((()))()()
source=(())(((()))()())() | factor=3 | A=(())(((()))()()) | B= | form=(())(((()))()())() | image=((())(((()))()()))
source=(())(((()))())()() | factor=1 | A=(((()))())()() | B=() | form=(((()))())()()(()) | image=((((()))())()())()
source=(())(((()))())()() | factor=2 | A=(())()() | B=((()))() | form=(())()()(((()))()) | image=((())()())((()))()
source=(())(((()))())()() | factor=3 | A=(())(((()))())() | B= | form=(())(((()))())()() | image=((())(((()))())())
source=(())(((()))())()() | factor=4 | A=(())(((()))())() | B= | form=(())(((()))())()() | image=((())(((()))())())
source=(())(((())))()()() | factor=1 | A=(((())))()()() | B=() | form=(((())))()()()(()) | image=((((())))()()())()
source=(())(((())))()()() | factor=2 | A=(())()()() | B=((())) | form=(())()()()(((()))) | image=((())()()())((()))
source=(())(((())))()()() | factor=3 | A=(())(((())))()() | B= | form=(())(((())))()()() | image=((())(((())))()())
source=(())(((())))()()() | factor=4 | A=(())(((())))()() | B= | form=(())(((())))()()() | image=((())(((())))()())
source=(())(((())))()()() | factor=5 | A=(())(((())))()() | B= | form=(())(((())))()()() | image=((())(((())))()())
source=(())((()()()()())) | factor=1 | A=((()()()()())) | B=() | form=((()()()()()))(()) | image=(((()()()()())))()
source=(())((()()()()())) | factor=2 | A=(()) | B=(()()()()()) | form=(())((()()()()())) | image=(()()()()())((()))
source=(())((()()()())()) | factor=1 | A=((()()()())()) | B=() | form=((()()()())())(()) | image=(((()()()())()))()
source=(())((()()()())()) | factor=2 | A=(()) | B=(()()()())() | form=(())((()()()())()) | image=(()()()())((()))()
source=(())((()()()()))() | factor=1 | A=((()()()()))() | B=() | form=((()()()()))()(()) | image=(((()()()()))())()
source=(())((()()()()))() | factor=2 | A=(())() | B=(()()()()) | form=(())()((()()()())) | image=(()()()())((())())
source=(())((()()()()))() | factor=3 | A=(())((()()()())) | B= | form=(())((()()()()))() | image=((())((()()()())))
source=(())((()()())(())) | factor=1 | A=((()()())(())) | B=() | form=((()()())(()))(()) | image=(((()()())(())))()
source=(())((()()())(())) | factor=2 | A=(()) | B=(()()())(()) | form=(())((()()())(())) | image=(()()())(())((()))
source=(())((()()())()()) | factor=1 | A=((()()())()()) | B=() | form=((()()())()())(()) | image=(((()()())()()))()
source=(())((()()())()()) | factor=2 | A=(()) | B=(()()())()() | form=(())((()()())()()) | image=(()()())((()))()()
source=(())((()()())())() | factor=1 | A=((()()())())() | B=() | form=((()()())())()(()) | image=(((()()())())())()
source=(())((()()())())() | factor=2 | A=(())() | B=(()()())() | form=(())()((()()())()) | image=(()()())((())())()
source=(())((()()())())() | factor=3 | A=(())((()()())()) | B= | form=(())((()()())())() | image=((())((()()())()))
source=(())((()()()))()() | factor=1 | A=((()()()))()() | B=() | form=((()()()))()()(()) | image=(((()()()))()())()
source=(())((()()()))()() | factor=2 | A=(())()() | B=(()()()) | form=(())()()((()()())) | image=(()()())((())()())
source=(())((()()()))()() | factor=3 | A=(())((()()()))() | B= | form=(())((()()()))()() | image=((())((()()()))())
source=(())((()()()))()() | factor=4 | A=(())((()()()))() | B= | form=(())((()()()))()() | image=((())((()()()))())
source=(())((()())((()))) | factor=1 | A=((()())((()))) | B=() | form=((()())((())))(()) | image=(((()())((()))))()
source=(())((()())((()))) | factor=2 | A=(()) | B=(()())((())) | form=(())((()())((()))) | image=(()())((()))((()))
source=(())((()())(()())) | factor=1 | A=((()())(()())) | B=() | form=((()())(()()))(()) | image=(((()())(()())))()
source=(())((()())(()())) | factor=2 | A=(()) | B=(()())(()()) | form=(())((()())(()())) | image=(()())(()())((()))
source=(())((()())(())()) | factor=1 | A=((()())(())()) | B=() | form=((()())(())())(()) | image=(((()())(())()))()
source=(())((()())(())()) | factor=2 | A=(()) | B=(()())(())() | form=(())((()())(())()) | image=(()())(())((()))()
source=(())((()())(()))() | factor=1 | A=((()())(()))() | B=() | form=((()())(()))()(()) | image=(((()())(()))())()
source=(())((()())(()))() | factor=2 | A=(())() | B=(()())(()) | form=(())()((()())(())) | image=(()())(())((())())
source=(())((()())(()))() | factor=3 | A=(())((()())(())) | B= | form=(())((()())(()))() | image=((())((()())(())))
source=(())((()())()()()) | factor=1 | A=((()())()()()) | B=() | form=((()())()()())(()) | image=(((()())()()()))()
source=(())((()())()()()) | factor=2 | A=(()) | B=(()())()()() | form=(())((()())()()()) | image=(()())((()))()()()
source=(())((()())()())() | factor=1 | A=((()())()())() | B=() | form=((()())()())()(()) | image=(((()())()())())()
source=(())((()())()())() | factor=2 | A=(())() | B=(()())()() | form=(())()((()())()()) | image=(()())((())())()()
source=(())((()())()())() | factor=3 | A=(())((()())()()) | B= | form=(())((()())()())() | image=((())((()())()()))
source=(())((()())())()() | factor=1 | A=((()())())()() | B=() | form=((()())())()()(()) | image=(((()())())()())()
source=(())((()())())()() | factor=2 | A=(())()() | B=(()())() | form=(())()()((()())()) | image=(()())((())()())()
source=(())((()())())()() | factor=3 | A=(())((()())())() | B= | form=(())((()())())()() | image=((())((()())())())
source=(())((()())())()() | factor=4 | A=(())((()())())() | B= | form=(())((()())())()() | image=((())((()())())())
source=(())((()()))()()() | factor=1 | A=((()()))()()() | B=() | form=((()()))()()()(()) | image=(((()()))()()())()
source=(())((()()))()()() | factor=2 | A=(())()()() | B=(()()) | form=(())()()()((()())) | image=(()())((())()()())
source=(())((()()))()()() | factor=3 | A=(())((()()))()() | B= | form=(())((()()))()()() | image=((())((()()))()())
source=(())((()()))()()() | factor=4 | A=(())((()()))()() | B= | form=(())((()()))()()() | image=((())((()()))()())
source=(())((()()))()()() | factor=5 | A=(())((()()))()() | B= | form=(())((()()))()()() | image=((())((()()))()())
source=(())((())(((())))) | factor=1 | A=((())(((())))) | B=() | form=((())(((()))))(()) | image=(((())(((())))))()
source=(())((())(((())))) | factor=2 | A=(()) | B=(())(((()))) | form=(())((())(((())))) | image=(())((()))(((())))
source=(())((())((()()))) | factor=1 | A=((())((()()))) | B=() | form=((())((()())))(()) | image=(((())((()()))))()
source=(())((())((()()))) | factor=2 | A=(()) | B=(())((()())) | form=(())((())((()()))) | image=(())((()))((()()))
source=(())((())((())())) | factor=1 | A=((())((())())) | B=() | form=((())((())()))(()) | image=(((())((())())))()
source=(())((())((())())) | factor=2 | A=(()) | B=(())((())()) | form=(())((())((())())) | image=(())((())())((()))
source=(())((())((()))()) | factor=1 | A=((())((()))()) | B=() | form=((())((()))())(()) | image=(((())((()))()))()
source=(())((())((()))()) | factor=2 | A=(()) | B=(())((()))() | form=(())((())((()))()) | image=(())((()))((()))()
source=(())((())((())))() | factor=1 | A=((())((())))() | B=() | form=((())((())))()(()) | image=(((())((())))())()
source=(())((())((())))() | factor=2 | A=(())() | B=(())((())) | form=(())()((())((()))) | image=(())((())())((()))
source=(())((())((())))() | factor=3 | A=(())((())((()))) | B= | form=(())((())((())))() | image=((())((())((()))))
source=(())((())(())(())) | factor=1 | A=((())(())(())) | B=() | form=((())(())(()))(()) | image=(((())(())(())))()
source=(())((())(())(())) | factor=2 | A=(()) | B=(())(())(()) | form=(())((())(())(())) | image=(())(())(())((()))
source=(())((())(())()()) | factor=1 | A=((())(())()()) | B=() | form=((())(())()())(()) | image=(((())(())()()))()
source=(())((())(())()()) | factor=2 | A=(()) | B=(())(())()() | form=(())((())(())()()) | image=(())(())((()))()()
source=(())((())(())())() | factor=1 | A=((())(())())() | B=() | form=((())(())())()(()) | image=(((())(())())())()
source=(())((())(())())() | factor=2 | A=(())() | B=(())(())() | form=(())()((())(())()) | image=(())(())((())())()
source=(())((())(())())() | factor=3 | A=(())((())(())()) | B= | form=(())((())(())())() | image=((())((())(())()))
source=(())((())(()))()() | factor=1 | A=((())(()))()() | B=() | form=((())(()))()()(()) | image=(((())(()))()())()
source=(())((())(()))()() | factor=2 | A=(())()() | B=(())(()) | form=(())()()((())(())) | image=(())(())((())()())
source=(())((())(()))()() | factor=3 | A=(())((())(()))() | B= | form=(())((())(()))()() | image=((())((())(()))())
source=(())((())(()))()() | factor=4 | A=(())((())(()))() | B= | form=(())((())(()))()() | image=((())((())(()))())
source=(())((())()()()()) | factor=1 | A=((())()()()()) | B=() | form=((())()()()())(()) | image=(((())()()()()))()
source=(())((())()()()()) | factor=2 | A=(()) | B=(())()()()() | form=(())((())()()()()) | image=(())((()))()()()()
source=(())((())()()())() | factor=1 | A=((())()()())() | B=() | form=((())()()())()(()) | image=(((())()()())())()
source=(())((())()()())() | factor=2 | A=(())() | B=(())()()() | form=(())()((())()()()) | image=(())((())())()()()
source=(())((())()()())() | factor=3 | A=(())((())()()()) | B= | form=(())((())()()())() | image=((())((())()()()))
source=(())((())()())()() | factor=1 | A=((())()())()() | B=() | form=((())()())()()(()) | image=(((())()())()())()
source=(())((())()())()() | factor=2 | A=(())()() | B=(())()() | form=(())()()((())()()) | image=(())((())()())()() | fixed
source=(())((())()())()() | factor=3 | A=(())((())()())() | B= | form=(())((())()())()() | image=((())((())()())())
source=(())((())()())()() | factor=4 | A=(())((())()())() | B= | form=(())((())()())()() | image=((())((())()())())
source=(())((())())((())) | factor=1 | A=((())())((())) | B=() | form=((())())((()))(()) | image=(((())())((())))()
source=(())((())())((())) | factor=2 | A=(())((())) | B=(())() | form=(())((()))((())()) | image=(())((())((())))()
source=(())((())())((())) | factor=3 | A=(())((())()) | B=(()) | form=(())((())())((())) | image=(())((())((())()))
source=(())((())())()()() | factor=1 | A=((())())()()() | B=() | form=((())())()()()(()) | image=(((())())()()())()
source=(())((())())()()() | factor=2 | A=(())()()() | B=(())() | form=(())()()()((())()) | image=(())((())()()())()
source=(())((())())()()() | factor=3 | A=(())((())())()() | B= | form=(())((())())()()() | image=((())((())())()())
source=(())((())())()()() | factor=4 | A=(())((())())()() | B= | form=(())((())())()()() | image=((())((())())()())
source=(())((())())()()() | factor=5 | A=(())((())())()() | B= | form=(())((())())()()() | image=((())((())())()())
source=(())((()))(((()))) | factor=1 | A=((()))(((()))) | B=() | form=((()))(((())))(()) | image=(((()))(((()))))()
source=(())((()))(((()))) | factor=2 | A=(())(((()))) | B=(()) | form=(())(((())))((())) | image=(())((())(((()))))
source=(())((()))(((()))) | factor=3 | A=(())((())) | B=((())) | form=(())((()))(((()))) | image=((())((())))((()))
source=(())((()))((()())) | factor=1 | A=((()))((()())) | B=() | form=((()))((()()))(()) | image=(((()))((()())))()
source=(())((()))((()())) | factor=2 | A=(())((()())) | B=(()) | form=(())((()()))((())) | image=(())((())((()())))
source=(())((()))((()())) | factor=3 | A=(())((())) | B=(()()) | form=(())((()))((()())) | image=(()())((())((())))
source=(())((()))((()))() | factor=1 | A=((()))((()))() | B=() | form=((()))((()))()(()) | image=(((()))((()))())()
source=(())((()))((()))() | factor=2 | A=(())((()))() | B=(()) | form=(())((()))()((())) | image=(())((())((()))())
source=(())((()))((()))() | factor=3 | A=(())((()))() | B=(()) | form=(())((()))()((())) | image=(())((())((()))())
source=(())((()))((()))() | factor=4 | A=(())((()))((())) | B= | form=(())((()))((()))() | image=((())((()))((())))
source=(())((()))()()()() | factor=1 | A=((()))()()()() | B=() | form=((()))()()()()(()) | image=(((()))()()()())()
source=(())((()))()()()() | factor=2 | A=(())()()()() | B=(()) | form=(())()()()()((())) | image=(())((())()()()())
source=(())((()))()()()() | factor=3 | A=(())((()))()()() | B= | form=(())((()))()()()() | image=((())((()))()()())
source=(())((()))()()()() | factor=4 | A=(())((()))()()() | B= | form=(())((()))()()()() | image=((())((()))()()())
source=(())((()))()()()() | factor=5 | A=(())((()))()()() | B= | form=(())((()))()()()() | image=((())((()))()()())
source=(())((()))()()()() | factor=6 | A=(())((()))()()() | B= | form=(())((()))()()()() | image=((())((()))()()())
source=(())(())((((())))) | factor=1 | A=(())((((())))) | B=() | form=(())((((()))))(()) | image=((())((((())))))()
source=(())(())((((())))) | factor=2 | A=(())((((())))) | B=() | form=(())((((()))))(()) | image=((())((((())))))()
source=(())(())((((())))) | factor=3 | A=(())(()) | B=(((()))) | form=(())(())((((())))) | image=((())(()))(((())))
source=(())(())(((()()))) | factor=1 | A=(())(((()()))) | B=() | form=(())(((()())))(()) | image=((())(((()()))))()
source=(())(())(((()()))) | factor=2 | A=(())(((()()))) | B=() | form=(())(((()())))(()) | image=((())(((()()))))()
source=(())(())(((()()))) | factor=3 | A=(())(()) | B=((()())) | form=(())(())(((()()))) | image=((())(()))((()()))
source=(())(())(((())())) | factor=1 | A=(())(((())())) | B=() | form=(())(((())()))(()) | image=((())(((())())))()
source=(())(())(((())())) | factor=2 | A=(())(((())())) | B=() | form=(())(((())()))(()) | image=((())(((())())))()
source=(())(())(((())())) | factor=3 | A=(())(()) | B=((())()) | form=(())(())(((())())) | image=((())())((())(()))
source=(())(())(((()))()) | factor=1 | A=(())(((()))()) | B=() | form=(())(((()))())(()) | image=((())(((()))()))()
source=(())(())(((()))()) | factor=2 | A=(())(((()))()) | B=() | form=(())(((()))())(()) | image=((())(((()))()))()
source=(())(())(((()))()) | factor=3 | A=(())(()) | B=((()))() | form=(())(())(((()))()) | image=((())(()))((()))()
source=(())(())(((())))() | factor=1 | A=(())(((())))() | B=() | form=(())(((())))()(()) | image=((())(((())))())()
source=(())(())(((())))() | factor=2 | A=(())(((())))() | B=() | form=(())(((())))()(()) | image=((())(((())))())()
source=(())(())(((())))() | factor=3 | A=(())(())() | B=((())) | form=(())(())()(((()))) | image=((())(())())((()))
source=(())(())(((())))() | factor=4 | A=(())(())(((()))) | B= | form=(())(())(((())))() | image=((())(())(((()))))
source=(())(())((()()())) | factor=1 | A=(())((()()())) | B=() | form=(())((()()()))(()) | image=((())((()()())))()
source=(())(())((()()())) | factor=2 | A=(())((()()())) | B=() | form=(())((()()()))(()) | image=((())((()()())))()
source=(())(())((()()())) | factor=3 | A=(())(()) | B=(()()()) | form=(())(())((()()())) | image=(()()())((())(()))
source=(())(())((()())()) | factor=1 | A=(())((()())()) | B=() | form=(())((()())())(()) | image=((())((()())()))()
source=(())(())((()())()) | factor=2 | A=(())((()())()) | B=() | form=(())((()())())(()) | image=((())((()())()))()
source=(())(())((()())()) | factor=3 | A=(())(()) | B=(()())() | form=(())(())((()())()) | image=(()())((())(()))()
source=(())(())((()()))() | factor=1 | A=(())((()()))() | B=() | form=(())((()()))()(()) | image=((())((()()))())()
source=(())(())((()()))() | factor=2 | A=(())((()()))() | B=() | form=(())((()()))()(()) | image=((())((()()))())()
source=(())(())((()()))() | factor=3 | A=(())(())() | B=(()()) | form=(())(())()((()())) | image=(()())((())(())())
source=(())(())((()()))() | factor=4 | A=(())(())((()())) | B= | form=(())(())((()()))() | image=((())(())((()())))
source=(())(())((())(())) | factor=1 | A=(())((())(())) | B=() | form=(())((())(()))(()) | image=((())((())(())))()
source=(())(())((())(())) | factor=2 | A=(())((())(())) | B=() | form=(())((())(()))(()) | image=((())((())(())))()
source=(())(())((())(())) | factor=3 | A=(())(()) | B=(())(()) | form=(())(())((())(())) | image=(())(())((())(())) | fixed
source=(())(())((())()()) | factor=1 | A=(())((())()()) | B=() | form=(())((())()())(()) | image=((())((())()()))()
source=(())(())((())()()) | factor=2 | A=(())((())()()) | B=() | form=(())((())()())(()) | image=((())((())()()))()
source=(())(())((())()()) | factor=3 | A=(())(()) | B=(())()() | form=(())(())((())()()) | image=(())((())(()))()()
source=(())(())((())())() | factor=1 | A=(())((())())() | B=() | form=(())((())())()(()) | image=((())((())())())()
source=(())(())((())())() | factor=2 | A=(())((())())() | B=() | form=(())((())())()(()) | image=((())((())())())()
source=(())(())((())())() | factor=3 | A=(())(())() | B=(())() | form=(())(())()((())()) | image=(())((())(())())()
source=(())(())((())())() | factor=4 | A=(())(())((())()) | B= | form=(())(())((())())() | image=((())(())((())()))
source=(())(())((()))()() | factor=1 | A=(())((()))()() | B=() | form=(())((()))()()(()) | image=((())((()))()())()
source=(())(())((()))()() | factor=2 | A=(())((()))()() | B=() | form=(())((()))()()(()) | image=((())((()))()())()
source=(())(())((()))()() | factor=3 | A=(())(())()() | B=(()) | form=(())(())()()((())) | image=(())((())(())()())
source=(())(())((()))()() | factor=4 | A=(())(())((()))() | B= | form=(())(())((()))()() | image=((())(())((()))())
source=(())(())((()))()() | factor=5 | A=(())(())((()))() | B= | form=(())(())((()))()() | image=((())(())((()))())
source=(())(())(())((())) | factor=1 | A=(())(())((())) | B=() | form=(())(())((()))(()) | image=((())(())((())))()
source=(())(())(())((())) | factor=2 | A=(())(())((())) | B=() | form=(())(())((()))(()) | image=((())(())((())))()
source=(())(())(())((())) | factor=3 | A=(())(())((())) | B=() | form=(())(())((()))(()) | image=((())(())((())))()
source=(())(())(())((())) | factor=4 | A=(())(())(()) | B=(()) | form=(())(())(())((())) | image=(())((())(())(()))
source=(())(())(())(())() | factor=1 | A=(())(())(())() | B=() | form=(())(())(())()(()) | image=((())(())(())())()
source=(())(())(())(())() | factor=2 | A=(())(())(())() | B=() | form=(())(())(())()(()) | image=((())(())(())())()
source=(())(())(())(())() | factor=3 | A=(())(())(())() | B=() | form=(())(())(())()(()) | image=((())(())(())())()
source=(())(())(())(())() | factor=4 | A=(())(())(())() | B=() | form=(())(())(())()(()) | image=((())(())(())())()
source=(())(())(())(())() | factor=5 | A=(())(())(())(()) | B= | form=(())(())(())(())() | image=((())(())(())(()))
source=(())(())(())()()() | factor=1 | A=(())(())()()() | B=() | form=(())(())()()()(()) | image=((())(())()()())()
source=(())(())(())()()() | factor=2 | A=(())(())()()() | B=() | form=(())(())()()()(()) | image=((())(())()()())()
source=(())(())(())()()() | factor=3 | A=(())(())()()() | B=() | form=(())(())()()()(()) | image=((())(())()()())()
source=(())(())(())()()() | factor=4 | A=(())(())(())()() | B= | form=(())(())(())()()() | image=((())(())(())()())
source=(())(())(())()()() | factor=5 | A=(())(())(())()() | B= | form=(())(())(())()()() | image=((())(())(())()())
source=(())(())(())()()() | factor=6 | A=(())(())(())()() | B= | form=(())(())(())()()() | image=((())(())(())()())
source=(())(())()()()()() | factor=1 | A=(())()()()()() | B=() | form=(())()()()()()(()) | image=((())()()()()())()
source=(())(())()()()()() | factor=2 | A=(())()()()()() | B=() | form=(())()()()()()(()) | image=((())()()()()())()
source=(())(())()()()()() | factor=3 | A=(())(())()()()() | B= | form=(())(())()()()()() | image=((())(())()()()())
source=(())(())()()()()() | factor=4 | A=(())(())()()()() | B= | form=(())(())()()()()() | image=((())(())()()()())
source=(())(())()()()()() | factor=5 | A=(())(())()()()() | B= | form=(())(())()()()()() | image=((())(())()()()())
source=(())(())()()()()() | factor=6 | A=(())(())()()()() | B= | form=(())(())()()()()() | image=((())(())()()()())
source=(())(())()()()()() | factor=7 | A=(())(())()()()() | B= | form=(())(())()()()()() | image=((())(())()()()())
source=(())()()()()()()() | factor=1 | A=()()()()()()() | B=() | form=()()()()()()()(()) | image=(()()()()()()())()
source=(())()()()()()()() | factor=2 | A=(())()()()()()() | B= | form=(())()()()()()()() | image=((())()()()()()())
source=(())()()()()()()() | factor=3 | A=(())()()()()()() | B= | form=(())()()()()()()() | image=((())()()()()()())
source=(())()()()()()()() | factor=4 | A=(())()()()()()() | B= | form=(())()()()()()()() | image=((())()()()()()())
source=(())()()()()()()() | factor=5 | A=(())()()()()()() | B= | form=(())()()()()()()() | image=((())()()()()()())
source=(())()()()()()()() | factor=6 | A=(())()()()()()() | B= | form=(())()()()()()()() | image=((())()()()()()())
source=(())()()()()()()() | factor=7 | A=(())()()()()()() | B= | form=(())()()()()()()() | image=((())()()()()()())
source=(())()()()()()()() | factor=8 | A=(())()()()()()() | B= | form=(())()()()()()()() | image=((())()()()()()())
source=()()()()()()()()() | factor=1 | A=()()()()()()()() | B= | form=()()()()()()()()() | image=(()()()()()()()())
source=()()()()()()()()() | factor=2 | A=()()()()()()()() | B= | form=()()()()()()()()() | image=(()()()()()()()())
source=()()()()()()()()() | factor=3 | A=()()()()()()()() | B= | form=()()()()()()()()() | image=(()()()()()()()())
source=()()()()()()()()() | factor=4 | A=()()()()()()()() | B= | form=()()()()()()()()() | image=(()()()()()()()())
source=()()()()()()()()() | factor=5 | A=()()()()()()()() | B= | form=()()()()()()()()() | image=(()()()()()()()())
source=()()()()()()()()() | factor=6 | A=()()()()()()()() | B= | form=()()()()()()()()() | image=(()()()()()()()())
source=()()()()()()()()() | factor=7 | A=()()()()()()()() | B= | form=()()()()()()()()() | image=(()()()()()()()())
source=()()()()()()()()() | factor=8 | A=()()()()()()()() | B= | form=()()()()()()()()() | image=(()()()()()()()())
source=()()()()()()()()() | factor=9 | A=()()()()()()()() | B= | form=()()()()()()()()() | image=(()()()()()()()())
```

