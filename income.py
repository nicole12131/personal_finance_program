# LV 1st Income and Expense Tracking
# import csv

# Create empty list/dictionary to store income entries in memory
# Each income entry will have: date, amount, source
# Create empty list/dictionary to store expense entries in memory
# Each expense entry will have: date, amount, category
# Define predefined expense categories (e.g., Food, Transport, Bills, Entertainment, Other)

#  Mainmenu
# Repeat until user chooses to Exit
# Display menu options with numbers:
# 1. Add Income
# 2. Add Expense
# 3. View Totals
# 4. Exit
# Prompt user to input a number (menu_option)

#   If user chooses 1:
#       take them to add incomefunciton

#   If user chooses 2:
#       take them to add expense

#   If user chooses 3:
#       take user to view totals

#   If user chooses 4:
#       take user to exit

# function error handling
# For all user inputs:
    # Catch invalid date formats
    # Catch non-numeric amounts
    # Catch invalid category selections
# Display appropriate error messages
# Loop back to input prompts instead of crashing
# Mostly used for the GUI

# function GUI
# Menu options can be represented as buttons/tabs
# Add Income / Add Expense:
    # Input fields for date, amount, and source/category
# View Totals:
    # Display totals in labels or table format
# Exit:
    # Save data to CSV and close GUI window


# Functions

# Add income
# make a function error handling
# For all user inputs:
    # Catch invalid date formats
    # Catch non-numeric amounts
    # Catch invalid category selections
# Display appropriate error messages
# Loop back to input prompts instead of crashing

# Add Expense
    # Prompt user to enter date of expense (format YYYY-MM-DD)
    # Prompt user to enter amount (numeric)
    # Display predefined categories and ask user to choose one
    # Validate input:
        # Check date format
        # Check amount is numeric
        # Check category selection is valid
    # If input invalid:
        # Display error message
        # Ask for input again
    # If input valid:
        # Create new expense entry dictionary:
            # date = user input
            # amount = user input
            # category = selected category
        # Add entry to expense entries list/dictionary in memory
        # Display confirmation message: "Expense added successfully"
    # Return to main menu

# View Totals
    # Prompt user to input start date (format YYYY-MM-DD)
    # Prompt user to input end date (format YYYY-MM-DD)
    # Validate date inputs:
        # Check both dates are in correct format
    # If invalid:
        # Display error message
        # Return to main menu
    # If valid:
        # Filter income entries between start date and end date
        # Filter expense entries between start date and end date
        # Calculate total income by summing amounts of filtered income entries
        # Calculate total expenses by summing amounts of filtered expense entries
        # Calculate net balance = total income - total expenses
        # Display results:
            # Total Income
            # Total Expenses
            # Net Balance
    # Return to main menu

# Exit
    # Save all income and expense entries to CSV file
    # Overwrite previous CSV file if exists
    # Ensure data is preserved for next program run
    # Display message: "Data saved. Goodbye!"
    # Exit program



# View Totals
# call main to test code

