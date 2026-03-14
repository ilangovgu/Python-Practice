class EVcar:
    def __init__(self, brand, battery_capacity, motor_power, range_km):
        self.brand = brand
        self.battery_capacity = battery_capacity
        self.motor_power = motor_power
        self.range_km = range_km
        print("Vehicle brand listed!")

    def display(self):
        print("Brand details:")
        print("Brand name:", self.brand)
        print("Battery capacity:", self.battery_capacity)
        print("Motor power:", self.motor_power)
        print("Vehicle range:", self.range_km)
        print()

Tesla = EVcar("Tesla", "75KWh", "150KW", "500KM")
BYD = EVcar("BYD", "80KWh", "160KW", "575KM")

Tesla.display()
BYD.display()