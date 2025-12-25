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


def run_tests():
    """Run all tests."""
    unittest.main(argv=[''], verbosity=2, exit=False)


if __name__ == '__main__':
    run_tests()
