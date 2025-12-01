# Create Animal → Dog and Cat subclasses, override sound() method

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print('Bark')

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()