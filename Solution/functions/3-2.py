# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

# def poly(a,b):
#     if type(a)==int or type(a)==str and type(b)==int:
#         return print(a*b)
#     elif type(a)==int and type(b)==int or type(b)==str:
#         return print(a*b)
#     elif type(a)==str and type(b)==str:
#         return print(a+b)


def poly(a,b):
    if a.isdigit()==True and b.isdigit()==True:
        return print(int(a)*int(b))
    if a.isdigit()==False and b.isdigit()==True:
        return print(a*int(b))
    if a.isdigit()==True and b.isdigit()==False:
        return print(int(a)*b)
    if a.isdigit()==False and b.isdigit()==False:
        return print(a+b)

    

poly(input("1."),input("2."))