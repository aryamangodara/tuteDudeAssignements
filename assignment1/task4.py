# Setting up lists from previous tasks to make this block runnable
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Microphone"]
categories = ["Electronics", "Accessories", "Accessories", "Electronics", "Audio", "Audio"]

# 1. Create a list of tuples named catalog (product_name, price, category)
catalog = []
for i in range(len(products)):
    p_name = products[i]
    # Use .get() to safely pull the price, defaulting to 0.0 if not found
    p_price = price_dict.get(p_name, 0.0) 
    p_cat = categories[i]
    
    # Append the tuple to the catalog
    catalog.append((p_name, p_price, p_cat))

print("--- Catalog Created ---")
print(f"Total items in catalog: {len(catalog)}")

# 2. Create category_to_products dictionary
category_to_products = {}

for name, price, category in catalog:
    # If the category doesn't exist in our dict yet, add it with an empty list
    if category not in category_to_products:
        category_to_products[category] = []
        
    # Append the product name to the appropriate category list
    category_to_products[category].append(name)

# 3. Print all products that belong to the category with the max number of products
max_category = None
max_count = 0

# Iterate through the dictionary to find the longest list
for category, prod_list in category_to_products.items():
    if len(prod_list) > max_count:
        max_count = len(prod_list)
        max_category = category

print("\n--- Category Analysis ---")
print(f"Category with most products: '{max_category}' (Count: {max_count})")
print(f"Products in this category: {category_to_products[max_category]}")