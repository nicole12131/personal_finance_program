import tkinter as tk
from tkinter import messagebox

# store data in memory
goal_data = {}


def new_goal():
    date = date_entry.get()

    if date == "":
        messagebox.showerror("Error", "Enter date")
        return

    try:
        goal = float(goal_entry.get())
    except:
        messagebox.showerror("Error", "Enter valid goal")
        return

    answer = goal_type.get()

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

    # save in dictionary
    goal_data[date] = [goal, saved]

    messagebox.showinfo("Success", "Goal created!")


def saving_progress():
    date = date_entry.get()

    if date not in goal_data:
        messagebox.showerror("Error", "Goal not found")
        return

    try:
        add = float(add_entry.get())
    except:
        messagebox.showerror("Error", "Enter valid amount")
        return

    goal, saved = goal_data[date]

    saved += add
    goal_data[date][1] = saved

    percent = (saved / goal) * 100

    if percent >= 75:
        msg = "Good job, almost there!"
    elif percent >= 40:
        msg = "You're doing okay, keep going."
    else:
        msg = "You should try to save more."

    messagebox.showinfo(
        "Progress",
        f"Goal: {goal}\nSaved: {saved}\nProgress: {round(percent,2)}%\n{msg}"
    )


def app():
    global date_entry, goal_entry, saved_entry, add_entry, goal_type

    window = tk.Tk()
    window.title("Saving Goal Tracker")
    window.geometry("350x400")

    # Date
    tk.Label(window, text="Date").pack()
    date_entry = tk.Entry(window)
    date_entry.pack()

    # Goal
    tk.Label(window, text="Goal Amount").pack()
    goal_entry = tk.Entry(window)
    goal_entry.pack()

    # Savings option
    goal_type = tk.StringVar()

    tk.Label(window, text="Do you already have savings?").pack()
    tk.Radiobutton(window, text="Yes", variable=goal_type, value="yes").pack()
    tk.Radiobutton(window, text="No", variable=goal_type, value="no").pack()

    # Saved
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


# run app
app()
