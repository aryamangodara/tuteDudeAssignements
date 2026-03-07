# Task 5: Loop Control with Conditions (break & continue)

daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

print("--- Processing Daily Sales ---")

for sale in daily:
    # Check for corrupted data first
    if sale == -1:
        print(f"Alert: Corrupted data ({sale}) encountered. Stopping processing immediately.")
        break  # Exits the for loop completely
        
    # Check for zero sales
    elif sale == 0:
        print(f"Notice: Zero sales recorded for this period. Skipping.")
        continue  # Skips the rest of this iteration and moves to the next item
        
    # Process valid positive sales
    elif sale > 0:
        total_sales += sale
        print(f"Processed valid sale: ${sale} | Running total: ${total_sales}")

# Print the final result after the loop finishes (or breaks)
print("-" * 30)
print(f"Final Total Sales: ${total_sales}")