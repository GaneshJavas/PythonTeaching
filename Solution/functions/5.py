# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.


def greet(name):
    if name=="":
        return print("hello User!")
    
    return print("hello {}!".format(name))

greet(input("Enter your name:"))