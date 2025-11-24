# Use map() + lambda to convert a list of Celsius values to Fahrenheit.
c = []
f = []

for i in range(5):
    try:
        temp = float(input("Enter temperature: "))
    except ValueError:
        print("Invalid temperature. Please enter a number. Entry skipped.")
        continue
    curr = input("Enter current unit (C for Celsius, F for Fahrenheit): ").strip()
    if curr.lower() == 'c':
        c.append(temp)
    elif curr.lower() == 'f':
        f.append(temp)
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit. Entry skipped.")
        
if c:
    fahrenheit = list(map(lambda x: (x * 9 / 5) + 32, c))
    print("The temperature(s) in Fahrenheit are:", fahrenheit)

if f:
    celsius = list(map(lambda x: (x - 32) * 5 / 9, f))
    print("The temperature(s) in Celsius are:", celsius)