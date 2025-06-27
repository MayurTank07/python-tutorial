

class Employee:  
    def __init__(self, id, name, sal):
        self.id = id
        self.__name = name
        self._sal = sal 

    def displayName(self):
        print(self.__name)

e1 = Employee(101, "dexter", 99999)

print(e1.id)
e1.displayName()
print(e1.sal)