# MH 1st Budgeting Functions
import tkinter as tk

# Set limits function:
def set_limits(relative_path):
    def check_number(value):
        return value == "" or isinstance
    root = tk.Tk()
    root.title("Set Budget Limits")
    root.minsize(250, 250)
    root.maxsize(2000, 2000)
    budget_limts = []
    budget_categories = ["food","rent","utilities","transportation","entertainment"]
    for category in budget_categories:
        # For every budget category ask how much the user is willing to spend
    # updates each value in the list pulled from the csv
    # returns the updated list

# Compare expenses function:
    # takes from the list how much the user has spent in each category
    # subtracts what they've spent in each category from what the limit is in each category
    # prints out how much they have left to spend for each category