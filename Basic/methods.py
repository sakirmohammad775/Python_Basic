class Phone:
    price=12000
    color='blue'
    brand='samsung'
    features=['camera','speaker','hammer']
    def call():
        print('calling one person')
my_phone=Phone()
print(my_phone.features)
my_phone.brand