from tkinter import *
import random

names_list = []
global answer_list
asked = []
score = 0


# Create the main window
class Main_Menu:

    #Defines the appearance of the main menu
    def __init__(self, parent):
        background_color = "DarkGreen"
        self.main_frame = Frame(parent,
                                bg=background_color,
                                padx=100,
                                pady=100)
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
                                      bg="Turquoise",
                                      command=self.next_window)
        self.continue_button.grid(row=3, pady=20)

    #This is the code that opens the next window
    def next_window(self):
        name = self.name_bar.get()
        names_list.append(name)
        print(names_list)
        self.main_frame.destroy()
        Questions_Menu(root)


#Create the quiz window
class Questions_Menu:

    #Defines the appearance of the quiz window
    def __init__(self, parent):
        background_colour = "DarkGreen"
        self.main_frame = Frame(parent,
                                bg=background_colour,
                                padx=100,
                                pady=100)
        self.main_frame.grid()

        self.questlabel = Label(self.main_frame,
                                text=answer_list[qnum][0],
                                font=("Tw Cen MT", "18", "bold"),
                                bg=background_colour)
        self.questlabel.grid(row=1, padx=10, pady=10, columnspan=2)

        self.variable1 = IntVar()

        #Question Button 1
        self.radiobutton1 = Radiobutton(self.main_frame,
                                        text=answer_list[qnum][1],
                                        font=("Helvetica", "12"),
                                        value=1,
                                        padx=10,
                                        pady=10,
                                        variable=self.variable1,
                                        bg=background_colour,
                                        highlightthickness=0)
        self.radiobutton1.grid(row=2, column=0, sticky=W)

        #Question Button 2
        self.radiobutton2 = Radiobutton(self.main_frame,
                                        text=answer_list[qnum][2],
                                        font=("Helvetica", "12"),
                                        value=2,
                                        padx=10,
                                        pady=10,
                                        variable=self.variable1,
                                        bg=background_colour,
                                        highlightthickness=0)
        self.radiobutton2.grid(row=2, column=1, sticky=W)

        #Question Button 3
        self.radiobutton3 = Radiobutton(self.main_frame,
                                        text=answer_list[qnum][3],
                                        font=("Helvetica", "12"),
                                        value=3,
                                        padx=10,
                                        pady=10,
                                        variable=self.variable1,
                                        bg=background_colour,
                                        highlightthickness=0)
        self.radiobutton3.grid(row=3, column=0, sticky=W)

        #Question button 4
        self.radiobutton4 = Radiobutton(self.main_frame,
                                        text=answer_list[qnum][4],
                                        font=("Helvetica", "12"),
                                        value=4,
                                        padx=10,
                                        pady=10,
                                        variable=self.variable1,
                                        bg=background_colour,
                                        highlightthickness=0)
        self.radiobutton4.grid(row=3, column=1, sticky=W)

        #Confirm Button
        self.confirm_button = Button(self.main_frame,
                                     text="Confirm",
                                     bg="White",
                                     font=("Helvetica", "12"),
                                     command=self.quiz_progress)

        self.confirm_button.grid(row=7, padx=5, pady=5, columnspan=2)

        #Total Score
        self.total_score = Label(self.main_frame,
                                 text="TOTAL SCORE",
                                 font=("Helvetica", "12"),
                                 bg=background_colour)
        self.total_score.grid(row=8, padx=10, pady=1, columnspan=2)

    def quiz_progress(self):
        global score
        ttl_scr = self.total_score
        choice = self.variable1.get()
        if len(asked) > 9:
            if choice == answer_list[qnum][6]:
                score += 1
                ttl_scr.configure(text=score)
                self.confirm_button.config(text="Confirm")
                #so something to end
            else:
                score += 0
                ttl_scr.configure(text="Correct answer was " +
                                  answer_list[qnum][5])
                self.confirm_button.config(text="Confirm")
        else:
            if choice == 0:
                self.confirm_button.config(text="Select an answer.")
                choice = self.variable1.get()
            else:
                if choice == answer_list[qnum][6]:
                    score += 1
                    ttl_scr.configure(text=score)
                    self.confirm_button.config(text="Confirm")
                    self.quiz_setup()
                else:
                    score += 0
                    ttl_scr.configure(text="The correct answer was " +
                                      answer_list[qnum][5])
                    self.confirm_button.config(text="confirm")
                    self.quiz_setup()

    def quiz_setup(self):
        randomiser()
        self.variable1.set(0)
        self.questlabel.config(text=answer_list[qnum][0])
        self.radiobutton1.config(text=answer_list[qnum][1])
        self.radiobutton2.config(text=answer_list[qnum][2])
        self.radiobutton3.config(text=answer_list[qnum][3])
        self.radiobutton4.config(text=answer_list[qnum][4])


    #This is the code that randomises the chosen questions
