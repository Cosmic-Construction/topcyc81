"""
Visualization utilities for circle topology transformations.

This module provides tools to visualize and analyze flip transformations
of circle topologies, as described in Section 2.2 of the paper.

The flip transformation corresponds to re-rooting the tree representation
of nested circles. When circles are embedded on a sphere, topologies that
differ only by which circle is considered the "root" become equivalent.

Each parentheses expression is also a rooted tree, so it has a Matula-Göbel
number (OEIS A061773) and an integer partition index given by the sizes of
its top-level factors. Flip clusters are sets of those Matula numbers. That
clustering is orthogonal to the partition index for fewer than 4 circles and
transverse to it after that.
"""

import math
from typing import Dict, List, NamedTuple, Set, Tuple
from collections import deque
from functools import lru_cache
from circle_topology import CircleTopology


@lru_cache(maxsize=None)
def generate_rooted_trees(n: int) -> Tuple[str, ...]:
    """
    Generate all unlabeled rooted trees with n nodes as nested parentheses.
    
    For n circles, use generate_rooted_trees(n+1) since the expressions
    represent trees with n+1 nodes (n circles plus the implicit root/plane).
    
    Args:
        n: Number of nodes in the tree (including root)
        
    Returns:
        Tuple of canonical expression strings, sorted lexicographically
        
    Verification:
        len(generate_rooted_trees(n)) == OEIS A000081(n)
    """
    if n == 0:
        return ()
    if n == 1:
        return ('',)  # Just the root, no children
    
    results = set()
    
    def generate_forests(remaining: int, max_size: int, current: List[str]):
        if remaining == 0:
            # Sort children to canonicalize (order doesn't matter for unlabeled trees)
            forest = tuple(sorted(current, reverse=True))
            expr = ''.join(f'({t})' for t in forest)
            results.add(expr)
            return
        for size in range(min(remaining, max_size), 0, -1):
            for tree in generate_rooted_trees(size):
                generate_forests(remaining - size, size, current + [tree])
    
    generate_forests(n - 1, n - 1, [])
    return tuple(sorted(results))


def expr_to_tree(expr: str) -> List:
    """
    Convert a parentheses expression to a tree structure.
    
    The tree is represented as a list of children, where each child
    is itself a tree (list of children).
    
    Args:
        expr: Nested parentheses expression
        
    Returns:
        Tree structure as nested lists
    """
    if not expr:
        return []
    
    trees = []
    depth = 0
    start = 0
    for i, c in enumerate(expr):
        if c == '(':
            if depth == 0:
                start = i
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                subtree = expr_to_tree(expr[start + 1:i])
                trees.append(subtree)
    return trees


def tree_to_expr(tree: List) -> str:
    """
    Convert a tree structure back to canonical parentheses expression.
    
    Children are sorted in reverse order to ensure canonical form.
    
    Args:
        tree: Tree structure as nested lists
        
    Returns:
        Canonical expression string
    """
    sorted_children = sorted(tree, key=lambda t: tree_to_expr(t), reverse=True)
    return ''.join(f'({tree_to_expr(sub)})' for sub in sorted_children)


def _get_node_at_path(tree: List, path: List[int]) -> List:
    """Get the node at the given path in the tree."""
    for i in path:
        tree = tree[i]
    return tree


def _build_chain(chain: List[Tuple[List, int]], bottom: List) -> List:
    """
    Build the reversed chain from the bottom up for re-rooting.
    
    Args:
        chain: List of (parent_tree, child_index) pairs from root to target
        bottom: The bottom-most subtree
        
    Returns:
        The rebuilt chain with bottom attached
    """
    if not chain:
        return bottom
    
    parent_tree, parent_idx = chain[-1]
    # Remove the branch that leads down to the target
    parent_without_branch = parent_tree[:parent_idx] + parent_tree[parent_idx + 1:]
    # Add the bottom as a child
    new_parent = parent_without_branch + [bottom]
    
    return _build_chain(chain[:-1], new_parent)


