import csv
import tkinter as tk
from tkinter import messagebox

FILE_PATH = "personal_finance_program\\CSV\\user_details.csv"


def new_goal():
    name = name_entry.get()
    answer = goal_type.get()

    if name == "":
        messagebox.showerror("Error", "Enter your name")
        return

    try:
        goal = float(goal_entry.get())
    except:
        messagebox.showerror("Error", "Enter a valid goal")
        return

    if answer == "no":
        saved = 0

    elif answer == "yes":
        try:
            saved = float(saved_entry.get())
        except:
            messagebox.showerror("Error", "Enter valid savings")
            return
    else:
        messagebox.showerror("Error", "Select yes or no")
        return

    file = open(FILE_PATH, "a", newline="")
    writer = csv.writer(file)
    writer.writerow([name, goal, saved])
    file.close()

    messagebox.showinfo("Success", "Goal saved!")


def saving_progress():
    name = name_entry.get()
    found = False
    new_rows = []

    file = open(FILE_PATH, "r")
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        if row[0] == name:
            found = True

            goal = float(row[1])
            saved = float(row[2])

            try:
                add = float(add_entry.get())
            except:
                messagebox.showerror("Error", "Enter valid amount")
                return

            saved += add
            percent = (saved / goal) * 100

            if percent >= 75:
                msg = "Good job, almost there!"
            elif percent >= 40:
                msg = "You're doing okay, keep going."
            else:
                msg = "You should try to save more."

            messagebox.showinfo("Progress",
                                f"Goal: {goal}\nSaved: {saved}\nProgress: {round(percent,2)}%\n{msg}")

            row[2] = saved

        new_rows.append(row)

    file.close()

    if not found:
        messagebox.showerror("Error", "User not found")
        return

    file = open(FILE_PATH, "w", newline="")
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
