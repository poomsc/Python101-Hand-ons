"""
Episode 4: Nested Dictionaries

Dictionaries can contain other dictionaries, allowing for complex data representation.

Example:
"""

school = {
    "name": "Python High",
    "classes": {
        "math": {"teacher": "Mr. Newton", "room": 105},
        "science": {"teacher": "Mrs. Curie", "room": 201}
    }
}

print("Example output:")
print(f"Science teacher: {school['classes']['science']['teacher']}")

"""
Assignment:
Expand your `book` dictionary to include a "publisher" key. The value for "publisher" 
should be another dictionary with keys for "name" and "year". Then, print the publisher's year.

Write your solution below:
"""

# Your code here
book = {
    "title": "Python Adventures",
    "author": "Coder McGee",
    "chapters": ["Basics", "Functions", "Classes"],
    "publisher": {
        # Add publisher details here
    }
}

# Print the publisher's year
# Your code here

# Tests
import doctest

def test_book_publisher():
    """
    >>> 'publisher' in book
    True
    >>> isinstance(book['publisher'], dict)
    True
    >>> 'name' in book['publisher']
    True
    >>> 'year' in book['publisher']
    True
    >>> isinstance(book['publisher']['year'], int)
    True
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Run the tests by executing: python -m doctest episode_4_nested_dictionaries.py")