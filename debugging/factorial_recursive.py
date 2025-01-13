#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function calculates the factorial of a given number n recursively.

    Parameters:
    n (int): The number for which the factorial is to be calculated. 
             It must be a non-negative integer.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive call to calculate factorial of (n-1)

# Taking input from command line argument, converting it to an integer and calculating the factorial
f = factorial(int(sys.argv[1]))

# Printing the calculated factorial
print(f)
