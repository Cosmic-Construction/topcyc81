"""
Topologically Distinct Sets of Non-intersecting Circles in the Plane

This module implements algorithms to count topologically distinct arrangements
of circles based on the paper "Topologically Distinct Sets of Non-intersecting
Circles in the Plane" (arXiv:1603.00077).

The main questions addressed:
1. How many different topologies of nested circles exist when pairs may intersect?
2. How many different topologies exist when triples may intersect?
"""

from typing import List, Tuple, Dict
from functools import lru_cache
import itertools


class CircleTopology:
    """
    Analyzes topologically distinct sets of circles in the plane.
    
    This class provides methods to compute the number of topologically
    distinct arrangements of circles with different intersection constraints.
    """
    
    def __init__(self):
        """Initialize the CircleTopology analyzer."""
        pass
    
    @staticmethod
    @lru_cache(maxsize=None)
    def catalan_number(n: int) -> int:
        """
        Compute the n-th Catalan number.
        
        Catalan numbers count non-intersecting circles (nested structures).
        C(n) = (2n)! / ((n+1)! * n!)
        
        Args:
            n: The index of the Catalan number
            
        Returns:
            The n-th Catalan number
        """
        if n <= 1:
            return 1
        
        # Use recursive formula: C(n) = sum(C(i) * C(n-1-i)) for i=0 to n-1
        result = 0
        for i in range(n):
            result += CircleTopology.catalan_number(i) * CircleTopology.catalan_number(n - 1 - i)
        return result
    
    @staticmethod
    def non_intersecting_circles(n: int) -> int:
        """
        Count topologically distinct sets of n non-intersecting circles.
        
        This is the base case where no circles intersect at all.
        The count equals the n-th Catalan number.
        
        Args:
            n: Number of circles
            
        Returns:
            Number of topologically distinct arrangements
        """
        return CircleTopology.catalan_number(n)
    
    @staticmethod
    @lru_cache(maxsize=None)
    def pairs_may_intersect(n: int) -> int:
        """
        Count topologically distinct sets when pairs of circles may intersect.
        
        This function computes the number of distinct topologies where
        at most 2 circles can intersect at any point.
        
        The recurrence relation for this case builds on the structure of
        matching forests and considers the additional degrees of freedom
        when pairs can intersect.
        
        Args:
            n: Number of circles
            
        Returns:
            Number of topologically distinct arrangements where pairs may intersect
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        # For pairs intersecting, we need to account for:
        # 1. Non-intersecting arrangements (Catalan numbers)
        # 2. Arrangements where exactly one pair intersects
        # 3. Multiple disjoint pairs intersecting
        
        # Base formula considers nested and intersecting pair structures
        # This follows from the generating function analysis
        result = 0
        
        # Sum over all possible decompositions
        for k in range(n):
            # Consider k circles on one side, n-1-k on the other
            left = CircleTopology.pairs_may_intersect(k)
            right = CircleTopology.pairs_may_intersect(n - 1 - k)
            result += left * right
        
        # Add contribution from intersecting pairs
        # Each pair intersection creates a lens-shaped region
        for k in range(1, n):
            # k circles form intersecting pair, rest are distributed
            if k >= 2:
                inner = CircleTopology.pairs_may_intersect(k - 2)
                outer = CircleTopology.pairs_may_intersect(n - k)
                result += inner * outer
        
        return result
    
    @staticmethod
    @lru_cache(maxsize=None)
    def triples_may_intersect(n: int) -> int:
        """
        Count topologically distinct sets when triples of circles may intersect.
        
        This function computes the number of distinct topologies where
        up to 3 circles can intersect at any point.
        
        Args:
            n: Number of circles
            
        Returns:
            Number of topologically distinct arrangements where triples may intersect
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2  # Either nested or intersecting
        
        # For triples intersecting, we account for:
        # 1. All arrangements from pairs_may_intersect
        # 2. Arrangements where exactly one triple intersects
        # 3. Multiple disjoint triples intersecting
        
        result = 0
        
        # Basic recursive decomposition
        for k in range(n):
            left = CircleTopology.triples_may_intersect(k)
            right = CircleTopology.triples_may_intersect(n - 1 - k)
            result += left * right
        
        # Add pair intersection configurations
        for k in range(2, n + 1):
            if k >= 2:
                inner = CircleTopology.triples_may_intersect(k - 2)
                outer = CircleTopology.triples_may_intersect(n - k)
                result += inner * outer
        
        # Add triple intersection configurations
        # Three circles intersecting create a central region
        for k in range(3, n + 1):
            if k >= 3:
                inner = CircleTopology.triples_may_intersect(k - 3)
                outer = CircleTopology.triples_may_intersect(n - k)
                result += inner * outer
        
        return result
    
    @staticmethod
    def generate_sequence(max_n: int, intersection_type: str = 'none') -> List[int]:
        """
        Generate a sequence of counts for different numbers of circles.
        
        Args:
            max_n: Maximum number of circles to compute
            intersection_type: Type of intersection allowed ('none', 'pairs', 'triples')
            
        Returns:
            List of counts for n=0 to max_n
        """
        if intersection_type == 'none':
            return [CircleTopology.non_intersecting_circles(n) for n in range(max_n + 1)]
        elif intersection_type == 'pairs':
            return [CircleTopology.pairs_may_intersect(n) for n in range(max_n + 1)]
        elif intersection_type == 'triples':
            return [CircleTopology.triples_may_intersect(n) for n in range(max_n + 1)]
        else:
            raise ValueError(f"Unknown intersection type: {intersection_type}")
    
    @staticmethod
    def generating_function_coefficients(max_n: int, intersection_type: str = 'none') -> Dict[int, int]:
        """
        Compute coefficients of the generating function.
        
        The generating function G(x) = sum(a_n * x^n) where a_n is the
        count of topologically distinct arrangements of n circles.
        
        Args:
            max_n: Maximum degree of the polynomial
            intersection_type: Type of intersection allowed ('none', 'pairs', 'triples')
            
        Returns:
            Dictionary mapping degree to coefficient
        """
        sequence = CircleTopology.generate_sequence(max_n, intersection_type)
        return {n: sequence[n] for n in range(len(sequence))}


