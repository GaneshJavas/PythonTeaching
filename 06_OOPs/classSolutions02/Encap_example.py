# Always prefer to keep the name of the class and file name same

from Car import Car as c

test = c("Tata","Safari",500)
try :
    print(test.__price)
except AttributeError:
    print("AttributeError")

try:
    print(5/1)
except ZeroDivisionError:
    print("Avoid dividing by Zero")