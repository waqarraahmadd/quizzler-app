from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "arial", 20, "italic"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            font=("arial", 15),
            pady=20, padx=20,
            bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightbackground=THEME_COLOR)
        self.question_text = self.canvas.create_text(
            150, 125,
            font=FONT,
            text="",
            fill=THEME_COLOR,
            anchor="center",
            width=250
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image,
            command=self.true,
            font=FONT,
            bd=0,
            highlightthickness=0
        )
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image,
            command=self.false,
            font=FONT,
            bd=0,
            highlightthickness=0
        )
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz.\nYour final score is {self.quiz.score}/{self.quiz.question_number}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.canvas.config(bg="white")
    def true(self):
        answer = self.quiz.check_answer("true")
        self.give_feedback(answer)

    def false(self):
        answer = self.quiz.check_answer("false")
        self.give_feedback(answer)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


