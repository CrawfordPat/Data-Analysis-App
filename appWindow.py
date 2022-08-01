# Create a window with a button and a text field. When the button is clicked, the text field should display the mean of the numbers in the text field.
import tkinter as tk

from numpy import array
from basicStats import *

# Make a function that takes an imput of what function it should run and the input for that function
def calculate_stat(stat_function, input_field):
    stats = [int(x) for x in input_field.get().split(",")]
    label = tk.Label(root, text=stat_function(stats))
    label.pack()

# Create a window
root = tk.Tk()
root.title("EZ Stat")
root.geometry("400x300")

# Create a text field
text_field = tk.Entry(root)
text_field.pack()

# Create a button that stores the text field's value in an array as integers and then displays the mean of the array.
# Make dropdown menu
dropdown = tk.OptionMenu(root, text_field, "count", "mean", "median", "mode", "range", "sum", "standard_deviation_population", "standard_deviation_sample", "variance_population", "variance_sample", "z_score", "quartiles", "iqr")
dropdown.pack()

# Create a button that runs the function that is selected in the dropdown menu
button = tk.Button(root, text="Calculate", command=lambda: calculate_stat(dropdown.get(), text_field))
button.pack()

root.mainloop()