"""
Episode 5: Combining It All

Real-world data often combines all these concepts into more complex structures.

Example:
"""

university = {
    "name": "Python University",
    "departments": [
        {
            "name": "Computer Science",
            "courses": [
                {"id": "CS101", "name": "Intro to Programming", "students": ["Alice", "Bob"]}
            ]
        },
        {
            "name": "Mathematics",
            "courses": [
                {"id": "MATH201", "name": "Calculus", "students": ["Charlie", "David"]}
            ]
        }
    ]
}

print("Example output:")
print(f"Second student in CS101: {university['departments'][0]['courses'][0]['students'][1]}")

"""
Assignment:
1. Create a similar structure for a `zoo` with at least two areas, each containing a list of animals. 
   Each animal should be a dictionary with keys for "name" and "species".
2. Print the species of the second animal in the first area.

Write your solution below:
"""

# Your code here
zoo = {
    # Create the zoo structure here
}

# Print the species of the second animal in the first area
# Your code here

# Tests
import doctest

def test_zoo_structure():
    """
    >>> len(zoo['areas']) >= 2
    True
    >>> all(isinstance(area, dict) for area in zoo['areas'])
    True
    >>> all('name' in area and 'animals' in area for area in zoo['areas'])
    True
    >>> all(isinstance(area['animals'], list) for area in zoo['areas'])
    True
    >>> all(isinstance(animal, dict) for area in zoo['areas'] for animal in area['animals'])
    True
    >>> all('name' in animal and 'species' in animal for area in zoo['areas'] for animal in area['animals'])
    True
    >>> isinstance(zoo['areas'][0]['animals'][1]['species'], str)
    True
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Run the tests by executing: python -m doctest episode_5_combining_it_all.py")