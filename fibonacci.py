"""
Fibonacci Sequence Implementation

This module provides efficient implementations of the Fibonacci sequence.
The Fibonacci sequence is an infinite sequence where each number is the sum
of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13, ...
"""


def fibonacci(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.

    This is the recommended method with O(n) time complexity and O(1) space complexity.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)

    Returns:
        int: The nth Fibonacci number

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
        >>> fibonacci(20)
        6765
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_sequence(length):
    """
    Generate a list of Fibonacci numbers up to the specified length.

    Args:
        length (int): The number of Fibonacci numbers to generate

    Returns:
        list: A list of Fibonacci numbers

    Examples:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci_sequence(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if length <= 0:
        return []
    elif length == 1:
        return [0]

    sequence = [0, 1]
    for i in range(2, length):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence


if __name__ == "__main__":
    # Example usage
    print("Fibonacci Sequence Examples:")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fibonacci(20) = {fibonacci(20)}")
    print(f"fibonacci(30) = {fibonacci(30)}")
    print(f"\nFirst 15 Fibonacci numbers:")
    print(fibonacci_sequence(15))
