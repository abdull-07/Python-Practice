# Find the sum of all digits of a number.
num =input("Enter a number like(23,345.4532): ")
sum_of_digit = 0
for d in str(num):
        sum_of_digit += int(d)
print("Sum of all digit is:", sum_of_digit)