from itertools import product


class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class ShoppingCart:
    def __init__(self):
        self.cart=[]
    def add_product(self,product):
        self.cart.append(product)
        print(f"added{product. name}to the cart.")
    def remove_product(self,product_name):
        for product in self.cart:
            if product_name==product_name:
                self.cart.remove(product)
                print(f"product{product_name}not fount in the cart.")
                return
            print(f"product{product_name}not found in the cart.")
        def calculate_total(self):
            total=sum(product. price for product in self.cart)
            print(f"total amount:${total:2f}")

    product1=Product(name="laptop",price=999.99)
    product2=Product(name="Mouse",price=49.99)
    product3=Product(name="Keyword", price=79.99)

cart=ShoppingCart()
cart.add_product("laptop")
cart.add_product(mouse)
cart.add_product()
cart.remove_product("laptop")
cart.remove_product("Mouse")
cart.calculate_total()





