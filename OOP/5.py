# Build a Shape class → Circle, Square, calculate area

class Shape:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def area(self):
        return self.radius * self.radius

circle = Circle(5)
print(circle.area())  

square = Square(5)
print(square.area())