#It is the concept of hiding the complex implementation details and showing only the necessary features of an object

# from abc import ABC, abstractmethod
#
# #abstract base class
# class Vehicle(ABC):
#     def drive(self):
#         print('The vehicle is driving')
#
#
#     #this is the method that we show these are features , but the actual implementation is done in the child class methods.
#     @abstractmethod
#     def start_engine(self):
#         pass
#
# class Car(Vehicle):
#
#     def start_engine(self):
#         print('The car is driving')
#
# def operate_vehicle(vehicle):
#     vehicle.start_engine()
#
#
# car = Car()
# operate_vehicle(car)


from abc import ABC,abstractmethod

class Vehicle:
    def __init__(self,no_of_wheels):
        self.no_of_wheels = no_of_wheels

    @abstractmethod
    def engine(self):
        print("Im driving a vehicle")


class Car(Vehicle):
    def __init__(self,no_of_wheels):
        super().__init__(no_of_wheels)

    def engine(self):
        print("Im driving a car")


o = Car(4)
o.engine()
