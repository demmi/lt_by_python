# OOP. GIT. GITHUB
# ----- Создаем класс Employee с атрибутами (параметрами) name, surname
# class Employee:
#     def __init__(self, name, surname):  # __init__ это конструктор
#         self.name = name  # задаем атрибут name
#         self.surname = surname  # задаем атрибут surname
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
# ----- Принцип наследования -----
# class Employee:  # Создаем класс Employee
#     def __init__(self, name, surname):
#         self.name = name  # задаем атрибуты
#         self.surname = surname
#
#     def walk(self):  # создаем метод (функцию, действие) класса
#         return 'I can walk!'
#
#
# employee1 = Employee('Alex', 'Smith')  # создаем employee1, объект класса Employee
# print(employee1.name)  # Alex
# print(employee1.walk())  # I can walk! Он уже имеет walk(), метод класса Employee
#
#
# class Developer(Employee):  # создаем подкласс Developer в классе Employee
#     def __init__(self, name, surname, language):  # вводим в подкласс свой атрибут, language
#         super().__init__(name, surname)  # super(), ссылка на родительский класс с его атрибутами
#         self.language = language
#
#     def coding(self):  # даем подклассу свой метод, coding
#         return 'I am coding!'
#
#
# class Tester(Employee):
#     def __init__(self, name, surname, language, test_framework):  # вводим свой атрибут, test_framework
#         super().__init__(name, surname)  # super(), ссылка на родительский класс с его атрибутами
#         self.language = language
#         self.test_framework = test_framework
#
#     def testing(self):
#         return 'I can write tests!'
#
#
# dev1 = Developer('Max', 'Frolov', 'Python')  # Создаем dev1, объект подкласса Developer
# print(dev1.name)  # Max
# print(dev1.language)  # Python
# print(dev1.walk())  # I can walk! - объект подкласса унаследовал метод родительского класса
# print(dev1.coding())  # I am coding!
# print(type(dev1))  # <class '__main__.Developer'>
#
# tester1 = Tester('Anna', 'Fisher', 'Java', 'TestNG')
# print(tester1.name, tester1.surname)  # Anna Fisher
# print(tester1.language)  # Java
# print(tester1.test_framework)  # TestNG
# print(tester1.walk())  # I can walk!
# print(tester1.testing())  # I can write tests!
#
# print(isinstance(dev1, Developer))  # True, dev1 есть объект подкласса Developer
# print(issubclass(Developer, Employee))  # True, Developer есть подкласс класса Employee
#
# ----- Полиморфизм -----
# Полиморфизм это разное поведение метода в разных классах
# class Employee:  # Создаем класс Employee
#     def __init__(self, name, surname):
#         self.name = name  # задаем атрибуты
#         self.surname = surname
#
#     def work(self):  # создаем метод (функцию, действие) класса
#         return 'I am working!'
#
#
# class Developer(Employee):  # создаем подкласс Developer в классе Employee
#     def __init__(self, name, surname, language):  # вводим в подкласс свой атрибут, language
#         super().__init__(name, surname)  # super(), ссылка на родительский класс с его атрибутами
#         self.language = language
#
#     def work(self):
#         return 'I am coding!'  # даем подклассу свою реализацию общего метода work
#
#     def get_language(self):
#         return f'My language is {self.language}'
#
#
# class Tester(Employee):
#     def __init__(self, name, surname, language, test_framework):  # вводим свой атрибут, test_framework
#         super().__init__(name, surname)  # super(), ссылка на родительский класс с его атрибутами
#         self.language = language
#         self.test_framework = test_framework
#
#     def work(self):
#         return 'I am testing!'
#
#
# # --- у объектов один и тот же метод work, но действия заданы разные:
#
# employee1 = Employee('Alex', 'Smith')  # создаем employee1, объект класса Employee
# print(employee1.name)  # Alex
# print(employee1.work())  # I am working!
#
# dev1 = Developer('Max', 'Frolov', 'Python')  # Создаем dev1, объект подкласса Developer
# print(dev1.name)  # Max
# print(dev1.work())  # I am coding!
# print(dev1.get_language())  # My language is Python
#
# tester1 = Tester('Anna', 'Fisher', 'Java', 'TestNG')
# print(tester1.name, tester1.surname)  # Anna Fisher
# print(tester1.language)  # Java
# print(tester1.work())  # I am testing!
#
# ----- Инкапсуляция -----
# Уровни доступа к данным:
# 1. Public (self.language = language)
# 2. Protected (self._language = language) - с одним нижним подчеркиванием
# 3. Private (self.__language = language) - с двумя нижними подчеркиваниями
# class Employee:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def work(self):
#         return 'I am working!'
#
#
# class Developer(Employee):
#     def __init__(self, name, surname, language):
#         super().__init__(name, surname)
#         self.__language = language  # двумя нижними подчеркиваниями доступ к атрибуту делаем Private
#
#     def get_language(self):
#         return f'My language is {self.__language}'
#
#     def set_language(self, newlang):  # чтоб самому изменить защищенный атрибут задаем метод set
#         self.__language = newlang
#
#
# dev1 = Developer('Max', 'Frolov', 'Python')  # Создаем dev1, объект подкласса Developer
# print(dev1.name)  # Max
# print(dev1.get_language())  # My language is Python
#
# # --- Из-за приватного режима доступа извне к атрибуту language не будет:
# # print(dev1.language)  # AttributeError: 'Developer' object has no attribute 'language'
# # print(dev1.__language)  # AttributeError: 'Developer' object has no attribute '__language'.
#
# # --- Меняем атрибут language с помощью метода set:
# dev1.set_language('Java')  # даем новое значение Java атрибуту language
# print(dev1.get_language())  # My language is Java
# # --- Выведем ля проверки атрибуты объекта dev1:
# print(dev1.__dict__)  # {'name': 'Max', 'surname': 'Frolov', '_Developer__language': 'Java'}
#
# dev2 = Developer('Alice', 'Brown', 'Go')  # создаем новый объект dev2
# dev2.premium = 200  # задаем атрибут только для dev2
# print(dev2.__dict__)  # {'name': 'Alice', 'surname': 'Brown', '_Developer__language': 'Go', 'premium': 200}

# ---------- Система контроля версий ----------
# GIT - консольная утилита для ведения истории изменения файлов.
# 1) открываем в PyCharm файл git_practice, который нужно добавить в репозиторий
# 2) во вкладке Terminal запускаем команду git init, чтобы сделать git репозиторий в папке, где лежит файл
# 3) запускаем git status и видим в репозитории служебную папку .idea/, она тут не нужна
# 4) создаем новый файл .gitignore и в него записываем файлы, которфе нужно игнорировать: .idea/
# 5) проверяем через git status
#

# ///// 1:33:45
