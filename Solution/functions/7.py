# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.


# *input = > (1,2,3)

def ran(*input):     
    sum=0
    for i in input:
        sum+=int(i)
    return print(sum)

ran((input().split()))


# n=map(ran,(1,2,3))

# *args => tuple

# def sum(n):
#     return int(n)*2
# # my_val=(1,2,3)
# n=map(sum,input().split())

# print(list(n))
