#!python3

def deco(get_func):
    def wrapper():
        print("Before calling function")
        get_func()
        print("After calling function")
    return wrapper()

@deco
def hello():
    print("Hello")


# hello = deco(hello)





