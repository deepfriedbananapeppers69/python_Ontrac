import time
import random 
import tkinter as tk
from tkinter import font as tkfont
from tkinter.constants import END, LEFT, RIGHT



#this part is where the frames are staged and change
class SampleApp(tk.Tk):

    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self,*args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        #container.grid_rowconfigure(0, weight=1)
        #container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (startwindow,tracgame,endwindow,winwindow):
            page_name = F.__name__
            frame = F(master=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("startwindow")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
  
#this is the starting window
class startwindow(tk.Frame):

    def __init__(self,master,controller):
        tk.Frame.__init__(self,master)

        self.controller = controller 
        #self.losetext =tk.StringVar()

        #Define the function for the timer

    
        self.label1 = tk.Label(self, text= "This is training for learning the area codes")
        self.label2 = tk.Label(self, text="HOW TO PLAY: when the area code is show you must chose the correct area that code belongs to. When you are ready click start")
        self.label3 = tk.Label(self, text="WARING: If you chose the incorrect area you can try again but if you get 3 wrong the game with close, but you can restart from this page.")
        #self.label4 = tk.Label(self, textvariable=self.losetext)
        self.Button1 = tk.Button(self,text="START",command=lambda: self.controller.show_frame("tracgame"),width=10,height=2,bg="green")
        #self.quitButton = tk.Button(self, text="  QUIT  ",width= 10, height= 2 ,command=self.frame.quit,bg="red")
        #self.quitButton.pack(side=tk.BOTTOM)
        self.Button1.pack(side=tk.BOTTOM)
        self.label1.pack(side=tk.TOP,padx=15, pady=2)
        self.label2.pack(side=tk.TOP,padx=15,pady=2)
        self.label3.pack(side=tk.TOP,padx=15,pady=2)
        #self.label4.pack(side=tk.BOTTOM)
       
    
#this is the game 
class tracgame(tk.Frame):

    def __init__(self, master,controller):
        tk.Frame.__init__(self,master)
        # Global Variables
        # When calling these variables use .self first 
        self.controller = controller
        self.lives = 3
        self.score = 0
        self.yourscore = 0
        self.highscore = 0
        self.index = 0 
        self.SoCal = ["ANA","PSP","BNS","LAX","BUR","ONT","COM","ORG","CPT","SAN","CXL","SMX","FON","VNS","HBC","WHP","JPD","YUM","JSG"]
        self.NoCal = ["CCR","PET","EUR","RED","HAY","SAC","MLO","SFO","MRY","SJC","STK"]
        self.Desert = ["BKY","GEG","BOI","PHX","CDC","RNO","COS","TRI","DIA","TUC","FLG","UTA","BFL","VEG","VIS","FAT"]
        self.Vancouver = ["VAN","SLE"]
        self.Seattle = ["SEA","SEZ"]
        self.Other = ["TAC","EUG","MED"]
        self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
        self.choice = random.choice(self.fullList)
        
        # This is the GUI 
        # ---------------------------------------
        # This parts makes the frame and for updateing labels 

        self.highscoretext = tk.StringVar()

        self.text = tk.StringVar()

        self.Lives = tk.StringVar()
        self.Lives.set(" You have " + (str(self.lives)) + " Lives left")

        self.pickchoice = tk.StringVar()
        self.pickchoice.set(" Where does this area code belong: " + str(self.choice))

        self.numberscore = tk.StringVar()
        self.numberscore.set("Your Score: " + str(self.score))
        # Main parts of the Gui that you see
        self.Score = tk.Label(self, textvariable=self.numberscore)
        self.Score.pack(side=tk.TOP, pady=1, padx=1)

        self.label3 = tk.Label(self, textvariable=self.Lives)
        self.label3.pack(side=tk.TOP, pady=1, padx=1)

        self.label2 = tk.Label(self, textvariable=self.text)
        self.label2.pack(side=tk.BOTTOM)

        self.label1 = tk.Label(self, textvariable=self.pickchoice)
        self.label1.pack(side=tk.TOP)

        self.socalbutton = tk.Button(self, text="So Cal",width= 10, height= 2 ,command=self.SOCALCHECK)
        self.socalbutton.pack(side=LEFT, pady=2, padx=15)

        self.nocalbutton = tk.Button(self, text="No Cal",width= 10, height= 2 ,command=self.NOCALCHECK)
        self.nocalbutton.pack(side=LEFT, pady=2, padx=15)

        self.nocalbutton = tk.Button(self, text="Desert",width= 10, height= 2 ,command=self.DESERTCHECK)
        self.nocalbutton.pack(side=LEFT, pady=2, padx=15)

        self.nocalbutton = tk.Button(self, text="Seattle",width= 10, height= 2 ,command=self.SEATTLECHECK)
        self.nocalbutton.pack(side=RIGHT, pady=2, padx=15)

        self.nocalbutton = tk.Button(self, text="Vancouver",width= 10, height= 2 ,command=self.VANCOUVERCHECK)
        self.nocalbutton.pack(side=RIGHT, pady=2, padx=15)

        self.nocalbutton = tk.Button(self, text="Other",width= 10, height= 2 ,command=self.OTHERCHECK)
        self.nocalbutton.pack(side=RIGHT, pady=2, padx=15)
        


        # end of GUI
        # -----------------------------------------
    # These are fuctions for checking the answers    
    # These functions will choose a new area code only when you pick the right choice for now  

    def NOCALCHECK (self,):
        answer = self.choice
        if answer in self.NoCal:
            self.score =  self.score + 1
            self.yourscore = self.score 
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")
            self.fullList.remove(answer)
            if self.fullList == []:
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.choice = random.choice(self.fullList)
                self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
                self.controller.show_frame("winwindow")
            else:
                self.choice = random.choice(self.fullList)
                self.pickchoice.set(" Where does this area code belong: " + str(self.choice))         
        else: 
            self.score =  self.score - 1
            if self.score < 0:
                self.score = 0
            self.lives = self.lives - 1
            if self.lives <= 0 or self.fullList == []:
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.currentanswer = answer
                self.lives = 3
                self.score = 0
                if self.lives == 3:
                    self.choice = random.choice(self.fullList)
                    self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
                    self.controller.show_frame("endwindow")
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have " + (str(self.lives)) + " Lives left")
        if self.lives <= 0:
            self.controller.show_frame("endwindow")
            
    def SOCALCHECK (self,):
        answer = self.choice
        if answer in self.SoCal:
            self.score =  self.score + 1
            self.yourscore = self.score 
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")          
            self.fullList.remove(answer)
            if self.fullList == []:
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.choice = random.choice(self.fullList)
                self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
                self.controller.show_frame("winwindow")
            else:
                self.choice = random.choice(self.fullList)
                self.pickchoice.set(" Where does this area code belong: " + str(self.choice))          
        else: 
            self.score =  self.score - 1
            if self.score < 0:
                self.score = 0
            self.lives = self.lives - 1
            if self.lives <= 0 or self.fullList == []:
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.lives = 3
                self.score = 0
                if self.lives == 3:
                    self.choice = random.choice(self.fullList)
                    self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
                    self.controller.show_frame("endwindow")
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have " + (str(self.lives)) + " Lives left")
        if self.lives <= 0:
             self.controller.show_frame("endwindow")
    
    def DESERTCHECK (self):
        answer = self.choice
        if answer in self.Desert:
            self.score =  self.score + 1
            self.yourscore = self.score 
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")
            self.fullList.remove(answer)
            if self.fullList == []:
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.choice = random.choice(self.fullList)
                self.controller.show_frame("winwindow")
            else:
                self.choice = random.choice(self.fullList)
                self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
        else: 
            self.score =  self.score - 1
            if self.score < 0:
                self.score = 0
            self.lives = self.lives - 1
            if self.lives <= 0 or self.fullList == []:
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.lives = 3
                self.score = 0
                self.text.set("")
                if self.lives == 3:
                    self.choice = random.choice(self.fullList)
                    self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
                    self.controller.show_frame("endwindow")
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have " + (str(self.lives)) + " Lives left")
        if self.lives <= 0:
             self.controller.show_frame("endwindow")

    def VANCOUVERCHECK (self):
        answer = self.choice
        if answer in self.Vancouver:
            self.score =  self.score + 1
            self.yourscore = self.score 
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")
            self.fullList.remove(answer)
            if self.fullList == []:
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.choice = random.choice(self.fullList)
                self.controller.show_frame("winwindow")
            else:
                self.choice = random.choice(self.fullList)
                self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
        else: 
            self.score =  self.score - 1
            if self.score < 0:
                self.score = 0
            self.lives = self.lives - 1
            if self.lives <= 0 or self.fullList == []:
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.lives = 3
                self.score = 0
                self.text.set("")
                if self.lives == 3:
                    self.choice = random.choice(self.fullList)
                    self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
                    self.controller.show_frame("endwindow")
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have " + (str(self.lives)) + " Lives left")
        if self.lives <= 0:
             self.controller.show_frame("endwindow")
        
             
    def SEATTLECHECK (self):
        answer = self.choice
        if answer in self.Seattle:
            self.score =  self.score + 1
            self.yourscore = self.score 
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")
            self.fullList.remove(answer)
            if self.fullList == []:
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.choice = random.choice(self.fullList)
                self.controller.show_frame("winwindow")
            else:
                self.choice = random.choice(self.fullList)
                self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
        else: 
            self.score =  self.score - 1
            if self.score < 0:
                self.score = 0
            self.lives = self.lives - 1
            if self.lives <= 0 or self.fullList == []:
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.lives = 3
                self.score = 0
                self.text.set("")
                if self.lives == 3:
                    self.choice = random.choice(self.fullList)
                    self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
                    self.controller.show_frame("endwindow")
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have " + (str(self.lives)) + " Lives left")
        if self.lives <= 0:
             self.controller.show_frame("endwindow")
            
    def OTHERCHECK (self):
        answer = self.choice
        if answer in self.Other:
            self.score =  self.score + 1
            self.yourscore = self.score 
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: correct")
            self.fullList.remove(answer)
            if self.fullList == []:
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.choice = random.choice(self.fullList)
                self.controller.show_frame("winwindow")
            else:
                self.choice = random.choice(self.fullList)
                self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
        else: 
            self.score =  self.score - 1
            if self.score < 0:
                self.score = 0
            self.lives = self.lives - 1
            self.numberscore.set("Your Score: " + str(self.score))
            self.text.set("Your Answer is: not correct")
            self.Lives.set(" You have " + (str(self.lives)) + " Lives left")
            if self.lives <= 0 or self.fullList == []:   
                self.fullList = self.SoCal + self.NoCal + self.Desert + self.Vancouver + self.Seattle + self.Other
                self.lives = 3
                self.score = 0
                if self.lives == 3:
                    self.choice = random.choice(self.fullList)
                    self.text.set("")
                    self.pickchoice.set(" Where does this area code belong: " + str(self.choice))
                    self.controller.show_frame("endwindow")
   

#this is the page after the 3 incorect answers 
class endwindow(tk.Frame):

    def __init__(self,master,controller):
        tk.Frame.__init__(self,master)
        #into = tracgame(master,controller)
        self.controller = controller
        #self.score = into.yourscore
        #self.label2 = tk.Label(self, text="Your score was " + str(self.score))
        self.label1 = tk.Label(self, text="OOPS!!!! you got to many mistake but you can retry")
        self.Button1 = tk.Button(self,text="RETRY",command=lambda: self.controller.show_frame("tracgame"),width=10,height=2,bg="green")
        self.label1.pack()
        #self.label2.pack()
        self.Button1.pack()


#this is the page for getting all of area code
class winwindow(tk.Frame):

    def __init__(self,master,controller):
        tk.Frame.__init__(self,master)
        #into = tracgame(master,controller)
        self.controller = controller
        #self.score = into.yourscore
        #self.label2 = tk.Label(self, text="Your score was " + str(self.score))
        self.label1 = tk.Label(self, text="good job you know all the area codes !!!!!!!!!!!!. You can Continue or Quit")
        self.Button1 = tk.Button(self,text="Continue",command=lambda: self.controller.show_frame("tracgame"),width=10,height=2,bg="green")
        self.Button2 = tk.Button(self, text="Quit",command=self.controller.quit(),width=10,height=2,bg="red")
        self.label1.pack()
        #self.label2.pack()
        self.Button1.pack()
        self.Button2.pack()


# this runs the whole program 
def main():
    app = SampleApp()
    app.geometry("800x400")
    app.mainloop()
if __name__ == '__main__':
    main()