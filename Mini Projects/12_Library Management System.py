# Student / Library Management System (OOP Project)
# Description: A program that stores student or book information using classes. Supports adding, updating, deleting, and displaying records.
# Classes & objects
# Constructors (__init__)
# Inheritance & polymorphism
# Encapsulation (private attributes)
# Lists/dictionaries to store multiple objects
# File handling: save records to separate files
# Book borrowing system

import json
import os
from datetime import datetime


# ==========================
# Library Management System
# ==========================

class Student:
    counter = 1  # Class variable to track student IDs
    
    def __init__(self, Id, name, age, gender, roll_no, marks):
        self.id = Student.counter  # assign ID automatically
        Student.counter += 1
        self.name = name
        self.age = age
        self.gender = gender
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Roll No: {self.roll_no}, Marks: {self.marks}"

    def update_info(self, name=None, age=None, gender=None, roll_no=None, marks=None):
        if name: self.name = name
        if age: self.age = age
        if gender: self.gender = gender
        if roll_no: self.roll_no = roll_no
        if marks: self.marks = marks


class Book:
    counter = 1  # Class variable to track book IDs
    
    def __init__(self, Id, title, author, isbn, publisher, price, available=True):
        self.id = Book.counter
        Book.counter += 1
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.price = price
        self.available = available  # Track if book is available for borrowing

    def display_info(self):
        status = "✅ Available" if self.available else "❌ Borrowed"
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Publisher: {self.publisher}, Price: {self.price}, Status: {status}"

    def update_info(self, title=None, author=None, isbn=None, publisher=None, price=None):
        if title: self.title = title
        if author: self.author = author
        if isbn: self.isbn = isbn
        if publisher: self.publisher = publisher
        if price: self.price = price


