# 0x07. Python - Test-driven development

## Project Details

- **Language:** Python
- **Topics:** UnitTests, TDD (Test-driven development)
- **Author:** Guillaume
- **Weight:** 1
- **Project Start:** Jan 2, 2024 6:00 AM
- **Project End:** Jan 8, 2024 6:00 AM
- **Checker Release:** Jan 8, 2024 6:00 AM
- **Auto Review:** Will be launched at the deadline

## Concepts

For this project, focus on the following concept:

- Never forget a test

## Background Context

Important notice on intranet checks for Python projects:

- Write documentation (module(s) + function(s)) and tests first, before coding
- Intranet checks for Python projects won't be released before the first deadline to emphasize TDD
- Work together on test cases, but not in the implementation
- Don't trust the user, always think about all possible edge cases

## Resources

Read or watch:

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until "26.2.3.7. Warnings" included)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://www.tutorialspoint.com/unittest/)
- [Unittest module](https://docs.python.org/3/library/unittest.html)
- [Interactive and Non-interactive tests](https://www.codementor.io/@dankhan/python-unit-testing-to-write-test-cases-for-your-functions-r2k50dwee)

## Learning Objectives

After completing this project, you should be able to:

- Explain why Python programming is awesome
- Understand what an interactive test is
- Comprehend the importance of tests
- Know how to write Docstrings to create tests
- Write documentation for each module and function
- Understand the basic option flags to create tests
- Know how to find edge cases

## Copyright - Plagiarism

- Solutions for tasks must be created to meet the learning objectives
- Do not copy and paste someone else’s work
- Do not publish any content of this project
- Any form of plagiarism is strictly forbidden and will result in removal from the program

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- Files will be interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- The length of your files will be tested using wc

### Python Test Cases

- Allowed editors: vi, vim, emacs
- All files should end with a new line
- All test files should be inside a folder named `tests`
- Test files should be text files (extension: .txt)
- Tests should be executed by using the command: `python3 -m doctest ./tests/*`
- All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All functions should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (length will be verified)
- Work together on test cases to avoid missing any edge case – The Checker is checking for tests!

## Tasks

### 0. Integers addition (mandatory)

Write a function that adds 2 integers.

```python
def add_integer(a, b=98):
    """ 
    a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    """

Certainly! Here is a README.md document for your project:

markdown
Copy code
# 0x07. Python - Test-driven development

## Project Details

- **Language:** Python
- **Topics:** UnitTests, TDD (Test-driven development)
- **Author:** Guillaume
- **Weight:** 1
- **Project Start:** Jan 2, 2024 6:00 AM
- **Project End:** Jan 8, 2024 6:00 AM
- **Checker Release:** Jan 8, 2024 6:00 AM
- **Auto Review:** Will be launched at the deadline

## Concepts

For this project, focus on the following concept:

- Never forget a test

## Background Context

Important notice on intranet checks for Python projects:

- Write documentation (module(s) + function(s)) and tests first, before coding
- Intranet checks for Python projects won't be released before the first deadline to emphasize TDD
- Work together on test cases, but not in the implementation
- Don't trust the user, always think about all possible edge cases

## Resources

Read or watch:

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until "26.2.3.7. Warnings" included)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://www.tutorialspoint.com/unittest/)
- [Unittest module](https://docs.python.org/3/library/unittest.html)
- [Interactive and Non-interactive tests](https://www.codementor.io/@dankhan/python-unit-testing-to-write-test-cases-for-your-functions-r2k50dwee)

## Learning Objectives

After completing this project, you should be able to:

- Explain why Python programming is awesome
- Understand what an interactive test is
- Comprehend the importance of tests
- Know how to write Docstrings to create tests
- Write documentation for each module and function
- Understand the basic option flags to create tests
- Know how to find edge cases

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- Files will be interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- The length of your files will be tested using wc

### Python Test Cases

- Allowed editors: vi, vim, emacs
- All files should end with a new line
- All test files should be inside a folder named `tests`
- Test files should be text files (extension: .txt)
- Tests should be executed by using the command: `python3 -m doctest ./tests/*`
- All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All functions should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (length will be verified)
- Work together on test cases to avoid missing any edge case – The Checker is checking for tests!

## Tasks

### 0. Integers addition (mandatory)

Write a function that adds 2 integers.

def add_integer(a, b=98):
    """ 
    a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    """
1. Divide a matrix (mandatory)
Write a function that divides all elements of a matrix.

python
Copy code
def matrix_divided(matrix, div):
    """
    matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
    Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
    div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
    div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
    All elements of the matrix should be divided by div, rounded to 2 decimal places
    Returns a new matrix
    """
2. Say my name (mandatory)
Write a function that prints My name is <first name> <last name>.

python
Copy code
def say_my_name(first_name, last_name=""):
    """
    first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
    """
3. Print square (mandatory)
Write a function that prints a square with the character #.

python
Copy code
def print_square(size):
    """
    size is the size length of the square
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
    """
4. Text indentation (mandatory)
Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

python
Copy code
def text_indentation(text):
    """
    text must be a string, otherwise raise a TypeError exception with the message text must be a string
    There should be no space at the beginning or at the end of each printed line
    """
5. Max integer - Unittest (mandatory)
Write unittests for the function def max_integer(list=[]):.

python
Copy code
def max_integer(list=[]):
    """ 
    Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None
    """

