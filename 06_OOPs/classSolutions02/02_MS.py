class Car:
    type_of_wheel = "Steel Round"
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_detail(self):
        return f"My Car: {self.brand} {self.model}" #"{} {}".format(self.brand,self.model)



# instance of a class // object of class Car
my_car = Car("Maruti","Wagon-R")

print(my_car.brand)
print(my_car.model)

my_other_car = Car("BMW", "M340-I")

print(my_other_car.brand)
print(my_other_car.model)

print(my_car.display_detail())


print(my_car.type_of_wheel)
print(my_other_car.type_of_wheel)

