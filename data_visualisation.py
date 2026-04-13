# CB 1st Data Visualisation

# import numpy, maybe pandas
import matplotlib.pyplot as plt
import customtkinter as ctk
import csv


# define function make pie charts (come up with a better name)
    # this graph is going to be used for displaying total amount of budget spent, how much each catergory takes up in the budget how much each atergory takes up in expenses, and a few other things
    # take in what mode the function is being run in depending on what it is being used for
    # take in values, do some math if necessary
    # return pie chart using pandas



# define function make_graph():
    # this graph is going to be for tracking expenses/income over time
    # take info from user CSV, and order based off of input date
    # plug those numbers into pandas to generate a pretty-ish chart, return and print on screen

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
            rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2]})
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
        # loops over csv and converts lines into dictionariess
        fieldnames = ['food','rent','utilties','transportation','entertainment']
        content = csv.DictReader(budget_csv,fieldnames)
        next(content)
        for i in content:
            return i
class Graph:
    def __init__(self, pieces, labels,title):
        self.pieces = pieces
        self.labels = labels
        self.title = title

    def make_pie_chart(self):
        plt.pie(self.pieces,labels = self.labels)

        plt.title(self.title)
        plt.show()



def visualization_menu():
    app = ctk.CTk()
    app.title("Visualization Menu")
    app.geometry("1200x500")

    def spent_command():
        food, rent, utilties, transportation, entertainment = get_amounts("personal_finance_program\\CSV\\john123_expense.csv")
        expenses = [food,rent,utilties,transportation,entertainment]
        labels = ["Food","Rent","Utilties","Transportation","Entertainment"]

        pie = Graph(expenses,labels,"Expenses by Category")
        pie.make_pie_chart()



    def budget_command():
        limits = get_budget("personal_finance_program\\CSV\\john123_budgets.csv")
        
        labels = ["Food","Rent","Utitlies","Transportation","Entertainment"]

        

        pie = Graph(limits.values(),labels,title="Budget Categories")
        pie.make_pie_chart()
        
    explanation = ctk.CTkLabel(app,text="Welcome to the visualization menu. Click the button below to create a pie chart for your budget categories, or click the other button to create a pie chart for your expenses by category.")
    budget_button = ctk.CTkButton(app,text="Create Pie Chart for Budget Categories",command=budget_command,fg_color = "blue")

    
    spent_button = ctk.CTkButton(app,text="Create Pie Chart for Expenses By Category",command=spent_command,fg_color = "blue")
    
    explanation.pack()
    budget_button.pack()
    spent_button.pack()
    


    app.mainloop()