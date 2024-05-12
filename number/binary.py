#! python

def dec_bin(n):

    print("Binary of {} is ".format(n),end="")
    s=""
    while n>0:
        s=str(n%2)+s
        n=n//2  
    return print(s)

def bin_dec_v1(n):
    print("Decimal of {} is ".format(n),end="")
    c=0
    sum=0

    for i in range(len(n)-1,-1,-1):
        sum=sum+(2*int(n[c]))**i
        c+=1
    return print(sum)

def bin_dec_v2(n):
    print("Decimal of {} is ".format(n),end="")
    sum=0
    for (i,c) in zip(range(len(n)-1,-1,-1),range(0,len(n))):
        sum=sum+(2*int(n[c]))**i
    return print(sum)

#bin_dec('1000101')

