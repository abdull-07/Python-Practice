# Print multiplication table of any number using a loop.
num=int(input("Enter a number: "))
for i in range(10):
    print(num, 'x', i+1, '=', num*(i+1))