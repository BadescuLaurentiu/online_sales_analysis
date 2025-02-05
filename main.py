from cart import Cart
from product import Product
from product_manager import ProductManager
import random

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
    
    manager.remove_product_by_name("Mouse")
    
    cart = Cart()
    
    selected_products = random.sample(manager.products, 3)
    
    for product in selected_products:
        quantity = random.randint(1, 3)
        cart.add_to_cart(product, quantity)
        
    cart.display_cart()
    total_value = cart.calculate_total()
    print(f"Total value of cart: {total_value: .2f}$")
    
if __name__ == "__main__":
    main()