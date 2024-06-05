# *****
# *
# *****
#     *
# *****
for r in range(1,6):
    for c in range(1,6):
        if (r%2) != 0 or (r == 2 and c == 1) or (r == 4 and c == 5):
            print("*",end="")
        else: 
            print(" ",end="")
    print("\n")