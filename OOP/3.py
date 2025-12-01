# Build a Student class that stores subject marks and calculates grade

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def cal_grads(self):
        if self.marks > 90:
            return "A"
        elif 80 < self.marks < 90:
            return "B"
        elif 70 < self.marks < 80:
            return "C"
        elif 60 < self.marks < 70:
            return "D"
        elif 50 < self.marks < 60:
            return "E"
        else:
            return "F"

stud1 = Student("Muhammad Abdullah", 59)
print(stud1.cal_grads())