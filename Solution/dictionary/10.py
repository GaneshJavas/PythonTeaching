sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }

# for i in sample_dict:
#     if sample_dict[i]["name"] == "Brad":
#         sample_dict[i]["salary"] = 1500
#         break 

for i in sample_dict:
    for j in sample_dict[i]:
        if sample_dict[i][j] == "Brad":
            sample_dict[i]["salary"] = 1500
            break  

print(sample_dict)
