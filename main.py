import random
import math
import tkinter as tk
import operator


class StdoutRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert('end', text)
        self.widget.see('end')
    
# Math function
def number_generator():
    num_1 = random.randrange(1, 20)
    num_2 = random.randrange(num_1,20)
    return num_1, num_2

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
        print("Answer is " ,calculator)
    return div_que, calculator

#Main window 
main_window = tk.Tk() 
main_window.geometry("800x600")
main_window.title("Puzzle Solver")
main_window.resizable(False, False) #disable maximize button 

#Title 
title_label = tk.Label(main_window, text="Puzzle Solver v0.1.0", font=("Comic Sans MS", 32))
title_label.pack(side="top", fill="x")

# Question label 
question_label = tk.Label(main_window, text="Answer this puzzle", font=("Arial", 18))
question_label.place(x=10, y=70)

# Main label and answer label
main_label = tk.Label(main_window, text="", font=("Arial", 18))
main_label.place(x=10, y=100)
answer_label = tk.Label(main_window, text="", font=("Arial", 18))
answer_label.place(x=10, y=130)

def update_problem():
    num_1, num_2 = number_generator()
    div_que, answer = question_maker(num_1, num_2)
    main_label.config(text=div_que)
    answer_label.config(text=f"Answer is {answer}")
    
update_problem()

# Button to generate new problem
new_problem_button = tk.Button(main_window, text="New Problem", command=update_problem)
new_problem_button.place(x=10, y=170)

main_window.mainloop()
