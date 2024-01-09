# 0x0B. Python - Input/Output

## Resources
Read or watch:
- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
- [Dive Into Python 3: Chapter 11. Files](https://diveintopython3.net/files.html) (until "11.4 Binary Files" (included))
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
- [Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)](https://automatetheboringstuff.com/2e/chapter8/)
- [All about py-file I/O](https://www.geeksforgeeks.org/read-json-file-using-python/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

### Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Tasks
### 0. Read file
Write a function that reads a text file (UTF8) and prints it to stdout:

def read_file(filename=""):
    """Read and print the content of a text file."""

# 0x0B. Python - Input/Output

## Resources
Read or watch:
- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
- [Dive Into Python 3: Chapter 11. Files](https://diveintopython3.net/files.html) (until "11.4 Binary Files" (included))
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
- [Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)](https://automatetheboringstuff.com/2e/chapter8/)
- [All about py-file I/O](https://www.geeksforgeeks.org/read-json-file-using-python/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

### Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Tasks
### 0. Read file
Write a function that reads a text file (UTF8) and prints it to stdout:

`def read_file(filename=""):
    """Read and print the content of a text file."""`
### 1. Write to a file
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

`def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters."""
`
### 2. Append to a file
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

```
def append_write(filename="", text=""):
    """Append a string to the end of a text file and return the number of characters added."""
```
### 3. To JSON string
Write a function that returns the JSON representation of an object (string):

```
def to_json_string(my_obj):
    """Return the JSON representation of an object."""
```
### 4. From JSON string to Object
Write a function that returns an object (Python data structure) represented by a JSON string:


```def from_json_string(my_str):
    """Return an object represented by a JSON string."""
```
### 5. Save Object to a file
Write a function that writes an Object to a text file, using a JSON representation:

```def save_to_json_file(my_obj, filename):
    """Write an Object to a text file using JSON representation."""
```
### 6. Create object from a JSON file
Write a function that creates an Object from a “JSON file”:
```
def load_from_json_file(filename):
    """Create an Object from a JSON file."""
```
### 7. Load, add, save
Write a script that adds all arguments to a Python list, and then save them to a file:


```./7-add_item.py```
### 8. Class to JSON
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:


```def class_to_json(obj):
    """Return the dictionary description with simple data structure for JSON serialization."""
```
### 9. Student to JSON
Write a class Student that defines a student by:

**Public instance attributes:**
* first_name
* last_name
* age
* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
* Public method  ```def to_json(self):```that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
```
class Student:
    """Define a student class."""
def to_json(self):
    """Retrieve a dictionary representation of a Student instance."""
```