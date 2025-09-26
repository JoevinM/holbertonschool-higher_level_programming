# Python - Abstract Classes and Interfaces

## Table of Contents
- [Table of Tasks](#table-of-tasks)  
- [Learning Objectives](#learning-objectives)  
- [Requirements](#requirements)  
- [Resources](#resources)  

---

## Table of Tasks

| #  | Task name                           | Description                                                                                       | File                     |
|----|-------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------|
| 0  | Abstract Animal Class               | Create an abstract class `Animal` with abstract method `sound()`. Subclasses: `Dog` → `"Bark"`, `Cat` → `"Meow"`. | `task_00_abc.py`         |
| 1  | Shapes and Duck Typing              | Create abstract class `Shape` with `area()` and `perimeter()`. Implement `Circle` and `Rectangle`. Use `shape_info()` with duck typing. | `task_01_duck_typing.py` |
| 2  | Extending the Python List           | Implement `VerboseList` extending `list`, overriding `append`, `extend`, `remove`, and `pop` to print notifications. | `task_02_verboselist.py` |
| 3  | CountedIterator                     | Create `CountedIterator` to wrap an iterable, count items iterated with `get_count()`. Override `__next__`. | `task_03_countediterator.py` |
| 4  | The Enigmatic FlyingFish            | Implement `FlyingFish` using multiple inheritance from `Fish` and `Bird`. Override methods for custom behavior. | `task_04_flyingfish.py`  |
| 5  | The Mystical Dragon (Mixins)        | Create `SwimMixin` and `FlyMixin`. Implement `Dragon` inheriting from both, with method `roar()`. | `task_05_dragon.py`      |

---

## Learning Objectives

-Abstract Classes: Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.
-Interfaces and Duck Typing: Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.
-Subclassing Standard Base Classes: Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.
-Method Overriding: Employ method overriding to alter or enhance the behavior of base class methods.
-Multiple Inheritance: Understand and apply multiple inheritance to form complex relationships between classes.
-Mixins: Utilize mixins to compose behavior across unrelated classes.
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
- Documentation must be a **real sentence** explaining the purpose of the module/class/method  

---

## Resources

Read or watch:  
- [Python 3 Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)  
- [ABC — Abstract Base Classes](https://docs.python.org/3/library/abc.html)  
- [Real Python - OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)  
- [Duck Typing in Python](https://realpython.com/lessons/duck-typing/)  
- Corey Schafer - [OOP Playlist (YouTube)](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)  
- Sentdex - [Python OOP Tutorial (YouTube)](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfhTF3Zfyzc_yD-Mq9iTp4G)  

---
