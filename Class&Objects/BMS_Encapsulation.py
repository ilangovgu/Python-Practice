# Battery Management System Module
# This class simulates a basic EV battery management system

class BMS:
    def __init__(self,SOC,temperature,voltage,range):
        self.__SOC=int(SOC)                             # SOC in %
        self.__temperature=int(temperature)             # Temperature in degree celcius
        self.__voltage=int(voltage)                     # Voltage in Volts
        self.__range=int(range)                         # Range in KM
        
    def get_values(self):
        return self.__SOC,self.__temperature,self.__voltage,self.__range

    def validate_SOC(self,updated_SOC):
        if updated_SOC>=0 and updated_SOC<=100:
            return "SOC GOOD"
        return "SOC ERROR"

    def validate_temperature(self,updated_temperature):
        if updated_temperature>=-15 and updated_temperature<=50:
            return "TEMPERATURE GOOD"
        return "TEMPERATURE ERROR"

    def validate_voltage(self,updated_voltage):
        if updated_voltage>=229 and updated_voltage<=430:
            return "VOLTAGE GOOD"
        return "VOLTAGE ERROR"

    def set_values(self,updated_SOC,updated_temperature,updated_voltage,updated_range):
        updated_SOC=int(updated_SOC)
        updated_temperature=int(updated_temperature)
        updated_voltage=int(updated_voltage)
        updated_range=int(updated_range)

# Perform validation checks
        soc_status=self.validate_SOC(updated_SOC)
        temperature_status=self.validate_temperature(updated_temperature)
        voltage_status=self.validate_voltage(updated_voltage)
        

# Block update if any parameter is unsafe
        if soc_status != "SOC GOOD":
            return soc_status
        if temperature_status != "TEMPERATURE GOOD":
            return temperature_status
        if voltage_status != "VOLTAGE GOOD":
            return voltage_status
        

# Update if only all validation pass
        self.__SOC=int(updated_SOC)
        self.__temperature=int(updated_temperature)
        self.__voltage=int(updated_voltage)
        self.__range=int(updated_range)

        return "UPDATED SUCESSFULLY"
    
    

    
mercedes=BMS("100","35","250","450")
bmw=BMS("95","30","255","470")

# print(mercedes.get_values())
# print(bmw.get_values())

result=mercedes.set_values("90","-13","431","490")
print(result)
print(mercedes.get_values())
