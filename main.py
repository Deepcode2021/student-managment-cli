from models import Student
import storage

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
        print("---------------------------------\n")
    # elif user == 3:
    # elif user == 4:
    # elif user == 5:
    elif user == 6:
        print("Goodbye !!!")
        break
    else:
        print("Error ye kya type kardiya !!!")

