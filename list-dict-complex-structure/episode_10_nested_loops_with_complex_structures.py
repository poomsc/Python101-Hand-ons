"""
Episode 10: Nested Loops with Complex Structures

For more complex nested structures, we might need to use nested loops.

Example:
"""

school = {
    "classes": [
        {"name": "Math", "students": ["Alice", "Bob"]},
        {"name": "Science", "students": ["Charlie", "David"]}
    ]
}

print("Example output:")
for class_info in school["classes"]:
    print(f"Class: {class_info['name']}")
    for student in class_info["students"]:
        print(f"  Student: {student}")

"""
Assignment:
Create a dictionary called `zoo` with the following structure:
- A key "areas" with a list value
- Each item in the "areas" list is a dictionary with keys "name" and "animals"
- "animals" is a list of animal names

Use nested loops to print each area name and the animals in that area.

Write your solution below:
"""

# Your code here
zoo = {
    "areas": [
        # Create at least 2 area dictionaries with name and animals
    ]
}

# Use nested loops to print each area name and its animals
# Your code here

# Tests
import doctest

def test_zoo_structure():
    """
    >>> 'areas' in zoo
    True
    >>> isinstance(zoo['areas'], list)
    True
    >>> len(zoo['areas']) >= 2
    True
    >>> all('name' in area and 'animals' in area for area in zoo['areas'])
    True
    >>> all(isinstance(area['animals'], list) for area in zoo['areas'])
    True
    >>> all(isinstance(animal, str) for area in zoo['areas'] for animal in area['animals'])
    True
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Run the tests by executing: python -m doctest episode_10_nested_loops_with_complex_structures.py")