"""
This Script is to build a quiz for the kuerzel.
"""
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import font

from kuerzel_questions import questions

# define global variables
score = 0
current_question = {}
answered_questions = []


# define the functions
def ask_question():
    """
    Creates the questions and outputs them randomly
    """
    global current_question, var, option_buttons
    while True:
        current_question = random.choice(list(questions.items()))
        if current_question not in answered_questions:
            break
    question_label.config(text=current_question[0])
    for i in range(len(current_question[1]["options"])):
        option_buttons[i].config(text=current_question[1]["options"][i], font=("Monospace", 40), height=2, width=len(current_question[1]["options"][i]) + 20, bg="white", command=lambda idx=i: set_answer_bg(idx))
        option_buttons[i].pack(side="top", fill="x", padx=10, pady=10)
        option_buttons[i].config(anchor="center", variable=var, value=i)
    answered_questions.append(current_question)


def set_answer_bg(button_idx):
    """
    Sets the background of the selected answer to orange and the background of the other options to white.
    """
    global option_buttons
    var.set(button_idx)
    for i, button in enumerate(option_buttons):
        if i == button_idx:
            button.config(bg="orange", fg="white")
        else:
            button.config(bg="white", fg="black")
        button.config(width=len(current_question[1]["options"][i]) + 20, anchor="center")


def submit():
    """
    Creates the Sumbit Button and adds to the Score if question is right. If it was the last Question it calls the end_quiz function.
    """
    global score, var, answered_questions, option_buttons
    if current_question[1]["answer"] == current_question[1]["options"][var.get()]:
        score += 1
    score_label.config(text="Score: " + str(score))
    if len(answered_questions) == len(questions):
        end_quiz()
    else:
        for button in option_buttons:
            button.pack_forget()
        ask_question()


def end_quiz():
    """
    When the last Question is asked, a pop up windows opens and shows the score
    """
    question_label.config(text="Quiz beendet! Dein Score ist: " + str(score) + " von " + str(len(questions)), font=("Monospace", 60))
    for button in option_buttons:
        button.config(state="disabled")
    submit_button.config(state="disabled")
    messagebox.showinfo("Quiz beendet", "Dein Score ist: " + str(score))
    root.destroy()


# create the GUI
root = tk.Tk()
var = tk.IntVar(value=-1)
root.title("Fragen zu den Kürzel v1")
root.geometry("1000x800")

# configure the style
root.configure(bg="white")
root.option_add("*Font", font.Font(family="Monospace", size=60))

# create the widgets
title_frame = tk.Frame(root, bg="white")
title_frame.pack(side="top", pady=10)

score_label = tk.Label(title_frame, text="Score: 0", fg="black", bg="white", anchor="w", font=("Monospace", 40))
score_label.pack(padx=50, pady=10)

question_label = tk.Label(title_frame, text="", fg="black", bg="white", font=("Monospace", 60))
question_label.pack(side="left", expand=True, fill="x")

spacer_frame = tk.Frame(title_frame, bg="white")
spacer_frame.pack(side="left", padx=50, fill="x")

submit_button = tk.Button(spacer_frame, text="Bestätigen", command=submit, fg="white", bg="#00cc00", padx=60, pady=20, font=("Monospace", 40))
submit_button.pack(side="right")

question_frame = tk.Frame(root, bg="white")
question_frame.pack(pady=40)

option_frame = tk.Frame(root, bg="white")
option_frame.pack()

option_buttons = []
max_answer_len = 0
for i in range(4):
    button = tk.Radiobutton(option_frame, text="", variable=var, value=i, fg="black", bg="white", pady=10, padx=20, indicatoron=0,
                            selectcolor="orange")
    button.pack(side="top", fill="x", padx=10, pady=10)
    option_buttons.append(button)

# ask the first question
ask_question()

# start the main loop
root.mainloop()
