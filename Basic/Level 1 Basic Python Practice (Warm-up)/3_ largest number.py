# Take 3 numbers from user and print the largest.
num1=int(input("Enter a number : "))
num2=int(input("Enter an other number : "))
num3=int(input("Enter an other number : "))
if (num1>=num2)and(num1>=num3):
    print(num1,"is the largest number")
elif (num2>=num1)and(num2>=num3):
    print(num2,"is the largest number")
else:
    print(num3,"is the largest number")