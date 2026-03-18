class Animal:
    def __init__(self,name):
        self.name = name

    def say(self):
        print("Animal is saying")

class Dog(Animal):
    def __init__(self,name,dog_name):
        super().__init__(name)
        self.dog_name = dog_name

    def say(self):
        print("Bow Bow")

class Cat(Animal):
    def say(self):
        print("Meow")

dog = Dog("Animal",'Rocky')
dog.say()
print(dog.name)
print(dog.dog_name)


