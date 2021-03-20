
import random 
from tkinter import *



class tracgame:

    def __init__(self, master):
        # Global Variables
        # When calling these variables use .self first 
        self.lives = 3
        self.score = 0
        self.SoCal = ["ANA","PSP","BNS","LAX","BUR","ONT","COM","ORG","CPT","SAN","CXL","SMX","FON","VNS","HBC","WHP","JPD","YUM","JSG"]
        self.NoCal = ["CCR","PET","EUR","RED","HAY","SAC","MLO","SFO","MRY","SJC","STK"]
        self.Desert = ["BKY","GEG","BOI","PHX","CDC","RNO","COS","TRI","DIA","TUC","FLG","UTA","BFL","VEG","VIS","FAT"]
        self.Vancouver = ["VAN"]
        self.Seattle = ["SEA","SEZ"]
        self.Other = ["TAC","EUG","MED"]
        self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
        self.choice = random.choice(self.fullList)
        
        # This is the GUI 
        # ---------------------------------------
        # This parts makes the frame and for updateing labels 
        frame = Frame(master)
        frame.pack()

        self.text = StringVar()

        self.Lives = StringVar()
        self.Lives.set(" You have Lives: " + (str(self.lives)) + " left") 

        self.pickchoice = StringVar()
        self.pickchoice.set(" Where does this area code belong: " + str(self.choice))

        self.numberscore = StringVar()
        self.numberscore.set("Your Score: " + str(self.score))
        # Main parts of the Gui that you see
        self.Score = Label(frame, textvariable=self.numberscore)
        self.Score.pack(side=TOP, pady=1, padx=1)

        self.label3 = Label(frame, textvariable=self.Lives)
        self.label3.pack(side=TOP, pady=1, padx=1)

        self.label2 = Label(frame, textvariable=self.text)
        self.label2.pack(side=BOTTOM)

        self.label1 = Label(frame, textvariable=self.pickchoice)
        self.label1.pack(side=TOP)

        self.quitButton = Button(frame, text="  QUIT  ",width= 10, height= 2 ,command=frame.quit)
        self.quitButton.pack(side=BOTTOM)

        self.socalbutton = Button(frame, text="So Cal",width= 10, height= 2 ,command=self.SOCALCHECK)
        self.socalbutton.pack(side=RIGHT, pady=1, padx=1)

        self.nocalbutton = Button(frame, text="No Cal",width= 10, height= 2 ,command=self.NOCALCHECK)
        self.nocalbutton.pack(side=RIGHT, pady=2, padx=2)\

        self.nocalbutton = Button(frame, text="Desert",width= 10, height= 2 ,command=self.DESERTCHECK)
        self.nocalbutton.pack(side=RIGHT, pady=2, padx=2)

        self.nocalbutton = Button(frame, text="Seattle",width= 10, height= 2 ,command=self.SEATTLECHECK)
        self.nocalbutton.pack(side=RIGHT, pady=2, padx=2)

        self.nocalbutton = Button(frame, text="Vancouver",width= 10, height= 2 ,command=self.VANCOUVERCHECK)
        self.nocalbutton.pack(side=RIGHT, pady=2, padx=2)

        self.nocalbutton = Button(frame, text="Other",width= 10, height= 2 ,command=self.OTHERCHECK)
        self.nocalbutton.pack(side=RIGHT, pady=2, padx=2)
        
        # end of GUI
        # -----------------------------------------

    # These are fuctions for checking the answers    
    # These functions will choose a new area code only when you pick the right choice for now  
    def NOCALCHECK (self):
        answer = self.choice
        if answer in self.NoCal:
            self.score =  self.score + 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")
            self.choice = random.choice(self.fullList)
            self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
        else: 
            self.score =  self.score - 1
            self.lives = self.lives - 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have Lives: " + (str(self.lives)) + " left") 
        if self.lives <= 0:
            root.destroy()
 
    def SOCALCHECK (self):
        answer = self.choice
        if answer in self.SoCal:
            self.score =  self.score + 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")
            self.choice = random.choice(self.fullList)
            self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
        else: 
            self.score =  self.score - 1
            self.lives = self.lives - 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have Lives: " + (str(self.lives)) + " left") 
        if self.lives <= 0:
            root.destroy()
    
    def DESERTCHECK (self):
        answer = self.choice
        if answer in self.Desert:
            self.score =  self.score + 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")
            self.choice = random.choice(self.fullList)
            self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
        else: 
            self.score =  self.score - 1
            self.lives = self.lives - 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have Lives: " + (str(self.lives)) + " left") 
        if self.lives <= 0:
            root.destroy()

    def VANCOUVERCHECK (self):  
        answer = self.choice
        if answer in self.Vancouver:
            self.score =  self.score + 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")
            self.choice = random.choice(self.fullList)
            self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
        else: 
            self.score =  self.score - 1
            self.lives = self.lives - 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have Lives: " + (str(self.lives)) + " left") 
        if self.lives <= 0:
            root.destroy()
            
    def SEATTLECHECK (self):
        answer = self.choice
        if answer in self.Seattle:
            self.score =  self.score + 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")
            self.choice = random.choice(self.fullList)
            self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
        else: 
            self.score =  self.score - 1
            self.lives = self.lives - 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have Lives: " + (str(self.lives)) + " left") 
        if self.lives <= 0:
            root.destroy()
    def OTHERCHECK (self):
        answer = self.choice
        if answer in self.Other:
            self.score =  self.score + 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")
            self.choice = random.choice(self.fullList)
            self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
        else: 
            self.score =  self.score - 1
            self.lives = self.lives - 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have Lives: " + (str(self.lives)) + " left") 
        if self.lives <= 0:
            root.destroy()
   
root = Tk() 
game = tracgame(root)
root.geometry("800x400")
root.mainloop()