import csv
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class TrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Income & Expense Tracker")
        self.root.geometry("300x300")

        self.income_entries = []
        self.expense_entries = []
        self.categories = ["food", "rent", "utilities", "transportation", "entertainment"]

        self.build_menu()


    # VALIDATION 
    def valid_date(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except:
            return False


    #  MENU UI 
    def build_menu(self):
        tk.Label(self.root, text="Main Menu", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="1. Add Income", command=self.open_income).pack(pady=5)
        tk.Button(self.root, text="2. Add Expense", command=self.open_expense).pack(pady=5)
        tk.Button(self.root, text="3. View Totals", command=self.open_totals).pack(pady=5)
        tk.Button(self.root, text="4. Exit", command=self.exit_app).pack(pady=5)


    #  ADD INCOME 
    def open_income(self):
        window = tk.Toplevel(self.root)
        window.title("Add Income")

        tk.Label(window, text="Date (YYYY-MM-DD)").pack()
        date_entry = tk.Entry(window)
        date_entry.pack()

        tk.Label(window, text="Amount").pack()
        amount_entry = tk.Entry(window)
        amount_entry.pack()

        tk.Label(window, text="Source").pack()
        source_entry = tk.Entry(window)
        source_entry.pack()

        def submit():
            date = date_entry.get()
            amount = amount_entry.get()
            source = source_entry.get()

            if not self.valid_date(date):
                messagebox.showerror("Error", "Invalid date")
                return

            if source == "":
                messagebox.showerror("Error", "Enter source")
                return

            try:
                amount = float(amount)
            except:
                messagebox.showerror("Error", "Amount must be number")
                return

            self.income_entries.append({
                "date": date,
                "amount": amount,
                "source": source
            })

            messagebox.showinfo("Success", "Income added")
            window.destroy()

        tk.Button(window, text="Submit", command=submit).pack()


    #  ADD EXPENSE 
    def open_expense(self):
        window = tk.Toplevel(self.root)
        window.title("Add Expense")

        tk.Label(window, text="Date (YYYY-MM-DD)").pack()
        date_entry = tk.Entry(window)
        date_entry.pack()

        tk.Label(window, text="Amount").pack()
        amount_entry = tk.Entry(window)
        amount_entry.pack()

        tk.Label(window, text="Category").pack()
        category_var = tk.StringVar(window)
        category_var.set(self.categories[0])
        tk.OptionMenu(window, category_var, *self.categories).pack()

        def submit():
            date = date_entry.get()
            amount = amount_entry.get()
            category = category_var.get()

            if not self.valid_date(date):
                messagebox.showerror("Error", "Invalid date")
                return

            try:
                amount = float(amount)
            except:
                messagebox.showerror("Error", "Amount must be number")
                return

            if category not in self.categories:
                messagebox.showerror("Error", "Invalid category")
                return

            self.expense_entries.append({
                "date": date,
                "amount": amount,
                "category": category
            })

            messagebox.showinfo("Success", "Expense added")
            window.destroy()

        tk.Button(window, text="Submit", command=submit).pack()


    # VIEW TOTALS 
    def open_totals(self):
        window = tk.Toplevel(self.root)
        window.title("View Totals")

        tk.Label(window, text="Start Date").pack()
        start_entry = tk.Entry(window)
        start_entry.pack()

        tk.Label(window, text="End Date").pack()
        end_entry = tk.Entry(window)
        end_entry.pack()

        result_label = tk.Label(window, text="")
        result_label.pack()

        def calculate():
            start = start_entry.get()
            end = end_entry.get()

            if not self.valid_date(start) or not self.valid_date(end):
                messagebox.showerror("Error", "Invalid date")
                return

            start_d = datetime.strptime(start, "%Y-%m-%d")
            end_d = datetime.strptime(end, "%Y-%m-%d")

            total_income = 0
            total_expense = 0

            for i in self.income_entries:
                d = datetime.strptime(i["date"], "%Y-%m-%d")
                if start_d <= d <= end_d:
                    total_income += i["amount"]

            for e in self.expense_entries:
                d = datetime.strptime(e["date"], "%Y-%m-%d")
                if start_d <= d <= end_d:
                    total_expense += e["amount"]

            balance = total_income - total_expense

            result_label.config(
                text=f"Income: {total_income} | Expenses: {total_expense} | Balance: {balance}"
            )

        tk.Button(window, text="Calculate", command=calculate).pack()


    #  SAVE 
    def save_data(self):
        with open("john123_income.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["date", "amount", "source"])
            writer.writeheader()
            writer.writerows(self.income_entries)

        with open("john123_expense.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["date", "amount", "category"])
            writer.writeheader()
            writer.writerows(self.expense_entries)


    # EXIT 
    def exit_app(self):
        self.save_data()
        self.root.destroy()


# MENU FUNCTION 
def menu():
    root = tk.Tk()
    app = TrackerApp(root)
    root.mainloop()


# RUN 
menu()