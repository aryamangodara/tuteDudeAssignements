def apply_discount(price, percent):
    discount_amount = price * (percent / 100)
    return price - discount_amount

def flat_discount(price):
    return price - 50