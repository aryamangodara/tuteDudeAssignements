# Python Modules & Packages Assignment

## Overview
This project demonstrates the core concepts of Python modules and packages. It features a structured directory layout with custom utility modules and a dedicated package for shop-related operations. 

As per the assignment restrictions, the codebase strictly uses simple functional logic and avoids Object-Oriented Programming (OOP), exception handling, and file I/O operations.

## Project Structure
The folder structure is organized as follows:

```text
modules_assignment/
│
├── main.py                # Main execution script testing all imports
├── math_utils.py          # Module for basic mathematical operations
├── string_utils.py        # Module for string manipulation
│
└── shop_package/          # Package containing shop-related modules
    ├── __init__.py        # Initializes the directory as a Python package
    ├── discount.py        # Module for calculating discounts
    └── billing.py         # Module for calculating totals and taxes