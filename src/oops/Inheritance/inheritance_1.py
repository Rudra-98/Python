from logging import critical
class Bird:
    def __init__(self,name):
        self.name=name


class Crow(Bird):
    def __init__(self,name,sound):
        super().__init__(name)
        self.sound =sound


    def bird_sound(self):
        print("crow")


crow_1 = Crow("crow_1",'croww')

print(crow_1.name)
print(crow_1.sound)