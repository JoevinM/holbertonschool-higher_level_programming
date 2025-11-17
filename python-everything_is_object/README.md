# Python - Everything is Object

## Table of Contents
- [Table of Tasks](#table-of-tasks)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Description](#description)
- [What to Expect](#what-to-expect)

---

## Table of Tasks

| #  | Task name                                        | Description                                                                                                  | File                    |
|----|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------|
| 0  | Who am I?                                        | Write the function name used to print the type of an object.                                                 | `0-answer.txt`          |
| 1  | Where are you?                                   | Write the function name used to get a variable identifier (memory address in CPython).                       | `1-answer.txt`          |
| 2  | Right count                                      | Determine whether two integers refer to the same object.                                                     | `2-answer.txt`          |
| 3  | Right count =                                    | Determine whether identical integers point to the same object.                                               | `3-answer.txt`          |
| 4  | Right count =                                    | Determine whether a variable assigned to another refers to the same object.                                  | `4-answer.txt`          |
| 5  | Right count =+                                   | Determine whether an integer and its incremented value are the same object.                                  | `5-answer.txt`          |
| 6  | Is equal                                         | Compare two identical strings using `==`.                                                                    | `6-answer.txt`          |
| 7  | Is the same                                      | Check whether two identical strings are the exact same object.                                               | `7-answer.txt`          |
| 8  | Is really equal                                  | Compare two separately defined identical strings using `==`.                                                 | `8-answer.txt`          |
| 9  | Is really the same                               | Check whether two separately defined identical strings are the same object using `is`.                       | `9-answer.txt`          |
| 10 | And with a list, is it equal                     | Compare two lists with `==`.                                                                                 | `10-answer.txt`         |
| 11 | And with a list, is it the same                  | Check object identity of two distinct lists.                                                                  | `11-answer.txt`         |
| 12 | And with a list, is it really equal              | Compare a list and its alias using `==`.                                                                      | `12-answer.txt`         |
| 13 | And with a list, is it really the same           | Check if a list and its alias are the same object.                                                            | `13-answer.txt`         |
| 14 | List append                                      | Predict the output after mutating a list shared by two variables.                                             | `14-answer.txt`         |
| 15 | List add                                         | Predict the output when concatenating a list instead of mutating it.                                          | `15-answer.txt`         |
| 16 | Integer incrementation                           | Predict output of a function attempting to mutate an integer.                                                 | `16-answer.txt`         |
| 17 | List incrementation                              | Predict output of a function mutating a list passed as parameter.                                             | `17-answer.txt`         |
| 18 | List assignation                                 | Predict output of a function reassigning a parameter.                                                         | `18-answer.txt`         |
| 19 | Copy a list object                               | Implement a function returning a copy of a list.                                                              | `19-copy_list.py`       |
| 20 | Tuple or not?                                    | Determine whether `()` is a tuple.                                                                            | `20-answer.txt`         |
| 21 | Tuple or not?                                    | Determine whether `(1, 2)` is a tuple.                                                                        | `21-answer.txt`         |
| 22 | Tuple or not?                                    | Determine whether `(1)` is a tuple.                                                                           | `22-answer.txt`         |
| 23 | Tuple or not?                                    | Determine whether `(1,)` is a tuple.                                                                          | `23-answer.txt`         |
| 24 | Who I am?                                        | Determine whether two integers in parentheses refer to the same object.                                       | `24-answer.txt`         |
| 25 | Tuple or not                                     | Determine whether identical tuple definitions refer to the same object.                                       | `25-answer.txt`         |
| 26 | Empty is not empty                               | Determine whether two empty tuples are the same object.                                                       | `26-answer.txt`         |
| 27 | Still the same?                                  | Determine whether list concatenation creates a new object.                                                    | `27-answer.txt`         |
| 28 | Same or not?                                     | Determine whether list inplace addition mutates or replaces the object.                                       | `28-answer.txt`         |
| 29 | Python3: Mutable, Immutable... everything is object! | Write a full blog post covering the concepts in this project.                                                | `29-answer.txt` (URLs)  |

---

## Learning Objectives

### General
- What is an **object**
- Difference between a **class** and an **object/instance**
- Difference between **immutable** and **mutable** objects
- What is a **reference**
- What is an **assignment**
- What is an **alias**
- How to check if two variables are **identical** (`==`)
- How to check if two variables refer to the **same object** (`is`)
- How to display the **identifier** of an object (memory address)
- Built-in **mutable types**
- Built-in **immutable types**
- How Python **passes variables** to functions
- Implications for mutable vs immutable types when passed to functions

---

## Requirements

### Python Scripts
- Editors allowed: *vi, vim, emacs*
- Files interpreted using **Python 3.8.5** on Ubuntu 20.04 LTS
- Must end with a **new line**
- First line must be:


- Must follow **pycodestyle 2.7.\***
- Must be **executable**
- File length tested using `wc`

### .txt Answer Files
- Must contain **one single line**
- **No shebang**
- Must end with a **new line**

---

## Resources

Read or watch:

- [9.10. Objects and values](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
- [9.11. Aliasing](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
- [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
- [Mutation](https://www.composingprograms.com/pages/24-mutable-data.html#sequence-objects)
- [9.12. Cloning lists](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
- [Python tuples: immutable but potentially changing](https://www.oreilly.com/radar/)
---

## Description

In Python, **everything is an object**, including numbers, strings, lists, functions, classes, and more.
This project focuses on understanding how Python handles:

- references
- object identity
- equality vs identity
- mutability and immutability
- aliasing and assignment
- memory behavior with lists and tuples

You will analyze Python expressions and predict results without executing code at first, building a deep understanding of how Python stores and handles data internally.

---

## What to Expect

You will progressively learn to:
1. Understand how variables *really* work in Python.
2. Differentiate between **value equality** (`==`) and **object identity** (`is`).
3. Predict behavior when mutating vs reassigning objects.
4. Understand why some objects (like integers) can appear to be "shared" across variables.
5. Work with lists, tuples, integers, and strings in terms of memory and references.
6. Write a safe list-copying function.
7. Produce a complete blog post summarizing all learned concepts.

By the end, you’ll have a solid conceptual foundation of Python’s memory model — essential for debugging, interviews, and writing correct code.

---
