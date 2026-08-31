#!/usr/bin/env python3
"""
EPS Diagram Generator for Circle Topology Flip Transformations

This script generates Graphviz DOT files and EPS diagrams for the
flip transformation graphs of circle topologies, matching the style
of the original paper figures (C4-C6).

Usage:
    python generate_eps.py          # Generate all EPS files (C4-C9)
    python generate_eps.py 7        # Generate only C7.eps
    python generate_eps.py 7 8 9    # Generate C7, C8, C9

Requirements:
    - Graphviz (dot command) must be installed
    - Python 3.x standard library only
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Set, Tuple

from flip_transforms import generate_rooted_trees, flip_top_level, find_flip_clusters


def generate_dot_file(n: int, output_path: Path) -> Tuple[int, int]:
    """
    Generate a Graphviz DOT file for n circles.
    
    Args:
        n: Number of circles
        output_path: Path to write the DOT file
        
    Returns:
        Tuple of (num_nodes, num_edges)
    """
    # Generate all expressions for n circles (trees with n+1 nodes)
    expressions = list(generate_rooted_trees(n + 1))
    
    # Build edge set (undirected, so we canonicalize edge direction)
    edges: Set[Tuple[str, str]] = set()
    for expr in expressions:
        for flipped in flip_top_level(expr):
            if flipped != expr and flipped in set(expressions):
                # Canonicalize edge direction to avoid duplicates
                edge = tuple(sorted([expr, flipped]))
                edges.add(edge)
    
    # Generate DOT content
    lines = [
        f'graph C_{n} {{',
        '  node [shape=ellipse, fontname="Times-Roman", fontsize=14];',
        '  edge [color=black];',
        '  graph [bgcolor=white];',
        '',
    ]
    
    # Add nodes (Graphviz will auto-layout)
    for expr in sorted(expressions):
        # Escape parentheses for DOT format
        label = expr.replace('\\', '\\\\').replace('"', '\\"')
        lines.append(f'  "{label}";')
    
    lines.append('')
    
    # Add edges
    for src, dst in sorted(edges):
        src_esc = src.replace('\\', '\\\\').replace('"', '\\"')
        dst_esc = dst.replace('\\', '\\\\').replace('"', '\\"')
        lines.append(f'  "{src_esc}" -- "{dst_esc}";')
    
    lines.append('}')
    
    output_path.write_text('\n'.join(lines))
    return len(expressions), len(edges)


def generate_eps(n: int, output_dir: Path) -> bool:
    """
    Generate EPS file for n circles.
    
    Args:
        n: Number of circles
        output_dir: Directory to write files
        
    Returns:
        True if successful, False otherwise
    """
    dot_path = output_dir / f'C{n}.dot'
    eps_path = output_dir / f'C{n}.eps'
    
    # Generate DOT file
    num_nodes, num_edges = generate_dot_file(n, dot_path)
    print(f'  Generated {dot_path.name}: {num_nodes} nodes, {num_edges} edges')
    
    # Call Graphviz dot to generate EPS
    try:
        result = subprocess.run(
            ['dot', '-Tps', str(dot_path), '-o', str(eps_path)],
            capture_output=True,
            text=True,
            check=True
        )
        print(f'  Generated {eps_path.name}')
        return True
    except subprocess.CalledProcessError as e:
        print(f'  Error generating EPS: {e.stderr}')
        return False
    except FileNotFoundError:
        print('  Error: Graphviz "dot" command not found.')
        print('  Install with: apt-get install graphviz')
        return False


def main():
    """Main entry point."""
    # Parse command line arguments
    if len(sys.argv) > 1:
        n_values = [int(arg) for arg in sys.argv[1:]]
    else:
        n_values = [4, 5, 6, 7, 8, 9]
    
    # Determine output directory (arXiv subdirectory)
    script_dir = Path(__file__).parent
    output_dir = script_dir / 'arXiv-1603.00077v2'
    
    if not output_dir.exists():
        print(f'Error: Output directory {output_dir} does not exist')
        sys.exit(1)
    
    print('EPS Diagram Generator for Circle Topologies')
    print('=' * 60)
    print()
    
    # Verify expected counts
    from circle_topology import CircleTopology
    
    print('Expected counts:')
    for n in n_values:
        rooted = CircleTopology.rooted_trees(n + 1)
        unrooted = CircleTopology.unrooted_trees(n + 1)
        print(f'  C{n}: {rooted} rooted trees, {unrooted} clusters')
    print()
    
    # Generate EPS files
    success_count = 0
    for n in n_values:
        print(f'Generating C{n}...')
        if generate_eps(n, output_dir):
            success_count += 1
        print()
    
    print('=' * 60)
    print(f'Generated {success_count}/{len(n_values)} EPS files')
    
    # Clean up DOT files (optional, keep for debugging)
    # for n in n_values:
    #     dot_path = output_dir / f'C{n}.dot'
    #     if dot_path.exists():
    #         dot_path.unlink()


if __name__ == '__main__':
    main()
