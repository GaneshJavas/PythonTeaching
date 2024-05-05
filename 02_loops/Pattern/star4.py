# Enter your range : 5
#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *
n=int(input("Enter your range : "))
t=n-1
for i in range(1,n+1):
    print(" "*t,"* "*i)
    t=t-1