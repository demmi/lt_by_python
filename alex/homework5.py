class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def speak(self):
        print("I am", self.__name, "and I am", self.get_age(), "years old")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__name = name
        self.__age = age
        self.__type = "dog"

    def speak(self):
        print(
            "I am",
            self.__name,
            "and I am a",
            self.__type,
            "and I'm",
            self.get_age(),
            "years old",
        )


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__name = name
        self.__age = age
        self.__type = "cat"

    def speak(self):
        print(
            "I am",
            self.__name,
            "and I am a",
            self.__type,
            "and I'm",
            self.get_age(),
            "years old",
        )


tim = Dog("Tim", 5)
tim.speak()

tom = Cat("Tom", 10)
tom.speak()
