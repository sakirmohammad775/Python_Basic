class Student :
    def __init__(self, name, age, grade ):
        self.name = name
        self.age = age
        self.grade = grade
    def __repr__(self)->str:
         return f'Teacher:{self.name},subject:{self.grade}'

alia=Student('alia rahman',9,1)
print(alia)