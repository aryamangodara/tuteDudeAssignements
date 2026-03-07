# Task 1: Discount Rules

user_input = input("Enter the order amount (integer): ")

# Handle non-numeric input to prevent errors
if not user_input.isdigit():
    print("Error: Input must be a valid numeric integer. Exiting program.")
else:
    order_amount = int(user_input)
    
    # Determine the discount based on the rules
    if order_amount >= 2000:
        discount_rate = 0.15
        discount_pct_str = "15%"
    elif order_amount >= 1500:
        discount_rate = 0.10
        discount_pct_str = "10%"
    elif order_amount >= 1000:
        discount_rate = 0.07
        discount_pct_str = "7%"
    else:
        discount_rate = 0.0
        discount_pct_str = "0%"

    # Calculate subtotal
    discount_amount = order_amount * discount_rate
    subtotal = order_amount - discount_amount
    
    # Extra (optional): Add tax (fixed 5%)
    tax_rate = 0.05
    tax_amount = subtotal * tax_rate
    final_total = subtotal + tax_amount
    
    # Print the results
    print("-" * 30)
    print(f"Original Amount : ${order_amount:.2f}")
    print(f"Discount ({discount_pct_str:^3}): -${discount_amount:.2f}")
    print(f"Subtotal        : ${subtotal:.2f}")
    print(f"Tax (5%)        : +${tax_amount:.2f}")
    print(f"Final Total     : ${final_total:.2f}")# Task 1: Discount Rules

user_input = input("Enter the order amount (integer): ")

# Handle non-numeric input to prevent errors
if not user_input.isdigit():
    print("Error: Input must be a valid numeric integer. Exiting program.")
else:
    order_amount = int(user_input)
    
    # Determine the discount based on the rules
    if order_amount >= 2000:
        discount_rate = 0.15
        discount_pct_str = "15%"
    elif order_amount >= 1500:
        discount_rate = 0.10
        discount_pct_str = "10%"
    elif order_amount >= 1000:
        discount_rate = 0.07
        discount_pct_str = "7%"
    else:
        discount_rate = 0.0
        discount_pct_str = "0%"

    # Calculate subtotal
    discount_amount = order_amount * discount_rate
    subtotal = order_amount - discount_amount
    
    # Extra (optional): Add tax (fixed 5%)
    tax_rate = 0.05
    tax_amount = subtotal * tax_rate
    final_total = subtotal + tax_amount
    
    # Print the results
    print("-" * 30)
    print(f"Original Amount : ${order_amount:.2f}")
    print(f"Discount ({discount_pct_str:^3}): -${discount_amount:.2f}")
    print(f"Subtotal        : ${subtotal:.2f}")
    print(f"Tax (5%)        : +${tax_amount:.2f}")
    print(f"Final Total     : ${final_total:.2f}")