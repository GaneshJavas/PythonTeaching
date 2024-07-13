#!python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(func(*args, **kwargs))
        end = time.time()
        result = end-start
        return f"{func.__name__} runs for {result} secs"
    return wrapper

@timer
def greet(name):
    rest = time.sleep(2)
    return f"Hello, {name}"

@timer
def greet_two(n1, n2):
    rest = time.sleep(5)
    return f"Hello, {n1} & {n2}"


def main():
    print(greet("Ganesh"))

    print(greet_two("Jai","Ganesh"))

if __name__ == "__main__":
    main()