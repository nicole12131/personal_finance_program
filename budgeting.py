# MH 1st Budgeting Functions
import tkinter as tk
import csv

# Set limits function:
def set_limits(relative_path):
    def validate():
        final_entry = []
        # checks user entries to make sure they're numbers
        for i in range(5):
            current = entry[i].get()
            try:
                current = float(current)
                final_entry.append(current)
            except:
                return "invalid"
        return final_entry
    
    def submit(relative_path):
        result = validate()
        if result == "invalid":
            # if the users inputs are invalid print out an error message
            label = tk.Label(root, text = "One of your entries is not a number! Please make sure you only enter numbers.")
            label.config(fg = "red")
            label.pack()
        else:
            # if all the users inputs are valid save them to their budget csv
            fieldnames = ["food", "rent", "utilities", "transportation", "entertainment"]
            with open(relative_path, "w") as budget_csv:
                writer = csv.DictWriter(budget_csv, fieldnames = fieldnames)
                writer.writeheader
                writer.writerow(result)
            label = tk.Label(root, text = "Your budget has been saved!")
            label.config(fg = "green")
            label.pack()

    # set up screen      
    count = 0
    entry = [None, None, None, None, None]
    root = tk.Tk()
    root.title("Set Budget Limits")
    root.minsize(250, 250)
    root.maxsize(2000, 2000)
    budget_categories = ["food","rent","utilities","transportation","entertainment"]
    for category in budget_categories:
        entry_label = tk.Label(root, text = f"What are you willing to spend on {category}?")
        # For every budget category ask how much the user is willing to spend
        entry[count] = tk.Entry(root, textvariable = "")
        entry_label.pack()
        entry[count].pack()
        count += 1
    sub_btn = tk.Button(root, text = "Submit", command = submit(relative_path))
    sub_btn.pack()
    # updates each value in the list pulled from the csv
    root.mainloop()
    # returns the updated list

# Compare expenses function:
def compare_expenses(expenses_path, budget_path):
    def get_expense_data(expenses_path):
        with open(expenses_path, "r") as expenses_csv:
            # loops over csv and converts lines into dictionaries
            content = csv.reader(expenses_csv)
            row_count = sum(1 for row in content)
            expenses_csv.seek(0)
            if row_count == 0:
                headers = ["date", "location", "amount", "category"]
            else:
                headers = next(content)
            rows = []
            for line in content:
                rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3]})
            return rows
    def get_amounts(expenses_path):
        food = 0
        rent = 0
        utilities = 0
        transportation = 0
        entertainment = 0
        # get expenses data from the users expense csv
        expense_csv = get_expense_data(expenses_path)
        # check expense category and add it to the corresponding total
        for expense in expense_csv:
            if expense["category"] == "food":
                food += float(expense["amount"])
            elif expense["category"] == "rent":
                rent += float(expense["amount"])
            elif expense["category"] == "utilities":
                utilities += float(expense["amount"])
            elif expense["category"] == "transportation":
                transportation += float(expense["amount"])
            elif expense["category"] == "entertainment":
                entertainment += float(expense["amount"])
        return food, rent, utilities, transportation, entertainment
    def get_budget(budget_path):
        with open(budget_path, "r") as budget_csv:
            # loops over csv and converts lines into dictionaries
            content = csv.reader(budget_csv)
            limits = []
            next(content)
            for line in content:
                limits.append(line[0], line[1], line[2], line[3], line[4])
            return limits
    count = 0
    # get how much they spent in each category
    food, rent, utilities, transportation, entertainment = get_amounts(expenses_path)
    expenses = [food, rent, utilities, transportation, entertainment]
    budget_limits = get_budget(budget_path)
    difference = []
    # subtracts what they've spent in each category from what the limit is in each category
    for limit in budget_limits:
        difference.append(limit - expenses[count])
        count += 1
    # displays how much they have left to spend for each category
    root = tk.Tk()
    root.title("Set Budget Limits")
    root.minsize(500, 500)
    root.maxsize(2000, 2000)
    food_label = tk.Label(root, text = f"Limit: {budget_limits[0]}, Spent: {expenses[0]}, Remaining: {difference[0]}")
    rent_label = tk.Label(root, text = f"Limit: {budget_limits[1]}, Spent: {expenses[1]}, Remaining: {difference[1]}")
    utilities_label = tk.Label(root, text = f"Limit: {budget_limits[2]}, Spent: {expenses[2]}, Remaining: {difference[2]}")
    transportation_label = tk.Label(root, text = f"Limit: {budget_limits[3]}, Spent: {expenses[3]}, Remaining: {difference[3]}")
    entertainment_label = tk.Label(root, text = f"Limit: {budget_limits[4]}, Spent: {expenses[4]}, Remaining: {difference[4]}")
    food_label.pack()
    rent_label.pack()
    utilities_label.pack()
    transportation_label.pack()
    entertainment_label.pack()