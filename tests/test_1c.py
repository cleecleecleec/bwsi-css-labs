"""
tests_1c.py

Unit tests for the max_subarray_sum function defined in lab_1c.py.
Tests cover edge cases: empty list, single element, all positives, all negatives, and mixed.
Derived from LeetCode: https://leetcode.com/problems/maximum-subarray/
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum


class TestMaxSubarraySum:
    """Test suite for max_subarray_sum function."""
    
    def test_mixed_array(self):
        """Test with mixed positive and negative numbers (LeetCode example)."""
        assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
        # Contiguous subarray [4, -1, 2, 1] has maximum sum 6
    
    def test_all_positive(self):
        """Test with all positive numbers."""
        assert max_subarray_sum([1, 2, 3, 4, 5]) == 15
        # Maximum sum is the entire array
    
    def test_all_negative(self):
        """Test with all negative numbers."""
        assert max_subarray_sum([-5, -2, -8, -1, -4]) == -1
        # Maximum sum is the least negative number
    
    def test_single_element_positive(self):
        """Test with a single positive element."""
        assert max_subarray_sum([5]) == 5
    
    def test_single_element_negative(self):
        """Test with a single negative element."""
        assert max_subarray_sum([-5]) == -5
    
    def test_single_element_zero(self):
        """Test with a single zero element."""
        assert max_subarray_sum([0]) == 0
    
    def test_two_elements_positive(self):
        """Test with two positive elements."""
        assert max_subarray_sum([2, 3]) == 5
    
    def test_two_elements_mixed(self):
        """Test with two mixed elements."""
        assert max_subarray_sum([5, -10]) == 5
        assert max_subarray_sum([-5, 10]) == 10
    
    def test_subarray_in_middle(self):
        """Test where max subarray is in the middle."""
        assert max_subarray_sum([1, -1, 5, 3, -2]) == 8
        # Maximum sum is [5, 3] = 8
    
    def test_with_zeros(self):
        """Test with zeros mixed in."""
        assert max_subarray_sum([0, -2, 0, 3, 0]) == 3
        # Maximum sum is [3]
    
    def test_alternating_signs(self):
        """Test with alternating positive and negative."""
        assert max_subarray_sum([1, -1, 1, -1, 1]) == 1
        # Maximum sum is any single positive element
    
    def test_large_positive_surrounded_by_negatives(self):
        """Test with large positive value in negative context."""
        assert max_subarray_sum([-10, -5, 100, -20, -30]) == 100
        # Maximum sum is the single large element
    
    def test_edge_case_multiple_equal_max_subarrays(self):
        """Test when multiple subarrays have the same max sum."""
        assert max_subarray_sum([3, -1, 3]) == 5
        # [3, -1, 3] has sum 5, which is the maximum


def test_empty_list_raises_error():
    """Test that empty list raises ValueError."""
    with pytest.raises(ValueError, match="nums must be a non-empty list"):
        max_subarray_sum([])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
