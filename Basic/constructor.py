class phone:
    manufactured='China'
    
    def __init__(self,owner,brand,price): # constructor
        self.owner=owner
        self.brand=brand
        self.price=price
    
    def send_sms(self,phone,sms):
        text=f'sending to:{phone}{sms}'
        print(text)
        
my_phone=phone('rahim','apple',900)
print(my_phone.owner,my_phone.brand,my_phone.price)

her_phone=phone('k','sam',800)
print( her_phone.owner,her_phone.brand,her_phone.price)