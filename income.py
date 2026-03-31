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

