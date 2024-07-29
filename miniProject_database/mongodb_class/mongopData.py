from pymongo import MongoClient
from bson import ObjectId

# Client Connection
client_conn = MongoClient("mongodb+srv://satyam:satyam01@cluster0.6yztvpl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Database Connection with the client
db = client_conn["Satyam"]
# Collection
col = db["personData"]
print(client_conn)
print(client_conn.list_database_names())

def display_data():
    for i in col.find():
        print(i)

def add_person(name, age):
    col.insert_one({"name": name, "age": age})

def update_person(id,new_name,new_age):
    col.update_one({"_id":ObjectId(id)},{"$set": {"name": new_name,"age": new_age}})

def delete_person(id):
    col.delete_one({"_id":ObjectId(id)})


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
                display_data()
            case '2':
                name = input("Enter Name: ")
                age = input("Enter Age: ")
                add_person(name, age)
            case '3':
                display_data()
                id = input("Enter the ID you want to Update: ")
                name = input("Enter Name: ")
                age = input("Enter Age: ")
                update_person(id,name,age)
            case '4':
                id = input("Enter the ID you want to DELETE: ")
                delete_person(id)
            case '5':
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()