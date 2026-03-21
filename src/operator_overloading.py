## operator overloading allows us to define the custom behaviour of mathematical operators like (+,-,*,/,etc.)

## basically + means we call __add__ function , so here we can customize this function

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1= Vector(1, 2)
v2= Vector(2, 3)


print(v1+v2)
print(v1*v2)
print(v1-v2)
