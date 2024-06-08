# user is a global scope variable
#  user = "amit"

# def some():
# user is a function scope variable 
#     #user = "vipin"
#     print(user)

# print(user)
# some()



# x = 300 // Global Scope => Top most values
# y = 100
# def some(y):
#     x = 200
#     global y
#     n = x + y
#     def some2():
#         a = n + y // n is the enclosing function => value of one level up 
#         return a
#     return print(some2())

# some(y)

total = 0
def add_to_total(n):
    total = total + n
add_to_total(5)
print(total)


# Local (L): The local, or current, scope. This could be the body of a function or the top-level scope of a script. It always represents the scope that the Python interpreter is currently working in.
# Enclosing (E): The enclosing scope. This is the scope one level up from the local scope. If the local scope is an inner function, the enclosing scope is the scope of the outer function. If the scope is a top-level function, the enclosing scope is the same as the global scope.
# Global (G): The global scope, which is the top-most scope in the script. This contains all of the names defined in the script that are not contained in a function body.
# Built-in (B): The built-in scope contains all of the names, such as keywords, that are built-in to Python. Functions such as round() and abs() are in the built-in scope. Anything that you can use without first defining yourself is contained in the built-in scope.
