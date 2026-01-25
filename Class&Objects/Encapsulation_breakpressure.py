class Break():
    def __init__(self):
        self.__breakpressure="1000psi"
    def get_breakpressure(self):
        return self.__breakpressure
    def set_breakpressure(self,name):
        self.__breakpressure=name

ford=Break()
print(ford.get_breakpressure())
ford.set_breakpressure("1100psi")
print(ford.get_breakpressure())
