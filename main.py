# MH 1st Main file

# imports
from currency_conversion import *
from Data_management import *
from budgeting import *
from data_visualisation import *
from income import *
from sign_in import *
import tkinter as tk
import sys

# main function:
def main():
    root = tk.Tk()
    def log_out():
        logged_in.pack_forget()
    def convert_currency():
        if is_connected() == True:
            convert_currency_online()
            update_currency_online()
        else:
            convert_currency_offline()
            update_currency_offline
    def logged_in_options():
        message, user = log_in()
        # provide user with more options: add expense, add income, view total income or expenses in a specified time, set budget limits, compare budget to expenses, set savings goal, track progress towards savings goal, view budget as pie chart, view income/expenses as graph, log out
        instruction = tk.Label(logged_in, text = "Welcome user. Choose an option below.")
            # EXPENSES:
                # run the income/expenses menu function
        income_expenses = tk.Button(logged_in, text = "Manage Income/Expenses", command = menu())
            # SET LIMITS:
        limits = tk.Button(logged_in, text = "Set Budget Limits", command = set_limits(user["savings_csv"]))
                # run the set budget limits function
            # COMPARE BUDGET/EXPENSES:
        compare = tk.Button(logged_in, text = "Compare Budget to Expenses", command = compare_expenses(user["expenses_csv"], user["savings_csv"]))
                # run the compare budget and expenses function
            # SET SAVINGS GOAL:
        set_goal = tk.Button(logged_in, text = "Set Savings Goal", command = new_goal())
                # run the set savings goal function
            # TRACK PROGRESS TO GOAL:
        track_goal = tk.Button(logged_in, text = "Track Progress to Goal", command = saving_progress())
                # run the track progress to savings goal function
            # VIEW PIE CHART:
        pie_chart = tk.Button(logged_in, text = "View Pie Chart", command = visualization_menu(user))
                # run the make pie chart function  
            # LOG OUT:
        log_out = tk.Button(logged_in, text = "Log Out", command = log_out())
                # set account status to inactive
                # take the user back to the first selection of choices
    def remove_welcome(welcome, confirm_btn, login, create_an_account, quit_program):
        welcome.pack_forget()
        confirm_btn.pack_forget()
        login.pack()
        create_an_account.pack()
        quit_program.pack()

    def exit_program():
        sys.exit(0)
    # print a welcome and instructions for the user
    welcome = Label(root, text = "Welcome user, to our personal finance program! In this program you have a wide variety of options of things to do! To budget, press the 'budgeting' button, to visualize your data, press the 'visualization' button, to do anything, press a button! Now go, and let your inner finance bro run wild!")
    welcome.pack()
    confirm_btn = tk.Button(root, text = "OK", command = remove_welcome(welcome, confirm_btn, login, create_an_account, quit_program))
    confirm_btn.pack()
    # ask if the user wants to log in, create an account, or quit
    sign_in = Label(root, text = "Do you want to log in, create an account, or quit?")
    # LOG IN:
    login = tk.Button(root, text = "Log In", command = logged_in_options())
    logged_in = tk.Tk()
        # run the log in function
    # CREATE ACCOUNT:
    create_an_account = tk.Button(root, text = "Create Account", command = create_account)
        # run the create account function
        # take the user back to the first selection of choices
    # QUIT:
    quit_program  = tk.Button(root, text = "Quit", command = exit_program)
        # exit the loop
    root.mainloop()


main()
