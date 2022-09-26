class Animal:
    def __init__(self, name):
        self.name = name
        self.weight = 0

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.weight = 10

    def speak(self):
        print("woof")


class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.weight = 4

    def speak(self):
        print("meow")



animal = Animal("animal")
animal.speak()
print(animal.weight)

dog = Dog("dog")
dog.speak()
print(dog.weight)

cat = Cat("cat")
cat.speak()
print(cat.weight)

