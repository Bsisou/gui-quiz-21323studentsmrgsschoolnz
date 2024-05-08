from tkinter import *

from random import *

names_list = []
global questions_answers
asked = []
score=0

def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()

randomiser()
if __name__ == "__main__":
    root = Tk()
    root.title("Nz Road Rules Quiz")
    quizStarter_object = QuizStarter(root)
    root.mainloop()