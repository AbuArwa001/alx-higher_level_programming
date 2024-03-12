# 0x13. JavaScript - Objects, Scopes and Closures

## Overview

This project is part of the SE Foundations curriculum and focuses on JavaScript concepts related to objects, scopes, and closures. The project includes several tasks that cover the creation and manipulation of objects, inheritance, and other advanced JavaScript features.

## Learning Objectives

- Understand the basics of JavaScript programming
- Create objects in JavaScript
- Understand the concepts of 'this' and 'undefined'
- Understand the importance of variable types and scope
- Learn about closures and prototypes in JavaScript
- Inherit an object from another
- Explore modern JavaScript features

## Resources

- JavaScript object basics
- Object-oriented JavaScript
- Class - ES6
- super - ES6
- extends - ES6
- Object prototypes
- Inheritance in JavaScript
- Closures
- this/self
- Modern JS

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the folder is mandatory
- Code should be semistandard compliant (Rules of Standard + semicolons on top)
- All files must be executable

## Setup

### Install Node 14:

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
Tasks
Rectangle #0
Write an empty class Rectangle that defines a rectangle.
Use the class notation for defining your class.
```

### Rectangle #1
Write a class Rectangle that defines a rectangle.

Use the class notation for defining your class.
The constructor must take 2 arguments w and h.
Initialize the instance attribute width with the value of w.
Initialize the instance attribute height with the value of h.
### Rectangle #2
Write a class Rectangle that defines a rectangle.

Use the class notation for defining your class.
The constructor must take 2 arguments w and h.
Initialize the instance attribute width with the value of w.
Initialize the instance attribute height with the value of h.
If w or h is equal to 0 or not a positive integer, create an empty object.
### Rectangle #3
Write a class Rectangle that defines a rectangle.

Use the class notation for defining your class.
The constructor must take 2 arguments w and h.
Initialize the instance attribute width with the value of w.
Initialize the instance attribute height with the value of h.
If w or h is equal to 0 or not a positive integer, create an empty object.
Create an instance method called print() that prints the rectangle using the character X.
### Rectangle #4
Write a class Rectangle that defines a rectangle.

Use the class notation for defining your class.
The constructor must take 2 arguments w and h.
Initialize the instance attribute width with the value of w.
Initialize the instance attribute height with the value of h.
If w or h is equal to 0 or not a positive integer, create an empty object.
Create an instance method called print() that prints the rectangle using the character X.
Create an instance method called rotate() that exchanges the width and the height of the rectangle.
Create an instance method called double() that multiples the width and the height of the rectangle by 2.
### Square #0
Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js.

Use the class notation for defining your class and extends.
The constructor must take 1 argument: size.
The constructor of Rectangle must be called (by using super()).
### Square #1
Write a class Square that defines a square and inherits from Square of 5-square.js.

Use the class notation for defining your class and extends.
Create an instance method called charPrint(c) that prints the rectangle using the character c.
If c is undefined, use the character X.
### Occurrences
Write a function that returns the number of occurrences in a list.

Prototype: exports.nbOccurences = function (list, searchElement)
Esrever
Write a function that returns the reversed version of a list.

Prototype: exports.esrever = function (list)
You are not allowed to use the built-in method reverse.
### Log me
Write a function that prints the number of arguments already printed and the new argument value.

Prototype: exports.logMe = function (item)
Number conversion
Write a function that converts a number from base 10 to another base passed as an argument.

Prototype: exports.converter = function (base)
You are not allowed to import any file.
You are not allowed to declare any new variable (var, let, etc.).
### Factor index
Write a script that imports an array and computes a new array.

Your script must import list from the file 100-data.js.
You must use a map.
A new list must be created with each value equal to the value of the initial list, multiplied by the index in the list.
Print both the initial list and the new list.
Sorted occurrences
Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

