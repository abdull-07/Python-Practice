# Write a function with default arguments (country="Pakistan").

def greet(name, country="Pakistan"):
    print(f"Hello {name}, You'r from {country}.")
name=input("Enter your name: ")
country=input("Enter your Country: ")
greet(name, country)