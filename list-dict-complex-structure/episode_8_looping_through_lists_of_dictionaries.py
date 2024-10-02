"""
Episode 8: Looping Through Lists of Dictionaries

When we have a list of dictionaries, we can use nested loops to access the data.

Example:
"""

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 21}
]

print("Example output:")
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}")

"""
Assignment:
Create a list called `books` with three book dictionaries. Each book should have "title" and "author" keys. 
Use a for loop to print each book's title and author.

Write your solution below:
"""

# Your code here
books = [
    # Create a list of 3 book dictionaries
]

# Use a for loop to print each book's title and author
# Your code here

# Tests
import doctest

def test_books_list():
    """
    >>> len(books) == 3
    True
    >>> all('title' in book and 'author' in book for book in books)
    True
    >>> all(isinstance(book['title'], str) and isinstance(book['author'], str) for book in books)
    True
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Run the tests by executing: python -m doctest episode_8_looping_through_lists_of_dictionaries.py")