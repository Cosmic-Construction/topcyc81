# Implementation Summary

## Overview

This repository implements algorithms from the paper ["Topologically Distinct Sets of Non-intersecting Circles in the Plane"](https://arxiv.org/abs/1603.00077) by Richard J. Mathar.

## Mathematical Framework

### Non-Intersecting Circles (Section 2)

Non-intersecting circles in the plane correspond to **rooted trees** (OEIS A000081). For n circles, the count is given by the rooted tree recurrence:

- a(0) = 0, a(1) = 1
- a(n) = (1/(n-1)) × Σ(i=1 to n-1) a(i) × Σ(d|n-i) d × a(d)

**Sequence**: 0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766...

The generating function satisfies:
```
C(z) = exp(Σ(j≥1) z^j × C(z^j) / j)
```

### Sphere Embedding (Section 2.2)

When circles are embedded on a sphere surface instead of the plane, topologies that differ by a "flip transformation" become equivalent. This reduces the count:

- n=4 circles: 9 planar topologies → 3 sphere topologies
- n=5 circles: 20 planar topologies → 6 sphere topologies  
- n=6 circles: 48 planar topologies → 11 sphere topologies

These sphere counts follow OEIS A000055 (unlabeled trees).

### Pairs Intersecting (Section 4)

When exactly one pair of circles may intersect at two points, the count follows different recurrences involving the distribution of circles in 5 regions created by the intersecting pair.

**Sequence |X_n|**: 0, 1, 4, 15, 50, 162, 506, 1558, 4727, 14227... (OEIS A261070)

### Triples Intersecting (Section 6)

When up to three circles may mutually intersect, six new fundamental topologies appear beyond the pair intersection case. The analysis examines symmetry properties of regions.

**Sequence |³X_n|**: 0, 1, 3, 14, 61, 252, 1019, 4127, 17242, 74007... (OEIS A250001)

## Files in This Repository

### Core Implementation

- **`circle_topology.py`**: Main implementation
  - `rooted_trees(n)`: Computes OEIS A000081
  - `catalan_number(n)`: Computes Catalan numbers (for reference)
  - `non_intersecting_circles(n)`: Maps to rooted_trees(n+1)
  - `pairs_may_intersect(n)`: Recursive counting for pair intersections
  - `triples_may_intersect(n)`: Recursive counting for triple intersections
  - Generating function coefficient computation

- **`flip_transforms.py`**: Flip transformation analysis
  - `CircleExpression`: Class for manipulating parenthesis expressions
  - `find_flip_clusters()`: Groups topologies by flip equivalence
  - Visualization utilities for understanding sphere embeddings

### Testing and Documentation

- **`test_circle_topology.py`**: Comprehensive test suite
  - 13 unit tests covering all major functions
  - Validation against known OEIS sequences
  - Recurrence relation tests

- **`README.md`**: User documentation with examples

- **`requirements.txt`**: No external dependencies (Python stdlib only)

## Key Algorithms Implemented

### 1. Rooted Trees (A000081)

```python
def rooted_trees(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1
    
    result = 0
    for i in range(1, n):
        divisor_sum = 0
        remainder = n - i
        for d in range(1, remainder + 1):
            if remainder % d == 0:
                divisor_sum += d * rooted_trees(d)
        result += rooted_trees(i) * divisor_sum
    
    return result // (n - 1)
```

### 2. Pairs Intersecting

Uses recursive decomposition considering:
- Circles can be wrapped by a non-intersecting circle
- Circles can be inside one of 3 regions of an intersecting pair
- Symmetry constraints on equivalent arrangements

### 3. Triples Intersecting

Extends pairs with 6 new fundamental topologies:
1. RGB spot diagram (3 circles, all mutually intersecting)
2. Torn version (3 circles, pairwise intersecting, no common center)
3. Linear chain
4. Compressed chain
5. Shrunk center variation
6. Asymmetric bundle

Each has specific symmetry groups (C₂, S₃, etc.)

## Usage Examples

```python
from circle_topology import CircleTopology

# Non-intersecting circles
print(CircleTopology.non_intersecting_circles(5))  # Output: 20

# Pairs may intersect  
print(CircleTopology.pairs_may_intersect(5))  # Output: 64

# Triples may intersect
print(CircleTopology.triples_may_intersect(5))  # Output: 252

# Generate sequence
seq = CircleTopology.generate_sequence(10, 'none')
print(seq)  # [1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842]
```

## Testing

Run the test suite:
```bash
python test_circle_topology.py
```

All 13 tests validate:
- Correct rooted tree computation
- Catalan number accuracy
- Non-intersecting circle counts
- Pairs and triples intersection logic
- Sequence consistency
- Recurrence relations

## References

1. Mathar, R. J. (2016). "Topologically Distinct Sets of Non-intersecting Circles in the Plane." arXiv:1603.00077

2. OEIS Sequences:
   - A000081: Number of unlabeled rooted trees
   - A000108: Catalan numbers
   - A261070: Circles with one pair intersecting
   - A250001: Circles with triple intersections allowed

3. Related combinatorics:
   - Dyck paths and nested parentheses
   - Cycle indices and P<C3><B3>lya enumeration theorem
   - Rooted forests and matching theory

## Future Work

Potential extensions:
- Complete flip transformation cluster analysis for arbitrary n
- Implement exact formulas from the paper's generating functions
- Visualization of circle arrangements
- Higher-order intersections (4+ circles)
- Computational verification of OEIS sequences for larger n

## License

GNU Affero General Public License v3.0 (AGPL-3.0)
