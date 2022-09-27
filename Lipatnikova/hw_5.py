class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("woof")


class Cat(Animal):
    def __init__(self, name, age, food):
        super(Cat, self).__init__(name, age)
        self.food = food

    def speak(self):
        print("meow")


dog = Dog("Tom", 1, 'black')
dog.speak()
print(f'My name is {dog.name}, my age: {dog.age}, my color is {dog.color}')

cat = Cat("Den", 2, 'wiskas')
cat.speak()
print(f'My name is {cat.name}, my age: {cat.age}, I love to eat {cat.food}')

