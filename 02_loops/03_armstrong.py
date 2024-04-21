# 52 

# 5^2 + 2^2 != 52 not armstrong

# 153 

# 1^3 + 5^3 + 3^3 = 153 armstrong


a = int(input("ENTER YOUR NUMBER :"))
sum = 0 # empty sum
n = "" # empty string
c=0 # counter
l=len(str(a)) # length of string
for i in str(a) :
    c+=1
    sum = sum+(int(i))**l
    if c<l : n+=i+"^"+str(l)+" + "
    else: n+=i+"^"+str(l)

if a==sum : print(n," = ",a,"ARMSTRONG")
else : print(n," != ",a,"NOT ARMSTRONG")    