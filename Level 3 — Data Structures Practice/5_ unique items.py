# Write a program that takes a list and prints only unique items

numbers = []
for i in range(10):
    num = int (input("Enter number{}: ".format(i+1)))
    numbers.append(num)
    unique_numbers=[]
    for n in numbers:
        if n not in unique_numbers:
            unique_numbers.append(n)

print(" The original list is: ", numbers, "\n The list after removing duplicates is: ", unique_numbers)