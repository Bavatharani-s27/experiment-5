# main.py

from product import Product
from sales import process_sale

# Create some products
inventory = {
    1: Product(1, "Pen", 50, 10.0),     # ₹10 per Pen
    2: Product(2, "Pencil", 30, 5.0),   # ₹5 per Pencil
}

# Restock Pens with 20 more
inventory[1].restock(20)  # Total: 70 Pens

# Sell 10 Pens
process_sale(inventory[1], 10)  # ₹100

# Sell 5 Pencils
process_sale(inventory[2], 5)   # ₹25

# Display inventory
for product in inventory.values():
    print(product)

