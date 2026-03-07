from abc import ABC, abstractmethod

# ==========================================
# Task 1, 2 & 6: Product Class (Base)
# ==========================================
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price  # Task 2: Private attribute
        self.category = category

    # Task 1: Method to print product details
    def get_info(self):
        print(f"Product: {self.name} | Category: {self.category} | Price: ${self.__price}")

    # Task 1: Extra optional method
    def apply_discount(self, percent):
        return self.__price - (self.__price * (percent / 100))

    # Task 2: Getter for price
    def get_price(self):
        return self.__price

    # Task 2: Setter for price
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Error: Price must be greater than 0.")

    # Task 6: Magic method for string representation
    def __str__(self):
        return f"Product({self.name}, {self.__price}, {self.category})"

    # Task 6: Operator overloading to combine prices
    def __add__(self, other):
        return self.get_price() + other.get_price()


# ==========================================
# Task 3: Inheritance (Single-Level)
# ==========================================
class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    # Overriding the base method
    def get_info(self):
        print(f"Electronic Product: {self.name} | Category: {self.category} | Price: ${self.get_price()} | Warranty: {self.warranty_years} years")


# ==========================================
# Task 4: Polymorphism
# ==========================================
class Laptop(Product):
    def get_info(self):
        print(f"[Laptop Style] Model: {self.name} - ${self.get_price()}")

class Mobile(Product):
    def get_info(self):
        print(f"[Mobile Style] Device: {self.name} - ${self.get_price()}")


# ==========================================
# Task 5: Abstraction
# ==========================================
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ${amount}")


# ==========================================
# Task 7: Mini Project - Inventory System
# ==========================================
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Removed {name} from inventory.")
                return
        print("Product not found.")

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        return total

    def show_all_products(self):
        for product in self.products:
            product.get_info()

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        print(f"\n--- Adding new product to {self.store_name} ---")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")
        new_product = Product(name, price, category)
        self.inventory.add_product(new_product)
        print("Product added successfully!")

    def show_summary(self):
        print(f"\n--- {self.store_name} Summary ---")
        print(f"Total Items: {len(self.inventory.products)}")
        print(f"Total Value: ${self.inventory.get_total_value()}")


# ==========================================
# Testing the Execution of All Tasks
# ==========================================
if __name__ == "__main__":
    print("--- TASK 1 & 2: Basic Class, Encapsulation ---")
    p1 = Product("Desk Chair", 150, "Furniture")
    p2 = Product("Notebook", 5, "Stationery")
    
    p1.get_info()
    p2.get_info()
    
    print(f"Discounted price of Desk Chair (10%): ${p1.apply_discount(10)}")
    
    print("Testing setter (Valid):")
    p2.set_price(10)
    p2.get_info()
    
    print("Testing setter (Invalid):")
    p2.set_price(-5)

    print("\n--- TASK 3: Inheritance ---")
    e_prod = ElectronicProduct("Blender", 45, "Appliances", 2)
    e_prod.get_info()

    print("\n--- TASK 4: Polymorphism ---")
    lap = Laptop("ThinkPad", 1200, "Computers")
    mob = Mobile("iPhone", 999, "Phones")
    
    devices = [lap, mob]
    for device in devices:
        device.get_info()

    print("\n--- TASK 5: Abstraction ---")
    cc_pay = CreditCardPayment()
    upi_pay = UPIPayment()
    
    cc_pay.process_payment(150.50)
    upi_pay.process_payment(20.00)

    print("\n--- TASK 6: Magic Methods ---")
    print(f"__str__ output: {p1}")
    print(f"__add__ output (Chair + Notebook): ${p1 + p2}")

    print("\n--- TASK 7: Simple Inventory System ---")
    my_store = Store("Tech Supermart")
    
    # We will simulate adding 3 products manually via the console as instructed
    print("Please enter details for 3 products to test the Store system:")
    for _ in range(3):
        my_store.add_new_product()
        
    my_store.show_summary()
    print("\nShowing all products in inventory:")
    my_store.inventory.show_all_products()
    
    # Testing __add__ on the newly added items (assuming at least 2 were added)
    if len(my_store.inventory.products) >= 2:
        prod_a = my_store.inventory.products[0]
        prod_b = my_store.inventory.products[1]
        print(f"\nCombined price of {prod_a.name} and {prod_b.name} using __add__: ${prod_a + prod_b}")