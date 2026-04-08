# CB 1st Data Visualisation

# import numpy, maybe pandas
import matplotlib.pyplot as plt
import customtkinter as ctk
from budgeting import *


# define function make pie charts (come up with a better name)
    # this graph is going to be used for displaying total amount of budget spent, how much each catergory takes up in the budget how much each atergory takes up in expenses, and a few other things
    # take in what mode the function is being run in depending on what it is being used for
    # take in values, do some math if necessary
    # return pie chart using pandas



# define function make_graph():
    # this graph is going to be for tracking expenses/income over time
    # take info from user CSV, and order based off of input date
    # plug those numbers into pandas to generate a pretty-ish chart, return and print on screen

class Graph:
    def __init__(self, pieces, labels,title):
        self.pieces = pieces
        self.labels = labels
        self.title = title

    def make_pie_chart(self,title):
        plt.pie(self.pieces,labels = self.labels)

        plt.title(self.title)
        plt.show()



def visualization_menu(user):
    app = ctk.CTk()
    app.title("Visualization Menu")
    app.geometry("300x300")

    def spent_command():
        food, rent, utilties, transportation, entertainment = get_amounts("CSV/john123_expense.csv")
        expenses = [food,rent,utilties,transportation,entertainment]
        labels = ["Food","Rent","Utilties","Transportation","Entertainment"]

        pie = Graph(expenses,labels,"Expenses by Category")
        pie.make_pie_chart()



    def budget_command():
        limits = get_budget("CSV/john123_budgets.csv")
        labels = "Food","Rent","Utitlies","Transportation","Entertainment"

        pie = Graph(limits,labels,"Budget Categories")
        pie.make_pie_chart()
        

    budget_button = ctk.CTkButton(app,text="Create Pie Chart for Budget Categories",command=budget_command,fg_color = "blue")

    
    spent_button = ctk.CTkButton(app,text="Create Pie Chart for Expenses By Category",command=spent_command,fg_color = "blue")
    
    
    graph_button.pack()
    pie_button.pack()


    app.mainloop()


