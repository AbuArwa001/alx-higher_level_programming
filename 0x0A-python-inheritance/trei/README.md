## Learning Objectives

- Explain why Python programming is awesome
- Understand concepts of superclass, baseclass, or parentclass
- Recognize subclasses
- List attributes and methods of a class or instance
- Determine when an instance can have new attributes
- Define a class with multiple base classes
- Identify the default class every class inherits from
- Override a method or attribute inherited from the base class
- Access attributes or methods available to subclasses by heritage
- Comprehend the purpose of inheritance
- Use `isinstance`, `issubclass`, `type`, and `super` built-in functions

## Requirements for Python Scripts

- Allowed editors: vi, vim, emacs
- Files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the project folder, is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- The length of files will be tested using wc

## Requirements for Python Test Cases

- Allowed editors: vi, vim, emacs
- Test files should be inside a folder named `tests`
- Test files should be text files (extension: .txt)
- All tests should be executed by using the command: `python3 -m doctest ./tests/*`
- All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- Documentation is not a simple word, it’s a real sentence explaining the purpose of the module, class, or method

## Tasks

### 0. Lookup

Write a function that returns the list of available attributes and methods of an object:

```
def lookup(obj):
    """Returns a list object"""
    pass
```
Usage:


lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
###  1. My list
Write a class MyList that inherits from list:



class MyList(list):
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        pass
Usage:



MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
###  2. Exact same object
Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.



def is_same_class(obj, a_class):
    pass
Usage:



is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
###  3. Same class or inherit from
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.



def is_kind_of_class(obj, a_class):
    pass
Usage:



is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
### 4. Only sub class of
Write a function that returns True if the object is an instance of the



class that inherited (directly or indirectly) from the specified class; otherwise `False`.


def inherits_from(obj, a_class):
    pass
Usage:



inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
5. Geometry module
Write an empty class BaseGeometry.



class BaseGeometry:
    pass
Usage:



BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))
###  6. Improve Geometry
Write a class BaseGeometry (based on 5-base_geometry.py).



class BaseGeometry:
    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
Usage:



BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
### 7. Integer validator
Write a class BaseGeometry (based on 6-base_geometry.py).



class BaseGeometry:
    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer"""
        pass
Usage:



BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
### 8. Rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).



class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Instantiation with width and height"""
        pass
Usage:



Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
### 9. Full rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).



class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Instantiation with width and height"""
        pass

    def area(self):
        """Calculates the area of the rectangle"""
        pass

    def __str__(self):
        """Returns the rectangle description"""
        pass
Usage:



Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())
### 10. Square #1
Write a class Square that inherits from Rectangle (9-rectangle.py).



class Square(Rectangle):
    def __init__(self, size):
        """Instantiation with size"""
        pass
Usage:



Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())
### 11. Square #2
Write a class Square that inherits from Rectangle (9-rectangle.py).



class Square(Rectangle):
    def __init__(self, size):
        """Instantiation with size"""
        pass

    def __str__(self):
        """Returns the square description"""
        pass
Usage:



Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
### 12. My integer
Write a class MyInt that inherits from int:



class MyInt(int):
    pass
Usage:



MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
### 13. Can I?
Write a function that adds a new attribute to an object if it’s possible:



def add_attribute(obj, name, value):
    """Raises a TypeError exception if the object can’t have a new attribute"""
    pass
Usage:



add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

