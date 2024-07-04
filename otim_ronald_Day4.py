#inheritance in python
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
#demonstrating multilevel inheritance
class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed
        dog = Dog("Nugu", "42","brown")
        dog.breed


