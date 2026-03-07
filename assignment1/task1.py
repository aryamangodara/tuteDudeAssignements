# Task 1: Product Collections (Lists & Tuples)

# 1. Create a list of products
products = ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse", "Monitor"]

# 2. Create a tuple for a sample product
sample_product = ("Laptop", 1200, "Electronics")

# 3. Print the 2nd and last product
print(products[1])
print(products[-1])

# 4. Append two new products and print updated list
products.append("Tablet")
products.append("Speaker")
print(products)

# Extra: Modify price by converting tuple -> list -> tuple
temp = list(sample_product)
temp[1] = 1100
sample_product = tuple(temp)
print(sample_product)