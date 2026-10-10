from models import Student
import storage
import math


def space():
    for _ in range(1,20):print("-",end="--")
    print(end="\n")

def add():
    id = int(input("Enter the ID: "))
    name = str(input("Enter the name: "))
    marks = input("Enter the marks of 3 (10,20,30): ")
    marks = [int(x) for x in marks.split(sep=",")]
    stu = Student(id=id, name=name, marks=marks)
    storage.save_students(stu)


# main funtion 
while True:
    print("1. Add  2. List  3. Search  4. Update  5. Delete  6. Quit")
    user = int(input("Choose : "))
    # add
    if user == 1:
        add()
    # list
    elif user == 2:
        print("\n--- Student Database Records ---")
        students = storage.load_students()
        
        if not students:
            print("No student records found in the database.")
        else:
            for s in students:
                s.display()  # This will print your formatted row nicely
        space()
    # search
    elif user == 3:
        data = storage.load_students()
        print("1 By ID  2 By Name")
        user = int(input(": "))
        if user == 1:
            search_id = int(input("Id :"))
            for s in data:
                if s.id == search_id: # error here i used s[id] this is used for dict not instance
                    s.display()

        elif user == 2:
            search_name = str(input("Name :"))
            for s in data:
                if s.name.lower() == (search_name).lower():
                    # print(type(s.name), type(search_name)) fuck me only adding .lower <- this is a function 
                    s.display()
                    continue
        else:
            print("what is this man!!!")
        space()
    # update 
    elif user == 4:
        data = storage.load_students()
        user_id = int(input("ID: "))
        for s in data:
            if s.id == user_id: 
                s.display()
                # user_name = str(input("Name: "))
            # if s.name == user_name:
                id = int(input("New ID: "))
                name = str(input("new name: "))
                marks = input("new marks of 3 (10,20,30): ")
                marks = [int(x) for x in marks.split(sep=",")]
                update_stu = Student(id=id,name=name,marks=marks)
                storage.update(update_stu ,id)
                print("Updated!")
                
    # delete
    elif user == 5:
        data = storage.load_students()
        delete_id = int(input("ID to be deleted: "))
        for s in data:
            if s.id == delete_id:
                storage.delete(delete_id)
                
    elif user == 6:
        print("Goodbye !!!")
        break
    else:
        print("Error ye kya type kardiya !!!")

