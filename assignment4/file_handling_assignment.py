import os

def main():
    # ---------------------------------------------------------
    # Task 1: Write Sales Records to a File
    # ---------------------------------------------------------
    print("--- Task 1: Write Sales Records to a File ---")
    sales = [1200, 450, 980, 1500, 3000]
    
    # Writing sales to the file (each on a new line)
    with open("sales_data.txt", "w") as file:
        for sale in sales:
            file.write(f"{sale}\n")
            
    # Reopen and print contents
    with open("sales_data.txt", "r") as file:
        print("Contents of sales_data.txt:")
        print(file.read())


    # ---------------------------------------------------------
    # Task 2: Read File in Different Ways
    # ---------------------------------------------------------
    print("--- Task 2: Read File in Different Ways ---")
    
    # 1. Read entire file using .read()
    with open("sales_data.txt", "r") as file:
        print("1. Using .read():")
        print(file.read())
        
    # 2. Read first line using .readline()
    with open("sales_data.txt", "r") as file:
        print("2. Using .readline():")
        print(file.readline().strip()) # .strip() cleans up the newline character
        
    # 3. Read all lines using .readlines() and convert to integers
    with open("sales_data.txt", "r") as file:
        lines = file.readlines()
        int_list = [int(line.strip()) for line in lines]
        print(f"3. Using .readlines() converted to integers:\n{int_list}\n")


    # ---------------------------------------------------------
    # Task 3: Append New Sales
    # ---------------------------------------------------------
    print("--- Task 3: Append New Sales ---")
    new_sales = [5000, 2500, 1700]
    
    # Append to the file
    with open("sales_data.txt", "a") as file:
        for sale in new_sales:
            file.write(f"{sale}\n")
            
    # Reopen and print entire updated file
    with open("sales_data.txt", "r") as file:
        lines = file.readlines()
        print("Updated contents of sales_data.txt:")
        # Print content cleanly
        for line in lines:
            print(line.strip())
            
        # Extra (optional): Print total number of lines
        print(f"\n[Extra] Total number of lines: {len(lines)}\n")


    # ---------------------------------------------------------
    # Task 4: Generate Summary Report from File
    # ---------------------------------------------------------
    print("--- Task 4: Generate Summary Report from File ---")
    with open("sales_data.txt", "r") as file:
        # Read and convert to integers inside list comprehension
        sales_values = [int(line.strip()) for line in file.readlines()]
        
    total_sales = sum(sales_values)
    highest_sale = max(sales_values)
    lowest_sale = min(sales_values)
    average_sale = total_sales / len(sales_values)
    
    print(f"Total Sales: {total_sales}")
    print(f"Highest Sale: {highest_sale}")
    print(f"Lowest Sale: {lowest_sale}")
    print(f"Average Sale: {average_sale:.2f}\n")


    # ---------------------------------------------------------
    # Task 5: Create Product Info File (User Input)
    # ---------------------------------------------------------
    print("--- Task 5: Create Product Info File ---")
    products = []
    
    # Ask user for 3 product names and prices
    for i in range(3):
        name = input(f"Enter product {i+1} name: ")
        price = input(f"Enter product {i+1} price: ")
        products.append((name, price))
        
    # Write to products.txt
    with open("products.txt", "w") as file:
        for name, price in products:
            file.write(f"{name} | {price}\n")
            
    # Read and print the file
    print("\nContents of products.txt:")
    with open("products.txt", "r") as file:
        for line in file:
            print(line.strip())
    print()


    # ---------------------------------------------------------
    # Task 6: Read File Safely 
    # ---------------------------------------------------------
    print("--- Task 6: Read File Safely ---")
    filename = input("Enter a filename to open (e.g., sales_data.txt or nonexistent.txt): ")
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            print(f"\nContents of {filename}:")
            print(file.read())
    else:
        print("File not found. Please check the filename.\n")


    # ---------------------------------------------------------
    # Task 7: Mini Project - Export Discounted Prices
    # ---------------------------------------------------------
    print("--- Task 7: Mini Project - Export Discounted Prices ---")
    prices = {
        "Mouse": 500,
        "Keyboard": 800,
        "Monitor": 7000,
        "Pendrive": 400,
        "Camera": 5000
    }
    
    try:
        discount_percentage = float(input("Enter the discount percentage (e.g., 10 for 10%): "))
    except ValueError:
        print("Invalid input. Defaulting to 0% discount.")
        discount_percentage = 0.0
        
    discounted_prices_list = []
    
    # Write to discount_report.txt
    with open("discount_report.txt", "w") as file:
        for product, original_price in prices.items():
            discount_amount = original_price * (discount_percentage / 100)
            discounted_price = original_price - discount_amount
            discounted_prices_list.append(discounted_price)
            
            file.write(f"{product} | {original_price} | {discounted_price:.2f}\n")
            
        # Extra (optional): Write summary at the bottom
        total_items = len(prices)
        avg_discounted_price = sum(discounted_prices_list) / total_items
        file.write(f"\nTotal Items: {total_items}\n")
        file.write(f"Average Discounted Price: {avg_discounted_price:.2f}\n")
        
    # Read and print to terminal
    print("\nContents of discount_report.txt:")
    with open("discount_report.txt", "r") as file:
        print(file.read())


if __name__ == "__main__":
    main()