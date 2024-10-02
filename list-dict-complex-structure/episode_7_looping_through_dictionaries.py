"""
Episode 7: Looping Through Dictionaries

We can loop through dictionaries to access keys, values, or both.

Example:
"""

student = {"name": "Alice", "age": 20, "grade": "A"}

print("Example output:")
print("Keys:")
for key in student:
    print(key)

print("\nKey-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

"""
Assignment:
Create a dictionary representing a car with keys for "make", "model", and "year". 
Use a for loop to print each key-value pair in the format "The car's [key] is [value]."

Write your solution below:
"""

# Your code here
car = {
    # Create a dictionary representing a car
}

# Use a for loop to print each key-value pair
# Your code here

# Tests
import doctest

def test_car_dictionary():
    """
    >>> 'make' in car and 'model' in car and 'year' in car
    True
    >>> isinstance(car['year'], int)
    True
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
    print("Run the tests by executing: python -m doctest episode_7_looping_through_dictionaries.py")