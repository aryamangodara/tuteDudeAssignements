# 1. Create a dictionary with at least 6 entries
price_dict = {
    "Laptop": 999.99,
    "Mouse": 25.50,
    "Keyboard": 45.00,
    "Monitor": 150.00,
    "Headphones": 80.00,
    "Webcam": 60.00
}

# 2. Write small code blocks for dictionary operations:

# Add a new product
price_dict["Microphone"] = 120.00

# Update the price of an existing product
price_dict["Mouse"] = 20.00

# Remove a product by name (handling the case when it does not exist)
product_to_remove = "Tablet"
if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(f"Removed '{product_to_remove}'")
else:
    print(f"Cannot remove '{product_to_remove}': Product not found in dictionary.")

# (Optional: actually remove one that exists to test)
if "Webcam" in price_dict:
    del price_dict["Webcam"]

# 3. Print the average price of all products
total_price = sum(price_dict.values())
num_products = len(price_dict)
average_price = total_price / num_products if num_products > 0 else 0

print(f"\nAverage Price: ${average_price:.2f}")

# Extra (optional): Print product with maximum and minimum prices
# Using the max() and min() functions with the 'key' argument mapped to dictionary values
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print(f"Most Expensive: {max_product} (${price_dict[max_product]:.2f})")
print(f"Least Expensive: {min_product} (${price_dict[min_product]:.2f})")