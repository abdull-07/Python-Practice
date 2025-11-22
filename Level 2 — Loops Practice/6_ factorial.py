# Find factorial of a number using a loop.
num=int(input("Enter a number for factorial: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("The factorial of", num, "is", factorial)