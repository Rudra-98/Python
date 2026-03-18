# In python , we refer interface as abstract class , used as decorator

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Truck(Vehicle):
    def drive(self):
        print("Truck is driving")

car = Car()
truck = Truck()
car.drive()
truck.drive()
