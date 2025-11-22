# Convert temperature:

# Celsius → Fahrenheit

# Fahrenheit → Celsius

temp = float(input("Enter temperature: "))
curr = input("Enter current unit (C for Celsius, F for Fahrenheit): ")

if curr == 'C':
    converted_temp = (temp * 9/5)+32
    print(f"{temp}°C is {converted_temp}°F")
elif curr == 'F':
    converted_temp = (temp - 32) * 5/9
    print(f"{temp}°F is {converted_temp}°C")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")