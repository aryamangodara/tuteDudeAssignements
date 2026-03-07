# control_flow_assignment.py

print("========== TASK 1: Discount Rules ==========")
user_input = input("Enter the order amount (integer): ")

if not user_input.isdigit():
    print("Error: Input must be a valid numeric integer.")
else:
    order_amount = int(user_input)
    
    # Apply discount rules
    if order_amount >= 2000:
        discount_rate = 0.15
    elif order_amount >= 1500:
        discount_rate = 0.10
    elif order_amount >= 1000:
        discount_rate = 0.07
    else:
        discount_rate = 0.0

    discount_amount = order_amount * discount_rate
    subtotal = order_amount - discount_amount
    tax_amount = subtotal * 0.05  # Optional 5% tax
    final_total = subtotal + tax_amount
    
    print(f"Original Amount : ${order_amount:.2f}")
    print(f"Discount        : -${discount_amount:.2f}")
    print(f"Subtotal        : ${subtotal:.2f}")
    print(f"Tax (5%)        : +${tax_amount:.2f}")
    print(f"Final Total     : ${final_total:.2f}")


print("\n========== TASK 2: Process Multiple Orders ==========")
task2_orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discounted_count = 0

print("Order Summary Table")
for amount in task2_orders:
    if amount >= 2000:
        rate = 0.15
        pct = "15%"
    elif amount >= 1500:
        rate = 0.10
        pct = "10%"
    elif amount >= 1000:
        rate = 0.07
        pct = "7%"
    else:
        rate = 0.0
        pct = "0%"
        
    discount = amount * rate
    final = amount - discount
    total_revenue += final
    
    if rate > 0:
        discounted_count += 1
        
    print(f"{amount} -> {pct} -> {final:.2f}")

print("-" * 25)
print(f"Total revenue: ${total_revenue:.2f}")
print(f"Discounted orders: {discounted_count}")


print("\n========== TASK 5: Loop Control ==========")
daily_sales = [200, 150, 0, 400, 50, -1, 300]
sales_total = 0

for sale in daily_sales:
    if sale == -1:
        print(f"Alert: Corrupted data ({sale}) encountered. Stopping loop.")
        break
    elif sale == 0:
        print("Notice: Zero sales. Skipping to next day.")
        continue
    elif sale > 0:
        sales_total += sale
        print(f"Processed: ${sale} | Running total: ${sales_total}")

print("-" * 25)
print(f"Final Total Sales: ${sales_total}")


print("\n========== TASK 3: User Menu ==========")
menu_orders = []

while True:
    print("\n--- Menu ---")
    print("1 — Add order amount")
    print("2 — Show all orders and totals")
    print("q — Quit")
    
    choice = input("Choose an action: ")
    
    if choice == 'q':
        print("Exiting program. Goodbye!")
        break
        
    elif choice == '1':
        amt_str = input("Enter order amount (integer): ")
        if amt_str.isdigit():
            menu_orders.append(int(amt_str))
            print(f"Success: Added ${amt_str}.")
        else:
            print("Error: Invalid amount. Please enter numbers only.")
            
    elif choice == '2':
        if not menu_orders:
            print("No orders have been added yet.")
        else:
            grand_total = 0
            for order in menu_orders:
                if order >= 2000:
                    disc = 0.15
                elif order >= 1500:
                    disc = 0.10
                elif order >= 1000:
                    disc = 0.07
                else:
                    disc = 0.0
                
                final_amt = order - (order * disc)
                grand_total += final_amt
                print(f"Order: ${order} | Final after discount: ${final_amt:.2f}")
                
            print("-" * 25)
            print(f"Grand Total: ${grand_total:.2f}")
            
    else:
        print("Invalid choice. Please try again.")
        continue