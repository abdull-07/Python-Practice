# Problem 1 — Advanced Calculator
# Create a calculator program that:
# Asks the user for two numbers.
# Asks the user for an operation (+, -, *, /, **, %).
# Performs the operation.
# Prints if the result is even/odd and positive/negative.
# Handles division by zero and invalid inputs gracefully using try/except.
# Encapsulate the calculator in a function called advanced_calculator(num1, num2, op).

opt = int(input("Enter 1 for Arithmetic Opractions (+, -, *, /, **, %) and 2 for Unit Conversion 3 for Exit: "))
while True:
    #  add functions for each operation
    add = lambda num1, num2 : num1 + num2
    # def add(num1, num2,):
    #     result = num1 + num2
    #     return result

    #  substract functions for each operation
    sun = lambda num1, num2 : num1 - num2
    # def sub(num1, num2,):
    #     result = num1 - num2
    #     return result

    #  dividsion functions for each operation
    def div(num1, num2,):
        if num2 != 0:
            result = num1 / num2
        else:
            raise ZeroDivisionError
        return result

    #  Multiply functions for each operation
    multi = lambda num1, num2 : num1 * num2
    # def multi(num1, num2,):
    #     result = num1 * num2
    #     return result

    #  modulus functions for each operation
    mod = lambda num1, num2 : num1 % num2
    # def mod(num1, num2,):
    #     result = num1 % num2
    #     return result

    #  Squre functions for each operation
    sqr = lambda num1, num2 : num1 ** num2
    # def sqr(num1, num2,):
    #     result = num1 ** num2
    #     return result

    #  Length Conversion
    length_units = {"m": 1, "cm": 0.01, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144}
    weight_units = {"mg": 0.000001, "g": 0.001, "kg": 1, "t": 1000}  # changed Kg → kg

    def length_conversion(length, unit):
        if unit not in length_units:
            return "Invalid Unit"
        meters = length * length_units[unit]   # fixed "value" → "length"
        conversions = {u: round(meters / length_units[u], 2) for u in length_units}
        return conversions

    def weight_conversion(weight, unit):
        if unit not in weight_units:
            return "Invalid Unit"
        kilograms = weight * weight_units[unit]
        conversions = {u: round(kilograms / weight_units[u], 2) for u in weight_units}
        return conversions

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
    if opt == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /, **, %): ").strip()

    #  call calculator function
        print("Result:", advanced_calculator(num1, num2, op), "which is:", check_result(advanced_calculator(num1, num2, op)), "and", check_res(advanced_calculator(num1, num2, op)))
    # Unit Conversion
    elif opt == 2:
        chose = int(input("Enter 1 for Length Conversion, 2 for Weight Conversion, 3 for Temperature Conversion: "))
        if chose == 1:
            # lenth Conversion
            length = float(input("Enter length: "))
            unit = input("Enter unit (m, cm, km, in, ft, yd): ").strip().lower()
            print("Conversions:", length_conversion(length, unit))
        elif chose == 2:
            # weight Conversion
            weight = float(input("Enter weight: "))
            unit = input("Enter unit (mg, g, Kg, t): ").strip().lower()
            print("Conversions:", weight_conversion(weight, unit))
        elif chose == 3:
            # temperature Conversion
            temp = float(input("Enter Temperature: "))
            unit = input("Enter Unit (c,f): ").strip()
            if unit == "f":
                def tem_c_to_f(temp):
                    return (temp* 9/5) + 32
                print(f"The converted temperature is {tem_c_to_f(temp)}{unit}")
            elif unit == "c":
                def tem_f_to_c(temp):
                    return (temp- 32) * 5/9
                print(f"The converted temperature is {tem_f_to_c(temp)}{unit}")
            else:
                print("Invalid unit. Please use c, f")
        else:
            print("Invalid choice. Please use 1, 2, 3")
    elif opt == 3:
        print("Thank you for using the calculator.")
        break
    else:
        print("Invalid choice. Please use 1, 2")