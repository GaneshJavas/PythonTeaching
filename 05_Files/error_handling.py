#!python3

# try:
#     file = open('file.txt','r')
#     print("File opened")
#     print(file.read())
#     print("Inside try")
# except FileNotFoundError :  
#     print("Create a file")
#     print("Inside except")
# finally:
#     file.close()
#     print("Inside finally")

# with open("file.txt",'w') as file:
#     print(file.write("Teri kuch nahi"))

with open("file.txt",'a') as file:
    print(file.write("Teri bahut kuch"))
# "with" will open the given file and close it once all the operation done inside it
    
with open("file.txt",'r') as file:
    print(file.read())

# 'r' -- read mode
# 'w' -- write mode
# 'a' -- append mode


