# Enter your range : 5
#  *****
#   ****
#    ***
#     **
#      *
n=int(input("Enter your range : "))
t=n
for i in range(0,n):
    print(" "*i,"*"*t)
    t=t-1
    