# Exception Handling Assignment

This repository contains the `exception_handling_assignment.py` script, which demonstrates various exception handling concepts in Python, including standard exceptions, custom exceptions, and context managers for file operations.

## How to Run
Ensure you have Python 3 installed. Run the script from your terminal or command prompt:

```bash
python exception_handling_assignment.py
```
The script runs sequentially through Tasks 1 to 5. Below are instructions on how to test the different edge cases for each task.

Task 1: Safe Division Utility
Test Valid Input: Enter 10 for numerator and 2 for denominator. (Expected: Result 5.0)

Test ValueError: Enter ten for numerator. (Expected: "Please enter a valid number.")

Test ZeroDivisionError: Enter 10 for numerator and 0 for denominator. (Expected: "Cannot divide by zero.")

Task 2: Bill Calculator
This task runs automatically against a hardcoded list: [120, 350, 'abc', 500, -200, 800].

Expected Output: It will skip 'abc' (TypeError) and -200 (ValueError), successfully adding the rest to reach a running total of 1770.

Task 3: Age Validator
Test Valid Input: Enter 25. (Expected: "Age 25 is valid.")

Test ValueError (Out of Range): Enter -5 or 150. (Expected: Custom error "Age must be between 1 and 120.")

Test ValueError (Type): Enter twenty. (Expected: Standard invalid literal error.)

Task 4: File Reader
Test Success: Create a file named test.txt in the same directory with at least 3 lines of text. Enter test.txt when prompted. (Expected: Prints the first 3 lines).

Test FileNotFoundError: Enter missing_file.txt. (Expected: "The file does not exist.")

Task 5: Safe Shopping Cart
Test Valid Input: Enter 10.50, then 5.

Test ValueError (Type): Enter apple. (Expected: "Invalid input. Please enter a numeric price.")

Test Custom Exception: Enter -10. (Expected: "Error: Price cannot be negative.")

To Exit: Enter q. (Expected: Prints the total items and the final bill).