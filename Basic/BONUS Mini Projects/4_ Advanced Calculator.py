# Problem 1 — Advanced Calculator
# Create a calculator program that:
# Asks the user for two numbers.
# Asks the user for an operation (+, -, *, /, **, %).
# Performs the operation.
# Prints if the result is even/odd and positive/negative.
# Handles division by zero and invalid inputs gracefully using try/except.
# Encapsulate the calculator in a function called advanced_calculator(num1, num2, op).


#  add functions for each operation
def add(num1, num2,):
    result = num1 + num2
    return result

#  substract functions for each operation
def sub(num1, num2,):
    result = num1 - num2
    return result

#  dividsion functions for each operation
def div(num1, num2,):
    if num2 != 0:
        result = num1 / num2
    else:
        raise ZeroDivisionError
    return result

#  Multiply functions for each operation
def multi(num1, num2,):
    result = num1 * num2
    return result

#  modulus functions for each operation
def mod(num1, num2,):
    result = num1 % num2
    return result

#  Squre functions for each operation
def sqr(num1, num2,):
    result = num1 ** num2
    return result

#  calculator fuction
def advanced_calculator(num1, num2, op):
    try:
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = sub(num1, num2)
        elif op == "*":
            result = multi(num1, num2)
        elif op == "/":
            result = div(num1, num2)
        elif op == "%":
            result = mod(num1, num2)
        elif op == "**":
            result = sqr(num1, num2)
        else:
            return "Invalid operation. Please use one of +, -, *, /, **, %"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

# Check positive/negative
def check_result(result):
    if result >= 0:
        res = "Positive"
    else:
        res = "Negative"
    return res

# Check even/odd
def check_res(res):
    if res % 2 == 0:
        res2 = "Even"
    else:
        res2 = "Odd"
    return res2

#  get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /, **, %): ").strip()

#  call calculator function
print("Result:", advanced_calculator(num1, num2, op), "which is:", check_result(advanced_calculator(num1, num2, op)), "and", check_res(advanced_calculator(num1, num2, op)))