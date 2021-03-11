class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.fuck=0
    def get_descript_name(self):
        long_name='this is '+self.make+' '+self.model+' '+self.year
        return long_name.title()
    def fill_gas_tank(self):
        return 'gas'
# """定义子类时，必须在括号内指定父类的名称""" 
class eleccar(car):
     def __init__(self,make,model,year):
         #初始化父类
         super().__init__(make,model,year)
         self.batt=battery()
     def fill_gas_tank(self):
        return 'eleccar no gas'


class battery():
    def __init__(self,batty_size=80):
        self.battery_size=batty_size
    def descript_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=300
        message="This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


my_tsla=eleccar('tesla','model s','2014')
name=my_tsla.get_descript_name()
print(name)
gass=my_tsla.fill_gas_tank()
print(gass)
my_tsla.batt.descript_battery()
my_tsla.batt.get_range()

