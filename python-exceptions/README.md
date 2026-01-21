# Python - Exceptions

This project focuses on **Errors and Exceptions** in Python and how to write safe and robust code using:

- `try / except`  
- `try / except / finally`  
- Raising built-in exceptions  
- Printing errors to `stderr`  

All scripts are compatible with **Ubuntu 20.04 LTS** using **Python 3.8.5** and follow **pycodestyle 2.7.\***.

---

## Learning Objectives

By the end of this project, you should be able to:

- Understand why Python programming is awesome  
- Differentiate between **errors** and **exceptions**  
- Explain what exceptions are and how to use them  
- Know when and why exceptions are needed  
- Correctly handle exceptions in code  
- Understand the purpose of catching exceptions  
- Raise built-in exceptions effectively  
- Use `finally` for clean-up or guaranteed actions  

---

## Requirements

- Python 3.8.5  
- All files must end with a new line  
- First line of all files: `#!/usr/bin/python3`  
- A `README.md` file is mandatory  
- All files must be executable  
- File length may be tested using `wc`  

---

## Directory Structure

**Repository:** `holbertonschool-higher_level_programming`  
**Directory:** `python-exceptions`

---

## Tasks Overview

### **0) 0-safe_print_list.py — Safe list printing**
**Goal:** Print up to `x` elements from a list safely and return the number of elements actually printed.  
**Key idea:** Use a loop with `try/except IndexError` to stop when the list ends. Do not use `len()`; rely on exceptions to detect out-of-range.

### **1) 1-safe_print_integer.py — Safe integer printing**
**Goal:** Print a value as an integer using `"{:d}".format()`.  
**Key idea:**  
- Formatting succeeds → it's an integer → return `True`  
- Formatting fails (`TypeError` / `ValueError`) → return `False`  

### **2) 2-safe_print_list_integers.py — Print only integers**
**Goal:** Access the first `x` elements of a list and print only integers, returning how many were printed.  
**Key idea:**  
- Loop through indexes `0..x-1`  
- Try printing each element with `"{:d}".format()`  
- Skip non-integers silently (catch `TypeError` / `ValueError`)  
- **Do not catch `IndexError`**  

### **3) 3-safe_print_division.py — Division with debug (finally)**
**Goal:** Divide `a / b`, return the result or `None`, and always print a debug line.  
**Key idea:**  
- Use `try` to compute division  
- Catch `ZeroDivisionError`  
- Use `finally` to print: `Inside result: <result>`  

### **4) 4-list_division.py — Divide two lists safely**
**Goal:** Divide elements of two lists safely and return a new list with the results.  
**Key idea:**  
- Loop through each index `i`:  
  - Try `my_list_1[i] / my_list_2[i]`  
  - Handle exceptions:  
    - `TypeError` → print "wrong type" and append `0`  
    - `ZeroDivisionError` → print "division by 0" and append `0`  
    - `IndexError` → print "out of range" and append `0`  
- Use `finally` to always append a result for each index  

### **5) 5-raise_exception.py — Raise TypeError**
**Goal:** Write a function that raises a `TypeError`.  
**Key idea:** Use `raise TypeError`.

### **6) 6-raise_exception_msg.py — Raise NameError with a message**
**Goal:** Raise a `NameError` with a custom message.  
**Key idea:** Use `raise NameError(message)`.


**Author**
**Raghad Almalki**
