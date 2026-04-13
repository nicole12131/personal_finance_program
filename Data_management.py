# import csv
import csv
import tkinter as tk

FILE_PATH = "personal_finance_program\\CSV\\user_details.csv"


# create function for new saving goal
# Ask user if they already have a saving goal
    # if user say no
        # ask for a new saving goal
    # if user say yes
        # Input current savings
    # else
        # print invalid choice 
def new_goal():
    name = input("Enter your name: ")

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
    writer.writerow([name, goal, saved])
    file.close()

    print("Your goal was saved!")

# create function for saving progress
# calcualte progress towards the goal

# if user is doing a good progress 
    # print that they are doing a good progress

# if user is doing a bad progress
    # print options to improve savings to complete the goal
def saving_progress():
    name = input("Enter your name: ")
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

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Saving Goal Tracker")
    window.geometry("350x400")

    # Name
    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    # Goal
    tk.Label(window, text="Goal Amount").pack()
    goal_entry = tk.Entry(window)
    goal_entry.pack()

    # Already have savings?
    goal_type = tk.StringVar()

    tk.Label(window, text="Do you already have savings?").pack()
    tk.Radiobutton(window, text="Yes", variable=goal_type, value="yes").pack()
    tk.Radiobutton(window, text="No", variable=goal_type, value="no").pack()

    # Saved amount
    tk.Label(window, text="Saved Amount (if yes)").pack()
    saved_entry = tk.Entry(window)
    saved_entry.pack()

    # Add savings
    tk.Label(window, text="Add Savings").pack()
    add_entry = tk.Entry(window)
    add_entry.pack()

    # Buttons
    tk.Button(window, text="Create Goal", command=new_goal).pack(pady=10)
    tk.Button(window, text="Add Savings", command=saving_progress).pack(pady=10)

    tk.Button(window, text="Exit", command=window.quit).pack(pady=10)

    window.mainloop()
