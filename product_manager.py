from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        
    def display_all_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product.display_info())
    
    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value
    
    def remove_product_by_name(self, product_name):
        product_to_remove = None
        for product in self.products:
            if product.name.lower() == product_name.lower():
                product_to_remove = product
                break
        
        if product_to_remove:
            self.products.remove(product_to_remove)
            print(f"Product '{product_name}' has been removed.")
        else:
            print(f"Product '{product_name}' not found.")    