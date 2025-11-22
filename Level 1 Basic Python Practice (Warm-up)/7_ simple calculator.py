# Create a simple calculator (add, subtract, multiply, divide).
num1 =int( input("Enter a first number: "))
num2 =int( input("Enter a second number: "))
sig=input("enter a operator:")

if sig=='+':
    result= num1+num2
elif sig=='-':
    result= num1-num2
elif sig=='*':
    result= num1*num2
elif sig=='/':
    if num2==0:
        print("Error: Division by zero is not allowed.")
    else:
        result= num1*num2
else:
    print("Invalid operator")
    exit()

print("The answer is:", result)

# if (result>0) and ((result)%2==0):
#     print ("The result is Even Positive")
# elif (result>0) and ((result)%2!=0):
#     print ("The result is Odd Positive")
# elif (result<0) and ((result)%2==0):
#     print ("The result is Even Negative")
# elif (result<0) and ((result)%2!=0):
#     print ("The result is Odd Negative")
# else:
#     print("The result is Zero")


print("Thank You!")