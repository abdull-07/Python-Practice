# Problem 5 — Mini “Todo + Password” App
# Create a todo list app that allows adding, deleting, and viewing tasks.
# When adding a task, ask for a password. Validate it using the following rules:
# At least 8 characters
# At least 1 digit
# At least 1 uppercase letter
# At least 1 special character
# If the password is invalid, reject adding the task and give proper feedback.
# Store tasks in a file so they persist after the program closes.
# Use functions for password validation and todo operations.

import os
print("Welcome to the Todo App!")
print("1. Add a task \n2. Delete task \n3. View all tasks \n4. Exit")

def load_tasks():
    if not os.path.exists("Todos.txt"):
        return []
    with open("Todos.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def save_tasks(tasks):
    with open("Todos.txt", "w") as f:
        for t in tasks:
            f.write(t+'\n')
    return



def validate_password():
    password = input("Enter a Password: ")
    has_upper_case = False
    has_digit=False
    has_special_char=False
    special_char=r"!@#$%^&*()-_=+[];:'\",<.>/?\|"

    for p in password:
        if p.isupper():
            has_upper_case = True
        if p.isdigit():
            has_digit = True
        if p in special_char:
            has_special_char = True
    if len(password)>= 8 and has_upper_case and has_digit and has_special_char:
        return True
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
        return False


dos = load_tasks()

while True:
    try:
        print("Your Existing tasks are: ", dos)
        opt=int(input("Chose an option: "))
        if opt==1:
            task=input("Enter the task: ")
            if validate_password():
                dos.append(task)
                print("Task added successfully!")
            else:
                print("Task NOT added due to weak password.")
        elif opt==2:
            task=input("Enter the task to be deleted: ")
            if task in dos:
                dos.remove(task)
                print("Task deleted successfully!")
            else:
                print("Task no found!")
        elif opt==3:
            print("your tasks are: ")
            print(type(dos))
            for i in dos:
                print(i)
        elif opt==4:
            break
        else:
            print("Invalid option! Please try again.")

        save_tasks(dos)
    except FileNotFoundError:
        print(f"Error: File Todos not found")
    except Exception as e:
        print("An unexpected error occoure")