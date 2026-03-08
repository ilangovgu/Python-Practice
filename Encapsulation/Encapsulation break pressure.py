# ENCAPSULATION_BREAK PRESSURE

class Break():
    def __init__(self):
        self.__break_pressure = "1000psi"
    
    def get_break_pressure(self):
        return self.__break_pressure
    
    def set_break_pressure(self, pressure):
        self.__break_pressure = pressure

toyota = Break()
print(toyota.get_break_pressure())
toyota.set_break_pressure("980psi")
print(toyota.get_break_pressure())