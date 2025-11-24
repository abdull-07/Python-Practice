# Write a program that asks for a number input, and handles invalid input (like letters).
def get_num():
    while True:
        try:
            num = float(input("enter a number: "))
            return num
        except ValueError:
            print("Invalid input please enter a valid number.")
num = get_num()