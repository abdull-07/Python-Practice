# Store 10 numbers in a list and find:
# Max
# Min
# Average


numbers = []
for i in range(10):
    num = int(input("Enter number{}: ".format(i+1)))
    numbers.append(num)
max = max(numbers)
min = min(numbers)
average = sum(numbers)/len(numbers)
print(" The list is: ", numbers, "\n Max number is: ", max, "\n Min number is: ", min, "\n Average of list is: ", average)