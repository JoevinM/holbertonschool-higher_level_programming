# Python - Inheritance

## Table of Contents
- [Table of Tasks](#table-of-tasks)  
- [Learning Objectives](#learning-objectives)  
- [Requirements](#requirements)  
- [Resources](#resources)  

---

## Table of Tasks  

| #  | Task name               | Description                                                                 | File(s) |
|----|-------------------------|-----------------------------------------------------------------------------|---------|
| 0  | Lookup                  | Function `lookup(obj)` that returns list of attributes and methods of object | `0-lookup.py` |
| 1  | My list                 | Class `MyList` that inherits from `list` and adds `print_sorted()`          | `1-my_list.py`, `tests/1-my_list.txt` |
| 2  | Exact same object       | Function `is_same_class(obj, a_class)`                                      | `2-is_same_class.py` |
| 3  | Same class or inherit   | Function `is_kind_of_class(obj, a_class)`                                   | `3-is_kind_of_class.py` |
| 4  | Only sub class of       | Function `inherits_from(obj, a_class)`                                      | `4-inherits_from.py` |
| 5  | Geometry module         | Empty class `BaseGeometry`                                                  | `5-base_geometry.py` |
| 6  | Improve Geometry        | Add `area()` method raising `Exception("area() is not implemented")`        | `6-base_geometry.py` |
| 7  | Integer validator       | Add `integer_validator(self, name, value)` method in `BaseGeometry`         | `7-base_geometry.py`, `tests/7-base_geometry.txt` |
| 8  | Rectangle               | Class `Rectangle` inheriting from `BaseGeometry`, validates `width`/`height`| `8-rectangle.py` |
| 9  | Full rectangle          | Implement `area()` and `__str__` in `Rectangle`                            | `9-rectangle.py` |
| 10 | Square #1               | Class `Square` inheriting from `Rectangle`, implements `area()`             | `10-square.py` |
| 11 | Square #2               | Modify `__str__` of `Square` to return `[Square] <size>/<size>`             | `11-square.py` |

---

## Learning Objectives  

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General  
- What is a superclass, baseclass or parentclass  
- What is a subclass  
- How to list all attributes and methods of a class or instance  
- When can an instance have new attributes  
- How to inherit class from another  
- How to define a class with multiple base classes  
- What is the default class every class inherit from  
- How to override a method or attribute inherited from the base class  
- Which attributes or methods are available by heritage to subclasses  
- What is the purpose of inheritance  
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions  

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

### Python Test Cases  
- Allowed editors: `vi`, `vim`, `emacs`  
- All files should end with a new line  
- All test files should be inside a folder **tests**  
- All test files should be text files (extension: `.txt`)  
- All your tests should be executed by using this command:  
  ```bash
  python3 -m doctest ./tests/*

---

## Ressources

Read or watch:

- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://www.packtpub.com/en-us/learning/how-to-tutorials/inheritance-python/)
- [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)