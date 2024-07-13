
def func_debug(func):
    def wrapper(*args, **kwargs):

        arg_values = ", ".join(str(arg) for arg in args) 
        kwarg_values = ", ".join(str(k+" = "+v) for k,v in kwargs.items())
        # arg_values = ", ".join(args)
        # kwarg_values = ", ".join(kwargs)
        print(f"{func.__name__} function as args {arg_values}")
        print(f"{func.__name__} function as kwargs {kwarg_values}")
        # return "MY WORK DONE"
        return func(*args, **kwargs)
    return wrapper



@func_debug
def student(name, standard, school = "BPS"):
    return(f"My name is {name} studing in standard {standard} from school: {school}")

print(student("Vipin","10",school = "BPS"))

# Output: student function as args {name}, {standard}
#         student function as kwargs school=BPS
