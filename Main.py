class Student:
    sepc = "devOps"
    def __init__(self, name, age):
        self.name =  name
        self.age = age
    def showMsg(self):
        print(f"moje jmeno je {self.name} a muj vek je {self.age}")

    def sayHi(self, greeting):
        print(f"{greeting}, ja jsem{self.name}")

    def checkAlcohol(self):
        if self.age < 18:
            alccheck = False
        else:
            alccheck = True
        return print(alccheck)

student = Student(" Adam", 17)
student1 = Student(" Osel", 55)

# student.showMsg()
# student1.sayHi("ahoj")
# student1.sayHi("dobrý denk")
# student.checkAlcohol()




# student1 = Student("Pavel", 2000)
# print(student1.name)
# print(student1.age)
#
# student2 = Student("Adam", 1999)
# print(student2.name)
# print(student2.age)
