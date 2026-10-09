from models import Student
import storage
import math


def space():
    for _ in range(1,20):print("-",end="--")
    print(end="\n")


# main funtion 
while True:
    print("1. Add  2. List  3. Search  4. Update  5. Delete  6. Quit")
    user = int(input("Choose : "))

    if user == 1:
        id = int(input("Enter the ID: "))
        name = str(input("Enter the name: "))
        marks = input("Enter the marks of 3 (10,20,30): ")
        marks = [int(x) for x in marks.split(sep=",")]
        stu = Student(id=id, name=name, marks=marks)
        storage.save_students(stu)
    elif user == 2:
        print("\n--- Student Database Records ---")
        students = storage.load_students()
        
        if not students:
            print("No student records found in the database.")
        else:
            for s in students:
                s.display()  # This will print your formatted row nicely
        space()

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

    elif user == 4:
        user_id = int(input("ID: "))
        
    # elif user == 5:
    elif user == 6:
        print("Goodbye !!!")
        break
    else:
        print("Error ye kya type kardiya !!!")

