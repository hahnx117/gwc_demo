#!/usr/bin/env python3
"""
Simple calculator script for GitHub practice.
Instructions:
1. Run the script to test existing operations
2. Add a new operation (like multiplication or division)
3. Commit your changes with a descriptive message
4. Push to GitHub
5. Create a pull request if working in teams
"""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

# TODO: Students can add multiplication and division functions


if __name__ == "__main__":
    print("Simple Calculator")
    print("=================")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    # Students can add their own function calls here
