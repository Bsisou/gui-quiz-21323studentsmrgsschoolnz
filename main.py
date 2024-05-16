import random
from tkinter import *

names = []
global answers
asked = []
score = 0


def randomiser():
    global questionNumber
    questionNumber = random.randint(1, 10)
    if questionNumber not in asked:
        asked.append(questionNumber)
    elif questionNumber in asked:
        randomiser()


randomiser()

answers = {
    1: [
        "What is the capital of France?", 'Berlin', 'Paris', 'London',
        'Madrid', 'Paris', 2
    ],
    2: ["What are the two most important subjects in school?",
        'Maths and English', "Art and Maths", \
        'English and Science', 'Maths and Science', \
        'Maths and English', 1],
    3: [
        "Who wrote the lord of the rings?", 'J.K. Rowling', 'Stephen King',
        "J.R.R Tolkien", 'George Orwell', 'J.R.R Tolkien', 3
    ],
    4: [
        "Where is mount Everest located?", 'India', 'Nepal', 'China', 'Bhutan',
        "Nepal", 2
    ],
    5: [
        "Who was the 40th president of the USA?", "Barack Obama",
        "Donald Trump", "Bill Clinton", "George Bush", "Barack Obama", 1
    ],
    6: ["When did WW2 end?", "1918", "1939", "1945", "1914", "1945", 3],
    7: [
        "How old is the universe?", "17.3 billion years", "13.8 billion years",
        "12.4 billion years", "19.6 billion years", "13.8 billion years", 2
    ],
    8: [
        "What was the largest dinosaur to roam the earth?", 'Titanosaurus',
        'Argentinosaurus', 'Giganotosaurus', 'Spinosaurus', 'Titanosaurus', 1
    ],
    9: [
        "Who invented the lightbulb?", 'Albert Einstein', 'Nikola Tesla',
        'Isaac Newton', 'Thomas Edison', 'Thomas Edison', 4
    ],
    10: [
        "Which Country is often not found on the world map?", 'Canada',
        'Australia', 'New Zealand', 'South Africa', 'New Zealand', 3
    ]
}


class QuizStarter:

    def __init__(self, parent):

        background_color = "DarkGreen"

        self.quiz_frame = Frame(parent,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()

        self.heading_label = Label(
            self.quiz_frame,
            text="10-question General Knowledge Quiz",
            font=("Arial", "30", "bold"),
            bg=background_color,
        )
        self.heading_label.grid(row=0, padx=20)

        self.var1 = IntVar()

        self.user_label = Label(
            self.quiz_frame,
            text="Enter your name below and start the quiz",
            font=("Roboto", "20"),
            bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20)

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)

        self.continue_button = Button(self.quiz_frame,
                                      text=("Continue"),
                                      font=(
                                          "Helvetica",
                                          "15",
                                      ))
        self.continue_button.grid(row=3, padx=20, pady=20)

    def name_collection(self):
        name = self.entry_box.get()
        names.append(name)
        self.quiz_frame.destroy()


if __name__ == "__main__":
    quizRoot = Tk()
    quizRoot.title(
        "10 question General Knowledge Quiz - Liam Fraser, assessment standard 2.7"
    )
    quiz_instance = QuizStarter(quizRoot)
    quizRoot.mainloop()
