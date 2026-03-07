# Task 2: Process Multiple Orders

orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discounted_orders_count = 0

print("Order Summary Table")
print("-" * 35)

# Loop through each order in the list
for order_amount in orders:
    
    # Apply discount rules
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
        
    # Compute the final amount for this order
    discount_amount = order_amount * discount_rate
    final_amount = order_amount - discount_amount
    
    # Add to total revenue
    total_revenue += final_amount
    
    # Extra (optional): Track how many orders got a discount
    if discount_rate > 0:
        discounted_orders_count += 1
        
    # Print summary row for the current order
    print(f"{order_amount} -> {discount_pct_str} -> {final_amount:.2f}")

print("-" * 35)
# Print final aggregates
print(f"Total revenue after discounts: ${total_revenue:.2f}")
print(f"Orders receiving a discount: {discounted_orders_count}")