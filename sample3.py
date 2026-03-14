import json
import os
class Book:
    def __init__(self, book_id, title, author, issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = issued
    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "issued": self.issued
        }
class Library:
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.books = {}
        self.load_books()
    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                for book in data:
                    b = Book(**book)
                    self.books[b.book_id] = b
    def save_books(self):
        with open(self.filename, "w") as file:
            json.dump([b.to_dict() for b in self.books.values()], file, indent=4)
    def add_book(self):
        book_id = input("Enter Book ID: ")
        if book_id in self.books:
            print(" Book ID already exists!")
            return
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        self.books[book_id] = Book(book_id, title, author)
        self.save_books()
        print(" Book added successfully!")
    def search_book(self):
        keyword = input("Enter title or author to search: ").lower()
        found = False
        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                status = "Issued" if book.issued else "Available"
                print(f"{book.book_id} | {book.title} | {book.author} | {status}")
                found = True
        if not found:
            print(" No book found.")
    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")
        if book_id not in self.books:
            print(" Book not found.")
            return
        book = self.books[book_id]
        if book.issued:
            print(" Book already issued.")
        else:
            book.issued = True
            self.save_books()
            print(" Book issued successfully.")
    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        if book_id not in self.books:
            print(" Book not found.")
            return
        book = self.books[book_id]
        if not book.issued:
            print(" Book was not issued.")
        else:
            book.issued = False
            self.save_books()
            print(" Book returned successfully.")
    def report(self):
        total = len(self.books)
        issued = sum(1 for b in self.books.values() if b.issued)
        print("\n Library Report")
        print("Total Books:", total)
        print("Issued Books:", issued)
        print("Available Books:", total - issued)
def main():
    library = Library()
    while True:
        print("\n Library Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Report")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.search_book()
        elif choice == "3":
            library.issue_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.report()
        elif choice == "6":
            print(" Exiting program...")
            break
        else:
            print(" Invalid choice!")
if __name__ == "__main__":
    main()