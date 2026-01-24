# Class and objects
# Electric vehicle range estimation model using energy consumption data

class EV:
    def __init__(self,name,battery_kwh,consumption_wh_km):
        self.name=name
        self.battery_kwh=battery_kwh
        self.consumption_wh_km=consumption_wh_km
    def range_calculation(self):
        return(self.battery_kwh*1000)/self.consumption_wh_km

Hyundai=EV("Hyundai EV",70,200)
Jaguar=EV("I-Pace",75,220)

print(Hyundai.name,"Range:",Hyundai.range_calculation(),"km")
print(Jaguar.name,"Range:",Jaguar.range_calculation(),"km")