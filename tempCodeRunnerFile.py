from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()
    
    manager.add_product(Product("Laptop", 1200.99, 5))
    manager.add_product(Product("Mouse", 25.50, 15))
    manager.add_product(Product("Keyboard", 45.00, 10))
    manager.add_product(Product("Monitor", 250.75, 7))
    
    print("Available Products: ")
    manager.display_all_products()
    
    total_value = manager.total_inventory_value()
    print(f"Total Inventory Value: {total_value: .2f}$")