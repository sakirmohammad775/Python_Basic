#customer
#employee
#admin

from abc import ABC
class User(ABC):
     def __init__(self, name,phone, email,address):
         self.name = name
         self.phone = phone
         self.email = email
         self.address = address
class Employee(User):
    def __init__(self, name, phone, email, address,age, designation, salary):
         