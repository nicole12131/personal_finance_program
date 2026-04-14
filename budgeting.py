# MH 1st Budgeting Functions
import tkinter as tk
import csv
import sys

# Set limits function:
def set_limits():
    def validate():
        message = False
        final_entry = []
        # checks user entries to make sure they're numbers
        for i in range(5):
            current = entry[i].get()
            print(current)
            try:
                current = float(current)
                final_entry.append(current)
            except:
                message = True
                break
        if message == True:
            label = tk.Label(root, text = "One of your entries is not a number! Please make sure you only enter numbers.")
            label.config(fg = "red")
            label.pack()
        else:
            submit(final_entry)
                
    
    def submit(result):
        result = {"food" : result[0], "rent" : result[1], "utilities" : result[2], "transportation" : result[3], "entertainment" : result[4]}
        # if all the users inputs are valid save them to their budget csv
        fieldnames = ["food", "rent", "utilities", "transportation", "entertainment"]
        with open("personal_finance_program\\CSV\\john123_budgets.csv", "w", newline = "") as budget_csv:
            writer = csv.DictWriter(budget_csv, fieldnames = fieldnames)
            writer.writeheader()
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
    sub_btn = tk.Button(root, text = "Submit", command = validate)
    close_btn = tk.Button(root, text = "Quit", command = sys.exit)
    sub_btn.pack()
    close_btn.pack()
    # updates each value in the list pulled from the csv
    root.mainloop()
    # returns the updated list

# Compare expenses function:
def compare_expenses():
    def get_expense_data():
        with open("CSV\\john123_expense.csv", "r") as expenses_csv:
            # loops over csv and converts lines into dictionaries
            content = csv.reader(expenses_csv)
            row_count = sum(1 for row in content)
            expenses_csv.seek(0)
            if row_count == 0:
                headers = ["date", "location", "amount", "category"]
            elif row_count == "1":
                label = tk.Label(root, text = "You have no logged expenses yet.")
                quit_btn = tk.Button(root, text = "Quit", command = sys.exit)
                label.pack()
                quit_btn.pack()
                food_label.pack_forget()
                rent_label.pack_forget()
                utilities_label.pack_forget()
                transportation_label.pack_forget()
                entertainment_label.pack_forget()
            else:
                headers = next(content)
            rows = []
            for line in content:
                rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2]})
            return rows
    def get_amounts():
        food = 0
        rent = 0
        utilities = 0
        transportation = 0
        entertainment = 0
        # get expenses data from the users expense csv
        expense_csv = get_expense_data()
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
    def get_budget():
        with open("CSV\\john123_budgets.csv", "r") as budget_csv:
            content = csv.reader(budget_csv)
            row_count = sum(1 for row in content)
            budget_csv.seek(0)
            if row_count == 0:
                headers = ["food", "rent", "utilities", "transportation", "entertainment"]
            elif row_count == 1:
                label = tk.Label(root, text = "You have no logged budget limits yet.")
                label.config(fg = "red")
                label.pack()
                return [{"food" : 0, "rent" : 0, "utilities" : 0, "transportation" : 0, "entertainment" : 0}]
            else:
                headers = next(content)
            rows = []
            for line in content:
                rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3], headers[4] : line[4]})
            return rows
    count = 0
    # get how much they spent in each category
    food, rent, utilities, transportation, entertainment = get_amounts()
    expenses = [food, rent, utilities, transportation, entertainment]
    categories = ["food", "rent", "utilities", "transportation", "entertainment"]
    root = tk.Tk()
    budget_limits = get_budget()
    difference = []
    # subtracts what they've spent in each category from what the limit is in each category
    for category in categories:
        difference.append(float(budget_limits[0][category]) - expenses[count])
        count += 1
    # displays how much they have left to spend for each category
    root.title("Compare Budget")
    root.minsize(250, 200)
    root.maxsize(800, 800)
    guide_label = tk.Label(root, text = "Limit   :   Spent   :   Amount left to spend")
    guide_label.config(fg = "blue")
    food_label = tk.Label(root, text = f"Limit: {budget_limits[0]["food"]}, Spent: {expenses[0]}, Remaining: {difference[0]}")
    rent_label = tk.Label(root, text = f"Limit: {budget_limits[0]["rent"]}, Spent: {expenses[1]}, Remaining: {difference[1]}")
    utilities_label = tk.Label(root, text = f"Limit: {budget_limits[0]["utilities"]}, Spent: {expenses[2]}, Remaining: {difference[2]}")
    transportation_label = tk.Label(root, text = f"Limit: {budget_limits[0]["transportation"]}, Spent: {expenses[3]}, Remaining: {difference[3]}")
    entertainment_label = tk.Label(root, text = f"Limit: {budget_limits[0]["entertainment"]}, Spent: {expenses[4]}, Remaining: {difference[4]}")
    quit_btn = tk.Button(root, text = "Quit", command = sys.exit)
    guide_label.pack()
    food_label.pack()
    rent_label.pack()
    utilities_label.pack()
    transportation_label.pack()
    entertainment_label.pack()
    quit_btn.pack()
    root.mainloop()

if __name__ == "__main__":
    compare_expenses()
