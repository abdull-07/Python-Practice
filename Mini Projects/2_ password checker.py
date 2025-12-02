# The code snippet you provided is a comment in Python that describes the requirements for a simple
# password checker program. It outlines the criteria that a password must meet in order to be
# considered valid. The program would likely prompt the user to enter a password and then check if it
# meets these requirements before accepting it as a valid password.
# Simple Password Checker
# Requirements:
# At least 8 characters
# At least 1 digit
# At least 1 uppercase letter
# At least 1 special character

password = input("Enter a Password: ")
has_upper_case = False
has_digit=False
has_special_char=False
special_char="!@#$%^&*()-_=+[];:'\",<.>/?\|"

for p in password:
    if p.isupper():
        has_upper_case = True
    if p.isdigit():
        has_digit = True
    if p in special_char:
        has_special_char = True
if len(password)>= 8 and has_upper_case and has_digit and has_special_char:
    print("Password is strong")
else:
    print("Password is week")
    if len(password) < 8:
        print("Password must be at least 8 characters long")
    if not has_upper_case:
        print("Password must contain at least one uppercase letter")
    if not has_digit:
        print("Password must contain at least one digit")
    if not has_special_char:
        print("Password must contain at least one special character")