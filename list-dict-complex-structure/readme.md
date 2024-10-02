# Python Nested Data Structures Tutorial

This tutorial series is designed to help you understand and work with complex nested data structures in Python. Each episode is contained in a separate Python file, focusing on a specific aspect of working with nested dictionaries and lists.

## Getting Started

1. Make sure you have Python installed on your system (Python 3.6 or higher is recommended).
2. Download all the Python files from this tutorial series.
3. You can run each file individually to see the examples and test your solutions.

## How to Use

1. Start with `episode1_basics_of_nested_structures.py` and work your way through the episodes in order.
2. Read the comments at the top of each file to understand the concept being taught.
3. Run the file to see the example output.
4. Complete the assignment in the section marked "Your code here".
5. Run the tests to check your solution.

## Running the Code

To run a Python file, open your terminal or command prompt, navigate to the directory containing the file, and type:
```python
python filename.py
```

Replace `filename.py` with the name of the specific episode file you want to run.

## Understanding and Running Tests

Each file includes tests written using Python's `doctest` module. These tests help verify that your solution meets the requirements.

To run the tests:

1. Complete the assignment in the file.
2. Save your changes.
3. In your terminal or command prompt, run:
```python
python -m doctest filename.py
```

Replace `filename.py` with the name of the file you're working on.

4. If you see no output, all tests have passed! If there are failing tests, you'll see output indicating which tests failed and why.

## Understanding Test Output

- No output means all tests passed.
- If you see output, it will look something like this:
```
Failed example:
len(book['chapters']) == 3
Expected:
True
Got:
False
```
This means the test expected your `book` dictionary to have exactly 3 chapters, but it found a different number.

## Tips for Completing Assignments

1. Read the assignment instructions carefully.
2. Look at the example provided in each file for guidance.
3. Pay attention to the structure of the data in the tests.
4. If you're stuck, try printing your data structure to see what it looks like.
5. Remember to run the tests after completing each assignment to check your work.

## Getting Help

If you're having trouble understanding a concept or passing a test, try:

1. Re-reading the comments and example in the file.
2. Printing your data structures to see what they look like.
3. Breaking down the problem into smaller steps.
4. Searching online for Python documentation on the concepts you're struggling with.

Happy coding, and enjoy your journey into nested data structures!

## Running the Example File

To better understand how the tests work, let's use the `basics_of_nested_structures.py` file as an example.

1. Open `basics_of_nested_structures.py` in a text editor.

2. You'll see three versions of the `book` dictionary: Initial, Successful, and Failed.

3. To run each version:
   - Uncomment the version you want to test (remove the `#` at the start of each line)
   - Make sure the other versions are commented out
   - Save the file
   - Run the file using: `python basics_of_nested_structures.py`

4. Initial Version Results:
   - You'll see multiple test failures because the dictionary is empty.
   - The output will show which tests failed and why.

5. Successful Version Results:
   - All tests will pass.
   - You'll see the message "All tests passed successfully!"

6. Failed Version Results:
   - You'll see a test failure because there are only 2 chapters instead of the required 3.
   - The output will show which specific test failed.

By running these different versions, you can see how the tests work and what they're checking for. This process will help you understand what's expected in your solutions for the assignments.