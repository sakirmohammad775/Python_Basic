class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart=[]
        
    def add_to_cart(self,item,price,quantity):
        product={'item':item ,'price':price,'quantity':quantity}
        self.cart.append(product)
    
    def checkout(self,amount):
        total=0
        for item in self.cart:
            # print(item)
            total+=item['price']*item['quantity']
        print('total price',total)
        if total>amount:
            print( f'please provide{total}')

sakib=Shopping('alen')
sakib.add_to_cart('alu',60,4)
print(sakib.cart)
sakib.checkout(1600)