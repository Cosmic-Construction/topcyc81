"""
Tests for the Circle Topology module.

This module tests the algorithms for counting topologically distinct
sets of circles with various intersection constraints.
"""

import unittest
from circle_topology import CircleTopology


class TestCircleTopology(unittest.TestCase):
    """Test cases for CircleTopology class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.topology = CircleTopology()
    
    def test_rooted_trees(self):
        """Test that rooted trees are computed correctly (OEIS A000081)."""
        # First terms of A000081
        expected = [0, 1, 1, 2, 4, 9, 20, 48, 115, 286]
        for n, expected_value in enumerate(expected):
            with self.subTest(n=n):
                self.assertEqual(
                    CircleTopology.rooted_trees(n),
                    expected_value,
                    f"Rooted trees A000081({n}) should be {expected_value}"
                )
    
    def test_catalan_numbers(self):
        """Test that Catalan numbers are computed correctly."""
        # First 10 Catalan numbers
        expected = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
        for n, expected_value in enumerate(expected):
            with self.subTest(n=n):
                self.assertEqual(
                    CircleTopology.catalan_number(n),
                    expected_value,
                    f"Catalan number C({n}) should be {expected_value}"
                )
    
    def test_non_intersecting_circles(self):
        """Test counting of non-intersecting circles (based on rooted trees)."""
        # Should equal rooted trees with n+1 nodes (A000081 shifted)
        # n circles -> A000081(n+1)
        expected = [1, 1, 2, 4, 9, 20, 48, 115, 286, 719]  # A000081 starting from n=1
        for n, expected_value in enumerate(expected):
            with self.subTest(n=n):
                self.assertEqual(
                    self.topology.non_intersecting_circles(n),
                    expected_value,
                    f"Non-intersecting circles for n={n} should be {expected_value}"
                )
    
    def test_pairs_may_intersect_base_cases(self):
        """Test base cases for pairs intersection."""
        self.assertEqual(self.topology.pairs_may_intersect(0), 1)
        self.assertEqual(self.topology.pairs_may_intersect(1), 1)
        # For n=2, we can have nested or intersecting
        self.assertGreaterEqual(self.topology.pairs_may_intersect(2), 2)
    
    def test_triples_may_intersect_base_cases(self):
        """Test base cases for triples intersection."""
        self.assertEqual(self.topology.triples_may_intersect(0), 1)
        self.assertEqual(self.topology.triples_may_intersect(1), 1)
        self.assertEqual(self.topology.triples_may_intersect(2), 2)
        # For n=3, should have more configurations than pairs
        self.assertGreaterEqual(self.topology.triples_may_intersect(3), 
                               self.topology.pairs_may_intersect(3))
    
    def test_monotonic_increase_with_intersection_freedom(self):
        """Test that allowing more intersections increases or maintains count."""
        for n in range(1, 8):
            with self.subTest(n=n):
                non_int = self.topology.non_intersecting_circles(n)
                pairs = self.topology.pairs_may_intersect(n)
                triples = self.topology.triples_may_intersect(n)
                
                # More freedom should allow at least as many topologies
                self.assertGreaterEqual(pairs, non_int,
                    f"Pairs count should be >= non-intersecting for n={n}")
                self.assertGreaterEqual(triples, pairs,
                    f"Triples count should be >= pairs for n={n}")
    
    def test_generate_sequence(self):
        """Test sequence generation."""
        max_n = 5
        
        # Test non-intersecting sequence
        seq_none = self.topology.generate_sequence(max_n, 'none')
        self.assertEqual(len(seq_none), max_n + 1)
        self.assertEqual(seq_none[0], 1)
        self.assertEqual(seq_none[1], 1)
        self.assertEqual(seq_none[2], 2)
        
        # Test pairs sequence
        seq_pairs = self.topology.generate_sequence(max_n, 'pairs')
        self.assertEqual(len(seq_pairs), max_n + 1)
        
        # Test triples sequence
        seq_triples = self.topology.generate_sequence(max_n, 'triples')
        self.assertEqual(len(seq_triples), max_n + 1)
    
    def test_generate_sequence_invalid_type(self):
        """Test that invalid intersection type raises error."""
        with self.assertRaises(ValueError):
            self.topology.generate_sequence(5, 'invalid')
    
    def test_generating_function_coefficients(self):
        """Test generating function coefficient computation."""
        max_n = 5
        
        # Test non-intersecting
        gf = self.topology.generating_function_coefficients(max_n, 'none')
        self.assertEqual(len(gf), max_n + 1)
        self.assertEqual(gf[0], 1)
        self.assertEqual(gf[1], 1)
        self.assertEqual(gf[2], 2)
        
        # Test pairs
        gf_pairs = self.topology.generating_function_coefficients(max_n, 'pairs')
        self.assertEqual(len(gf_pairs), max_n + 1)
        
        # Test triples
        gf_triples = self.topology.generating_function_coefficients(max_n, 'triples')
        self.assertEqual(len(gf_triples), max_n + 1)
    
    def test_consistency_of_sequences(self):
        """Test that different methods produce consistent results."""
        for n in range(6):
            with self.subTest(n=n):
                # Direct call should match sequence generation
                direct_none = self.topology.non_intersecting_circles(n)
                seq_none = self.topology.generate_sequence(n, 'none')
                self.assertEqual(direct_none, seq_none[n])
                
                direct_pairs = self.topology.pairs_may_intersect(n)
                seq_pairs = self.topology.generate_sequence(n, 'pairs')
                self.assertEqual(direct_pairs, seq_pairs[n])
                
                direct_triples = self.topology.triples_may_intersect(n)
                seq_triples = self.topology.generate_sequence(n, 'triples')
                self.assertEqual(direct_triples, seq_triples[n])


class TestRecurrenceRelations(unittest.TestCase):
    """Test the recurrence relations used in the algorithms."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.topology = CircleTopology()
    
    def test_catalan_recurrence(self):
        """Test that Catalan numbers match known values."""
        # Known Catalan numbers for verification
        known_catalan = {
            0: 1, 1: 1, 2: 2, 3: 5, 4: 14, 5: 42, 6: 132, 7: 429,
            8: 1430, 9: 4862, 10: 16796
        }
        for n, expected in known_catalan.items():
            computed = self.topology.catalan_number(n)
            self.assertEqual(computed, expected,
                f"Catalan number C({n}) should be {expected}")
    
    def test_pairs_recurrence_structure(self):
        """Test that pairs intersection follows a valid recurrence."""
        # The function should produce increasing values with n (starting from n=2)
        values = [self.topology.pairs_may_intersect(n) for n in range(8)]
        for i in range(2, len(values)):
            self.assertGreater(values[i], values[i-1],
                f"Count should increase with n: n={i}")
    
    def test_triples_recurrence_structure(self):
        """Test that triples intersection follows a valid recurrence."""
        # The function should produce increasing values with n (starting from n=2)
        values = [self.topology.triples_may_intersect(n) for n in range(8)]
        for i in range(2, len(values)):
            self.assertGreater(values[i], values[i-1],
                f"Count should increase with n: n={i}")


