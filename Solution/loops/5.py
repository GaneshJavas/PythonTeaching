# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

n=(input("enter the number:"))
for i in n:
    if n.count(i)==1:
        print(i,"is the first non repeating number")
        break