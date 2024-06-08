from sys import argv

toolname, filename = argv

# read() -- reads the complete file content at once
print("TOTAL CONTENT",open(filename).read())

# also takes an argument to read specific number of characters
print("SPECIFIC BYTES: ",open(filename).read(10))

# readline() -- reads the first line of a file
# type -- str
print("READLINE: ",open(filename).readline())

#readlines() -- reads the file as a list of string of each line
# type -- list['str']
print("READLINE: ",open(filename).readlines()[0])
