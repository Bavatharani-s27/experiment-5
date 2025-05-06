# sales.py

def process_sale(product, quantity):
    if product.reduce_stock(quantity):
        total = quantity * product.price
        print(f"Sold {quantity} x {product.name}. Total: ₹{total:.2f}")
        return total
    else:
        print(f"Insufficient stock for {product.name}.")
        return 0.0

