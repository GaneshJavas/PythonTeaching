# ----*----
# ---***---
# --*****--
# -*******-
# *********

import math
row = 5
col = (row * 2) - 1

for i in range(1,row+1):
    for j in range(1,col+1):
        if j <= math.ceil(col/2)-i:
            print("-",end="")
        elif j > math.ceil(col/2)-i and j <= math.ceil(col/2) + (i-1):
            print("*",end="")
        else:
            print("-",end="")   
        
    print()