import csv
from datetime import datetime

FILE = "expenses.csv"

# Add transaction
def add_entry():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (food, travel, salary, etc): ")
    amount = float(input("Enter amount: "))
    type_t = input("Type (income/expense): ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, type_t])

    print("Entry added successfully!")


# Show all records
def view_entries():
    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No records found.")


# Monthly summary
def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    income = 0
    expense = 0

    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                if row[0].startswith(month):
                    if row[3] == "income":
                        income += float(row[2])
                    else:
                        expense += float(row[2])

        print("Total Income:", income)
        print("Total Expense:", expense)
        print("Balance:", income - expense)

    except FileNotFoundError:
        print("No records found.")


while True:
    print("\nExpense Tracker")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Monthly Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_entry()

    elif choice == "2":
        view_entries()

    elif choice == "3":
        monthly_summary()

    elif choice == "4":
        break

    else:
        print("Invalid choice")