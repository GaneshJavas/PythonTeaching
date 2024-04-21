# Q1. Enter the range: n
#     1 * 2 * 3 * 4 * 5 * .... * n = product 

n = int(input("Enter the range : "))
product = 1
a = ""
for i in range ( 1, n+1) :
    product *= i
    if i<n : a += str(i) + " * "
    else : a += str(i) + " = "
print (a, product)


