# 1. Create a parallel list of categories and convert to a set
categories = ["Electronics", "Accessories", "Accessories", "Electronics", "Audio", "Accessories"]
categories_set = set(categories)
print("Initial set:", categories_set)

# 2. Add a new category and show duplicates are ignored
categories_set.add("Storage")
categories_set.add("Audio")  # 'Audio' is already in the set; it will be ignored
print("Set after additions:", categories_set)

# 3. Check whether a category exists (returns a boolean)
category_exists = "Electronics" in categories_set
print("Does 'Electronics' exist?", category_exists)

# Extra (optional): Get total number of unique categories
total_unique = len(categories_set)
print("Total unique categories:", total_unique)