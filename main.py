from cart import Cart
from product import Product
from product_manager import ProductManager
import random

def main():
    manager = ProductManager()
    
    manager.add_product(Product("Smartphone", 899.99, 10))  
    manager.add_product(Product("Wireless Mouse", 30.00, 20))  
    manager.add_product(Product("Mechanical Keyboard", 120.00, 5))  
    manager.add_product(Product("4K Monitor", 499.99, 8))
    
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