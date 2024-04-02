class Student:
    sepc = "devOps"
    def __init__(self, name, year):
        self.name =  name
        self.age = 2024 - year

student1 = Student("Pavel", 2000)
print(student1.name)
print(student1.age)

student2 = Student("Adam", 1999)
print(student2.name)
print(student2.age)
