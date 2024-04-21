# Q1. Enter the range: n
#     1! + 2! + 3! + .... + n! = sum(fact) 

def factorial(n):
    product = 1
    for i in range(1 , n+1) :
        product *= i
    return product

n = int(input("Enter the range : "))
sum = 0
a=""
for i in range(1, n+1):
    sum+=factorial(i)
    if i<n : a += str(i) + "! + "
    else : a += str(i) + "! = "

print(a,sum)


