
def msg():
    print("\n\nthis is msg from ModuleEx1.py")

def dexter():
    print("this is dexter")

class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("\n\nEmp name : ", self.name)
        print("Emp age : ", self.age)

class Std:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("\n\nStd name : ", self.name)
        print("Std age : ", self.age)