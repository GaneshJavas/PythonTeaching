#!python3

import json

# Load File data in List/json format
def load_file():
    try:
        file = open("person_data.txt",'r')
        return json.load(file)
    except FileNotFoundError :
        return []

# Write the changes into the File
def saver_op(details):
    with open("person_data.txt",'w') as file: 
        return json.dump(details,file)

# Display the contents of the file in a structured way 
def display_data(details):
    file = enumerate(details, start=1)
    print("\nListed Persons")
    for i in file:
        print(f"{i[0]}. Name: {i[1]['name']} Age: {i[1]['age']}")
    print()

# Add new data
def add_person(details):
    name = input("Enter name : ")
    age = input("Enter age : ")
    details.append({'name': name, 'age': age})
    saver_op(details)
    print("Added Succesfully.....\n")

# Update data
def update_person(details):
    display_data(details)
    u_index = int(input("Enter the index you want to update : "))
    if 1 <= u_index <= len(details):
        name = input("Enter name : ")
        age = input("Enter age : ")
        details[u_index-1] = {'name': name, 'age': age}
        saver_op(details)
        print("Updated Succesfully.....\n")
    else:
        print("Invalid Selection")

# Delete data
def delete_person(details):
    display_data(details)
    d_index = int(input("Enter the index you want to update : "))
    if 1 <= d_index <= len(details):
        del details[d_index-1]
        saver_op(details)
        print("Deleted Succesfully.....\n")
    else:
        print("Invalid Selection")


details = load_file()
# print(details)

def main():
    print("PERSON DATA ENTRY\n")
    while True:
        
        print("1. Display Details")
        print("2. Add a Person")
        print("3. Update person details")
        print("4. Delete a person")
        print("5. Exit")

        choice = input("\nEnter your choice : ")    
        
        match choice :
            case '1':
                display_data(details)
            case '2':
                add_person(details)
            case '3':
                update_person(details)
            case '4':
                delete_person(details)
            case '5':
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()
        