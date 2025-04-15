# customer
# employee
# admin

from abc import ABC


class User(ABC):  ##english talking youtube
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address) # calling the parent class constructor
        
    def add_employee(self, restaurant):
        restaurant.add_employee(self) # adding employee to the restaurant
    
    def view_employee(self,restaurant): # view all employees in database
        restaurant.view_employee()
      
class Restaurant:
    def __init__(self,name):
        self.name = name
        self.employees = []  # Database of employees
        
    def add_employee(self,employee):
        self.employees.append(employee) # add employee to database
       
class Menu:
    def __init__(self):
        self.items=[] # items er database
    
    def add_menu_item(self,item):
        self.items.append(item) # add item to database

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower()==item_name.lower():
                return item
        return None
    
    def remove_item(self,item_name):
        item=self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("item deleted")
        else:
            print("item not found")

ad=Admin("karim","123123","karim","Dhaka")
ad.add_employee("Rahim","rahim@gmail.com","123456","Dhaka",32,"chef",12000)
ad.view_employee()