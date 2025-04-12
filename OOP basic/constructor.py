class shop:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, name, price):
        product=Product(name,price)
        self.products.append(product)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


shop1 = shop("top class")
shop1.add_product('mobile',40000)
shop1.add_product('laptop',50000)
print(shop1.products)
