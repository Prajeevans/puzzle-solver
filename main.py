import random
import math
import tkinter as tk
import operator

# Math function
def number_generator():
    num_1 = random.randrange(1, 20)
    num_2 = random.randrange(num_1,20)
    return num_1, num_2

num_1, num_2 = number_generator()
def question_maker(num_1, num_2):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    operations = random.choice(list(operators.keys()))
    calculator = operators.get(operations)(num_1,num_2)
    div_que = f"{num_1} {operations} {num_2} "
    print(div_que)
    if operations == '/':
        print("Answer is " ,"%.2f" % calculator)
    else:   
        # print(div_que)
        print("Answer is " ,calculator)

# question_maker(num_1,num_2)

#Main window 
main_window = tk.Tk()  # create the main_window window

# set the window size and position
main_window.geometry("800x600")

# set the window title
main_window.title("Puzzle Solver")
main_window.resizable(False, False) #disable maximize button 

# start the main event loop
main_window.mainloop()