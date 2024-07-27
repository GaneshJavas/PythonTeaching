#!python
import sqlite3

conn_server = sqlite3.connect("personal_data.db")

cur = conn_server.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS pData(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INT NOT NULL
            )
        ''')


def display_data():
    cur.execute('''
    SELECT * FROM pData
        ''')
    
    for i in cur.fetchall():
        print(i)

def add_person(name, age):
    cur.execute('''
    INSERT INTO pData(name,age) VALUES(? , ?)
        ''',(name,age))
    conn_server.commit()

def update_person(id,name,age):
    #display_data()
    cur.execute('''
    UPDATE pData SET name = ?, age = ? WHERE id = ?
        ''',(name,age,id))
    conn_server.commit()

def delete_person(id):
    cur.execute('''
    DELETE FROM pData WHERE id = ?
        ''',(id))
    conn_server.commit()


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
    cur.close()



    