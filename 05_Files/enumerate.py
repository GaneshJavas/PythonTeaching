#!python3

# enumerate

my_list = [{"name": "Amit", "age": "18"},{"name": "Vipin", "age": "19"}]

enum_list = enumerate(my_list)

# print(enum_list)

# print(list(enum_list))



# for i in enum_list:
#     print(i)

# Output:
# (0, {'name': 'Amit', 'age': '18'})
# (1, {'name': 'Vipin', 'age': '19'})

# for i in enum_list:
#     print(i[0])

# Output:
# 0
# 1

# for i in enum_list:
#     print(i[1])

# Output:
# {'name': 'Amit', 'age': '18'}
# {'name': 'Vipin', 'age': '19'}

for i in enum_list:
    print(f"{i[1]['name']}")

# Output:
# Amit
# Vipin