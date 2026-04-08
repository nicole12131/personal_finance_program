# import csv
import csv
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

# create function for new saving goal
# Ask user if they already have a saving goal
    # if user say no
        # ask for a new saving goal
    # if user say yes
        # Input current savings
    # else
        # print invalid choice 
def new_goal():
    username = input("Enter your name: ")

    answer = input("Do you already have a goal? (yes/no): ")

    if answer == "no":
        goal = float(input("Enter your goal amount: "))
        saved = 0

    elif answer == "yes":
        goal = float(input("Enter your goal amount: "))
        saved = float(input("Enter how much you already saved: "))

    else:
        print("Invalid input")
        return

    file = open("CSV\\user_details.csv", "a", newline="")
    writer = csv.writer(file)
    writer.writerow([username, goal, saved])
    file.close()

    print("Your goal was saved!")

# create function for saving progress
# calcualte progress towards the goal

# if user is doing a good progress 
    # print that they are doing a good progress

# if user is doing a bad progress
    # print options to improve savings to complete the goal
def saving_progress():
    name = input("Enter your username: ")
    found = False
    new_rows = []

    file = open("CSV\\user_details.csv", "r")
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        if row[0] == name:
            found = True

            goal = float(row[1])
            saved = float(row[2])

            print("Goal:", goal)
            print("Saved:", saved)

            add = float(input("How much do you want to add? "))
            saved = saved + add

            percent = (saved / goal) * 100
            print("Progress:", round(percent, 2), "%")

            if percent >= 75:
                print("Good job, almost there!")
            elif percent >= 40:
                print("You're doing okay, keep going.")
            else:
                print("You should try to save more.")

            row[2] = saved

        new_rows.append(row)

    file.close()
# if a new profile is created add it to the csv file
    # if user make progress add it to csv file
    if found == False:
        print("User not found")
        return

    file = open("CSV\\user_details.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["name", "goal", "saved"])
    writer.writerows(new_rows)
    file.close()

# create function to save progress between sessions 
# if user if loged in print their current savings
# if user want to log out save their progress to the saving goal CSV file
# Save data to the saving goal CSV file
# display final progress 
def progress_sessions():
    while True:
        print("1. New Goal")
        print("2. Add Savings")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            new_goal()

        elif choice == "2":
            saving_progress()

        elif choice == "3":
            print("Bye")
            break

        else:
            print("Not a valid option")

progress_sessions()