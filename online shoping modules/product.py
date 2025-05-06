# product.py

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def restock(self, amount):
        self.quantity += amount

    def reduce_stock(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False

    def __repr__(self):
        return f"{self.name} (ID: {self.product_id}) - {self.quantity} in stock, ₹{self.price:.2f} each"
