# Q1. Enter the range: n
#     1!/1 + 2!/2 + 3!/3 + .... + n!/n = sum(fact/no.) 

def gulshan(n) :
    product = 1
    for i in range( 1 , n+1) :
        product *= i
    return product/n 
n = int(input("ENTER YOUR RANGE : "))
sum = 0
a = ""
for i in range(1,n+1) :
    sum+= gulshan(i)
    if i<n : a+=str(i)+"!/"+str(i)+" + "
    else : a+=str(i)+"!/"+str(i)+" = "
print (a,sum)