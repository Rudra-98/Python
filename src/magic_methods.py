# "Dunder" means Double underscore. They are special methods Python calls automatically behind the scenes.


#__init__ — called when an object is created (constructor)

class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Bruno")  # __init__ is automatically called


#__str__ — called when you print() an object
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog's name is {self.name}"


d = Dog("Bruno")
print(d)  # Dog's name is Bruno

#__len__ — called when you use len() on an object

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


m = MyList([1, 2, 3])
print(len(m))  # 3


#__add__ — called when you use + operator

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # __add__ is automatically called

#__eq__ — called when you use == operator

class Dog:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


d1 = Dog("Bruno")
d2 = Dog("Bruno")
print(d1 == d2)  # True