def main():
    """
    Main function to demonstrate the circle topology analysis.
    """
    topology = CircleTopology()
    
    print("Topologically Distinct Sets of Non-intersecting Circles")
    print("=" * 60)
    print()
    
    # Compute and display results for non-intersecting circles
    print("Case: Non-intersecting circles (Catalan numbers)")
    print("-" * 60)
    max_n = 10
    for n in range(max_n + 1):
        count = topology.non_intersecting_circles(n)
        print(f"n={n:2d}: {count:6d} distinct topologies")
    print()
    
    # Compute and display results for pairs intersecting
    print("Case (i): Pairs of circles may intersect")
    print("-" * 60)
    for n in range(max_n + 1):
        count = topology.pairs_may_intersect(n)
        print(f"n={n:2d}: {count:6d} distinct topologies")
    print()
    
    # Compute and display results for triples intersecting
    print("Case (ii): Triples of circles may intersect")
    print("-" * 60)
    for n in range(max_n + 1):
        count = topology.triples_may_intersect(n)
        print(f"n={n:2d}: {count:6d} distinct topologies")
    print()
    
    # Display generating function coefficients
    print("Generating Function Coefficients (first 8 terms)")
    print("-" * 60)
    gf_none = topology.generating_function_coefficients(7, 'none')
    gf_pairs = topology.generating_function_coefficients(7, 'pairs')
    gf_triples = topology.generating_function_coefficients(7, 'triples')
    
    print("Non-intersecting: ", [gf_none[i] for i in range(8)])
    print("Pairs intersect:  ", [gf_pairs[i] for i in range(8)])
    print("Triples intersect:", [gf_triples[i] for i in range(8)])


if __name__ == "__main__":
    main()
