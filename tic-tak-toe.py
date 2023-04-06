
import random
import math
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import operator
import numpy
from fractions import Fraction
import os
from image_loader import *

#Main window 
main_window = tk.Tk() 
main_window.geometry("800x600")
main_window.title("Tic Tak Toe")
main_window.resizable(False, False) #disable maximize button 

#Title 
title_label = tk.Label(main_window, text="Tic-Tak-Toe v0.1.0", font=("Comic Sans MS", 32))
title_label.pack(side="top", fill="x")

# Question label 
question_label = tk.Label(main_window, text="Answer this puzzle", font=("Arial", 18))
question_label.place(x=10, y=70)

# Main label and answer label
main_label = tk.Label(main_window, text="", font=("Arial", 18))
main_label.place(x=10, y=100)
answer_label = tk.Label(main_window, text="", font=("Arial", 18))
answer_label.place(x=10, y=130)


# Button to generate new problem
new_problem_button = tk.Button(main_window, text="New Problem")
new_problem_button.place(x=10, y=170)

# Import Picture
# my_image = ImageTk.PhotoImage(Image.open("./assets/angles/images.png"))
random_image = random.choice(image_array)

#Image label
image_label = Label(main_window, image=random_image)
image_label.pack()

main_window.mainloop()
