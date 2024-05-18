#! python

def poly(a,b):
    if a.isdigit() == True and b.isdigit() == True:
        return print(int(a)*int(b))
    elif a.isdigit() == True and b.isdigit() == False:
        return print(int(a)*b)
    elif a.isdigit() == False and b.isdigit() == True:
        return print(a*int(b))
    else:
        return print(a+b)

poly(input(),input())