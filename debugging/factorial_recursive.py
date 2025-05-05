#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer recursively.

    Parameters:
        n (int): The non-negative integer for which to compute the factorial.

    Returns:
        int: The factorial of the input integer `n`. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the input from command line arguments and print the factorial
f = factorial(int(sys.argv[1]))
print(f)
