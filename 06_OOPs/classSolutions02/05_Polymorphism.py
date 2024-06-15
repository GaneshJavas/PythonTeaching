class Car:
    
    def __init__(self, brand, model, price):
        # To make an attribute private we use __ (double underscore) before the attribute name
        self.brand = brand
        self.model = model
        self.__price = price
        

    def get_price(self):
         return f"Rs.{self.__price}"
    
    def display_detail(self):
        return f"My Car: {self.brand} {self.model}" 

    def display_fuel_type(self):
         return "Diesel or Petrol"


class ElectricCar(Car):
        def __init__(self,brand, model, price, battery_size):
             super().__init__(brand, model, price)
             self.battery_size = battery_size

        def display_fuel_type(self):
         return "Electric"

tata = Car("Tata", "Safari", "1500000")
print(tata.display_fuel_type())
bmw = ElectricCar("Tata", "Safari", "1500000", "75kWh")
print(bmw.display_fuel_type())

