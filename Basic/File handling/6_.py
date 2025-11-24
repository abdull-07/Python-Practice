# Use the math module to calculate factorial and square root of a number.
import math
def calcul_fact(num):
    try:
        result=math.factorial(num)
        return result
    except ValueError:
        return "Error: Factorial is not defined for negative numbers."

def calcul_sqrt(num):
    try:
        result=math.sqrt(num)
        return result
    except ValueError:
        return "Error: Square Root is not defined for negative numbers."

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {calcul_fact(num)} and Square root is: {calcul_sqrt(num)}")