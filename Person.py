class Person:
    def __init__(self, name, surename, age):
        self.name = name
        self.surename = surename
        self.age = age

    def showMsg(self):
        print(f"jmenuji se {self.name} {self.surename} a je mi {self.age}")


clovek1 = Person("Pavel", "Nowak", 45)

clovek1.showMsg()