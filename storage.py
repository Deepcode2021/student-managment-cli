import json
import os
from dataclasses import asdict
from models import Student

def load_students():
    try:
        # Attempt to open and read the file
        with open("student_data.json", "r") as file:

            data = json.load(file) #if i am storing the data in json
            return Student(**data)
        
            # print("File loaded successfully!", data)
    except FileNotFoundError:
        # This block runs ONLY if the file doesn't exist
        print("File not exist")
        print({"name": "Unknown", "marks": []})

def save_students(student):
    student_dict = asdict(student) # converts the class into dict

    with open("student_data.json", "w") as file:
        json.dump(student_dict ,file, indent=4)


# load_students()
# WRONG: Passing the Class template itself
# save_students(Student)