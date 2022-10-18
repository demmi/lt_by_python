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
# 2) git init - во вкладке Terminal запускаем команду, чтобы создать репозиторий в папке, где лежит файл
# 3) запускаем git status и видим в репозитории служебную папку .idea/, она тут не нужна
# 4) создаем файл: .gitignore и в него записываем файлы, которые нужно игнорировать: .idea/
# 5) git status - проверяем статус в Terminal, видим измененные файлы красного цвета
# 6) Changes not staged for commit - изменения, не подготовлены для фиксации
# 7) git add . для отслеживания (индексирования) всех (.) файлов в папке или git add <file> для одного файла
# или git restore <file>, чтобы отменить изменения в рабочем каталоге
# 8) git status проверяем статус в Terminal, видим индексированные файлы зеленого цвета
# 9) git commit -m 'message' помещение всех изменений в репозиторий (-m это флаг для сообщения при фиксации)
# 10) git log - смотрим лог по всем коммитам: автор, дата, сообщение, HEAD -> указатель на последний коммит,
# master это основная ветка репозитория (HEAD -> master)
# 11) git branch test1 - создаем параллельную версию репозитория, branch - ветка с именем test1
# 12) git checkout test1 - переходим на ветку test1 (- Switched to branch 'test1')
# 13) в ветке test1 добавляем новую функцию (subtract)
# 14) git add git_practice.py индексируем изменения в файле git_practice.py
# 15) git commit -m 'add subtract' помещаем измиенения в репозиторий, видим HEAD -> test1
# 16) git checkout master перейдем в master, обновим файл и увидим, что в нем нет добавленной функции subtract
# 17) git branch test2 - создаем еще одну ветку test2
# 18) git checkout test2 - переходим на ветку test2
# 19) в ветке test2 добавляем функцию (remain), git add ., git commit -m 'added remain', git log, видим HEAD -> test2
# 20) git branch - видим все ветки и где мы находимся (*):
# * master
#   test1
#   test2
# 21) git merge test1 объединим master, где мы находимся, и ветку test1:
# git_practice.py | 4 ++++
# 1 file changed, 4 insertions(+)
# 22) git merge test2 объединим master и ветку test2
# 23) CONFLICT (content): Merge conflict in git_practice.py
# Automatic merge failed; fix conflicts and then commit the result.
# 24) git checkout test2
# error: you need to resolve your current index first (вам нужно разобраться с текущим индексом сначала)
# git_practice.py: needs merge
# 25) git merge --abort (это отмена изменений test2)
# 26) git checkout master  переходим в мастер
# 27) вручную удаляем появившиеся метки: <<<<<<< HEAD, =======, >>>>>>> test2
# 28) git add .
# 29) git merge --continue  продолжить слияние
# 30) git commit -m 'merging'  помещаем измиенения в репозиторий
#
# ---------- GITHUB ----------
#
# ///// 2:17:00

