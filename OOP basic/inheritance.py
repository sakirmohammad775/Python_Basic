class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def speed(self):
        pass
        

class Car(Vehicle):
    def __init__(self,brand,model,capacity):
        super().__init__(brand,model)
        self.capacity=capacity

class ElectricalCar(Car):
    def __init__(self, brand, model, capacity,battery_capacity):
        super().__init__(brand, model, capacity)
        self.battery_capacity=battery_capacity

class Bike:
    def __init__(self,brand,model,milage):
        self.milage=milage
        
        
bmw=Car("BMW","AB",7)

# print(bmw.brand,bmw.model,bmw.capacity)

tesla=ElectricalCar("Tesla","XB",7,10000)
print(tesla.brand,tesla.model,tesla.capacity,tesla.battery_capacity)