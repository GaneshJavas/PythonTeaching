# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

def ac(r):
    a=22/7
    return print(round(a*(r)**2,2) ,int(2*a*(r)))

ac(int(input("raidus:")))