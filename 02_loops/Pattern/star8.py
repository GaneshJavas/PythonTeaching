# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------



import math
col = 27
row = 9
# for i in range(1,col+1):
#     if i <= math.ceil((col-7)/2) or i > (math.ceil((col-7)/2) + 7):
#         if i == math.ceil((col-7)/2):print("-WELCOME",end="")
#         else:print("-",end="")
#     else:continue
# print()
# print("WELCOME".center(col,'-'))
t = 1
for i in range(1,row+1):
    if i < math.ceil(row/2) :
        print((".|."*t).center(col,'-'))
        t += 2
    elif i == math.ceil(row/2):
        print("WELCOME".center(col,'-'))
        t -= 2
    else:
        print((".|."*t).center(col,'-'))
        t -= 2
