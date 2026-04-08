# CB 1st Saving & Loading Files

import csv

# define function load_details():
    # go through details file, load each row into into a list, return that list

# define function load_user(file_paths):
    # define function load_expenses(expense_path):
        # create an expenses list, use with open to open the file, go through file and load into a list, then return list

    # define function load_incomes(income_path):
        # create an incomes list, use with open to open the file, go through file and load into a list, then return list

    # define function load_savings(savings_path):
        # create an savings list, use with open to open the file, go through file and load into a list, then return list

# define function save_user(file_paths,data lists):
    # define funcion save_expenses(expense_path,expenses):
        # first, go through and sort list by date (most recent is first)
        # then, go through and write each dict in list to file (if we save them as objects, make sure they are turned into dicts)

    # define function save_incomes(income_path,expenses):
        # first, go through and sort list by date (most recent is first)
        # then, go through and write each dict in list to file (if we save them as objects, make sure they are turned into dicts)

    # function save_savings(income_path,savings):
        # save each item in savings dict

# define function create_user():

    # define function make_paths():
        # set all of the files so they are in the documents folder
        # have the names be "document\\username_filetype.csv" or something like that
        # return filepaths

    # define function write_details(username, password, filepaths):
        # write hashed password, username, filepaths, and set currency to USD

    # define function init_expenses(expense_path):
        # create file with expense fieldnames, use expense_path

    # define function init_incomes(income_path):
        # create file with income fieldnames, use income_path

    # define function load_savings(savings_path):
        # create file with savings fieldnames, use savings_path

def load_details():
    details = []
    with open("details.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            details.append(row)

        return details
    
def load_user(file_paths):
    expenses = []
    with open(file_paths["expenses"], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)

    incomes = []
    with open(file_paths["incomes"], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            incomes.append(row)

    savings = []
    with open(file_paths["savings"], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            savings.append(row)

    return expenses, incomes, savings

def save_user(file_paths, expenses, incomes, savings):
    with open(file_paths["expenses"], "w", newline="") as file:
        fieldnames = ["date", "amount", "category","location"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

    with open(file_paths["incomes"], "w", newline="") as file:
        fieldnames = ["date", "amount", "source"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for income in incomes:
            writer.writerow(income)

    with open(file_paths["savings"], "w", newline="") as file:
        fieldnames = ["goal",'budget',"amount_saved","amount_spent"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for saving in savings:
            writer.writerow(saving)

def create_user(username, password):
    def make_paths(username):
        file_paths = {
            "expenses": f"documents\\{username}_expenses.csv",
            "incomes": f"documents\\{username}_incomes.csv",
            "savings": f"documents\\{username}_savings.csv"
        }
        return file_paths

    def write_details(username, password, file_paths):
        with open("details.csv", "a", newline="") as file:
            fieldnames = ["username", "password", "file_paths", "currency"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({
                "username": username,
                "password": password,
                "file_paths": file_paths,
                "currency": "USD"
            })

    def init_expenses(expense_path):
        with open(expense_path, "w", newline="") as file:
            fieldnames = ["date", "amount", "category","location"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

        expenses = []
        return expenses

    def init_incomes(income_path):
        with open(income_path, "w", newline="") as file:
            fieldnames = ["date", "amount", "source"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
        
        incomes = []
        return incomes

    def init_savings(savings_path):
        with open(savings_path, "w", newline="") as file:
            fieldnames = ["goal",'budget',"amount_saved","amount_spent"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

        savings = []
        return savings
    
    file_paths = make_paths(username)
    write_details(username, password, file_paths)
    expenses = init_expenses(file_paths["expenses"])
    incomes = init_incomes(file_paths["incomes"])
    savings = init_savings(file_paths["savings"])
    return expenses, incomes, savings