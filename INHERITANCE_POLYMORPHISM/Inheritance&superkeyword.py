# Automotive simulation software
# Inheritance & Super keyword

class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
    
    def start(self):
        print("vehicle started")
    
    def drive(self):
        print(f"driving at maximum speed: {self.max_speed}km/h")

class ICEcar(Vehicle):
    def __init__(self, brand, max_speed, fuel_type):
        super().__init__(brand, max_speed)
        self.fuel_type = fuel_type
    
    def start(self):
        print(f"starting vehicle with {self.fuel_type}")

class Electriccar(Vehicle):
    def __init__(self, brand, max_speed, battery_capacity):
        super().__init__(brand, max_speed)
        self.battery_capacity = battery_capacity
    
    def start(self):
        print(f"Electric motor started, battery capacity: {self.battery_capacity}KWh")

class Autonomouscar(Electriccar):
    def __init__(self, brand, max_speed, battery_capacity, autonomy_level):
        super().__init__(brand, max_speed, battery_capacity)
        self.autonomy_level = autonomy_level
    
    def drive(self):
        print(f"Autonomous driving activated: {self.autonomy_level}")

# Testing vehicle instances
mazda = ICEcar("mazda cx-5", 200, "petrol")
mazda.start()
mazda.drive()
print()

tesla = Electriccar("tesla", 230, 150)
tesla.start()
print()

waymo = Autonomouscar("jaguar-I Pace", 100, 140, "level 4")
waymo.drive()

