from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        score_brain = QuizBrain(quiz_brain)
        score = score_brain.score
        self.score_count_label = Label(text=f"Score: {score}", font=("Arial", 8), bg=THEME_COLOR, fg="white")
        self.score_count_label.grid(column=1, row=0)

        correct_symbol_image = PhotoImage(file="images/true.png")
        self.correct_symbol = Button(image=correct_symbol_image, highlightthickness=0, command=self.true_symbol)
        self.correct_symbol.grid(column=0, row=2)

        wrong_symbol_image = PhotoImage(file="images/false.png")
        self.wrong_symbol = Button(image=wrong_symbol_image, highlightthickness=0, command=self.false_symbol)
        self.wrong_symbol.grid(column=1, row=2)

        # question = QuizBrain.next_question(quiz_brain)
        # text = question.q_text
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 125, text="text", font=("Arial", 15, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.get_next_question()



        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You have reached the end of the Quiz! Thanks for playing.")
            # The below codes switch off the buttons and they won't work anymore
            self.correct_symbol.config(state="disabled")
            self.wrong_symbol.config(state="disabled")

    def true_symbol(self):
        self.give_feedback(self.quiz.check_answer("True"))
        score = self.quiz.score
        self.score_count_label.config(text=f"Score: {score}")

    def false_symbol(self):
        self.give_feedback(self.quiz.check_answer("False"))
        score = self.quiz.score
        self.score_count_label.config(text=f"Score: {score}")

    def give_feedback(self, is_right):
        def original_background():
            self.canvas.config(bg="white")
            self.window.after_cancel(event)
            self.get_next_question()
        if is_right is True:
            self.canvas.config(bg="green")
            event = self.window.after(1000, original_background)
        else:
            self.canvas.config(bg="red")
            event = self.window.after(1000, original_background)