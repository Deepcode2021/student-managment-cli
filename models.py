from dataclasses import dataclass ,field


@dataclass
class Student:
    id: int
    name: str
    marks: list[int]
    average_mark :float = field(init=False)
        # self.marks
    def __post_init__(self):
        self.average_mark = self.average()

    def add_marks(self ,mark):
        self.marks.append(mark)

    def average(self):
        if len(self.marks) == 0 :
            return 0
        else:
            return sum(self.marks)/len(self.marks) # average of the marks 
            # print(average())
    
    def display(self):
        print(f"ID | {self.id} | Name : {self.name} | Marks : {self.marks} | Avg :{self.average():.2f} |") #calling of average funtion is necessary

# id = int(input("Enter the ID: "))
# name = str(input("Enter the name: "))
# marks = input("Enter the marks of 3 (10,20,30): ")
# marks = [int(x) for x in marks.split(sep=",")] # this will convert the marks values in "int"
# marks = marks.split(sep=",")
# print(marks)

# student1 = Student(id ,name ,marks)
# student1.display()

# can directly put the list to the main class but lets do this way also
# for _ in marks:
#     student1.add_marks(_)

