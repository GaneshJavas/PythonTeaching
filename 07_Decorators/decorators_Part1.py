def greet_hi(name):
    return print(f"Hi! {name}")

def greet_hey(name):
    return print(f"Hey! {name}")

def greet(greet_func):
    return greet_func(input("Name: "))


#greet(greet_hey)

def parent(num):
    #print("I'm inside parent")
    #print("I'm Sanjay")

    def first_child():
        #print("I'm inside first child")
        # print("I'm Satyam")
        return ("I'm Satyam")


    def second_child():
        #print("I'm inside second child")
        # print("I'm Sahil")
        return ("I'm Sahil")

    if num == 1: return first_child
    elif num == 2: return second_child
    


first = parent(1)
second = parent(2)

print(first())





