# import csv
import csv
# Load data from the saving goal CSV file

# create function for new saving goal
def new_goal():
# Ask user if they already have a saving goal
    goal = input("Do you have a saving goal?: ")
    # if user say no
    if goal == "no":
        # ask for a new saving goal
        new = input("Type a new saving goal: ")
    # if user say yes
    if goal == "yes":
        # Input current savings
        print("current savings")
    # else
    else:
        # print invalid choice 
        print("invalid choice try again")
        new_goal()

# create function for saving progress
#def saving_progress():
# calcualte progress towards the goal

# if user is doing a good progress 
    # print that they are doing a good progress

# if user is doing a bad progress
    # print options to improve savings to complete the goal

# Save data to the saving goal CSV file
# display final progress 

# create function to save progress between sessions 
#def save_progress():
# if user if loged in print their current savings
# if user want to log out save their progress to the saving goal CSV file

# if a new profile is created add it to the csv file
    # if user make progress add it to csv file
new_goal()