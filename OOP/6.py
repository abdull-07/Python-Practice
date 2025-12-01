# Use __str__ and __len__ magic methods in a custom class

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return self.name + " - " + str(self.marks)
    def __len__(self):
        return len(self.marks)

student1 = Student("Muhammad Abdullah", [90, 79, 89, 98, 90, 80])
print(student1)
print(len(student1))