# import libraries needed
import random as rand
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# creates the function that approximates pi given the number of points
def pi_approximation(num_points):
    rand.seed(0)
    points = 0
    for i in range(num_points):
        x = rand.uniform(-1, 1)
        y = rand.uniform(-1, 1)
        if x**2 + y**2 < 1: points = points + 1
    return points*4/num_points

# use tkinter to make interactive gui for pi approximation
window = tk.Tk()
window.title("Pi Approximation Simulation using Monte Carlo Method")
window.geometry("800x600")
window.configure(bg="lightblue")
label = tk.Label(window, text="Enter number of points to approximate pi:", bg="lightblue")

# buttons for user to control the simulation
start = tk.Button(
    text="Start",
    width=3,
    height=1,
    bg="blue",
    fg="black",
    
)
reset = tk.Button(
    text="Reset",
    width=3,
    height=1,
    bg="blue",
    fg="black",
)

# user enters how many iterations they want to run
entry = tk.Entry(window, width=10)

label.pack()
start.pack()
reset.pack()
entry.pack()

# create matplotlib figure to show inside tkinter
fig, ax = plt.subplots(figsize=(4,4))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(pady=10)

# function to start the simulation
def start_simulation():

def reset_simulation():
    window.title("Pi Approximation Simulation using Monte Carlo Method")
    window.update()  # makes the title text change immediately
    ax.clear()
    canvas.draw()

# link buttons to functions
start.config(command=start_simulation)
reset.config(command=reset_simulation)

window.mainloop()