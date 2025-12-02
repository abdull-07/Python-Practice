# Description: Track daily expenses. Add, remove, view, and categorize expenses. Optionally, save data in a CSV file.
# Topics Covered:
# Lists/dictionaries
# Functions & modular code
# File handling (CSV or TXT)
# Loops & conditionals
# Exception handling


import os
from datetime import datetime

# -------------------- Expense Class -------------------- #
class Expense:
    def __init__(self, amount, category, date, note=""):
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.note = note

    def to_csv(self):
        return f"{self.amount},{self.category},{self.date},{self.note}"

    @staticmethod
    def from_csv(line):
        amount, category, date, note = line.strip().split(",", 3)
        return Expense(float(amount), category, date, note)

# -------------------- Expense Tracker Class -------------------- #
class Expense_Tracker:
    def __init__(self):
        self.expenses = []

    # Add Expense
    def add_expense(self, expense):
        self.expenses.append(expense)

    # Remove Expense
    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"Deleted Expense: {removed.amount} - {removed.category}")
        else:
            print("Invalid Index!")

    # View Expenses
    def view_expense(self):
        if not self.expenses:
            print("No Expenses Found!")
            return
        print("\n---- All Expenses ----")
        for i, exp in enumerate(self.expenses):
            print(f"{i + 1}. Amount: {exp.amount} | Category: {exp.category} "
                  f"| Date: {exp.date} | Note: {exp.note}")
        print("-----------------------")

    # Calculate Total
    def calculate_total_expense(self):
        return sum(exp.amount for exp in self.expenses)

    # Save to file
    def save_to_file(self, filename="expenses.csv"):
        with open(filename, "w") as f:
            for exp in self.expenses:
                f.write(exp.to_csv() + "\n")
        print("Expenses saved to file.")

    # Load from file
    def load_from_file(self, filename="expenses.csv"):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                for line in f:
                    exp = Expense.from_csv(line)
                    self.expenses.append(exp)
            print("Expenses loaded from file.")
        else:
            print("No expenses found in file.")

# -------------------- User Interaction Functions -------------------- #
def add_expense(tracker):
    print("--- Add New Expense ---")
    try:
        amount = float(input("Enter Expense Amount: "))
    except ValueError:
        print("Invalid Input! Please enter a valid number.")
        return

    category = input("Enter Expense Category: ")
    date = input("Enter Expense Date (YYYY-MM-DD) or leave blank for today: ")
    if not date.strip():
        date = datetime.now().strftime("%Y-%m-%d")
    note = input("Enter Expense Note (optional): ")

    expense = Expense(amount, category, date, note)
    tracker.add_expense(expense)
    print("Expense added successfully!")

def view_expense(tracker):
    tracker.view_expense()

def delete_expense(tracker):
    if not tracker.expenses:
        print("No Expenses Found!")
        return
    tracker.view_expense()
    try:
        index = int(input("Enter Expense Number to Delete: ")) - 1
        tracker.remove_expense(index)
    except ValueError:
        print("Invalid Input! Please enter a number.")

def calculate_total(tracker):
    total = tracker.calculate_total_expense()
    print(f"Total Expense: {total}")

def save_to_file(tracker):
    tracker.save_to_file()

def load_from_file(tracker):
    tracker.load_from_file()

# -------------------- Main Menu Loop -------------------- #
def main():
    tracker = Expense_Tracker()
    load_from_file(tracker)

    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total Spending")
        print("5. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(tracker)
        elif choice == "2":
            view_expense(tracker)
        elif choice == "3":
            delete_expense(tracker)
        elif choice == "4":
            calculate_total(tracker)
        elif choice == "5":
            save_to_file(tracker)
            print("Goodbye!")
            break
        else:
            print("Invalid Choice! Please enter a valid option.")

# -------------------- Run App -------------------- #
if __name__ == "__main__":
    main()