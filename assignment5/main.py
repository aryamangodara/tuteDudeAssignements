# --- Task 1: math_utils ---
import math_utils
from math_utils import square

print("--- Testing math_utils ---")
print(f"Add (10 + 5): {math_utils.add(10, 5)}")
print(f"Subtract (10 - 5): {math_utils.subtract(10, 5)}")
print(f"Square (4): {square(4)}\n")


# --- Task 2: string_utils ---
import string_utils

print("--- Testing string_utils ---")
sample_text = "hello world from python"
print(f"Original text: '{sample_text}'")
print(f"Capitalized: {string_utils.capitalize_words(sample_text)}")
print(f"Reversed: {string_utils.reverse_string(sample_text)}")
print(f"Word Count: {string_utils.word_count(sample_text)}\n")


# --- Task 4: Importing the Package in main.py ---
import shop_package.discount as disc
from shop_package.billing import calculate_total
# Importing apply_tax separately to fulfill the "Call every function" requirement
from shop_package.billing import apply_tax 

print("--- Testing shop_package ---")
# Testing discount.py functions
print(f"Apply Discount (10% off 1000): {disc.apply_discount(1000, 10)}")
print(f"Flat Discount (50 off 200): {disc.flat_discount(200)}")

# Testing billing.py functions
prices = [100, 200, 300]
total = calculate_total(prices)
print(f"Calculate Total ([100, 200, 300]): {total}")
print(f"Apply Tax (5% on 600): {apply_tax(total)}")