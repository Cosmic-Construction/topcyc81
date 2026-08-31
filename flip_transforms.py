"""
Visualization utilities for circle topology transformations.

This module provides tools to visualize and analyze flip transformations
of circle topologies, as described in Section 2.2 of the paper.

The flip transformation corresponds to re-rooting the tree representation
of nested circles. When circles are embedded on a sphere, topologies that
differ only by which circle is considered the "root" become equivalent.
"""

from typing import List, Set, Tuple, Dict
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
    
    Args:
        n: Number of circles (default 4)
    """
    analysis = analyze_flip_structure(n)
    
    print(f"Flip Transformation Analysis for {n} circles")
    print("=" * 60)
    print(f"Total topologies: {analysis['total_topologies']}")
    print(f"Number of flip-equivalence clusters: {analysis['num_clusters']}")
    print(f"Cluster sizes: {analysis['cluster_sizes']}")
    print()
    print("Clusters:")
    for i, cluster in enumerate(analysis['clusters'], 1):
        print(f"  Cluster {i} (size {len(cluster)}):")
        for expr in sorted(cluster):
            tree = expr_to_tree(expr)
            print(f"    {expr} [{len(tree)} factors]")
    print()
    print("Note: Each cluster represents circle topologies that are")
    print("equivalent when embedded on a sphere surface.")


if __name__ == "__main__":
    # Demo the flip transformation analysis
    print_flip_analysis(4)
