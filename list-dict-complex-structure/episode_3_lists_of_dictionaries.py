"""
Episode 3: Lists of Dictionaries

Often, we have lists containing multiple dictionaries. This is common when representing 
multiple objects of the same type.

Example:
"""

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22}
]

print("Example output:")
print(f"Second student's name: {students[1]['name']}")

"""
Assignment:
Create a list called `library` containing three book dictionaries. Each book should have 
"title" and "author" keys. Then, print the author of the second book.

Write your solution below:
"""

# Your code here
library = [
    # Fill in the list of dictionaries
]

# Print the author of the second book
# Your code here

# Tests
import doctest

def test_library_structure():
    """
    >>> len(library) == 3
    True
    >>> all('title' in book and 'author' in book for book in library)
    True
    >>> isinstance(library[1]['author'], str)
    True
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Run the tests by executing: python -m doctest episode_3_lists_of_dictionaries.py")