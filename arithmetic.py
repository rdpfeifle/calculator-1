"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of num1 and num2."""
    sum = num1 + num2

    return sum

def subtract(num1, num2):
    """Return the value of num1 minus num2."""

    minus = num1 - num2

    return minus

def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""

    product = num1 * num2

    return product

def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""

    division = num1 / num2
    return division

def square(num1):
    """Return the square of num1."""

    squared = num1 * num1
    return squared

def cube(num1):
    """Return the cube of num1."""

    cubed = num1 * num1 * num1
    return cubed


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    powered = num1 ** num2
    return powered

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    
    remainder = num1 % num2
    return remainder 

def add_mult(num1, num2, num3):
    """Get the sum of num1 and num2, then multiply sum with num3."""
    sum_mult = (num1 + num2) * num3
    return sum_mult

def add_cubes(num1, num2):
    """Add the cubes of num1 and num2."""
    cubed_num1 = num1 * num1 * num1
    cubed_num2 = num2 * num2 * num2
    sum_cubes = cubed_num1 + cubed_num2

    return sum_cubes