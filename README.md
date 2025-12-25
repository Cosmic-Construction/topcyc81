# topcyc81 - Topologically Distinct Sets of Non-intersecting Circles

Implementation of algorithms for counting topologically distinct arrangements of circles in the plane, based on the paper ["Topologically Distinct Sets of Non-intersecting Circles in the Plane"](https://arxiv.org/abs/1603.00077) by Richard J. Mathar (arXiv:1603.00077).

## Overview

This project provides computational tools to analyze and count different topological configurations of circles in the plane under various intersection constraints. The implementation explores:

1. **Non-intersecting circles**: Circles are completely separated (nested or disjoint) - corresponds to rooted trees
2. **Pairs may intersect**: Exactly one pair of circles intersects at two points
3. **Triples may intersect**: Up to three circles can mutually intersect
4. **Dimensional progression**: Analysis of how surface topology constrains non-crossing partitions across dimensions (1D→2D→3D→4D)

## Mathematical Background

The problem of counting topologically distinct circle arrangements is related to:
- **Catalan numbers (OEIS A000108)**: All labeled/ordered arrangements
- **Rooted trees (OEIS A000081)**: Count non-intersecting nested structures (quotient by ordering)
- **Unrooted trees (OEIS A000055)**: Sphere surface embeddings (quotient by root choice/flip transformations)
- **Matching forests**: Represent intersection patterns as rooted forests
- **Generating functions**: Encode the counting sequences
- **Recurrence relations**: Define recursive structure of the counts

### Dimensional Progression

The repository now includes analysis of how circle topologies reduce as we move through dimensions:

| N | 1D Linear<br/>(Catalan) | 2D Planar<br/>(Rooted) | 3D Sphere<br/>(Unrooted) | 4D Hypersurface<br/>(Theoretical) |
|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 1 | 1 |
| 3 | 5 | 4 | 2 | 1 |
| 4 | 14 | 9 | 3 | 2 |
| 5 | 42 | 20 | 6 | 3 |
| 6 | 132 | 48 | 11 | 6 |
| 7 | 429 | 115 | 23 | 11 |
| 8 | 1430 | 286 | 47 | 23 |
| 9 | 4862 | 719 | 106 | 44 |

**Progression explanation:**
- **1D → 2D**: Forget order (commutative property)
- **2D → 3D**: Forget roots (flip transformations on sphere)
- **3D → 4D**: Quotient by centrosymmetry and full spatial rotations

### Key Results

For *n* circles:
- **Non-intersecting (|C_n|)**: Rooted trees sequence (1, 1, 2, 4, 9, 20, 48, 115, 286, 719, ...)  [OEIS A000081]
- **Sphere clusters**: Unrooted trees sequence (1, 1, 1, 2, 3, 6, 11, 23, 47, 106, ...) [OEIS A000055]
- **Pairs intersecting (|X_n|)**: (0, 1, 4, 15, 50, 162, 506, 1558, 4727, 14227, ...) [OEIS A261070]
- **Triples intersecting (|³X_n|)**: (0, 1, 3, 14, 61, 252, 1019, 4127, 17242, 74007, ...) [OEIS A250001]

As expected, allowing more complex intersections increases the number of distinct topologies.

## Installation

No external dependencies are required. The implementation uses only Python standard library.

```bash
git clone https://github.com/Cosmic-Construction/topcyc81.git
cd topcyc81
```

## Usage

### Running the Main Program

```bash
python circle_topology.py
```

This will display:
- **Dimensional progression table** (1D→2D→3D→4D)
- Counts for non-intersecting circles
- Counts for case (i): pairs may intersect
- Counts for case (ii): triples may intersect
- Generating function coefficients

### Using as a Module

```python
from circle_topology import CircleTopology

topology = CircleTopology()

# Count non-intersecting arrangements
count = topology.non_intersecting_circles(5)  # Returns 42

# Count non-intersecting arrangements (2D planar)
count = topology.non_intersecting_circles(5)  # Returns 20

# Count sphere surface clusters (3D)
count = topology.sphere_surface_clusters(5)  # Returns 6

# Count 4D hypersphere clusters (theoretical)
count = topology.hypersphere_4d_clusters(5)  # Returns 3

# Count when pairs may intersect
count = topology.pairs_may_intersect(5)  # Returns 64

# Count when triples may intersect
count = topology.triples_may_intersect(5)  # Returns 69

# Generate dimensional progression
for n in range(10):
    cat = topology.catalan_number(n)
    planar = topology.non_intersecting_circles(n)
    sphere = topology.sphere_surface_clusters(n)
    hyper = topology.hypersphere_4d_clusters(n)
    print(f"n={n}: {cat} → {planar} → {sphere} → {hyper}")

# Generate sequences
sequence = topology.generate_sequence(10, 'pairs')
print(sequence)  # [1, 1, 2, 6, 19, 64, 225, 816, 3031, 11473, 44096]

# Get generating function coefficients
coeffs = topology.generating_function_coefficients(7, 'triples')
print(coeffs)  # {0: 1, 1: 1, 2: 2, 3: 6, 4: 20, 5: 69, 6: 248, 7: 919}
```

## Running Tests

```bash
python test_circle_topology.py
```

The test suite includes:
- Verification of Catalan number computation
- Tests for rooted and unrooted trees (OEIS A000081, A000055)
- Dimensional progression validation (1D→2D→3D→4D)
- Tests for base cases and recurrence relations
- Consistency checks across different methods
- Validation that intersection freedom increases counts

## API Reference

### CircleTopology Class

#### Methods

- **`catalan_number(n: int) -> int`**: Compute the n-th Catalan number (1D linear arrangements)
- **`rooted_trees(n: int) -> int`**: Compute OEIS A000081 (rooted trees with n nodes)
- **`unrooted_trees(n: int) -> int`**: Compute OEIS A000055 (unrooted trees with n nodes)
- **`non_intersecting_circles(n: int) -> int`**: Count 2D planar topologies with no intersections
- **`sphere_surface_clusters(n: int) -> int`**: Count 3D sphere surface equivalence classes
- **`hypersphere_4d_clusters(n: int) -> int`**: Count 4D hypersphere surface equivalence classes (theoretical)
- **`non_intersecting_circles(n: int) -> int`**: Count topologies with no intersections
- **`pairs_may_intersect(n: int) -> int`**: Count topologies where pairs may intersect
- **`triples_may_intersect(n: int) -> int`**: Count topologies where triples may intersect
- **`generate_sequence(max_n: int, intersection_type: str) -> List[int]`**: Generate counting sequence
- **`generating_function_coefficients(max_n: int, intersection_type: str) -> Dict[int, int]`**: Get generating function coefficients

#### Parameters

- `intersection_type`: One of `'none'`, `'pairs'`, or `'triples'`

## Example Output

```
Topologically Distinct Sets of Non-intersecting Circles
============================================================

Case: Non-intersecting circles (Catalan numbers)
------------------------------------------------------------
n= 0:      1 distinct topologies
n= 1:      1 distinct topologies
n= 2:      2 distinct topologies
n= 3:      5 distinct topologies
n= 4:     14 distinct topologies
...

Case (i): Pairs of circles may intersect
------------------------------------------------------------
n= 0:      1 distinct topologies
n= 1:      1 distinct topologies
n= 2:      2 distinct topologies
n= 3:      6 distinct topologies
n= 4:     19 distinct topologies
...

Case (ii): Triples of circles may intersect
------------------------------------------------------------
n= 0:      1 distinct topologies
n= 1:      1 distinct topologies
n= 2:      2 distinct topologies
n= 3:      8 distinct topologies
n= 4:     27 distinct topologies
...
```

## Algorithm Details

### Recurrence Relations

The implementation uses recursive decomposition:

1. **Catalan numbers** (non-intersecting):
   ```
   C(n) = Σ C(i) × C(n-1-i) for i=0 to n-1
   ```

2. **Pairs intersecting**: Extends the Catalan recurrence by adding configurations where pairs form intersecting lens-shaped regions

3. **Triples intersecting**: Further extends by including configurations where three circles create a central intersection region

### Caching

All recursive functions use `@lru_cache` for memoization, ensuring efficient computation even for larger values of n.

## References

- Original paper: [arXiv:1603.00077](https://arxiv.org/abs/1603.00077) - "Topologically Distinct Sets of Non-intersecting Circles in the Plane"
- Catalan numbers: [OEIS A000108](https://oeis.org/A000108)
- Related to matching forests and nested structures in combinatorics

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs, feature requests, or improvements to the algorithms.