class Car:
    
    def __init__(self, brand, model, price):
        # To make an attribute private we use __ (double underscore) before the attribute name
        self.brand = brand
        self.model = model
        self.__price = price

    def get_price(self):
         return f"Rs.{self.__price}"
    
    def display_detail(self):
        return f"My Car: {self.brand} {self.model}" #"{} {}".format(self.brand,self.model)

class ElectricCar(Car):
        def __init__(self,brand, model, battery_size):
             super().__init__(brand, model)
             self.battery_size = battery_size



# instance of a class // object of class Car

#my_EV = ElectricCar("KIA", "Comet", "330kW")
#print(my_EV.display_detail())

tata = Car("Tata","Safari",400)

print(tata.get_price())


# Every Instance of a class will be assigned a new location inside the memory
# tata = Car("Tata","Safari")
# print(tata)
# print(tata.get_brand)
# tata1 = Car("Tata","Safari")
# print(tata1)
# print(tata1.get_brand)
