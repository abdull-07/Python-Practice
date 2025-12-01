# Make a Car class with properties and methods (start, stop, accelerate)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_started = False
        self.speed = 0
    
    def car_start(self):
        if self.is_started:
            print("Car is already started")
        else:
            self.is_started = True
            print("Car started")
    
    def car_stop(self):
        if self.is_started:
            self.is_started = False
            print("Car Stoped")
        else:
            print("car is unable to stop")
    
    def accelerate(self):
        if self.is_started:
            self.speed += 100
            print(f"Car accelerated to {self.speed} km/h")
        else:
            print("Car is stoped")

car1=Car("Dodge Challenger Demon", "170", "2023")
print(car1.make, car1.model, car1.year, car1.is_started, car1.speed)