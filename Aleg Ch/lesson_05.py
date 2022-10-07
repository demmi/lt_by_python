# OOP. GIT. GITHUB
# ----- Создаем класс Employee с атрибутами (параметрами) name, surname
# class Employee:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# employee1 = Employee('Alex', 'Smith')  # Создаем объект класса Employee с конкретными аргументами
# print(employee1.name)  # Alex
# print(employee1.surname)  # Smith
#
# employee2 = Employee(surname='Anders', name='Nika')
# print(employee2.name)  # Nika
# print(employee2.surname)  # Anders
#
# ----- Принцип наследования
class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def walk(self):  # Создаем метод (функцию, действие) класса
        return 'I can walk!'

employee1 = Employee('Alex', 'Smith')
print(employee1.walk())  # I can walk!

class Developer(Employee):  # Создаем подкласс Developer в классе Employee


dev1 =

///// 26:50
