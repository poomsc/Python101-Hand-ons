"""
Episode 1: The Basics of Nested Structures

In Python, we often deal with complex data structures that combine dictionaries and lists. 
These are called nested structures because one data structure is "nested" inside another.

Example:
"""

student = {
    "name": "Alice",
    "grades": [90, 85, 88]
}

print("Example output:")
print(student)

"""
Assignment:
Create a dictionary called `book` with the following structure:
- Key "title" with a string value
- Key "author" with a string value
- Key "chapters" with a list of 3 chapter names

Write your solution below:
"""

# Your code here
book = {
    # Fill in the dictionary
}

# Tests
import doctest

def test_book_structure():
    """
    >>> 'title' in book
    True
    >>> isinstance(book['title'], str)
    True
    >>> 'author' in book
    True
    >>> isinstance(book['author'], str)
    True
    >>> 'chapters' in book
    True
    >>> isinstance(book['chapters'], list)
    True
    >>> len(book['chapters']) == 3
    True
    >>> all(isinstance(chapter, str) for chapter in book['chapters'])
    True
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Run the tests by executing: python -m doctest episode_1_basics_of_nested_structures.py")