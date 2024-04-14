r=int(input("Enter your limit: "))
a=0
b=1
c=0
print("{},{}".format(a,b), end=',')
# for i in range(0,r):
#     if c>=50:
#         break
#     c=a+b
#     print(c,end=',')
#     a=b
#     b=c

while c<=50: 
    c=a+b
    print(c,end=',')
    a=b
    b=c