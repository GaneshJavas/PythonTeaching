# 8. Prime Number Checker
# Problem: Check if a number is prime.

def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("Not a Prime")
            return
    print("Prime")


n=int(input("enter the number:"))
for i in range(2,n):
    
    if n%int(i)==0:
        print("not a prime number")
        break
    elif i==n-1:
        print("prime munber")
        