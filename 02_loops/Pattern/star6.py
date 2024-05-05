# Enter your range : 5
#       * 
#      * *
#     * * *
#    * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
n=int(input("Enter your range : "))
t=n
p=n
x=n-1

for i in range(1,t+1):
    print(" "*p,"* "*i)
    p-=1
    if i==n:
        for j in range(2,n+1):
            print(" "*j,"* "*x)
            x=x-1
        