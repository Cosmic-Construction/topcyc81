# topcyc81 - Topologically Distinct Sets of Non-intersecting Circles

Implementation of algorithms for counting topologically distinct arrangements of circles in the plane, based on the paper ["Topologically Distinct Sets of Non-intersecting Circles in the Plane"](https://arxiv.org/abs/1603.00077) (arXiv:1603.00077).

## Overview

This project provides computational tools to analyze and count different topological configurations of circles in the plane under various intersection constraints. The implementation explores three scenarios:

1. **Non-intersecting circles**: Circles are completely separated (nested or disjoint)
2. **Pairs may intersect**: At most 2 circles can intersect at any point
3. **Triples may intersect**: At most 3 circles can intersect at any point

## Mathematical Background

The problem of counting topologically distinct circle arrangements is related to:
- **Catalan numbers**: Count non-intersecting nested structures
- **Matching forests**: Represent intersection patterns as rooted forests
- **Generating functions**: Encode the counting sequences
- **Recurrence relations**: Define recursive structure of the counts

### Key Results

For *n* circles:
- **Non-intersecting**: Follows the Catalan sequence (1, 1, 2, 5, 14, 42, 132, ...)
- **Pairs intersecting**: Enhanced sequence (1, 1, 2, 6, 19, 64, 225, 816, ...)
- **Triples intersecting**: Further enhanced (1, 1, 2, 8, 27, 99, 378, 1484, ...)

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
- Counts for non-intersecting circles (Catalan numbers)
- Counts for case (i): pairs may intersect
- Counts for case (ii): triples may intersect
- Generating function coefficients

### Using as a Module

```python
from circle_topology import CircleTopology

topology = CircleTopology()

# Count non-intersecting arrangements
count = topology.non_intersecting_circles(5)  # Returns 42

# Count when pairs may intersect
count = topology.pairs_may_intersect(5)  # Returns 64

# Count when triples may intersect
count = topology.triples_may_intersect(5)  # Returns 99

# Generate sequences
sequence = topology.generate_sequence(10, 'pairs')
print(sequence)  # [1, 1, 2, 6, 19, 64, 225, 816, 3031, 11473, 44096]

# Get generating function coefficients
coeffs = topology.generating_function_coefficients(7, 'triples')
print(coeffs)  # {0: 1, 1: 1, 2: 2, 3: 8, 4: 27, 5: 99, 6: 378, 7: 1484}
```

## Running Tests

```bash
python test_circle_topology.py
```

The test suite includes:
- Verification of Catalan number computation
- Tests for base cases and recurrence relations
- Consistency checks across different methods
- Validation that intersection freedom increases counts

## API Reference

### CircleTopology Class

#### Methods

- **`catalan_number(n: int) -> int`**: Compute the n-th Catalan number
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