def randomiser():
    global qnum
    qnum = random.randint(1, 50)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


randomiser()

#Dictionary that holds all possible questions and answers
answer_list = {
    1: [
        "What is the scientific name for Humans?", "Homo Sapiens",
        "Homo Neanderthalas", "Homo Erectus", "Homo Reptillias",
        "Homo Sapiens", 1
    ],
    2: [
        "Which is the largest planet in our solar system?", "Earth", "Mars",
        "Jupiter", "Saturn", "Jupiter", 3
    ],
    3: [
        "Which mesozoic period occured 200 million years ago?", "Triassic",
        "Jurassic", "Cretaceous", "Paleogene", "Jurassic", 2
    ],
    4: [
        "What is the largest organ in the human body?", "Skin", "Liver",
        "Heart", "Brain", "Skin", 1
    ],
    5: [
        "What is the largest exoplanet ever found?", "j1407b", "Kepler-24b",
        "ROXs-42Bb", "TrES-4b", "TrES-4b", 4
    ],
    6: [
        "How fast is the speed of light?", "300,000 km/s", "300,000 m/s",
        "300,000 mph", "300,000 knots", "300,000 km/s", 1
    ],
    7: [
        "What is the largest country in the world?", "USA", "China", "Russia",
        "France", "Russia", 3
    ],
    8: [
        "What is the largest ocean in the world?", "Atlantic", "Pacific",
        "Indian", "Arctic", "Pacific", 2
    ],
    9: [
        "Who discovered gravity?", "Isaac Newton", "Albert Einstein",
        "Galileo", "Thomas Edison", "Isaac Newton", 1
    ],
    10:
    ["When did World War II end?", "1945", "1939", "1918", "1947", "1945", 1],
    11: [
        "How many planets are there in our solar system?", "7", "9", "8", "6",
        "8", 3
    ],
    12: [
        "What country has the highest Education Index?", "New Zealand",
        "Iceland", "Germany", "USA", "Iceland", 2
    ],
    13: [
        "Which country is often not found on the world map?", "Russia",
        "Australia", "Canada", "New Zealand", "New Zealand", 4
    ],
    14: [
        "When did the american revolution start?", "1775", "1789", "1775",
        "1783", "1775", 1
    ],
    15: [
        "What is the capital of France?", "London", "Paris", "Berlin",
        "Madrid", "Paris", 2
    ],
    16: [
        "What was the first video game ever made?", "Froggers", "Pacman",
        "Pong", "Space Invaders", "Pong", 3
    ],
    17: [
        "What is the largest animal in the world?", "Blue Whale", "Elephant",
        "Giraffe", "Hippopotamus", "Blue Whale", 1
    ],
    18: [
        "Who was the first president of the United States?",
        "Alexander Hamilton", "George Washington", "Thomas Jefferson",
        "John Adams", "George Washington", 2
    ],
    19: [
        "William Buckland discovered the first Dinosaur \n Fossil in the world. What was it?",
        "T-Rex", "Triceratops", "Stegosaurus", "Megalosaurus", "Megalosaurus",
        4
    ],
    20: [
        "Who built the world's first car?", "Karl Benz", "Henry Ford",
        "Alexander Winton", "Étienne Lenoir", "Karl Benz", 1
    ],
    21: [
        "What is the tallest tower ever built?", "The Burj Khalifa",
        "Shanghai Tower", "The Sky Tower", "The Empire State Building",
        "The Burj Khalifa", 1
    ],
    22: [
        "A manhole cover was launched into space in 1957 after a nuclear bomb was tested underground. \n How fast did this manhole cover go?",
        "70,000mph", "100,000mph", "80,000mph", "130,000mph", "130,000mph", 4
    ],
    23: [
        "When did the first iPhone come out?", "2005", "2006", "2007", "2008",
        "2007", 3
    ],
    24: [
        "Which country has the most islands?", "Canada", "Sweden", "Finland",
        "Norway", "Sweden", 2
    ],
    25: [
        "Why did the dinosaurs go extinct?", "Supervolcano Eruption",
        "Global Virus infection", "Giant meteor collision",
        "The first Ice Age", "Giant meteor collision", 3
    ],
    26: [
        "What is planet j1407b famous for?",
        "It is the largest planet discovered",
        "It has the largest rings in the observable universe",
        "It was the first exoplanet discovered",
        "It is the largest planet in the solar system",
        "It has the largest rings in the observable universe", 2
    ],
    27:
    ["When was the black plague?", "1642", "1378", "1794", "1421", "1642", 1],
    28: [
        "1918 was the year that...", "The first iPhone came out",
        "The first car was invented", "The dinosaur fossil was found",
        "The first world war began", "The first world war began", 4
    ],
    29: [
        "Who invented the light bulb?", "Thomas Edison", "Alexander Winton",
        "Joseph Swan", "The true inventor is unknown",
        "The true inventor is unknown", 4
    ],
    30: [
        "What was the first planet formed in our solar system?", "Jupiter",
        "Saturn", "Uranus", "Neptune", "Jupiter", 1
    ],
    31: [
        "What mathematical subject uses letters?", "Algebra", "Trigonometry",
        "Calculus", "All of the above", "All of the above", 4
    ],
    32: [
        "Who was the first person to walk on the moon?", "Neil Armstrong",
        "Buzz Aldrin", "Michael Collins", "Yuri Gagarin", "Neil Armstrong", 1
    ],
    33: [
        "Which animal has the highest successful hunting rate?",
        "African Wild dog", "Black-footed Cat", "Dragonfly", "Cheetah",
        "Dragonfly", 3
    ],
    34: [
        "The Bald Eagle is a symbol of which country?", "United Kingdom",
        "United States", "France", "Canada", "United States", 2
    ],
    35: [
        "Guess which button is the correct one", "This one",
        "No, it's this one", "Don't listen to them- this is the right one!",
        "Nah, it's this one", "Nah, it's this one", 4
    ],
    36: [
        "What is the tallest bird to ever roam the earth?",
        "The common pigeon", "The Elephant Bird", "The Island Moa",
        "The Ostrich", "The Island Moa", 3
    ],
    37: [
        "How many letters are there in the English alphabet?", "26", "25",
        "24", "23", "26", 1
    ],
    38: [
        "What shape is the earth?", "Round", "Flat", "Sphere", "Cube",
        "Sphere", 3
    ],
    39: [
        "Which of these iconic films is all about dinosaurs?", "Interstellar",
        "Jaws", "Star Wars", "Jurassic Park", "Jurassic Park", 4
    ],
    40: [
        "This quiz is coded in what programming language?", "Python", "Java",
        "C++", "C#", "Python", 1
    ],
    41:
    ["How old do you have the be to vote?", "18", "17", "16", "15", "18", 1],
    42: [
        "What is the Tallest LEGO set ever made?", "The Avengers' Tower",
        "The Eiffel Tower", "The Death Star", "The LEGO world map",
        "The Eiffel Tower", 2
    ],
    43: [
        "What is the circumference of the earth?", "40,000ft", "40,000m",
        "40,000km", "40,000mi", "40,000km", 3
    ],
    44: [
        "If bob has 273 lollies, and he eats 237, how many lollies does he have now?",
        "100", "946", "241", "Diabetes. Bob has diabetes.",
        "Diabetes. Bob has diabetes.", 4
    ],
    45: [
        "If you stare directly at the sun, what will happen?",
        "You will explode", "Nothing", "You will go blind",
        "You will magically write the whole declaration of independence",
        "You will go blind", 3
    ],
    46: [
        "What does 'GOAT' stand for in internet slang?",
        "Greatest Of All Time", "Great Orange Apple Taste",
        "Good old Apple Tooth", "Got Owens All Time", "Greatest Of All Time", 1
    ],
    47: [
        "Water, or H20 in scientific terms, is a liquid that humans require to survive. What two elements are in it?",
        "Hydrogen and Oxygen", "Hydrogen and Carbon Dioxide",
        "Hydrogen and Carbon", "Oxygen and Carbon Dioxide",
        "Hydrogen and Oxygen", 1
    ],
    48: [
        "How many bones are in the human body?", "206", "205", "207", "204",
        "207", 3
    ],
    49: [
        "How many languages are there in the world?", "4,982", "7,164",
        "3,129", "1,960", "7,164", 2
    ],
    50: [
        "How much of the universe have we discovered?", "2%", "3%", "5%",
        "10%", "5%", 3
    ],
}

#The mainloop that creates the window for all code to run
if __name__ == "__main__":
    root = Tk()
    root.title("Liam Fraser CSC 2.7 assessment")
    root.resizable(height=None, width=None)
    main_menu = Main_Menu(root)

    root.mainloop()
