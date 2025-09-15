# Python - Classes and Objects

## Table of Contents
- [Table of Tasks](#table-of-tasks)  
- [Learning Objectives](#learning-objectives)  
- [Requirements](#requirements)  
- [Resources](#resources)  

---

## Table of Tasks

| #  | Task name                   | Description                                                                 | File             |
|----|-----------------------------|-----------------------------------------------------------------------------|------------------|
| 0  | My first square             | Write an empty class `Square` that defines a square.                        | `0-square.py`    |
| 1  | Square with size            | Add a private instance attribute `size`. Instantiation with size (no checks). | `1-square.py`    |
| 2  | Size validation             | Add validation: size must be an integer ≥ 0.                                | `2-square.py`    |
| 3  | Area of a square            | Add method `area()` to compute and return square area.                       | `3-square.py`    |
| 4  | Access and update attribute | Add `@property` getter and setter for `size` with validation.               | `4-square.py`    |
| 5  | Printing a square           | Add method `my_print()` that prints the square with `#`, or empty line if 0. | `5-square.py`    |
| 6  | Coordinates of a square     | Add attribute `position` (tuple of 2 positive ints) to control printing.     | `6-square.py`    |

---

## Learning Objectives

- What is OOP  
- What does “first-class everything” mean  
- What is a class  
- What is an object and an instance  
- Difference between a class and an object/instance  
- What is an attribute  
- How to use public, protected and private attributes  
- What is `self`  
- What is a method  
- What is the special `__init__` method and how to use it  
- What is Data Abstraction, Data Encapsulation, and Information Hiding  
- What is a property  
- Difference between an attribute and a property in Python  
- The Pythonic way to write getters and setters  
- How to dynamically create arbitrary new attributes for existing instances  
- How to bind attributes to objects and classes  
- What is the `__dict__` of a class and/or instance and what it contains  
- How Python finds the attributes of an object or class  
- How to use the `getattr` function  

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`  
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3 (version 3.8.5)`  
- All files should end with a new line  
- The first line of all files should be exactly `#!/usr/bin/python3`  
- A `README.md` file at the root of the project folder is mandatory  
- Your code should use **pycodestyle (version 2.7.*)**  
- All files must be executable  
- File length will be tested using `wc`  
- All modules must have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)  
- All classes must have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)  
- All functions (inside and outside a class) must have documentation  
- A documentation is a **real sentence** explaining the purpose of the module/class/method (not just one word)  

---

## Resources

Read or watch:  
- [Object Oriented Programming](https://python.swaroopch.com/oop.html) *(Read until “Inheritance”, excluded)*  
- [Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/) *(Intro, minimal class, attributes, methods, `__init__`, public/protected/private attributes)*  
- [Properties vs. Getters and Setters](https://www.programiz.com/python-programming/property)  
- [Learn to Program 9: Object Oriented Programming](https://www.youtube.com/watch?v=apACNr7DC_s)  
- [Python Classes and Objects (Official Docs)](https://docs.python.org/3/tutorial/classes.html)  
- [Object Oriented Programming - Python Course](https://www.geeksforgeeks.org/python-classes-and-objects/)  
