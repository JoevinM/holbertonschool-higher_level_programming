# Python - More Classes

## Table of Contents
- [Table of Tasks](#table-of-tasks)  
- [Learning Objectives](#learning-objectives)  
- [Requirements](#requirements)  
- [Resources](#resources)  

---

## Table of Tasks  

| #  | Task name                  | Description                                                                  | File(s)                |
|----|----------------------------|------------------------------------------------------------------------------|-------------------------|
| 0  | Simple rectangle           | Write an empty class `Rectangle`                                              | `0-rectangle.py`        |
| 1  | Real definition of a rectangle | Class `Rectangle` with private attributes `width` and `height`, including getters and setters | `1-rectangle.py` |
| 2  | Area and Perimeter         | Add methods `area()` and `perimeter()` to the class                           | `2-rectangle.py`        |
| 3  | String representation      | Add `__str__` to print the rectangle with `#`                                 | `3-rectangle.py`        |
| 4  | Eval is magic              | Add `__repr__` to recreate a new instance with `eval()`                       | `4-rectangle.py`        |
| 5  | Detect instance deletion   | Print `"Bye rectangle..."` when an instance is deleted (`__del__`)            | `5-rectangle.py`        |
| 6  | How many instances         | Add class attribute `number_of_instances`                                     | `6-rectangle.py`        |
| 7  | Change representation      | Add class attribute `print_symbol` to change print representation             | `7-rectangle.py`        |
| 8  | Compare rectangles         | Add static method `bigger_or_equal(rect_1, rect_2)`                           | `8-rectangle.py`        |
| 9  | A square is a rectangle    | Add class method `square(size=0)` to create a square                          | `9-rectangle.py`        |

---

## Learning Objectives  

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General  
- Why Python programming is awesome  
- What is OOP  
- “first-class everything”  
- What is a class  
- What is an object and an instance  
- What is the difference between a class and an object or instance  
- What is an attribute  
- What are and how to use public, protected and private attributes  
- What is `self`  
- What is a method  
- What is the special `__init__` method and how to use it  
- What is Data Abstraction, Data Encapsulation, and Information Hiding  
- What is a property  
- What is the difference between an attribute and a property in Python  
- What is the Pythonic way to write getters and setters in Python  
- What are the special `__str__` and `__repr__` methods and how to use them  
- What is the difference between `__str__` and `__repr__`  
- What is a class attribute  
- What is the difference between an object attribute and a class attribute  
- What is a class method  
- What is a static method  
- How to dynamically create arbitrary new attributes for existing instances of a class  
- How to bind attributes to objects and classes  
- What is and what does contain `__dict__` of a class and of an instance of a class  
- How does Python find the attributes of an object or class  
- How to use the `getattr` function  

---

## Requirements  

### General  
- Allowed editors: `vi`, `vim`, `emacs`  
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3 (version 3.8.5)`  
- All files should end with a new line  
- The first line of all files should be exactly `#!/usr/bin/python3`  
- A `README.md` file at the root of the project is mandatory  
- Your code should use **pycodestyle (version 2.7.*)**  
- All your files must be executable  
- File length will be tested using `wc`  

---

## Resources  

Read or watch:  
- [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” excluded)  
- [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
- [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
- [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)
