import json
import os
from dataclasses import asdict
from models import Student

def load_students():
    if not os.path.exists("student_data.json"):
        return []


    try:
        
        with open("student_data.json", "r") as file:
            data_list = json.load(file)
            # don't know what was happijng here
            if not isinstance(data_list, list):
                return []

            students = []
            for item in data_list:
                item.pop("average_mark", None)
                students.append(Student(**item))
            return students
            # return [Student(**item) for item in data_list]
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
    #         data = json.load(file) #if i am storing the data in json
    #         # return Student(**data)
    #         return [Student(**data) for data in data]
    #         # print("File loaded successfully!", data)
    # except FileNotFoundError:
    #     # This block runs ONLY if the file doesn't exist
    #     print("File not exist")
    #     print({"name": "Unknown", "marks": []})

def save_students(student):
    # student_dict = asdict(student) # converts the class into dict
    current_students = load_students()
    current_students.append(student)
    serialized_list = [asdict(s) for s in current_students]
    with open("student_data.json", "w") as file:
        json.dump(serialized_list ,file, indent=4)
        print("Student Added.")

def update(original_id, new_id=None, new_name=None, new_marks=None):
    # student_dict = asdict(student) # converts the class into dict
    students = load_students()

    # for s in current_students:
        
        # if s.id == ID:
        #     s.id = student.id
        #     s.name = student.name
        #     s.marks = student.marks 
        #     s.average = student.average()

    if new_id is not None and new_id != original_id:
        for s in students:
            if s.id == new_id:
                print(f"Error: ID {new_id} is already taken. Cannot update.")
                return # Stop here

    # 3. FIND & MODIFY
    found = False
    for index, s in enumerate(students):
        if s.id == original_id:
            # Update only what the user entered
            if new_id is not None: s.id = new_id
            if new_name is not None: s.name = new_name
            if new_marks is not None: s.marks = new_marks
            
            # Recalculate average
            s.__post_init__()
            
            # Save back to list
            students[index] = s
            found = True
            break


    serialized_list = [asdict(s) for s in students]
    with open("student_data.json", "w") as file:
        json.dump(serialized_list ,file, indent=4)
        print("Updated!!!")

def delete(ID):
    # student_dict = asdict(student) # converts the class into dict
    current_students = load_students()
    for index, s in enumerate(current_students):
        if s.id == ID:
            student_found = s
            # Remove the item at this specific index
            del current_students[index]  
            break
    serialized_list = [asdict(s) for s in current_students]
    with open("student_data.json", "w") as file:
        json.dump(serialized_list ,file, indent=4)
        print("Student Deleted.")
# load_students()
# WRONG: Passing the Class template itself
# save_students(Student)