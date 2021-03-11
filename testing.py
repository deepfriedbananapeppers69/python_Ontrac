
import random 
<<<<<<< HEAD
lives = 3
score = 1
while lives > 0:
    SoCal = ["ANA","PSP","BNS","LAX","BUR","ONT","COM","ORG","CPT","SAN","CXL","SMX","FON","VNS","HBC","WHP","JPD","YUM","JSG"]
    NoCal = ["CCR","PET","EUR","RED","HAY","SAC","MLO","SFO","MRY","SJC","STK"]
    socal = SoCal
    nocal = NoCal
    wrong = []
    strwrong = wrong
    fullList = SoCal + NoCal
    choice = random.choice(fullList)
    print(choice)
    answer = input("socal or nocal: ")
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
        wrong.append(choice)
        print("You have " + str(lives) + " lives left.")
    if lives == 0:
        print("Sorry try again.")
        print(str(strwrong))
=======
from tkinter import *
def main():
    lives = 3
    score = 1

    while lives > 0:
        SoCal = ["ANA","PSP","BNS","LAX","BUR","ONT","COM","ORG","CPT","SAN","CXL","SMX","FON","VNS","HBC","WHP","JPD","YUM","JSG"]
        NoCal = ["CCR","PET","EUR","RED","HAY","SAC","MLO","SFO","MRY","SJC","STK"]
        socal = SoCal
        nocal = NoCal
        wrong = []
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
            wrong.append(choice)
        if lives == 0:
            print("Sorry try again.")
            print(wrong)
root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottemFrame = Frame(root)
bottemFrame.pack(side=BOTTOM)

Button1 = Button(topFrame, text="so cal", fg="red")
Button2 = Button(topFrame, text="no cal", fg="green")
Button3 = Button(topFrame, text="button3", fg="blue")
Button4 = Button(bottemFrame, text="button4", fg="orange")
Button1.pack(side=LEFT)
Button2.pack(side=RIGHT)
Button3.pack()
Button4.pack()



root.mainloop()
>>>>>>> bde5f5a... starting on the gui pushed the wrong list off to the side for now want to make it look pretty
