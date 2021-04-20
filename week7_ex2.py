class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)


class Employee(Person):
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        self.id = id

    def getID(self):
        print(self.id)


worker = Employee("동양", 65, 2019)
worker.getName()
worker.getAge()
worker.getID()