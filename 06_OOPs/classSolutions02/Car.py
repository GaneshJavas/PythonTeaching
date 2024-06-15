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