class TestDimensionalProgression(unittest.TestCase):
    """Test the dimensional progression: 1D → 2D → 3D → 4D."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.topology = CircleTopology()
    
    def test_unrooted_trees_oeis_a000055(self):
        """Test that unrooted trees match OEIS A000055."""
        # First terms of A000055 (unrooted trees)
        expected = [1, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235]
        for n, expected_value in enumerate(expected):
            with self.subTest(n=n):
                self.assertEqual(
                    CircleTopology.unrooted_trees(n),
                    expected_value,
                    f"Unrooted trees A000055({n}) should be {expected_value}"
                )
    
    def test_sphere_surface_clusters(self):
        """Test sphere surface cluster counts (3D embedding)."""
        # Expected sphere clusters for n circles
        # These correspond to unrooted trees with n+1 nodes
        expected = [1, 1, 1, 2, 3, 6, 11, 23, 47, 106]
        for n, expected_value in enumerate(expected):
            with self.subTest(n=n):
                computed = self.topology.sphere_surface_clusters(n)
                self.assertEqual(
                    computed,
                    expected_value,
                    f"Sphere clusters for n={n} should be {expected_value}"
                )
    
    def test_hypersphere_4d_clusters_base_cases(self):
        """Test 4D hypersphere cluster base cases."""
        # Base cases for 4D hypersphere
        self.assertEqual(self.topology.hypersphere_4d_clusters(0), 1)
        self.assertEqual(self.topology.hypersphere_4d_clusters(1), 1)
        self.assertEqual(self.topology.hypersphere_4d_clusters(2), 1)
        self.assertEqual(self.topology.hypersphere_4d_clusters(3), 1)
        self.assertEqual(self.topology.hypersphere_4d_clusters(4), 2)
        self.assertEqual(self.topology.hypersphere_4d_clusters(5), 3)
    
    def test_dimensional_reduction_monotonic(self):
        """Test that each dimension reduces or maintains count."""
        # Each higher dimension should have fewer or equal clusters
        for n in range(1, 10):
            with self.subTest(n=n):
                catalan = self.topology.catalan_number(n)
                planar = self.topology.non_intersecting_circles(n)
                sphere = self.topology.sphere_surface_clusters(n)
                hypersphere = self.topology.hypersphere_4d_clusters(n)
                
                # 1D ≥ 2D ≥ 3D ≥ 4D
                self.assertGreaterEqual(catalan, planar,
                    f"Catalan should be ≥ planar for n={n}")
                self.assertGreaterEqual(planar, sphere,
                    f"Planar should be ≥ sphere for n={n}")
                self.assertGreaterEqual(sphere, hypersphere,
                    f"Sphere should be ≥ hypersphere for n={n}")
    
    def test_dimensional_progression_known_values(self):
        """Test known values in the dimensional progression table."""
        # From problem statement
        test_cases = [
            # n, catalan, planar, sphere, expected_hypersphere (from pattern)
            (0, 1, 1, 1, 1),
            (1, 1, 1, 1, 1),
            (2, 2, 2, 1, 1),
            (3, 5, 4, 2, 1),
            (4, 14, 9, 3, 2),
            (5, 42, 20, 6, 3),
            (6, 132, 48, 11, 6),
            (7, 429, 115, 23, 11),
            (8, 1430, 286, 47, 23),
            (9, 4862, 719, 106, 44),
        ]
        
        for n, exp_cat, exp_planar, exp_sphere, exp_hyper in test_cases:
            with self.subTest(n=n):
                self.assertEqual(self.topology.catalan_number(n), exp_cat)
                self.assertEqual(self.topology.non_intersecting_circles(n), exp_planar)
                self.assertEqual(self.topology.sphere_surface_clusters(n), exp_sphere)
                # 4D is theoretical, so we check it computes something reasonable
                hyper = self.topology.hypersphere_4d_clusters(n)
                self.assertLessEqual(hyper, exp_sphere,
                    f"Hypersphere should be ≤ sphere for n={n}")
                if n <= 9:
                    self.assertEqual(hyper, exp_hyper,
                        f"Hypersphere for n={n} should be {exp_hyper}")
    
    def test_unrooted_from_rooted_formula(self):
        """Test Otter's formula relating unrooted to rooted trees."""
        # For small n, verify the relationship manually
        for n in range(1, 8):
            with self.subTest(n=n):
                unrooted = self.topology.unrooted_trees(n)
                # Unrooted count should be positive
                self.assertGreater(unrooted, 0)
                # Unrooted should be ≤ rooted
                rooted = self.topology.rooted_trees(n)
                self.assertLessEqual(unrooted, rooted,
                    f"Unrooted trees should be ≤ rooted trees for n={n}")


