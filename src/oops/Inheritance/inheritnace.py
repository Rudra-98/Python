
class Vehicle:
    def __init__(self,no_of_wheels):
        self.no_of_wheels = no_of_wheels


    def ride(self):
        print("I ride the vehicle")


class Car(Vehicle):
     def __init__(self,no_of_wheels):
         super().__init__(no_of_wheels)


     def ride(self):
         print("I ride the car")


o = Car(5)
o.ride()


