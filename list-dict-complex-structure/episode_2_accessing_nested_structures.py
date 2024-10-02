"""
Episode 2: Accessing Nested Structures

To access elements in nested structures, we chain together square brackets [] or dot notation.

Example:
"""

student = {
    "name": "Alice",
    "grades": [90, 85, 88]
}

print("Example output:")
print(f"Student name: {student['name']}")
print(f"First grade: {student['grades'][0]}")

"""
Assignment:
Using the `book` dictionary you created in Episode 1, complete the following tasks:
1. Print the book's title
2. Print the second chapter name

Write your solution below:
"""

# Your code here
book = {
    "title": "Python Adventures",
    "author": "Coder McGee",
    "chapters": ["Basics", "Functions", "Classes"]
}

# Print book title
# Your code here

# Print second chapter name
# Your code here

# Tests
import doctest

def test_book_access():
    """
    >>> book['title']
    'Python Adventures'
    >>> book['chapters'][1]
    'Functions'
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Run the tests by executing: python -m doctest episode_2_accessing_nested_structures.py")