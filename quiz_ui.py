from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_brain import QuizBrain
import sys

THEME_COLOR = "#1e2324"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Fun Quiz") # title of the window
        self.window.attributes("-fullscreen", True)# to make window full screen

        # Display Title
        self.display_title()

        # Create a canvas for question text, and display question
        self.canvas = Canvas(width=2000,height=250)
        self.question_text = self.canvas.create_text(750, 200, text="Question here", width=680, fill=THEME_COLOR, font=('Ariel', 15, 'italic'))
        self.canvas.grid(row=5, column=0, columnspan=2, pady=50)
        self.display_question()

        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()

        # Display four options (radio buttons)
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is right or wrong
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(relx=0.4,rely=0.6)

        # Next and Quit Button
        self.buttons()

        # Mainloop
        self.window.mainloop()

    def display_title(self):
        # To display title
        maxwidth = self.window.winfo_screenwidth()
        
        # Title
        title = Label(self.window, text="Fun Quiz",
                      width=int(maxwidth/16), height=2, bg="#1BB1D9", fg="white", font=("ariel", 20, "bold"))

        # place of the title    
        title.place(relx= 0.5, rely=0, anchor='n')

    def display_question(self):
        # To display the question

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):
        # To create four options (radio buttons)

        # initialize the list with an empty list of options
        choice_list = []

        # position of the first option
        y_pos = 340

        # adding the options to the list
        while len(choice_list) < 4:

            # setting the radio button properties
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer,
                                    value='', font=("ariel", 14))

            # adding the button to the list
            choice_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=400, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return choice_list

    def display_options(self):
        # To display four options

        val = 0

        # deselecting the options
        self.user_answer.set(None)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        # To show feedback for each answer and keep checking for more questions

        # Check if the answer is correct and to give a valid response to the user if they are wrong or right
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Oops! \n'
                                     f'The right answer is: {self.quiz.current_question.correct_answer}')

        if self.quiz.has_more_questions():
            # Moves to next to display next question and its options
            self.display_question()
            self.display_options()
        else:
            # if no more questions, then it displays the score
            self.display_result()

            # destroys the self.window
            self.window.destroy()

    def buttons(self):
        maxwidth2 = self.window.winfo_screenwidth()
        # To show next button and quit button

        # The first button is the Next button to move to the
        # next Question
        next_button = Button(self.window, text="Next", command=self.next_btn,
                             width=int(maxwidth2/100), bg="#1BB1D9", fg="white", font=("ariel", 16, "bold"))

        # palcing the button on the screen
        next_button.place(relx=0.43, rely=0.7)

        # This is the second button which is used to Quit the self.window
        quit_button = Button(self.window, text="Quit", command=quit,
                             width=int(maxwidth2/100), bg="red", fg="white", font=("ariel", 16, " bold"))

        # placing the Quit button on the screen
        quit_button.place(relx=0.8, rely=0.1)
    
    def quit(self):
        sys.exit()

    def display_result(self):
        # To display the result using messagebox
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

         # calculates the percentage of correct answers
        result = f"Score: {score_percent}%"

         # Shows a message box to display the result
        messagebox.showinfo("Your result is:", f"{result}\n{correct}\n{wrong}")