class Librarian:
    counter = 1  # Class variable to track librarian IDs
    
    def __init__(self, Id, name, age, gender, salary):
        self.id = Librarian.counter
        Librarian.counter += 1
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

    def display_info(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Salary: {self.salary}"

    def update_info(self, name=None, age=None, gender=None, salary=None):
        if name: self.name = name
        if age: self.age = age
        if gender: self.gender = gender
        if salary: self.salary = salary


class BorrowRecord:
    counter = 1  # Class variable to track borrow record IDs
    
    def __init__(self, Id, student_id, book_id, student_name, book_title, borrow_date):
        self.id = BorrowRecord.counter
        BorrowRecord.counter += 1
        self.student_id = student_id
        self.book_id = book_id
        self.student_name = student_name
        self.book_title = book_title
        self.borrow_date = borrow_date
        self.return_date = None
        self.returned = False
    
    def display_info(self):
        status = "✅ Returned" if self.returned else "📖 Borrowed"
        return_info = f", Return Date: {self.return_date}" if self.returned else ""
        return f"ID: {self.id}, Student: {self.student_name} (ID: {self.student_id}), Book: {self.book_title} (ID: {self.book_id}), Borrow Date: {self.borrow_date}, Status: {status}{return_info}"


# ==========================
# Data Storage
# ==========================
students = []
books = []
librarians = []
borrow_records = []

# File paths
STUDENTS_FILE = "students.txt"
BOOKS_FILE = "books.txt"
LIBRARIANS_FILE = "librarians.txt"
BORROW_RECORDS_FILE = "borrow_records.txt"


# ==========================
# File Handling Functions
# ==========================
def save_students():
    """Save all students to students.txt"""
    with open(STUDENTS_FILE, "w") as f:
        for student in students:
            data = {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "gender": student.gender,
                "roll_no": student.roll_no,
                "marks": student.marks
            }
            f.write(json.dumps(data) + "\n")


def load_students():
    """Load students from students.txt"""
    global students
    if not os.path.exists(STUDENTS_FILE):
        return
    
    students = []
    max_id = 0
    with open(STUDENTS_FILE, "r") as f:
        for line in f:
            if line.strip():
                data = json.loads(line.strip())
                student = Student.__new__(Student)
                student.id = data["id"]
                student.name = data["name"]
                student.age = data["age"]
                student.gender = data["gender"]
                student.roll_no = data["roll_no"]
                student.marks = data["marks"]
                students.append(student)
                max_id = max(max_id, student.id)
    
    # Update counter to avoid ID conflicts
    Student.counter = max_id + 1


def save_books():
    """Save all books to books.txt"""
    with open(BOOKS_FILE, "w") as f:
        for book in books:
            data = {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "publisher": book.publisher,
                "price": book.price,
                "available": book.available
            }
            f.write(json.dumps(data) + "\n")


def load_books():
    """Load books from books.txt"""
    global books
    if not os.path.exists(BOOKS_FILE):
        return
    
    books = []
    max_id = 0
    with open(BOOKS_FILE, "r") as f:
        for line in f:
            if line.strip():
                data = json.loads(line.strip())
                book = Book.__new__(Book)
                book.id = data["id"]
                book.title = data["title"]
                book.author = data["author"]
                book.isbn = data["isbn"]
                book.publisher = data["publisher"]
                book.price = data["price"]
                book.available = data.get("available", True)
                books.append(book)
                max_id = max(max_id, book.id)
    
    # Update counter to avoid ID conflicts
    Book.counter = max_id + 1


def save_librarians():
    """Save all librarians to librarians.txt"""
    with open(LIBRARIANS_FILE, "w") as f:
        for librarian in librarians:
            data = {
                "id": librarian.id,
                "name": librarian.name,
                "age": librarian.age,
                "gender": librarian.gender,
                "salary": librarian.salary
            }
            f.write(json.dumps(data) + "\n")


def load_librarians():
    """Load librarians from librarians.txt"""
    global librarians
    if not os.path.exists(LIBRARIANS_FILE):
        return
    
    librarians = []
    max_id = 0
    with open(LIBRARIANS_FILE, "r") as f:
        for line in f:
            if line.strip():
                data = json.loads(line.strip())
                librarian = Librarian.__new__(Librarian)
                librarian.id = data["id"]
                librarian.name = data["name"]
                librarian.age = data["age"]
                librarian.gender = data["gender"]
                librarian.salary = data["salary"]
                librarians.append(librarian)
                max_id = max(max_id, librarian.id)
    
    # Update counter to avoid ID conflicts
    Librarian.counter = max_id + 1


def save_borrow_records():
    """Save all borrow records to borrow_records.txt"""
    with open(BORROW_RECORDS_FILE, "w") as f:
        for record in borrow_records:
            data = {
                "id": record.id,
                "student_id": record.student_id,
                "book_id": record.book_id,
                "student_name": record.student_name,
                "book_title": record.book_title,
                "borrow_date": record.borrow_date,
                "return_date": record.return_date,
                "returned": record.returned
            }
            f.write(json.dumps(data) + "\n")


def load_borrow_records():
    """Load borrow records from borrow_records.txt"""
    global borrow_records
    if not os.path.exists(BORROW_RECORDS_FILE):
        return
    
    borrow_records = []
    max_id = 0
    with open(BORROW_RECORDS_FILE, "r") as f:
        for line in f:
            if line.strip():
                data = json.loads(line.strip())
                record = BorrowRecord.__new__(BorrowRecord)
                record.id = data["id"]
                record.student_id = data["student_id"]
                record.book_id = data["book_id"]
                record.student_name = data["student_name"]
                record.book_title = data["book_title"]
                record.borrow_date = data["borrow_date"]
                record.return_date = data.get("return_date")
                record.returned = data.get("returned", False)
                borrow_records.append(record)
                max_id = max(max_id, record.id)
    
    # Update counter to avoid ID conflicts
    BorrowRecord.counter = max_id + 1


# ==========================
# Utility Functions
# ==========================
def find_student(student_id):
    for s in students:
        if s.id == student_id:
            return s
    return None


def find_book(book_id):
    for b in books:
        if b.id == book_id:
            return b
    return None


def find_librarian(lib_id):
    for l in librarians:
        if l.id == lib_id:
            return l
    return None


# ==========================
# Menu Functions
# ==========================
def manage_students():
    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Show All Students")
        print("6. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            roll_no = int(input("Roll No: "))
            marks = float(input("Marks: "))
            students.append(Student(None, name, age, gender, roll_no, marks))
            save_students()
            print("✅ Student added successfully!")

        elif choice == "2":
            Id = int(input("Enter Student ID to update: "))
            student = find_student(Id)
            if student:
                name = input("Name (leave blank to skip): ")
                age = input("Age (leave blank to skip): ")
                gender = input("Gender (leave blank to skip): ")
                roll_no = input("Roll No (leave blank to skip): ")
                marks = input("Marks (leave blank to skip): ")
                student.update_info(
                    name=name or None,
                    age=int(age) if age else None,
                    gender=gender or None,
                    roll_no=int(roll_no) if roll_no else None,
                    marks=float(marks) if marks else None
                )
                save_students()
                print("✅ Student updated successfully!")
            else:
                print("❌ Student not found.")

        elif choice == "3":
            Id = int(input("Enter Student ID to delete: "))
            student = find_student(Id)
            if student:
                students.remove(student)
                save_students()
                print("✅ Student deleted successfully!")
            else:
                print("❌ Student not found.")

        elif choice == "4":
            Id = int(input("Enter Student ID to search: "))
            student = find_student(Id)
            if student:
                print(student.display_info())
            else:
                print("❌ Student not found.")

        elif choice == "5":
            if students:
                for s in students:
                    print(s.display_info())
            else:
                print("No students available.")

        elif choice == "6":
            break
        else:
            print("❌ Invalid choice.")


def manage_books():
    while True:
        print("\n--- Book Management ---")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. Show All Books")
        print("6. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            publisher = input("Publisher: ")
            price = float(input("Price: "))
            books.append(Book(None, title, author, isbn, publisher, price))
            save_books()
            print("✅ Book added successfully!")

        elif choice == "2":
            Id = int(input("Enter Book ID to update: "))
            book = find_book(Id)
            if book:
                title = input("Title (leave blank to skip): ")
                author = input("Author (leave blank to skip): ")
                isbn = input("ISBN (leave blank to skip): ")
                publisher = input("Publisher (leave blank to skip): ")
                price = input("Price (leave blank to skip): ")
                book.update_info(
                    title=title or None,
                    author=author or None,
                    isbn=isbn or None,
                    publisher=publisher or None,
                    price=float(price) if price else None
                )
                save_books()
                print("✅ Book updated successfully!")
            else:
                print("❌ Book not found.")

        elif choice == "3":
            Id = int(input("Enter Book ID to delete: "))
            book = find_book(Id)
            if book:
                books.remove(book)
                save_books()
                print("✅ Book deleted successfully!")
            else:
                print("❌ Book not found.")

        elif choice == "4":
            Id = int(input("Enter Book ID to search: "))
            book = find_book(Id)
            if book:
                print(book.display_info())
            else:
                print("❌ Book not found.")

        elif choice == "5":
            if books:
                for b in books:
                    print(b.display_info())
            else:
                print("No books available.")

        elif choice == "6":
            break
        else:
            print("❌ Invalid choice.")


def manage_librarians():
    while True:
        print("\n--- Librarian Management ---")
        print("1. Add Librarian")
        print("2. Update Librarian")
        print("3. Delete Librarian")
        print("4. Search Librarian")
        print("5. Show All Librarians")
        print("6. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            salary = float(input("Salary: "))
            librarians.append(Librarian(None, name, age, gender, salary))
            save_librarians()
            print("✅ Librarian added successfully!")

        elif choice == "2":
            Id = int(input("Enter Librarian ID to update: "))
            librarian = find_librarian(Id)
            if librarian:
                name = input("Name (leave blank to skip): ")
                age = input("Age (leave blank to skip): ")
                gender = input("Gender (leave blank to skip): ")
                salary = input("Salary (leave blank to skip): ")
                librarian.update_info(
                    name=name or None,
                    age=int(age) if age else None,
                    gender=gender or None,
                    salary=float(salary) if salary else None
                )
                save_librarians()
                print("✅ Librarian updated successfully!")
            else:
                print("❌ Librarian not found.")

        elif choice == "3":
            Id = int(input("Enter Librarian ID to delete: "))
            librarian = find_librarian(Id)
            if librarian:
                librarians.remove(librarian)
                save_librarians()
                print("✅ Librarian deleted successfully!")
            else:
                print("❌ Librarian not found.")

        elif choice == "4":
            Id = int(input("Enter Librarian ID to search: "))
            librarian = find_librarian(Id)
            if librarian:
                print(librarian.display_info())
            else:
                print("❌ Librarian not found.")

        elif choice == "5":
            if librarians:
                for l in librarians:
                    print(l.display_info())
            else:
                print("No librarians available.")

        elif choice == "6":
            break
        else:
            print("❌ Invalid choice.")


def manage_borrow_books():
    """Manage book borrowing and returns"""
    while True:
        print("\n--- 📚 Book Borrowing System ---")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. View Borrowed Books")
        print("4. View Borrow History")
        print("5. Back")
        choice = input("Enter choice: ")

        if choice == "1":  # Borrow Book
            # Show available books
            available_books = [b for b in books if b.available]
            if not available_books:
                print("❌ No books available for borrowing.")
                continue
            
            print("\n📚 Available Books:")
            for book in available_books:
                print(book.display_info())
            
            try:
                book_id = int(input("\nEnter Book ID to borrow: "))
                book = find_book(book_id)
                
                if not book:
                    print("❌ Book not found.")
                    continue
                
                if not book.available:
                    print("❌ This book is already borrowed.")
                    continue
                
                # Show students
                if not students:
                    print("❌ No students registered.")
                    continue
                
                print("\n👥 Registered Students:")
                for student in students:
                    print(student.display_info())
                
                student_id = int(input("\nEnter Student ID: "))
                student = find_student(student_id)
                
                if not student:
                    print("❌ Student not found.")
                    continue
                
                # Create borrow record
                borrow_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                record = BorrowRecord(
                    None,
                    student.id,
                    book.id,
                    student.name,
                    book.title,
                    borrow_date
                )
                borrow_records.append(record)
                book.available = False
                
                save_borrow_records()
                save_books()
                
                print(f"✅ Book '{book.title}' borrowed by {student.name} successfully!")
                
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")

        elif choice == "2":  # Return Book
            # Show borrowed books
            active_borrows = [r for r in borrow_records if not r.returned]
            if not active_borrows:
                print("❌ No books currently borrowed.")
                continue
            
            print("\n📖 Currently Borrowed Books:")
            for record in active_borrows:
                print(record.display_info())
            
            try:
                record_id = int(input("\nEnter Borrow Record ID to return: "))
                record = None
                for r in borrow_records:
                    if r.id == record_id:
                        record = r
                        break
                
                if not record:
                    print("❌ Borrow record not found.")
                    continue
                
                if record.returned:
                    print("❌ This book has already been returned.")
                    continue
                
                # Mark as returned
                record.returned = True
                record.return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Make book available again
                book = find_book(record.book_id)
                if book:
                    book.available = True
                
                save_borrow_records()
                save_books()
                
                print(f"✅ Book '{record.book_title}' returned successfully!")
                
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")

        elif choice == "3":  # View Borrowed Books
            active_borrows = [r for r in borrow_records if not r.returned]
            if not active_borrows:
                print("\n📚 No books currently borrowed.")
            else:
                print("\n📖 Currently Borrowed Books:")
                for record in active_borrows:
                    print(record.display_info())

        elif choice == "4":  # View Borrow History
            if not borrow_records:
                print("\n📚 No borrow history available.")
            else:
                print("\n📜 Borrow History:")
                for record in borrow_records:
                    print(record.display_info())

        elif choice == "5":  # Back
            break
        else:
            print("❌ Invalid choice.")


# ==========================
# Main Program
# ==========================
def main():
    # Load existing data from files
    print("📚 Loading data from files...")
    load_students()
    load_books()
    load_librarians()
    load_borrow_records()
    print(f"✅ Loaded {len(students)} students, {len(books)} books, {len(librarians)} librarians, {len(borrow_records)} borrow records\n")
    
    while True:
        print("\n=== Library Management System ===")
        print("1. Manage Students")
        print("2. Manage Books")
        print("3. Manage Librarians")
        print("4. Borrow/Return Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_students()
        elif choice == "2":
            manage_books()
        elif choice == "3":
            manage_librarians()
        elif choice == "4":
            manage_borrow_books()
        elif choice == "5":
            print("💾 Saving all data...")
            save_students()
            save_books()
            save_librarians()
            save_borrow_records()
            print("✅ Data saved successfully!")
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()