# import csv
import csv
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

user = []
# Load data from the saving goal CSV file
try:
    file = open("CSV\\user_details.csv", "x", newline="")
    writer = csv.writer(file)
    writer.writerow(["username", "goal", "saved"])
    file.close()
    for row in writer:
        user.append({
            "username": row["username"].strip()})
except:
    pass  

class AddSavings:
    def __init__(self, root):
        self.root = root
        self.root.title("Income & Expense Tracker")
        self.root.geometry("300x300")

        self.income_entries = []
        self.expense_entries = []
        self.categories = ["food", "rent", "utilities", "transportation", "entertainment"]

        self.build_menu()
# create function for new saving goal
# Ask user if they already have a saving goal
    # if user say no
        # ask for a new saving goal
    # if user say yes
        # Input current savings
    # else
        # print invalid choice 
    def new_goal(self):
        window = tk.Toplevel(self.root)
        window.title("new goal")

        tk.Label(window, text="Date (YYYY-MM-DD)").pack()
        date_entry = tk.Entry(window)
        date_entry.pack()

        tk.Label(window, text="Amount").pack()
        amount_entry = tk.Entry(window)
        amount_entry.pack()

        def submit():
            date = date_entry.get()
            amount = amount_entry.get()
       
            if not self.valid_date(date):
                messagebox.showerror("Error", "Invalid date")
                return
            try:
                    amount = float(amount)
            except:
                messagebox.showerror("Error", "Amount must be number")
                return

            self.income_entries.append({
                "date": date,
                "amount": amount,
                })

            messagebox.showinfo("Success", "goal added")
            window.destroy()

        tk.Button(window, text="Submit", command=submit).pack()

        

    # create function for saving progress
    # calcualte progress towards the goal

    # if user is doing a good progress 
        # print that they are doing a good progress

    # if user is doing a bad progress
        # print options to improve savings to complete the goal
    def add_savings(self):
        window = tk.Toplevel(self.root)
        window.title("")

        tk.Label(window, text="Date (YYYY-MM-DD)").pack()
        date_entry = tk.Entry(window)
        date_entry.pack()

        tk.Label(window, text="Amount").pack()
        amount_entry = tk.Entry(window)
        amount_entry.pack()

        def submit():
            date = date_entry.get()
            amount = amount_entry.get()
        
            if not self.valid_date(date):
                messagebox.showerror("Error", "Invalid date")
                return
            try:
                    amount = float(amount)
            except:
                messagebox.showerror("Error", "Amount must be number")
                return

            self.income_entries.append({
                "date": date,
                "amount": amount,
                })

            messagebox.showinfo("Success", "goal added")
            window.destroy()

        tk.Button(window, text="Submit", command=submit).pack()

    # create function to save progress between sessions 
    # if user if loged in print their current savings
    # if user want to log out save their progress to the saving goal CSV file
    # Save data to the saving goal CSV file
    # display final progress 
    #def progress_sessions(self):
        #while True:
            #print("1. New Goal")
            #print("2. add savings")
            #print("3. Exit")

            #choice = input("Choose: ")

            #if choice == "1":
                #new_goal()

            #elif choice == "2":
                #add_savings()

            #elif choice == "3":
                #print("Bye")
                #break

            #else:
                #print("Not a valid option")

    def build_menu(self):
        tk.Label(self.root, text="Main Menu", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="1. New goal", command=self.new_goal).pack(pady=5)
        tk.Button(self.root, text="2. Add Savings", command=self.saving_progress).pack(pady=5)
        tk.Button(self.root, text="3. Exit", command=self.exit).pack(pady=5)

    def exit(self):
        self.add_savings()
        self.root.new_goal()

def menu():
    root = tk.Tk()
    app = AddSavings(root)
    root.mainloop()

menu()