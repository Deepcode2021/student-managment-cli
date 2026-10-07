class Student:
    def __init__(self, id ,name, marks):
        self.id = id
        self.name = name
        self.marks = []
    def add_marks(self ,mark):
        self.marks.append(mark)

    def average(self , average):
        if len(self.marks) == 0 :
            return 0
        else:
            return sum(self.marks)/len(self.marks) # average of the marks 

id = int(input("Enter the ID: "))
name = str(input("Enter the name: "))
marks = input("Enter the marks of 3 (10,20,30): ").split(sep=",")
# marks = marks.split(sep=",")
# print(marks)
student1 = Student(id ,name ,marks)

# WE can directly put the list to the main class but lets do this way also
# for _ in marks:
#     student1.add_marks(_)

