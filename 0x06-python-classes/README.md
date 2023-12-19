# 0x06. Python - Classes and Objects

## Description
This project introduces Object-Oriented Programming (OOP) concepts in Python. It covers topics such as classes, objects, attributes, methods, encapsulation, properties, and more.

## Resources
- [Object Oriented Programming](https://docs.python.org/3/tutorial/classes.html) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)
- [Object-Oriented Programming](https://python.swaroopch.com/oop.html) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
- [Properties vs. Getters and Setters](https://www.python-course.eu/python3_properties.php)
- [Learn to Program 9: Object-Oriented Programming](https://www.youtube.com/watch?v=apACNr7DC_s)
- [Python Classes and Objects](https://www.programiz.com/python-programming/class)

## Learning Objectives
- Understand the fundamentals of Object-Oriented Programming (OOP).
- Learn about classes, objects, and instances.
- Differentiate between public, protected, and private attributes.
- Implement properties, getters, and setters in Python.
- Explore data abstraction, data encapsulation, and information hiding.
- Understand the Pythonic way to write getters and setters.
- Work with class and instance attributes.
- Learn about the __dict__ attribute of a class and/or instance.
- Use the getattr function in Python.

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should follow PEP 8 style guide (check with pycodestyle)
- All modules should have documentation (check with `python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (check with `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (check with `python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation should be more than a simple word, it’s a real sentence explaining the purpose of the module, class, or method (length will be verified)

## Task List
1. **My first square**
   - Write an empty class `Square` that defines a square.

2. **Square with size**
   - Write a class `Square` that defines a square with a private instance attribute `size`.

3. **Size validation**
   - Update the `Square` class to include validation for the `size` attribute.

4. **Area of a square**
   - Add a public instance method `def area(self):` to the `Square` class that returns the current square area.

5. **Access and update private attribute**
   - Add a private instance attribute `size` to the `Square` class with a getter and setter method.

6. **Printing a square**
   - Extend the `Square` class to include a public instance method `def my_print(self):` that prints the square using the `#` character.

7. **Coordinates of a square**
   - Enhance the `Square` class to include a private instance attribute `position` and update the `my_print` method to include a space for the `position`.


