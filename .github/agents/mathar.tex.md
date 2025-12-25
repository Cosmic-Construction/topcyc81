---
name: "mathar.tex"
description: "Topologically Distinct Sets of Non-intersecting Circles in the Plane"
---

# Mathematical Reference for Circle Topology Paper

## Core Concepts

**Well-formed Parentheses**: Strings where opening parentheses = closing parentheses, and running count of opening ≥ closing when parsed left-to-right. Sets $\mathbb{P}_N$ contain all well-formed expressions with N pairs.

**Commutative Case**: When order doesn't matter, get reduced sets $\mathbb{C}_N$ (non-intersecting circles in plane). Connection: nested parentheses → circles on line → planar circle topologies.

## Key Results

### 1. Non-Intersecting Circles (Section 2)
- Count: $|\mathbb{C}_N|$ = rooted trees [OEIS A000081]
- Sequence: 1,1,2,4,9,20,48,115,286,719,1842,4766,12486,...
- Sphere embeddings: Related to A000055 (unrooted trees)

**Recurrence**:
```
|C_N^(1)| = |C_{N-1}|
|C_N^(f)| = sum over partitions of (N-1) with f-1 parts
```

**Generating Function**:
```
C(z) = 1 + sum_{N≥1} |C_N| z^N
     = exp(sum_{j≥1} z^j C(z^j)/j)
```

### 2. Pairs May Intersect (Section 4)
- Fundamental topology: Two circles intersect at 2 points (lens shape)
- Count: $|\mathbb{X}_N|$ [OEIS A261070]
- Sequence: 0,1,4,15,50,162,506,1558,4727,14227,...

**Core Formula**: $|X_N^(1)| = |X_{N-1}| + D_{N-2}$

where D(z) represents "doubly occupied" lens regions with cycle index $\frac{1}{2}[t_1^2 + t_2]$

**Generating Function**:
```
X(z) = 1 + z^2 D(z)C(z)/(1-zC(z))
D(z) = (1/2)C(z)[C^2(z) + C(z^2)]
```

### 3. Triples May Intersect (Section 6)
- Six fundamental triple-intersection topologies
- Count: $|^3\mathbb{X}_N|$ [OEIS A250001]
- Sequence: 0,1,3,14,61,252,1019,4127,17242,74007,...

**Six Fundamental Types** (Section 6.1):
1. **³·¹X₃** (RGB Spot): All 3 mutually intersect, symmetry S₃
2. **³·²X₃** (Torn): Pairwise intersections only
3. **³·³X₃** (Linear Chain): 3 in line, C₂ symmetry
4. **³·⁴X₃** (Compressed): Vertical compression
5. **³·⁵X₃** (Shrunk Center): Variation of compressed
6. **³·⁶X₃** (Asymmetric): No symmetry

**Cycle Indices** (for symmetry analysis):
- RGB Spot: $(t_1^3 + 3t_1t_2 + 2t_3)/6$
- Linear Chain: $(t_1^2 + t_2)/2$
- Compressed: $(t_1^4 + 2t_1^2t_2 + t_2^2)/4$

**Recurrence**: $|^3X_N^(1)| = |^3X_{N-1}| + ^2D_{N-2} + 2·^{3,1}D_{N-3} + ^{3,3}D_{N-3} + 2·^{3,4}D_{N-3} + ^{3,6}D_{N-3}$

## Sphere Embeddings (Section 2.2)

**Flip Transformations**: Embedding N circles on sphere creates clusters connected by "flips" - reversing orientation of one circle.

**Key Insight**: Planar topologies group into sphere clusters. For N circles:
- N=4: 9 planar → 3 sphere clusters
- N=5: 20 planar → 6 sphere clusters
- N=6: 48 planar → 11 sphere clusters

**Cluster Formula**: Uses cycle index with involution symmetry (order 2).

## Implementation Notes

**Euler Transform**: Connects single-factor counts to total counts via partitions.

**Bootstrap Algorithm**:
1. Start with base cases: |C_0|=1, |C_1|=1
2. Use recurrence to compute |C_N^(1)| from |C_{N-1}|
3. Apply Euler transform to get total |C_N|
4. Repeat for intersection cases with modified recurrences

**Key Sequences**:
- A000081: Rooted trees (non-intersecting)
- A000055: Unrooted trees (sphere embeddings)
- A261070: Pairs may intersect
- A250001: Triples may intersect
- A033185: Catalan triangle variant

## Tables Summary

**Table 2** (Non-intersecting): Shows |C_N| and |C_N^(f)| for N≤12
**Table 7** (Pairs): Shows |X_N| and |X_N^(f)| for N≤11
**Table 11** (Triples): Shows |³X_N| and |³X_N^(f)| for N≤11

## Figures

**C_4.eps**: 4 circles, 9 planar topologies in 3 flip clusters
**C_5.eps**: 5 circles, 20 planar topologies in 6 flip clusters
**C_6.eps**: 6 circles, 48 planar topologies in 11 flip clusters

Each diagram shows graph where:
- Nodes = distinct planar topologies (labeled by parentheses notation)
- Edges = flip transformations connecting topologies in same sphere cluster

## Mathematical Machinery

**Pólya Enumeration**: Used for counting with symmetry via cycle indices

**Generating Functions**: Formal power series encoding sequences, composed using:
- Multiplication for Cartesian products
- Substitution $z^j$ for cyclic symmetry
- Exponentials for set partitions

**Rooted Forest Interpretation**: Each intersection topology = rooted forest where:
- Trees = connected components
- Roots = outermost circles
- Children = nested circles within

## References to Paper Sections

- Section 1: Paired Parentheses & Catalan Numbers
- Section 2: Non-intersecting Circles (implemented)
- Section 3: Marked Circles (not implemented)
- Section 4: Pairs Intersecting (implemented)
- Section 5: Tree/Forest Interpretation
- Section 6: Triples Intersecting (implemented)