class TestFlipTransformations(unittest.TestCase):
    """Test flip transformation and clustering (OEIS A000055 verification)."""
    
    def test_generate_rooted_trees(self):
        """Test that generate_rooted_trees produces correct counts (A000081)."""
        from flip_transforms import generate_rooted_trees
        
        # First terms of A000081
        expected = [0, 1, 1, 2, 4, 9, 20, 48, 115, 286]
        for n, expected_count in enumerate(expected):
            if n == 0:
                continue  # Skip n=0 (empty)
            with self.subTest(n=n):
                trees = generate_rooted_trees(n)
                self.assertEqual(
                    len(trees),
                    expected_count,
                    f"generate_rooted_trees({n}) should return {expected_count} trees"
                )
    
    def test_flip_clusters_c4(self):
        """Test C4 gives 3 clusters (9 rooted trees -> 3 free trees)."""
        from flip_transforms import generate_rooted_trees, find_flip_clusters
        exprs = list(generate_rooted_trees(5))  # 4 circles = 5 nodes
        clusters = find_flip_clusters(exprs)
        self.assertEqual(len(exprs), 9, "C4 should have 9 expressions")
        self.assertEqual(len(clusters), 3, "C4 should have 3 clusters")
    
    def test_flip_clusters_c5(self):
        """Test C5 gives 6 clusters (20 rooted trees -> 6 free trees)."""
        from flip_transforms import generate_rooted_trees, find_flip_clusters
        exprs = list(generate_rooted_trees(6))  # 5 circles = 6 nodes
        clusters = find_flip_clusters(exprs)
        self.assertEqual(len(exprs), 20, "C5 should have 20 expressions")
        self.assertEqual(len(clusters), 6, "C5 should have 6 clusters")
    
    def test_flip_clusters_c6(self):
        """Test C6 gives 11 clusters (48 rooted trees -> 11 free trees)."""
        from flip_transforms import generate_rooted_trees, find_flip_clusters
        exprs = list(generate_rooted_trees(7))  # 6 circles = 7 nodes
        clusters = find_flip_clusters(exprs)
        self.assertEqual(len(exprs), 48, "C6 should have 48 expressions")
        self.assertEqual(len(clusters), 11, "C6 should have 11 clusters")
    
    def test_flip_clusters_c7(self):
        """Test C7 gives 23 clusters (115 rooted trees -> 23 free trees)."""
        from flip_transforms import generate_rooted_trees, find_flip_clusters
        exprs = list(generate_rooted_trees(8))  # 7 circles = 8 nodes
        clusters = find_flip_clusters(exprs)
        self.assertEqual(len(exprs), 115, "C7 should have 115 expressions")
        self.assertEqual(len(clusters), 23, "C7 should have 23 clusters")
    
    def test_flip_clusters_c8(self):
        """Test C8 gives 47 clusters (286 rooted trees -> 47 free trees)."""
        from flip_transforms import generate_rooted_trees, find_flip_clusters
        exprs = list(generate_rooted_trees(9))  # 8 circles = 9 nodes
        clusters = find_flip_clusters(exprs)
        self.assertEqual(len(exprs), 286, "C8 should have 286 expressions")
        self.assertEqual(len(clusters), 47, "C8 should have 47 clusters")
    
    def test_flip_clusters_c9(self):
        """Test C9 gives 106 clusters (719 rooted trees -> 106 free trees)."""
        from flip_transforms import generate_rooted_trees, find_flip_clusters
        exprs = list(generate_rooted_trees(10))  # 9 circles = 10 nodes
        clusters = find_flip_clusters(exprs)
        self.assertEqual(len(exprs), 719, "C9 should have 719 expressions")
        self.assertEqual(len(clusters), 106, "C9 should have 106 clusters")
    
    def test_flip_clusters_match_unrooted_trees(self):
        """Test that cluster counts match OEIS A000055 for all n."""
        from flip_transforms import generate_rooted_trees, find_flip_clusters
        from circle_topology import CircleTopology
        
        for n in range(1, 10):
            with self.subTest(n=n):
                exprs = list(generate_rooted_trees(n + 1))
                clusters = find_flip_clusters(exprs)
                expected = CircleTopology.unrooted_trees(n + 1)
                self.assertEqual(
                    len(clusters),
                    expected,
                    f"C{n} should have {expected} clusters (A000055)"
                )


def run_tests():
    """Run all tests."""
    unittest.main(argv=[''], verbosity=2, exit=False)


if __name__ == '__main__':
    run_tests()
