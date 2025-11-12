# import libraries needed
import random as rand
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

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
stop = tk.Button(
    text="Stop",
    width=3,
    height=1,
    bg="blue",
    fg="black",
)
pause = tk.Button(
    text="Pause/Resume",
    width=10,
    height=1,
    bg="blue",
    fg="black",
)

# user enters how many iterations they want to run
entry = tk.Entry(window, width=10)

label.pack()
start.pack()
stop.pack()
pause.pack()
entry.pack()
window.mainloop()