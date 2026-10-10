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

def update(student, ID):
    # student_dict = asdict(student) # converts the class into dict
    current_students = load_students()
    for s in current_students:
        if s.id == ID:
            s.id = student.id
            s.name = student.name
            s.marks = student.marks 
            s.average = student.average()
    serialized_list = [asdict(s) for s in current_students]
    with open("student_data.json", "w") as file:
        json.dump(serialized_list ,file, indent=4)

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