"""
Unit tests for the Fibonacci implementation
"""

import unittest
from fibonacci import fibonacci, fibonacci_sequence


class TestFibonacci(unittest.TestCase):
    """Test cases for Fibonacci functions"""

    def test_fibonacci_base_cases(self):
        """Test base cases"""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        """Test small Fibonacci numbers"""
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_larger_numbers(self):
        """Test larger Fibonacci numbers"""
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_fibonacci_negative(self):
        """Test negative input"""
        self.assertEqual(fibonacci(-1), 0)
        self.assertEqual(fibonacci(-10), 0)

    def test_fibonacci_sequence_base_cases(self):
        """Test fibonacci_sequence base cases"""
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(2), [0, 1])

    def test_fibonacci_sequence_small(self):
        """Test small fibonacci sequences"""
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_fibonacci_sequence_negative(self):
        """Test negative input for sequence"""
        self.assertEqual(fibonacci_sequence(-1), [])
        self.assertEqual(fibonacci_sequence(-5), [])


if __name__ == "__main__":
    unittest.main()
