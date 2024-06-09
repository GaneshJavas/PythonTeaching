# 10.2 - Instantiate an Object
# Solutions to review exercises


# Exercise 1
class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# The value for `age` can vary in your solution
philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")


# Exercise 2
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


blue_car = Car("blue", 20000)
red_car = Car("red", 30000)

for car in (blue_car, red_car):
    print(f"The {car.color} car has {car.mileage:,} miles")


# Exercise 3
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, miles):
        self.mileage = self.mileage + miles


blue_car = Car("blue", 0)
blue_car.drive(100)
print(blue_car.mileage)

# 10.3 - Inherit From Other Classes
# Solutions to review exercises


# Exercise 1
# The parent `Dog` class (given in exercise)
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# The GoldenRetriever class that solves the exercise
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


# Exercise 2
# Rectangle and Square classes
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


square = Square(4)
print(square.area())  # 16

square.width = 5  # Modifies .width but not .length
print(square.area())  # 20

# 10.4 - Challenge: Model a Farm
# Solutions to challenge


class Animal:

    # Class attributes
    stuff_in_belly = 0
    position = 0

    # Initializer
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Instance methods
    def talk(self, sound=None):
        """Return the string "<name> says <sound>"

        If `sound` is left out, returns "Hello, I'm <name>"
        """
        if sound is None:
            return f"Hello. I'm {self.name}!"
        return f"{self.name} says {sound}"

    def walk(self, walk_increment):
        self.position = self.position + walk_increment
        return self.position

    def run(self, run_increment):
        self.position = self.position + run_increment
        return self.position

    def feed(self):
        self.stuff_in_belly = self.stuff_in_belly + 1
        if self.stuff_in_belly > 3:
            return self.poop()
        else:
            return f"{self.name} is eating."

    def is_hungry(self):
        if self.stuff_in_belly < 2:
            return f"{self.name} is hungry"
        else:
            return f"{self.name} is not hungry"

    def poop(self):
        self.stuff_in_belly = 0
        return "Ate too much ... need to find a bathroom"


class Dog(Animal):
    def talk(self, sound="Bark Bark!"):
        return super().talk(sound)

    def fetch(self):
        return f"{self.name} is fetching."


class Sheep(Animal):
    def talk(self, sound="Baaa Baaa"):
        return super().talk(sound)


class Pig(Animal):
    def talk(self, sound="Oink Oink"):
        return super().talk(sound)


# The following code illustrates how to use the classes defined above.
# It is not necesarrily a part of the solution, and is included for
# illustration purposes only.

# Create a dog
dog = Dog("Blitzer", "yellow")

# Output the dog's attributes
print(f"Our dog's name is {dog.name}.")
print(f"And he's {dog.color}.")

# Output some behavior
print(f"Say something, {dog.name}.")
print(dog.talk())
print("Go fetch!")
print(dog.fetch())

# Walk the dog
print(f"{dog.name} is at position {dog.walk(2)}.")

# Run the dog
print(f"{dog.name} is now at position {dog.run(4)}")

# Feed the dog
print(dog.feed())

# Is the dog hungry?
print(dog.is_hungry())

# Feed the dog more
print(dog.feed())
print(dog.feed())
print(dog.is_hungry())
print(dog.feed())

print("\n")

# Create a sheep
sheep = Sheep("Shaun", "white")

# The sheep talks!
print(sheep.talk())

# When the sheep runs, the distance is returned
print(sheep.run(2))
print(sheep.run(2))

print("\n")

# Create a pig
pig = Pig("Carl", "pink")

# Pigs love to oink!
print(pig.talk())