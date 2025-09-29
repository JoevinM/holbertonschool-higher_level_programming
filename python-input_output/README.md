# Python - Input/Output

## Table of Contents
- [Table of Tasks](#table-of-tasks)  
- [Learning Objectives](#learning-objectives)  
- [Requirements](#requirements)  
- [Resources](#resources)  

---

## Table of Tasks

| #  | Task name                 | Description                                                                                     | File                  |
|----|---------------------------|-------------------------------------------------------------------------------------------------|-----------------------|
| 0  | Read file                 | Function `read_file(filename="")` that reads a text file (UTF8) and prints it to stdout.        | `0-read_file.py`      |
| 1  | Write to a file           | Function `write_file(filename="", text="")` that writes a string to a text file (UTF8).         | `1-write_file.py`     |
| 2  | Append to a file          | Function `append_write(filename="", text="")` that appends a string at the end of a text file.  | `2-append_write.py`   |
| 3  | To JSON string            | Function `to_json_string(my_obj)` that returns the JSON representation of an object (string).   | `3-to_json_string.py` |
| 4  | From JSON string to Object| Function `from_json_string(my_str)` that returns an object represented by a JSON string.        | `4-from_json_string.py` |
| 5  | Save Object to a file     | Function `save_to_json_file(my_obj, filename)` that writes an Object to a text file in JSON.    | `5-save_to_json_file.py` |
| 6  | Create object from a file | Function `load_from_json_file(filename)` that creates an Object from a JSON file.               | `6-load_from_json_file.py` |
| 7  | Load, add, save           | Script that adds all arguments to a Python list, then saves them to `add_item.json`.            | `7-add_item.py`       |
| 8  | Class to JSON             | Function `class_to_json(obj)` that returns the dictionary description for JSON serialization.   | `8-class_to_json.py`  |
| 9  | Student to JSON           | Class `Student` with attributes `first_name`, `last_name`, `age` and method `to_json()`.        | `9-student.py`        |
| 10 | Student to JSON with filter | Class `Student` with method `to_json(attrs=None)` (filtering attributes).                    | `10-student.py`       |
| 11 | Student to disk and reload | Class `Student` with methods `to_json(attrs=None)` and `reload_from_json(json)`.               | `11-student.py`       |
| 12 | Pascal’s Triangle         | Function `pascal_triangle(n)` that returns a list of lists of integers representing Pascal’s triangle. | `12-pascal_triangle.py` |

---

## Learning Objectives

- Why Python programming is awesome  
- How to open a file  
- How to write text in a file  
- How to read the full content of a file  
- How to read a file line by line  
- How to move the cursor in a file  
- How to make sure a file is closed after using it  
- What is and how to use the `with` statement  
- What is JSON  
- What is serialization  
- What is deserialization  
- How to convert a Python data structure to a JSON string  
- How to convert a JSON string to a Python data structure  
- How to access command line parameters in a Python script  

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`  
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3 (version 3.8.5)`  
- All files should end with a new line  
- The first line of all files should be exactly `#!/usr/bin/python3`  
- A `README.md` file at the root of the project folder is mandatory  
- Your code should use **pycodestyle (version 2.7.\*)**  
- All files must be executable  
- File length will be tested using `wc`  
- All modules must have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)  
- All classes must have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)  
- All functions (inside and outside a class) must have documentation  
- A documentation is a **real sentence** explaining the purpose of the module/class/method (not just one word)  

---

## Resources

Read or watch:

- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)  
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)  
- [Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)  
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)  
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)  
- [Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)](https://automatetheboringstuff.com/)
-[sys package](https://docs.python.org/3/library/sys.html)