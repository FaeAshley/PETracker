import csv
from datetime import datetime

# File to store expenses
FILE_NAME = 'expenses.csv'


# Initialize CSV if not exists
def initialize_file():
    try:
        with open(FILE_NAME, 'x') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Amount', 'Category', 'Description'])
    except FileExistsError:
        pass


def add_expense():
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        amount = float(input("Enter the amount: "))  # Convert to float for currency
        category = input("Enter the category (e.g., Food, Travel): ")
        description = input("Enter a short description: ")

        with open(FILE_NAME, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([date, amount, category, description])
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input for amount. Please enter a number.")


def view_expenses():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found. Start by adding one!")


def edit_expense(index):
    # Step 1: Read all expenses from the file
    expenses = []
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)  # Each row is a dictionary

    # Step 2: Check if the index is valid
    if index < 0 or index >= len(expenses):
        print("Invalid index. Please try again.")
        return

    # Step 3: Display the selected expense
    expense = expenses[index]
    print(f"Editing expense: {expense}")

    # Step 4: Update fields interactively
    if input("Update Date? (yes/no): ").strip().lower() == 'yes':
        expense["Date"] = input("Enter new date (YYYY-MM-DD): ")

    if input("Update Amount? (yes/no): ").strip().lower() == 'yes':
        try:
            expense["Amount"] = str(float(input("Enter new amount: ")))  # Convert to float, then back to string
        except ValueError:
            print("Invalid amount. Keeping the original value.")

    if input("Update Category? (yes/no): ").strip().lower() == 'yes':
        expense["Category"] = input("Enter new category: ")

    if input("Update Description? (yes/no): ").strip().lower() == 'yes':
        expense["Description"] = input("Enter new description: ")

    # Step 5: Write the updated expenses list back to the file
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Amount", "Category", "Description"])
        writer.writeheader()
        writer.writerows(expenses)  # Write all expenses, including the updated one

    print("Expense updated successfully!")
    print("Updated Expense: ")
    print(expense)


def delete_expense(index):
    # Step 1: Read all expenses from the file
    expenses = []
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)

    # Step 2: Validate the index
    if index < 0 or index >= len(expenses):
        print("Invalid index. Please try again.")
        return

    # Step 3: Remove the specified expense
    removed_expense = expenses.pop(index)
    print(f"Deleted expense: {removed_expense}")

    # Step 4: Write the updated list back to the file
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Amount", "Category", "Description"])
        writer.writeheader()  # Write the header
        writer.writerows(expenses)  # Write all remaining expenses

    print("Expense deleted successfully!")


def main_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. Delete Expense")
        print("4. View All Expenses")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            edit_expense(int(input("Enter Expense Index: ")))
        elif choice == '3':
            delete_expense(int(input("Enter Expense Index: ")))
        elif choice == '4':
            view_expenses()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    main_menu()


if __name__ == "__main__":
    main()

