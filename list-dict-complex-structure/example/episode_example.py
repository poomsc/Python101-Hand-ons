"""
Episode 1: The Basics of Nested Structures

This file contains three versions:
1. Initial version (uncomment to run)
2. Successful version (uncomment to run)
3. Failed version (uncomment to run)

Uncomment one version at a time and run the file to see different outcomes.
"""

import doctest

# Example (always runs)
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
"""

# === Initial Version (uncomment to run) ===
book = {}  # Empty dictionary

# === Successful Version (uncomment to run) ===
# book = {
#     "title": "Python Basics",
#     "author": "John Doe",
#     "chapters": ["Introduction", "Data Types", "Functions"]
# }

# === Failed Version (uncomment to run) ===
# book = {
#     "title": "Python Basics",
#     "author": "John Doe",
#     "chapters": ["Introduction", "Data Types"]  # Only 2 chapters instead of 3
# }

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
    # Run the tests
    result = doctest.testmod()
    
    if result.failed == 0:
        print("\nAll tests passed successfully!")
    else:
        print(f"\n{result.failed} tests failed.")
    
    # Print the current state of the book dictionary
    print("\nCurrent 'book' dictionary:")
    print(book)