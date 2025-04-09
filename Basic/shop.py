class Shop: #constructor
    cart=[] # cart is a class attribute
    def __init__(self,buyer):
        self.buyer=buyer
    
    def add_to_cart(self,item):
        self.cart.append(item)
        
meh = Shop('mehii')
meh.add_to_cart('apple')
meh.add_to_cart('apple')
print(meh.cart)

noss=Shop('noise')
noss.add_to_cart('samsung')
noss.add_to_cart('huwai')
print(noss.cart)
