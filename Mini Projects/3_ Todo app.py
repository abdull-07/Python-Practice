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

MASTER_PASSWORD_FILE = "password.txt"
TODO_FILE = "Todos.txt"

print("Welcome to the Todo App!")
print("1. Add Task \n2. Delete Task \n3. View All Tasks \n4. Update Task \n5. Exit")

# LOAD / SAVE TASKS
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for t in tasks:
            f.write(t + '\n')

# PASSWORD VALIDATION

def validate_password(password):
    has_upper = any(p.isupper() for p in password)
    has_digit = any(p.isdigit() for p in password)
    special_characters = r"!@#$%^&*()-_=+[];:'\",<.>/?\|"
    has_special = any(p in special_characters for p in password)

    if len(password) >= 8 and has_upper and has_digit and has_special:
        return True

    # Error messages
    print("❌ Password is weak!")
    if len(password) < 8:
        print("→ Must be at least 8 characters")
    if not has_upper:
        print("→ Must have at least 1 uppercase letter")
    if not has_digit:
        print("→ Must have at least 1 digit")
    if not has_special:
        print("→ Must have at least 1 special character")

    return False

# MASTER PASSWORD SETUP

def setup_master_password():
    if os.path.exists(MASTER_PASSWORD_FILE):
        return  # Already exists

    print("\n🔐 Set your MASTER PASSWORD (required to access Todo App):")
    while True:
        pwd = input("Create Master Password: ")
        if validate_password(pwd):
            with open(MASTER_PASSWORD_FILE, "w") as f:
                f.write(pwd)
            print("✅ Master Password Saved!")
            break

def verify_master_password():
    with open(MASTER_PASSWORD_FILE, "r") as f:
        correct_password = f.read().strip()

    while True:
        pwd = input("\nEnter Master Password to continue: ")

        if pwd == correct_password:
            print("🔓 Access Granted!\n")
            return True
        else:
            print("❌ Incorrect Password. Try again.\n")

# TODO OPERATIONS

def update_task(tasks):
    print("\nCurrent Tasks:")
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t}")

    try:
        num = int(input("\nEnter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter new updated task: ")
            tasks[num - 1] = new_task
            print("✔ Task updated successfully!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# MAIN PROGRAM

setup_master_password()
verify_master_password()

tasks = load_tasks()

while True:
    print("\nYour existing tasks:", tasks)
    
    opt = input("\nChoose option (1–5): ")

    if opt == "1":   # Add Task
        task = input("Enter new task: ")
        pwd = input("Enter password to validate: ")
        if validate_password(pwd):
            tasks.append(task)
            print("✔ Task added!")
        else:
            print("❌ Task NOT added due to weak password.")

    elif opt == "2":  # Delete Task
        task = input("Enter task to delete: ")
        if task in tasks:
            tasks.remove(task)
            print("✔ Task deleted!")
        else:
            print("❌ Task not found.")

    elif opt == "3":  # View Tasks
        print("\n📌 Your Tasks:")
        for t in tasks:
            print("•", t)

    elif opt == "4":  # Update Task
        update_task(tasks)

    elif opt == "5":  # Exit
        print("Goodbye!")
        save_tasks(tasks)
        break

    else:
        print("❌ Invalid option! Try again.")
    save_tasks(tasks)