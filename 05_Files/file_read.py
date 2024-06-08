#! python3

from sys import argv

script, filename = argv

print("My Script name : ", script)
print("File i want to display : ", filename)

opens_my_file = open(filename)

reads_my_file = opens_my_file.read()

print(reads_my_file)