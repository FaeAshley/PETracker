Personal Expense Tracker

This Personal Expense Tracker is a Python-based command-line application that helps users log, view, edit, and delete their expenses. All data is stored in a CSV file (expenses.csv), making it lightweight and easy to manage.

Features

Add Expense: Record new expenses with fields for date, amount, category, and description.

View All Expenses: Display a list of all recorded expenses.

Edit Expense: Update an existing expense's details (e.g., date, amount, category, or description).

Delete Expense: Remove an expense by its index.

CSV-Based Storage: Data is persisted in a CSV file, ensuring it is available even after restarting the application.

Requirements

Python 3.x

Getting Started

1. Clone the Repository

Download or clone the code to your local machine:

$ git clone https://github.com/your-repo/personal-expense-tracker.git
$ cd personal-expense-tracker

2. Install Dependencies

This program does not require any external libraries beyond Python's standard library.

3. Run the Program

Execute the script using Python:

$ python expense_tracker.py

How to Use

Main Menu

The program provides a menu with the following options:

Add Expense: Prompts the user to enter expense details (date, amount, category, and description) and saves them to the CSV file.

Edit Expense: Allows the user to select an expense by its index and update any of its fields.

Delete Expense: Removes an expense from the CSV file based on its index.

View All Expenses: Displays a list of all recorded expenses in the terminal.

Exit: Closes the program.

Example Workflow

Start the program.

Add an expense (e.g., 2024-12-01, 50.0, Food, Groceries).

View all expenses to verify it was added.

Edit an expense to correct any mistakes.

Delete an expense if it's no longer needed.

Exit the program.

File Details

expenses.csv: The file where all expense data is stored. Each row contains:

Date: The date of the expense (e.g., YYYY-MM-DD).

Amount: The amount spent (e.g., 50.0).

Category: The category of the expense (e.g., Food).

Description: A short description of the expense (e.g., Groceries).

Script Functions:

initialize_file: Ensures the CSV file exists and creates it if not.

add_expense: Adds a new expense to the CSV file.

view_expenses: Displays all expenses from the CSV file.

edit_expense: Updates an expense based on its index.

delete_expense: Removes an expense based on its index.

main_menu: Provides the user with a navigable menu to access the program's features.

Notes

The program uses zero-based indexing when referencing expenses.

Make sure to provide valid inputs (e.g., numeric amounts, valid dates) to avoid errors.

Future Enhancements

Add support for data visualization (e.g., spending charts by category or time).

Implement user authentication for multi-user functionality.

Allow filtering expenses by date or category.

Integrate a database (e.g., SQLite) for more robust data management.

License

This project is licensed under the MIT License. Feel free to modify and distribute it as needed.

Contributions

Contributions are welcome! Feel free to submit issues or pull requests on the GitHub repository.

Happy tracking your expenses! 💸
