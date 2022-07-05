from tkinter import *
from question_model import Question1
from quiz_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from random import shuffle
import html
import sys
import tkinter as tk
from tkinter import messagebox

def quit(): # function for quit button
    sys.exit()

def credits(): # To allow "Credits" button to display message
    messagebox.showinfo(message="Created by William Yu 2022", title="Credits")


def about(): # To allow "About" button to display message
    messagebox.showinfo(message="This game is a quiz with general science as the topic", title="About")

def age(): # Try and except function as well as if and elif statments for age/response section of user details component
    global user_age
    answer = user_age.get()
    try:
        if user_age.get() == "":
            messagebox.showinfo(message="Please enter your age",title="age") # if the user does not enter anything in the textbox
        elif float(answer) <=3:
            messagebox.showinfo(message="You are joking with me right? Please write a proper response",title="age") # if the user enters values 3 or lower in the textbox
        elif float(answer) <=11:
            messagebox.showinfo(message="I would suggest having parental guidance",title="age") # if the user enters values >3 and <=11 in the textbox
            win.destroy()
        elif float(answer) <=19:
            messagebox.showinfo(message="A good age to attempt the quiz",title="age") # if the user enters values >11 and <=19 in the textbox
            win.destroy()
        elif float(answer) <=125:
            messagebox.showinfo(message="Never too late to try",title="age") # if the user enters values >19 and <=125 in the textbox
            win.destroy()
        elif float(answer) >125:
            messagebox.showinfo(message="You are joking with me right? Please write a proper response",title="age") # if the user enters values >125 in the textbox
    except ValueError:
            messagebox.showinfo(message="It must be a valid number",title="Error") # if the user enters clearly invalid answers like symbols
    

def name(): # Function for responses for names section for user details component
    global user_name
    answer2 = user_name.get()
    if user_name.get() == "":
         messagebox.showinfo(message="Please enter your username",title="name") # if the user enters nothing in the textbox
    else:
        messagebox.showinfo(message="Hi, {}".format(answer2),title="name") # when the user enteres something in the textbox
        win.destroy()
    
win = Tk() # creating an Tkinter frame
win.attributes("-fullscreen",True) #  To make it full screen
win.title("Fun quiz main menu") # title of the window
Label(text="Welcome to fun quiz",bg="#1BB1D9", fg="white", font=("ariel", 60, "bold"),width=60).place(relx= 0.5, rely=0, anchor='n') # big title in the main menu
button = tk.Button(win, text = "Start", command= win.destroy, width = 15,bg="#1BB1D9", fg="white",font=("ariel",38,"bold"))# start button
button.place(relx=0.350,rely=0.2)

button2= tk.Button(win,text= "Quit", command= quit, width = 15,bg="#1BB1D9", fg="white",font=("ariel",38,"bold"))# quit button
button2.place(relx=0.350,rely=0.65)

button3 = tk.Button(win, text = "Credits", command= credits, width = 15,bg="#1BB1D9", fg="white",font=("ariel",38,"bold"))# credits button
button3.place(relx=0.350,rely=0.5)

button4= tk.Button(win,text= "About", command= about, width = 15,bg="#1BB1D9", fg="white",font=("ariel",38,"bold"))# about button
button4.place(relx=0.350,rely=0.35)


Label(bg="#1BB1D9",height=30,width=300).place(relx= 0.5, rely=0.9, anchor='n')# Label for bottom border for the main menu

win.mainloop()

win=Tk() # creating an Tkinter frame
win.attributes("-fullscreen",True) # to make it full screen
user_name= Entry(win,fg="black",font=("ariel",25,"bold")) # textbox for name section
user_name.place(relx=0.38,rely=0.45)
Label(text="Please enter your desired username",bg="#1BB1D9", fg="white", font=("ariel", 50, "bold"),width=60).place(relx= 0.5, rely=0, anchor='n')# label for title
Label(text="Enter username here", fg="black", font=("ariel", 30, "bold")).place(relx= 0.5, rely=0.3, anchor='n')# label for subtitle

press2 =tk.Button(win,text="Next",command=name,width=10,bg="#1BB1D9", fg="white",font=("ariel",30,"bold"))# next button for name section of user details component
press2.place(relx=0.415,rely=0.56)

press3 =tk.Button(win,text="Quit",command=quit, width = 15,bg="#1BB1D9", fg="white",font=("ariel",20,"bold"))# quit button for name section of user details component
press3.place(relx=0.8,rely=0.15)

Label(bg="#1BB1D9",height=30,width=300).place(relx= 0.5, rely=0.9, anchor='n')# Label for bottom border for the name window
win.mainloop()

win=Tk()# Creating Tkinter frame
win.attributes("-fullscreen",True)# To make it full screen
user_age= Entry(win,fg="black",font=("ariel",25,"bold"))# Textbox for age section of user details component
user_age.place(relx=0.38,rely=0.45)
Label(text="Please enter your age",bg="#1BB1D9", fg="white", font=("ariel", 50, "bold"),width=60).place(relx= 0.5, rely=0, anchor='n')# Label for title for age section of user details component
Label(text="Enter your age here", fg="black", font=("ariel", 30, "bold")).place(relx= 0.5, rely=0.3, anchor='n')# label for subtitle for age section for user details component

press2 =tk.Button(win,text="Next",command=age,width=10,bg="#1BB1D9", fg="white",font=("ariel",30,"bold"))# next button for age section of user details component
press2.place(relx=0.415,rely=0.56)

press3 =tk.Button(win,text="Quit",command=quit, width = 15,bg="#1BB1D9", fg="white",font=("ariel",20,"bold"))# quit button for age section of user details component
press3.place(relx=0.8,rely=0.15)
Label(bg="#1BB1D9",height=30,width=300).place(relx= 0.5, rely=0.9, anchor='n')# Label for bottom border for the age window
win.mainloop()

# these codes will manage and link the other python scripts into one to form as my main quiz 
question_bank = []
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"]) # used to encode the HTML
    correct_answer = html.unescape(question["correct_answer"]) # used to encode the HTML
    incorrect_answers = question["incorrect_answers"] # used to encode the HTML
    for ans in incorrect_answers:
        choices.append(html.unescape(ans)) # used to encode the HTML
    choices.append(correct_answer)
    shuffle(choices) # shuffles up the choices of answers
    new_question = Question1(question_text, correct_answer, choices) #creates question
    question_bank.append(new_question) # appends it to question_bank


quiz = QuizBrain(question_bank) # to show score in print

quiz_ui = QuizInterface(quiz) # forms the interface of the quiz

# prints out the response and score to user
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}")