# Task 3: User Menu (while loop + break/continue)

orders = []

while True:
    print("\n--- Menu ---")
    print("1 — Add order amount")
    print("2 — Show all orders and totals")
    print("q — Quit")
    
    choice = input("Choose an action: ")
    
    # Exit condition
    if choice == 'q':
        print("Exiting program. Goodbye!")
        break
        
    # Add order condition
    elif choice == '1':
        amount_str = input("Enter order amount (integer): ")
        if amount_str.isdigit():
            orders.append(int(amount_str))
            print(f"Success: Added ${amount_str} to orders.")
        else:
            print("Error: Invalid amount. Please enter a number.")
            
    # Show orders condition
    elif choice == '2':
        if not orders:
            print("No orders have been added yet.")
        else:
            print("\n--- Order Totals ---")
            grand_total = 0
            
            for order in orders:
                # Re-using the discount logic from earlier tasks
                if order >= 2000:
                    discount = 0.15
                elif order >= 1500:
                    discount = 0.10
                elif order >= 1000:
                    discount = 0.07
                else:
                    discount = 0.0
                
                final_amount = order - (order * discount)
                grand_total += final_amount
                print(f"Order: ${order} | Discount: {int(discount * 100)}% | Final: ${final_amount:.2f}")
                
            print("-" * 20)
            print(f"Grand Total: ${grand_total:.2f}")
            
    # Invalid input condition
    else:
        print("Invalid choice. Please select 1, 2, or q.")
        # Re-show the menu immediately
        continue