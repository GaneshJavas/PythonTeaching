#!python3

# enumerate

my_list = ("amit", "satyam", "gulshan", "vipin")

enum_list = enumerate(my_list)

print(enum_list)

print(list(enum_list))



for i in enum_list:
    print(i)