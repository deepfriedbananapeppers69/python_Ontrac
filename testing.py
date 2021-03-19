
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
        self.socal = self.SoCal
        self.nocal = self.NoCal
        self.wrong = []
        self.fullList = self.SoCal + self.NoCal
        self.choice = random.choice(self.fullList)
        
        
        # This is the GUI 
        # ---------------------------------------
        # This parts makes the frame and for updateing labels 
        frame = Frame(master)
        frame.pack()

        self.text = StringVar()

        self.pickchoice = StringVar()
        self.pickchoice.set(self.choice)

        self.numberscore = StringVar()
        self.numberscore.set(self.score)
        # Main parts of the Gui that you see
        self.Score = Label(frame, textvariable=self.numberscore)
        self.Score.pack(side=TOP, pady=1, padx=1)

        self.label2 = Label(frame, textvariable=self.text, width= 10, height= 2 )
        self.label2.pack(side=BOTTOM)

        self.label1 = Label(frame, textvariable=self.pickchoice)
        self.label1.pack(side=TOP)

        self.quitButton = Button(frame, text="  QUIT  ",width= 10, height= 2 ,command=frame.quit)
        self.quitButton.pack(side=BOTTOM)

        self.socalbutton = Button(frame, text="So Cal",width= 10, height= 2 ,command=self.SOCALCHECK)
        self.socalbutton.pack(side=RIGHT, pady=1, padx=1)

        self.nocalbutton = Button(frame, text="No Cal",width= 10, height= 2 ,command=self.NOCALCHECK)
        self.nocalbutton.pack(side=RIGHT, pady=2, padx=2)
        # end of GUI
        # -----------------------------------------

    # These are fuctions for checking the answers    
    # These functions will choose a new area code only when you pick the right choice for now  
    def NOCALCHECK (self):
        answer = self.choice
        if answer in self.NoCal:
            self.score =  self.score + 1
            self.numberscore.set(self.score)
            self.text.set("correct")
            self.choice = random.choice(self.fullList)
            self.pickchoice.set(self.choice)
        else: 
            self.score =  self.score - 1
            self.numberscore.set(self.score)
            self.text.set("not correct")

    def SOCALCHECK (self):
        answer = self.choice
        if answer in self.SoCal:
            self.score =  self.score + 1
            self.numberscore.set(self.score)
            self.text.set("correct")
            self.choice = random.choice(self.fullList)
            self.pickchoice.set(self.choice)
        else: 
            self.score =  self.score - 1
            self.numberscore.set(self.score)
            self.text.set("not correct")
           
   
root = Tk() 
game = tracgame(root)
root.geometry("800x400")
root.mainloop()