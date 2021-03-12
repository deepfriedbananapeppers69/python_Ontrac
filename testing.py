
import random 
from tkinter import *


class tracgame:

  

    def __init__(self, master):
        frame = Frame(master, width=400,height=300)
        frame.pack()

        self.quitButton = Button(frame, text="QUIT", command=frame.quit)
        self.quitButton.pack(side=LEFT,)

        self.socalbutton = Button(frame, text="START",command=self.main)
        self.socalbutton.pack(side=RIGHT)

    
    def main(self):
        lives = 3
        score = 1

        while lives > 0:
            SoCal = ["ANA","PSP","BNS","LAX","BUR","ONT","COM","ORG","CPT","SAN","CXL","SMX","FON","VNS","HBC","WHP","JPD","YUM","JSG"]
            NoCal = ["CCR","PET","EUR","RED","HAY","SAC","MLO","SFO","MRY","SJC","STK"]
            socal = SoCal
            nocal = NoCal
            fullList = SoCal + NoCal
            choice = random.choice(fullList)
            print(choice)
            answer = input("socal or nocal:")
            if "socal" in answer:
                answer = socal
            else:
                answer = nocal

            if choice in answer:
                print("correct")
                score = score + 1
                print("Your score is: " + str(score))
            else:
                print("not correct")
                score = score - 1
                lives = lives - 1
                print("You have " + str(lives) + " lives left.")
            if lives == 0:
                print("sorry try again")
    

root = Tk() 
game = tracgame(root)
root.mainloop()
