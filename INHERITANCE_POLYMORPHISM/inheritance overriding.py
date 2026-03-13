# INHERITANCE, CLASS & METHOD OVERRIDING

class Vehicle:                  # Parent class (Base class)            
    # Method that can be inherited or overridden
    def start(self):
        print("Vehicle started")


# Child class (Derived class)
# Car inherits from Vehicle
class Car(Vehicle):
    # Overriding the start() method from Vehicle
    def start(self):
        print("Car started")


# Creating an object of Car class
tesla = Car()

# Calls the overridden method in Car
tesla.start()