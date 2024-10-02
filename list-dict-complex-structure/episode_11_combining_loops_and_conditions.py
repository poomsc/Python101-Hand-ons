"""
Episode 11: Combining Loops and Conditions in Complex Structures

We can combine loops and conditions to perform more specific operations on nested data.

Example:
"""

university = {
    "departments": [
        {
            "name": "Computer Science",
            "courses": [
                {"id": "CS101", "students": 20},
                {"id": "CS202", "students": 15}
            ]
        },
        {
            "name": "Physics",
            "courses": [
                {"id": "PHY101", "students": 10},
                {"id": "PHY202", "students": 25}
            ]
        }
    ]
}

print("Example output:")
for dept in university["departments"]:
    print(f"Department: {dept['name']}")
    for course in dept['courses']:
        if course['students'] > 15:
            print(f"  Large course: {course['id']} with {course['students']} students")

"""
Assignment:
Expand your `zoo` dictionary:
- Add a "species" key to each animal, with values like "mammal", "bird", or "reptile"
- Use nested loops and a condition to print only the mammals in each area

Write your solution below:
"""

# Your code here
zoo = {
    "areas": [
        {
            "name": "Safari",
            "animals": [
                {"name": "Lion", "species": "mammal"},
                {"name": "Eagle", "species": "bird"},
                {"name": "Elephant", "species": "mammal"}
            ]
        },
        {
            "name": "Aquatic",
            "animals": [
                {"name": "Dolphin", "species": "mammal"},
                {"name": "Shark", "species": "fish"},
                {"name": "Penguin", "species": "bird"}
            ]
        }
    ]
}

# Use nested loops and a condition to print only the mammals in each area
# Your code here

# Tests
import doctest

def test_zoo_mammals():
    """
    >>> all('species' in animal for area in zoo['areas'] for animal in area['animals'])
    True
    >>> any(animal['species'] == 'mammal' for area in zoo['areas'] for animal in area['animals'])
    True
    >>> any(animal['species'] != 'mammal' for area in zoo['areas'] for animal in area['animals'])
    True
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Run the tests by executing: python -m doctest episode_11_combining_loops_and_conditions.py")