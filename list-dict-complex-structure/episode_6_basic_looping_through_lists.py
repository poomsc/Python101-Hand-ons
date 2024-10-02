"""
Episode 6: Basic Looping Through Lists

Before we dive into complex structures, let's review basic looping through lists.

Example:
"""

fruits = ["apple", "banana", "cherry"]
print("Example output:")
for fruit in fruits:
    print(fruit)

"""
Assignment:
Create a list of five animals. Use a for loop to print each animal.

Write your solution below:
"""

# Your code here
animals = [
    # Create a list of 5 animals
]

# Use a for loop to print each animal
# Your code here

# Tests
import doctest

def test_animal_list():
    """
    >>> len(animals) == 5
    True
    >>> all(isinstance(animal, str) for animal in animals)
    True
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Run the tests by executing: python -m doctest episode_6_basic_looping_through_lists.py")