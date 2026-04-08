# CB 1st Data Visualisation

# import numpy, maybe pandas
import matplotlib.pyplot as plt

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
    def __init__(self, data):
        self.data = data

    def make_pie_chart(self, mode):
        # code to generate pie chart based on mode and self.data
        pass

    def make_line_graph(self):
        dates = []
        amounts = []
        for i in self.data:
            dates.append(i.date)
            amounts.append(i.amount)
        
        plt.plot(dates, amounts)

        plt.title("Expenses Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount")

        plt.show()


# Data points
x = [1, 2, 3, 4, 5]
y = [10, 24, 36, 40, 52]

# Plotting the data
plt.plot(x, y)

# Adding labels and title
plt.title("Sample Line Graph")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")

# Displaying the plot
plt.show()