# Write a program that divides two numbers and handles division by zero.
def divide_numbers(num1, num2):
    try:
        result = num1/num2
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
num1 = float(input("Enter a number: "))
num2 = float(input("Enter an other number: "))
print(divide_numbers(num1, num2))