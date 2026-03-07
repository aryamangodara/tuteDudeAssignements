# ==========================================
# Task 1 - Basic Function: Price After Discount
# ==========================================
def apply_discount(price, discount_percent=5):
    # Extra (optional): Ensure discount never exceeds 60%
    if discount_percent > 60:
        discount_percent = 60
    
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

print("--- Task 1 ---")
print(f"Discount (1000, 10%): {apply_discount(1000, 10)}")
print(f"Discount (500, default 5%): {apply_discount(500)}")


# ==========================================
# Task 2 - Recursive Function: Factorial Utility
# ==========================================
def factorial(n):
    if n < 0:
        print("Error: Cannot calculate factorial of a negative number.")
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\n--- Task 2 ---")
print(f"factorial(5): {factorial(5)}")
print(f"factorial(0): {factorial(0)}")
print("factorial(-3): ", end="")
factorial(-3)


# ==========================================
# Task 3 - Lambda Function: GST Calculator
# ==========================================
gst = lambda price: price + (0.18 * price)

# Extra (optional): Lambda to compute final price after GST + discount
final_price_calc = lambda price, discount: gst(price - (price * (discount / 100)))

print("\n--- Task 3 ---")
print(f"Price after GST (100): {gst(100)}")


# ==========================================
# Task 4 - Using map(): Apply GST to List of Prices
# ==========================================
prices_task4 = [100, 250, 400, 1200, 50]
prices_with_gst = list(map(gst, prices_task4))

print("\n--- Task 4 ---")
print(f"Original prices: {prices_task4}")
print(f"Prices after GST: {prices_with_gst}")


# ==========================================
# Task 5 - Using filter(): Filter Expensive Products
# ==========================================
prices_task5 = [100, 250, 400, 1200, 50, 2000, 850]

prices_greater_than_500 = list(filter(lambda p: p > 500, prices_task5))
prices_less_or_equal_500 = list(filter(lambda p: p <= 500, prices_task5))

print("\n--- Task 5 ---")
print(f"Prices > 500: {prices_greater_than_500}")
print(f"Prices <= 500: {prices_less_or_equal_500}")


# ==========================================
# Task 6 - Combined Utility Function
# ==========================================
def process_prices(prices):
    # Map + lambda to apply 10% discount
    discounted_prices = list(map(lambda p: p - (p * 0.10), prices))
    # Filter to keep discounted prices > 300
    filtered_prices = list(filter(lambda p: p > 300, discounted_prices))
    
    return discounted_prices, filtered_prices

print("\n--- Task 6 ---")
test_prices = [100, 500, 900, 50, 750]
discounted, filtered = process_prices(test_prices)
print(f"Discounted prices: {discounted}")
print(f"Filtered prices (> 300): {filtered}")


# ==========================================
# Task 7 - Mini Problem: Menu Using Functions
# ==========================================
def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    if not prices_list:
        return 0
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    if not prices_list:
        return 0
    return max(prices_list)

def menu():
    current_prices = []
    while True:
        print("\n=== Pricing Menu ===")
        print("1 -> Add price")
        print("2 -> Show average price")
        print("3 -> Show highest price")
        print("q -> Quit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            try:
                p = float(input("Enter price to add: "))
                add_price(current_prices, p)
                print(f"Success! Added {p} to the list.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            print(f"Average price: {get_average_price(current_prices):.2f}")
        elif choice == '3':
            print(f"Highest price: {get_max_price(current_prices)}")
        elif choice == 'q':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")

# Note: The menu is commented out by default so it doesn't interrupt 
# the grading execution of Tasks 1-6. Remove the '#' to test it interactively!
# print("\n--- Task 7 ---")
# menu()