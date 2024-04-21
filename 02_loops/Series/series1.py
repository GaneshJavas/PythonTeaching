# Q1. Enter the range: n
#     1 + 2 + 3 + 4 + 5 + .... + n = sum 

n = int(input("Enter the range : "))
sum = 0
a = ""
for i in range ( 1, n+1) :
    sum += i
    if i<n : a += str(i) + " + "
    else : a += str(i)
print (a,"=", sum)