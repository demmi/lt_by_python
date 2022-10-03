class Employee:
    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary

    def reputaion(self):
        return "is always on time."

    def sal(self):
        return f"{self.name}'s salary is"


class President(Employee):
    def __init__(self, name, lastname, salary, function):
        super().__init__(name, lastname, salary)
        self.__function = function

    def func(self):
        return f"{self.name}'s function is {self.__function} the company."


class Assistent(Employee):
    def __init__(self, name, lastname, salary, function):
        super().__init__(name, lastname, salary)
        self.function = function

    def func(self):
        return f"{self.name}'s function is {self.function} the company."


employee_1 = Employee("John", "Smith", "$10000.")
funct1 = President("John", "Smith", "$10000.", "to manage")
print(funct1.name, funct1.reputaion(), funct1.func(), funct1.sal(), funct1.salary)
employee_2 = Employee("Sarah", "Adamson", "$2000.")
funct2 = Assistent("Sarah", "Adamson", "$2000.", "to make phone calls for")
print(funct2.name, funct2.reputaion(), funct2.func(), funct2.sal(), funct2.salary)
# print(employee_1.name, employee_1.lastname, employee_1.position, employee_1.salary)
# print(employee_2.name, employee_2.lastname, employee_2.position, employee_2.salary)
