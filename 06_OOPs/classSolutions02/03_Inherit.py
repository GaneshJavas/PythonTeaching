class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_detail(self):
        return f"My Car: {self.brand} {self.model}" #"{} {}".format(self.brand,self.model)

class ElectricCar(Car):
        def __init__(self,brand, model, battery_size):
             super().__init__(brand, model)
             self.battery_size = battery_size



# instance of a class // object of class Car

my_EV = ElectricCar("KIA", "Comet", "330kW")
print(my_EV.display_detail())




