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
            
        

