#!/usr/bin/env python3
"""
Word counter script for GitHub practice.
Instructions:
1. Run the script with a text file
2. Add functionality (counting characters, most common words, etc.)
3. Commit changes with a descriptive message
4. Push to GitHub
5. Practice creating branches for new features
"""

def count_words(filename):
    """Count the number of words in a file."""
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

def create_sample_file(filename="sample.txt"):
    """Create a sample text file if needed."""
    with open(filename, 'w') as file:
        file.write("""This is a sample text file.
It contains a few lines of text.
Students can use this to test the word counter program.
They can also modify this program to count characters or find the most common word.
Learning GitHub is fun and practical!""")
    print(f"Created sample file: {filename}")


if __name__ == "__main__":
    import sys
    
    # Create a sample file if none is provided
    if len(sys.argv) < 2:
        filename = "sample.txt"
        create_sample_file(filename)
    else:
        filename = sys.argv[1]
    
    # Count words
    word_count = count_words(filename)
    if isinstance(word_count, int):
        print(f"The file '{filename}' contains {word_count} words.")
    else:
        print(word_count)
    
    # TODO: Students can add more features here
    # For example: count characters, count lines, find most common words, etc.