def re_root_at_path(tree: List, path: List[int]) -> List:
    """
    Re-root the tree at the node given by path.
    
    This implements the flip transformation: the target node becomes the
    new root, its children stay with it, and the path from the old root
    becomes a chain of children in reverse.
    
    Args:
        tree: Original tree structure
        path: List of indices navigating to the target node
        
    Returns:
        New tree with target as root
    """
    if not path:
        return tree
    
    target = _get_node_at_path(tree, path)
    
    # Build chain from root to target (excluding target)
    chain = []
    current = tree
    for i in path:
        chain.append((current, i))
        current = current[i]
    
    # New root children = target's original children + reversed chain
    new_root_children = list(target)
    
    if chain:
        parent_tree, parent_idx = chain[-1]
        parent_without_target = parent_tree[:parent_idx] + parent_tree[parent_idx + 1:]
        new_child = _build_chain(chain[:-1], parent_without_target)
        new_root_children.append(new_child)
    
    return new_root_children


_PRIMES: List[int] = []


def nth_prime(k: int) -> int:
    """
    Return the k-th prime, 1-based, so nth_prime(1) is 2.

    Used as the prime map in the Matula-Göbel encoding: p_k = nth_prime(k).

    Args:
        k: Prime index, starting at 1

    Returns:
        The k-th prime
    """
    if k < 1:
        raise ValueError("prime index must be a positive integer")
    if len(_PRIMES) >= k:
        return _PRIMES[k - 1]
    # Rosser's theorem: p_n < n (ln n + ln ln n) for n >= 6.
    if k < 6:
        limit = 12
    else:
        log_k = math.log(k)
        limit = int(k * (log_k + math.log(log_k))) + 3
    while True:
        sieve = bytearray(b"\x01") * (limit + 1)
        sieve[0] = 0
        sieve[1] = 0
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                start = i * i
                count = ((limit - start) // i) + 1
                sieve[start:limit + 1:i] = b"\x00" * count
        found = [i for i, flag in enumerate(sieve) if flag]
        if len(found) >= k:
            _PRIMES[:] = found
            return found[k - 1]
        limit = limit * 2 + 10


@lru_cache(maxsize=None)
def matula_number(expr: str) -> int:
    """
    Matula-Göbel number of a parentheses expression, including the implicit root.

    The expression is a forest of top-level factors. The implicit outer root is
    the plane (the extra node that makes n circles a tree on n+1 nodes). A
    factor ``(B)`` is the rooted tree whose Matula number is ``matula_number(B)``.
    If those factor numbers are m1, ..., mk, the expression's Matula number is

        p_{m1} * ... * p_{mk}

    where p_j is the j-th prime (p_1 = 2). The bare root (empty expression) is 1.
    A single leaf factor ``()`` is p_1 = 2.

    The same product written with indices descending is the prime word used in
    the cluster tables: ``(())()`` is p2p1 = 3 * 2 = 6.

    Args:
        expr: Canonical or non-canonical parentheses expression

    Returns:
        Matula-Göbel number of the rooted tree

    Verification:
        The numbers for n circles are exactly OEIS A061773, row n+1.
    """
    if not expr:
        return 1
    product = 1
    for child in expr_to_tree(expr):
        product *= nth_prime(matula_number(tree_to_expr(child)))
    return product


def factor_matula_indices(expr: str) -> Tuple[int, ...]:
    """
    Matula numbers of the top-level factors, descending.

    These are the indices in the prime word. ``(())()`` has factors of Matula
    numbers 2 and 1, so the indices are ``(2, 1)`` and the word is ``p2p1``.

    Args:
        expr: Parentheses expression

    Returns:
        Descending tuple of factor Matula numbers
    """
    indices = [
        matula_number(tree_to_expr(child))
        for child in expr_to_tree(expr)
    ]
    return tuple(sorted(indices, reverse=True))


def format_prime_product(indices: Tuple[int, ...]) -> str:
    """
    Write a descending prime-index product as a word such as ``p3p1`` or ``p5``.

    Args:
        indices: Prime indices, already in the order to print

    Returns:
        Concatenated ``p``-word. Empty for the bare root.
    """
    return "".join(f"p{index}" for index in indices)


def _node_count(tree: List) -> int:
    """Number of nodes in a tree, including its root."""
    return 1 + sum(_node_count(child) for child in tree)


def factor_size_partition(expr: str) -> Tuple[int, ...]:
    """
    Integer partition index of an expression: descending top-level factor sizes.

    A factor's size is the number of circles in it (parentheses pairs), which
    is the number of nodes in that factor's tree. The parts sum to the number
    of circles. ``((()))()`` is ``(3, 1)``, written ``[3+1]``.

    Args:
        expr: Parentheses expression

    Returns:
        Descending partition of the circle count
    """
    sizes = [_node_count(child) for child in expr_to_tree(expr)]
    return tuple(sorted(sizes, reverse=True))


def format_partition(parts: Tuple[int, ...]) -> str:
    """
    Write a partition as ``[3+1]`` or ``[4]``.

    Args:
        parts: Partition parts, already in the order to print

    Returns:
        Bracketed sum. ``[]`` for the empty partition.
    """
    return "[" + "+".join(str(part) for part in parts) + "]"


def format_matula_set(expressions: Set[str]) -> str:
    """
    Sorted Matula numbers of a flip cluster, written ``{5,6}``.

    Args:
        expressions: Expressions in one flip-equivalence cluster

    Returns:
        Brace-wrapped comma-separated Matula numbers, ascending
    """
    numbers = sorted(matula_number(expr) for expr in expressions)
    return "{" + ",".join(str(number) for number in numbers) + "}"


def format_expression_record(expr: str) -> str:
    """
    One catalog line: expression, factor count, partition index, prime word, Matula number.

    ``((()))`` is ``((())) [1 factors]: [3] : p3 = 5``.

    Args:
        expr: Parentheses expression

    Returns:
        Record line without leading indent
    """
    parts = factor_size_partition(expr)
    indices = factor_matula_indices(expr)
    factors = len(indices)
    return (
        f"{expr} [{factors} factors]: {format_partition(parts)} : "
        f"{format_prime_product(indices)} = {matula_number(expr)}"
    )


class PartitionCell(NamedTuple):
    """Expressions of one partition index inside one Matula cluster."""

    cluster: int
    matula_set: str
    expressions: Tuple[str, ...]
    matulas: Tuple[int, ...]
    prime_products: Tuple[str, ...]

    @property
    def count(self) -> int:
        """Number of expressions in this cell."""
        return len(self.expressions)


class PartitionIncidence(NamedTuple):
    """One integer partition index and the Matula clusters it meets."""

    partition: Tuple[int, ...]
    index: str
    clusters: Tuple[PartitionCell, ...]


def partition_incidence(clusters: List[Set[str]]) -> List[PartitionIncidence]:
    """
    Group expressions by integer partition index, then by flip cluster.

    Cluster numbers follow discovery order in ``clusters`` (the order returned
    by ``find_flip_clusters``). Partition indices are listed largest-part first.

    Args:
        clusters: Flip-equivalence clusters in discovery order

    Returns:
        One record per partition index, each with the cells that meet it
    """
    grouped: Dict[Tuple[int, ...], Dict[int, List[str]]] = {}
    matula_sets: Dict[int, str] = {}
    for cluster_index, cluster in enumerate(clusters, 1):
        matula_sets[cluster_index] = format_matula_set(cluster)
        for expr in cluster:
            parts = factor_size_partition(expr)
            grouped.setdefault(parts, {}).setdefault(cluster_index, []).append(expr)

    items: List[PartitionIncidence] = []
    for parts in sorted(grouped, reverse=True):
        cells = []
        for cluster_index in sorted(grouped[parts]):
            expressions = tuple(sorted(grouped[parts][cluster_index]))
            cells.append(PartitionCell(
                cluster=cluster_index,
                matula_set=matula_sets[cluster_index],
                expressions=expressions,
                matulas=tuple(matula_number(expr) for expr in expressions),
                prime_products=tuple(
                    format_prime_product(factor_matula_indices(expr))
                    for expr in expressions
                ),
            ))
        items.append(PartitionIncidence(
            partition=parts,
            index=format_partition(parts),
            clusters=tuple(cells),
        ))
    return items


def _plural(count: int, singular: str, plural: str = "") -> str:
    """Return ``1 cluster`` or ``2 clusters``."""
    word = singular if count == 1 else (plural or singular + "s")
    return f"{count} {word}"


def format_partition_orthogonality(n: int, clusters: List[Set[str]]) -> str:
    """
    Describe how Matula clusters sit across the integer partition index.

    The two labels of an expression are independent classifications of the
    set of expressions. A partition index such as ``[3]`` can meet several
    Matula clusters, and one cluster can contain several partition indices.
    Combinatorial orthogonality is the stronger condition that every
    cluster/partition cell has at most one expression. That holds for
    n < 4 and fails from n = 4, when a free tree first has two expressions
    of the same partition index.

    Args:
        n: Number of circles
        clusters: Flip clusters in discovery order

    Returns:
        Multiline report, without a trailing newline
    """
    incidence = partition_incidence(clusters)
    lines = [
        "Integer partition index vs Matula clusters:",
        "  The partition index is the descending sizes of the top-level factors.",
        "  Each cluster is the set of Matula numbers of one free tree.",
    ]
    partitions_meeting_several = 0
    max_cell = 0
    oversized = []
    for item in incidence:
        cells = item.clusters
        meets = len(cells)
        if meets > 1:
            partitions_meeting_several += 1
        sets = ", ".join(cell.matula_set for cell in cells)
        lines.append(
            f"  Partition index {item.index} meets {_plural(meets, 'Matula cluster')}: {sets}"
        )
        for cell in cells:
            max_cell = max(max_cell, cell.count)
            if cell.count > 1:
                details = ", ".join(
                    f"{product} = {number}"
                    for product, number in zip(cell.prime_products, cell.matulas)
                )
                oversized.append(
                    f"  Cell larger than 1: partition {item.index} ∩ {cell.matula_set} "
                    f"has {_plural(cell.count, 'expression')} ({details})."
                )

    clusters_with_several = 0
    for cluster in clusters:
        partitions = {factor_size_partition(expr) for expr in cluster}
        if len(partitions) > 1:
            clusters_with_several += 1

    lines.append(f"  Partition index [{n}] meets every Matula cluster.")
    if partitions_meeting_several and clusters_with_several:
        lines.append(
            "  Matula clusters are transverse to the integer partition index: "
            f"{_plural(partitions_meeting_several, 'partition index', 'partition indices')} "
            f"{'meets' if partitions_meeting_several == 1 else 'meet'} more than one cluster, "
            f"and {_plural(clusters_with_several, 'cluster')} "
            f"{'contains' if clusters_with_several == 1 else 'contain'} more than one partition index."
        )
    elif clusters_with_several:
        lines.append(
            "  Every partition index lies in a single Matula cluster, "
            f"but {_plural(clusters_with_several, 'cluster')} "
            f"{'contains' if clusters_with_several == 1 else 'contain'} more than one partition index."
        )
    else:
        lines.append(
            "  The Matula clusters and the integer partition index do not yet cross."
        )
    lines.extend(oversized)
    if max_cell <= 1:
        lines.append(
            "  Largest cluster/partition cell has 1 expression "
            "(combinatorially orthogonal)."
        )
        lines.append(
            "  The Matula numbers form clusters orthogonal to the integer partition index."
        )
    else:
        lines.append(
            f"  Largest cluster/partition cell has {_plural(max_cell, 'expression')} "
            "(crossing, but not combinatorially orthogonal)."
        )
        lines.append(
            "  The Matula numbers form clusters transverse to the integer partition "
            "index, but not orthogonal to it: a cluster meets one partition index "
            "in more than one expression."
        )
    return "\n".join(lines)


def format_flip_analysis(n: int) -> str:
    """
    Full flip analysis, with Matula numbers and the partition-index crossing.

    Args:
        n: Number of circles

    Returns:
        Report text, without a trailing newline
    """
    analysis = analyze_flip_structure(n)
    clusters = analysis["clusters"]
    lines = [
        f"Flip Transformation Analysis for {n} circles",
        "=" * 60,
        f"Total topologies: {analysis['total_topologies']}",
        f"Number of flip-equivalence clusters: {analysis['num_clusters']}",
        f"Cluster sizes: {analysis['cluster_sizes']}",
        "",
        "Clusters:",
    ]
    for i, cluster in enumerate(clusters, 1):
        lines.append(f"  Cluster {i} (size {len(cluster)}): {format_matula_set(cluster)}")
        for expr in sorted(cluster):
            lines.append(f"    {format_expression_record(expr)}")
    lines.append("")
    lines.append(format_partition_orthogonality(n, clusters))
    lines.append("")
    lines.append(
        "Note: Each cluster represents circle topologies that are equivalent "
        "when embedded on a sphere surface. The Matula number labels the rooted "
        "tree; the brace-set on each cluster is those numbers. The integer "
        "partition index is a second label of the same expression."
    )
    return "\n".join(lines)


def flip_top_level(expr: str) -> Set[str]:
    """
    Generate all expressions reachable by flip transformations.
    
    The flip operation re-roots the tree at each top-level factor.
    Only top-level factors are flipped, not nested sub-expressions.
    This produces exactly the edges shown in the paper's C4-C6 figures.
    
    Args:
        expr: Parentheses expression string
        
    Returns:
        Set of expression strings reachable by flip operations
    """
    tree = expr_to_tree(expr)
    results = {tree_to_expr(tree)}  # Include original
    
    for i in range(len(tree)):
        new_tree = re_root_at_path(tree, [i])
        results.add(tree_to_expr(new_tree))
    
    return results


def find_flip_clusters(expressions: List[str]) -> List[Set[str]]:
    """
    Find clusters of expressions connected by flip transformations.
    
    Uses BFS to find connected components in the flip graph.
    
    Args:
        expressions: List of circle expressions as strings
        
    Returns:
        List of sets, where each set contains expressions in the same cluster
        
    Verification:
        For n circles, len(find_flip_clusters(expressions)) should equal
        OEIS A000055(n+1) - the number of unrooted trees with n+1 nodes.
    """
    expr_set = set(expressions)
    visited = set()
    clusters = []
    
    for expr in expressions:
        if expr in visited:
            continue
        
        # BFS to find all connected expressions
        cluster = set()
        queue = deque([expr])
        cluster.add(expr)
        
        while queue:
            current = queue.popleft()
            for flipped in flip_top_level(current):
                if flipped in expr_set and flipped not in cluster:
                    cluster.add(flipped)
                    queue.append(flipped)
        
        visited.update(cluster)
        clusters.append(cluster)
    
    return clusters


def analyze_flip_structure(n: int) -> Dict[str, any]:
    """
    Analyze the flip transformation structure for n circles.
    
    Args:
        n: Number of circles
        
    Returns:
        Dictionary with analysis results including clusters
    """
    # Generate all expressions for n circles (trees with n+1 nodes)
    exprs = list(generate_rooted_trees(n + 1))
    clusters = find_flip_clusters(exprs)
    
    return {
        'n': n,
        'total_topologies': len(exprs),
        'clusters': clusters,
        'num_clusters': len(clusters),
        'cluster_sizes': sorted([len(c) for c in clusters], reverse=True)
    }


def print_flip_analysis(n: int = 4):
    """
    Print analysis of flip transformation clusters.
    
    Each expression is labeled with its integer partition index and its
    Matula-Göbel number. The report then shows how those Matula clusters
    sit across the partition index.
    
    Args:
        n: Number of circles (default 4)
    """
    print(format_flip_analysis(n))


if __name__ == "__main__":
    # Demo the flip transformation analysis for C1-C9
    for n in range(1, 10):
        print_flip_analysis(n)
        if n < 9:
            print()
