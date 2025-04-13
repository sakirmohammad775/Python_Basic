
class shop:

    def __init__(self, name):
        self.name = name
        self.products = []
        self.__balance = 500 # private attribute
        self._owner='Mr. X '

    def add_product(self, name, price):
        product = Product(name, price)
        self.products.append(product)

    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return f"This is a shop with the name {self.name}"

class subShop(shop):
    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name


shop1 = shop("top class")
shop1.add_product("mobile", 40000)
shop1.add_product("laptop", 50000)

shop2 = shop("top class 2")
shop2.add_product("keyboard", 40000)
shop2.add_product("mouse", 50000)

print(shop2._owner)

"""
brac bank [class attribute]
- account number
- account holder name [ instance attribute]
"""