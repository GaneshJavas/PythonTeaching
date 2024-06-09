class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    
# instance of a class // object of class Car
my_car = Car("Maruti","Wagon-R")

print(my_car.brand)
print(my_car.model)

my_other_car = Car("BMW", "M340-I")

print(my_other_car.brand)
print(my_other_car.model)


