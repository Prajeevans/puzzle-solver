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
main_window = tk.Tk() 
main_window.geometry("800x600")
main_window.title("Puzzle Solver")
main_window.resizable(False, False) #disable maximize button 

#Title 
title_label = tk.Label(main_window, text="Puzzle Solver v0.1.0", font=("Comic Sans MS", 32))
title_label.pack(side="top", fill="x")

# Question label 
question_label = tk.Label(main_window, text="Solve this puzzle", font=("Arial", 18))
question_label.place(x=10, y=60)


main_window.mainloop()