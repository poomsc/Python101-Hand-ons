"""
Episode 9: Conditional Looping

We can use if statements inside loops to filter or perform actions based on conditions.

Example:
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Example output:")
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")

"""
Assignment:
Using the `books` list from the previous exercise, add a "pages" key to each book dictionary. 
Then, write a loop that prints the title of books with more than 300 pages.

Write your solution below:
"""

# Your code here
books = [
    {"title": "Book1", "author": "Author1", "pages": 250},
    {"title": "Book2", "author": "Author2", "pages": 350},
    {"title": "Book3", "author": "Author3", "pages": 400}
]

# Write a loop to print titles of books with more than 300 pages
# Your code here

# Tests
import doctest

def test_books_pages():
    """
    >>> all('pages' in book for book in books)
    True
    >>> all(isinstance(book['pages'], int) for book in books)
    True
    >>> any(book['pages'] > 300 for book in books)
    True
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Run the tests by executing: python -m doctest episode_9_conditional_looping.py")