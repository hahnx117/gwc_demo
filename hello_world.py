#!/usr/bin/env python3
"""
Simple Hello World script that students can modify to practice with GitHub.
Instructions:
1. Run the script to see the current output
2. Modify the greeting or name
3. Commit your changes
4. Push to GitHub
"""

def say_hello(name="World"):
    """Return a greeting message."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Students can change the name here
    message = say_hello("GitHub")
    print(message)
    
    # They could also add their own message below
    print("I'm learning to use GitHub!")
