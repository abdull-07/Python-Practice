str1=input("Enter String: ")
print(str1)
str2="".join(reversed(str1))
print(str2)

if str1==str2:
    print("The Entered String is Palindrome")
else:
    print("The Entered String is Not Palindrome")

