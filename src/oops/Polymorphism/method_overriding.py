#polymorphism means many forms
#In python , it can be achieved in two ways , 1.Method Overriding and 2.Interfaces



class Vehicle:
    def ride(self):
        print("Im riding a vehicle.")


class Car(Vehicle):
    def ride(self):
        print("Im riding a car.")


class Truck(Vehicle):
    def ride(self):
        print("Im riding a truck.")


car = Car()
car.ride()
truck = Truck()
truck.ride()
