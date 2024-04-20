# s="abcd"
# for i in range(0,len(s)):
#     for j in range(-1,i):
#         print(s[i],end=' ')
#     print("\n")

# c=0
# for i in range(10,0,-2):
#     c=c+1
#     print("value of i : {}  count {}".format(i,c))

# Q. Enter your range : 5
#     *         
#     * *       
#     * * *     
#     * * * *   
#     * * * * *
# Solution:

# ran = int(input("Enter your range : "))

# for i in range(1,ran+1):
#     print(i*"* ")

# Q2. Enter your range : 5
#     * * * * * 
#     * * * *
#     * * *
#     * *
#     *
# Solution:

# ran = int(input("Enter your range : "))

# for i in range(ran,0,-1):
#     print(i*"* ")

for i in range(1,5):
    print(i*str(i))