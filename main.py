from tkinter import *
import random

names_list = []
global questions_answers
asked = []
score = 0


# Create the main window
class Main_Menu:

  def __init__(self, parent):
    background_color = "White"
    self.main_frame = Frame(parent, bg=background_color, padx=100, pady=100)
    self.main_frame.grid()

    self.title = Label(self.main_frame,
                       text="Untitled General Knowledge Quiz",
                       font=("Tw Cen MT", "18", "bold"),
                       bg=background_color)
    self.title.grid(row=0)

    self.name_prompt = Label(self.main_frame,
                             text="Enter your name below",
                             font=("Tw Cen MT", "16"),
                             bg=background_color)
    self.name_prompt.grid(row=1, pady=20)

    self.name_bar = Entry(self.main_frame)
    self.name_bar.grid(row=2, pady=20)

    self.continue_button = Button(self.main_frame,
                                  text="Continue",
                                  bg="pink",
                                  command=self.next_window)
    self.continue_button.grid(row=3, pady=20)

  def next_window(self):
    name = self.name_bar.get()
    names_list.append(name)
    print(names_list)
    self.main_frame.destroy()
    Quiz_Menu(root)
    

class Quiz_Menu:
  def __init__(self, parent):
    pass
    
    
if __name__ == "__main__":
  root = Tk()
  root.title("Liam Fraser CSC 2.7 assessment")
  root.resizable(height=None, width=None)
  main_menu = Main_Menu(root)
  root.mainloop()
