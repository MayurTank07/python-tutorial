
class Employee:
    def __init__(self, id, name, sal):
        # protected variables
        self._id = id
        self._name = name
        self._sal = sal 

    def displayData(self):
        print(self._id)
        print(self._name)
        print(self._sal)

class XYZ(Employee):
    def __init__(self, id, name, sal):
        super().__init__(id, name, sal)

    def displayData(self):
        print(self._id)
        print(self._name)
        print(self._sal)

x1 = XYZ(101, "Dexter", 99999)
x1.displayData()

