class Person:
    def __init__(self, name):
        self.__name = name

class Employee(Person):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.__salary = salary

    def get_income(self):
        return __salary

class Student(Person):
    def __init__(self, name, stipend):
        Person.__init__(self, name)
        self.__stipend = stipend

    def get_income(self):
        return self.__stipend

class WorkingStudent(Employee, Student):
    def __init__(self, name, slalary, stipend):
        Employee.__init__(self, name, slalary)
        Student.__init__(self, name, stipend)

