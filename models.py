class Student:
    def __init__(self, id ,name, marks):
        self.id = id
        self.name = name
        self.marks = marks
        # self.marks =0
    def add_marks(self ,mark):
        self.marks.append(mark)

    def average(self , average):
        if len(self.marks) == 0 :
            return 0
        else:
            return sum(self.marks)/len(self.marks) # average of the marks 
    def display(self):
        print(f"Student | {self.id} | {self.name} | {self.marks} | {self.average} |")

id = int(input("Enter the ID: "))
name = str(input("Enter the name: "))
marks = input("Enter the marks of 3 (10,20,30): ")

marks = marks.split(sep=",")
# print(marks)

student1 = Student(id ,name ,marks)
student1.display()


# WE can directly put the list to the main class but lets do this way also
# for _ in marks:
#     student1.add_marks(_)

