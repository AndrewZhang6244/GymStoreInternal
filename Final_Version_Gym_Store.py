#=========================Imports=====================
import tkinter as tk                
from tkinter import font as tkfont  
from tkinter import *
from tkinter import ttk
from random import *
from tkinter import messagebox
import os
import time
import re
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter import simpledialog
import random
#===================================Main class for managing frames and windows==============================
class Main(tk.Tk):

    def __init__(self, *args, **kwargs): #Initialising attributes of class
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic") #Font
        manager = tk.Frame(self) #Stacking all the classes/windows/frames. 
        manager.pack(side="top", fill="both", expand=True) 
        manager.grid_rowconfigure(0, weight=1) #The weight will increase for the window/frame when it is showing so that it overlaps over the other frames/windows.
        manager.grid_columnconfigure(0, weight=1) #Or in simpler terms, the window that is showing will be raised. 
        self.windows = {} #List for all the windows
        self.windows["home_page"] = home_page( manager=self, parent=manager) #Creates gym_store window
        self.windows["barbells_page"] = barbells_page( manager=self, parent=manager, ) #Creates gym_store window
        self.windows["dumbbells_page"] = dumbbells_page( manager=self, parent=manager) #Creates gym_store window
        self.windows["machines_page"] = machines_page( manager=self, parent=manager) #Creates gym_store window
        self.windows["plates_page"] = plates_page( manager=self, parent=manager) #Creates gym_store window
        self.windows["ordering_page"] = ordering_page( manager=self, parent=manager) #Creates gym_store window

        self.windows["home_page"].grid(row=0, column=0, sticky="nsew")#Geometry manager organising widgets for gym_store 
        self.windows["barbells_page"].grid(row=0, column=0, sticky="nsew")#Geometry manager organising widgets for gym_store 
        self.windows["dumbbells_page"].grid(row=0, column=0, sticky="nsew")#Geometry manager organising widgets for gym_store 
        self.windows["machines_page"].grid(row=0, column=0, sticky="nsew")#Geometry manager organising widgets for gym_store 
        self.windows["plates_page"].grid(row=0, column=0, sticky="nsew")#Geometry manager organising widgets for gym_store 
        self.windows["ordering_page"].grid(row=0, column=0, sticky="nsew")#Geometry manager organising widgets for gym_store 

        self.show_window("home_page") #Show home page window
    def show_window(self, page_name): #Show_window method 
        window = self.windows[page_name] 
        window.tkraise() #Raises the window to make the desired window to be on top of all the others(shows window).
    def exit(self):
        exityesorno = messagebox.askquestion("Quit", "Are you sure you would like to exit the program?")
        if exityesorno == "yes":
            app.destroy()
        else:
            return

#=========================================Home page for the gym store=======================================
class home_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        home_top_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue") #Top border for the banner
        home_top_border.pack(side=TOP)
        self.TitleImage = PhotoImage(file="images/GymHomeBanner.png")  #Banner for the home page
        self.title_label = tk.Label(self, image=self.TitleImage, bd=3).pack(side=TOP)

        
        home_bottom_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue")
        home_bottom_border.pack(side=TOP) #Bottom border for the banner
       

        FrameOne = tk.Frame(self, width = 440, height = 650, bd = 8, relief = "raise", background = "light blue")
        FrameOne.pack(side=LEFT) #First frame for the design
        self.FrameTwo = tk.Frame(self, width = 900, height = 350, bd = 8, relief ="raise", background = "light blue")
        self.FrameTwo.pack(side=RIGHT) #Second frame for the design
        FrameTwoFront = tk.Label(self.FrameTwo, width = 60, height = 540, bd = 8,text = "Welcome to our gym store, to use this \nprogram, click on the desired windows shown\n to the left and tick the items you would like to buy.\n Once you have ticked the items, please enter\n the number of items you would like to buy\n and then proceed to the finish ordering window \nwhere you can find your receipt and the total price. \nIf you have chosen the delivery option, please enter\n your delivery address." ,relief = "raise", background = "light blue",font=('Helvactical bold', 20))
        FrameTwoFront.pack(side=RIGHT)  #Frame ontop of second frame.
       
        home_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Home", command = lambda:manager.show_window("home_page"))
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Barbells", command = lambda:manager.show_window("barbells_page")) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Dumbbells", command = lambda:manager.show_window("dumbbells_page")) 
        dumbbells_button.pack(side=TOP) #Dumbbells button
        machines_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Machines", command = lambda:manager.show_window("machines_page")) 
        machines_button.pack(side=TOP) #Machines button
        plates_button = tk.Button(FrameOne, width = 47, height =3, bd = 12, relief = "raise", background = "light blue", text = "Plates", command = lambda:manager.show_window("plates_page")) 
        plates_button.pack(side=TOP) #Plates button
        ordering_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Finish Ordering", command = lambda:manager.show_window("ordering_page")) 
        ordering_button.pack(side=TOP) #Ordering button.
        exit_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Exit", command = manager.exit) 
        exit_button.pack(side=TOP)#Exit button
#=======================================================Barbells page====================================
class barbells_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        barbells_top_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue")
        barbells_top_border.place(x=0,y=0) #Barbells top border
        self.TitleImage = PhotoImage(file="images/GymHomeBanner.png") 
        self.title_label = tk.Label(self, image=self.TitleImage, bd=3).place(x=0, y=56) #Banner for barbells
        barbells_bottom_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue")
        barbells_bottom_border.place(x=0, y=156) #Barbells bottom border 
    
        self.TitleImage2 = PhotoImage(file="images/barbellbanner.png") #Barbells banner
        self.title_label2 = tk.Label(self, image=self.TitleImage2, bd=3).place(x=365, y=215)
        FrameOne = tk.Frame(self, width = 500, height = 650, bd = 8, relief = "raise", background = "light blue")
        FrameOne.place(x=0, y=215) #First  frame
        self.FrameTwo = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        self.FrameTwo.place(x=374, y=420) #Second frame
        self.FrameThree = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        self.FrameThree.place(x=960, y=420) #Third frame
        FrameFour = tk.Frame(self, width = 180, height = 359, bd = 8, relief ="raise", background = "light blue")
        FrameFour.place(x=780, y=420) #Fourth frame

       
        home_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Home", command = lambda:manager.show_window("home_page"))
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Barbells", command = lambda:manager.show_window("barbells_page")) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Dumbbells", command = lambda:manager.show_window("dumbbells_page")) 
        dumbbells_button.pack(side=TOP)#Dumbells button
        machines_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Machines", command = lambda:manager.show_window("machines_page")) 
        machines_button.pack(side=TOP)#Machines button
        plates_button = tk.Button(FrameOne, width = 47, height =3, bd = 12, relief = "raise", background = "light blue", text = "Plates", command = lambda:manager.show_window("plates_page")) 
        plates_button.pack(side=TOP)#Plates button
        ordering_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Finish Ordering", command = lambda:manager.show_window("ordering_page")) 
        ordering_button.pack(side=TOP)#Ordering button
        exit_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Exit", command = manager.exit) 
        exit_button.pack(side=TOP)#Exit button
        #===============================================================Variables===================================

        self.ItemVar = {checkbutton: IntVar() for checkbutton in range(0, 17, 1)}
        
        self.barbells = {weight: StringVar() for weight in range(5, 85, 5)}
        barbell_items = [self.barbells[5], self.barbells[10],self.barbells[15],self.barbells[20],self.barbells[25],self.barbells[30],self.barbells[35],self.barbells[40],self.barbells[45], self.barbells[50], self.barbells[55],self.barbells[60],self.barbells[65],self.barbells[70],self.barbells[75],self.barbells[80]]
        for i in barbell_items:
            i.set("0")
        #===================================================Widgets for barbell items===========================================
        #===================================================First section for barbell items=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Barbells 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        fivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 5kgs ($15.00)\t\t" ,variable = self.ItemVar[1],command = self.barbell_checked_checkbuttons, onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        tenkgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 10kgs ($30.00) " , variable = self.ItemVar[2],command = self.barbell_checked_checkbuttons, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fifteenkgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 15kgs ($45.00)" , variable = self.ItemVar[3], command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        twentykgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 20kgs ($60.00) ", variable = self.ItemVar[4], command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        twentyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 25kg ($75.00) ",variable = self.ItemVar[5],command = self.barbell_checked_checkbuttons, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        thirtykgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 30kgs ($90.00) ",variable = self.ItemVar[6], command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        thirtyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 35kgs ($105.00) ", variable = self.ItemVar[7],command = self.barbell_checked_checkbuttons, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        fourtykgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 40kgs ($120.00) ", variable = self.ItemVar[8], command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fivekgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.barbells[5], state = DISABLED)
        self.fivekgs_barbell_entry.grid(row =1, column = 1)
        self.tenkgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable =  self.barbells[10], state = DISABLED)
        self.tenkgs_barbell_entry.grid(row =2, column = 1)
        self.fifteenkgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable =  self.barbells[15], state = DISABLED)
        self.fifteenkgs_barbell_entry.grid(row =3, column = 1)
        self.twentykgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable =  self.barbells[20], state = DISABLED)
        self.twentykgs_barbell_entry.grid(row =4, column = 1)
        self.twentyfivekgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable =  self.barbells[25], state = DISABLED)
        self.twentyfivekgs_barbell_entry.grid(row =5, column = 1)
        self.thirtykgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable =  self.barbells[30] ,state = DISABLED)
        self.thirtykgs_barbell_entry.grid(row =6, column = 1)
        self.thirtyfivekgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable =  self.barbells[35], state = DISABLED)
        self.thirtyfivekgs_barbell_entry.grid(row =7, column = 1)
        self.fourtykgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable =  self.barbells[40], state = DISABLED)
        self.fourtykgs_barbell_entry.grid(row =8, column = 1)
        #=====================================================================Second section for barbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Barbells 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 45kgs ($135.00) \t\t", variable = self.ItemVar[9], command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        fiftykgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 50kgs ($150.00) \t", variable = self.ItemVar[10], command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fiftyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 55kgs ($165.00) \t", variable = self.ItemVar[11], command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        sixtykgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 60kgs ($180.00)\t", variable = self.ItemVar[12],command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        sixtyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 65kgs ($195.00) \t", variable = self.ItemVar[13],command = self.barbell_checked_checkbuttons, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        seventyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 70kgs ($210.00) \t", variable = self.ItemVar[14], command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        seventyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 75kgs ($225.00) \t", variable = self.ItemVar[15],command = self.barbell_checked_checkbuttons, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        eightykgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 80kgs ($240.00) \t",variable = self.ItemVar[16], command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fourtyfivekgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.barbells[45], state = DISABLED)
        self.fourtyfivekgs_barbell_entry.grid(row =1, column = 1)
        self.fiftykgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =  self.barbells[50], state = DISABLED)
        self.fiftykgs_barbell_entry.grid(row=2, column=1)
        self.fiftyfivekgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.barbells[55], state = DISABLED)
        self.fiftyfivekgs_barbell_entry.grid(row =3, column = 1)
        self.sixtykgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.barbells[60], state = DISABLED)
        self.sixtykgs_barbell_entry.grid(row =4, column = 1)
        self.sixtyfivekgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =  self.barbells[65], state = DISABLED)
        self.sixtyfivekgs_barbell_entry.grid(row =5, column = 1)
        self.seventykgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =  self.barbells[70], state = DISABLED)
        self.seventykgs_barbell_entry.grid(row =6, column = 1)
        self.seventyfivekgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =  self.barbells[75], state = DISABLED)
        self.seventyfivekgs_barbell_entry.grid(row =7, column = 1)
        self.eightykgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable =  self.barbells[80], state = DISABLED)
        self.eightykgs_barbell_entry.grid(row =8, column = 1)  
        
        
    def barbell_checked_checkbuttons(self):
        if (self.ItemVar[1].get()==1):
            self.fivekgs_barbell_entry.config(state = NORMAL)
        elif self.ItemVar[1].get()==0:
            self.fivekgs_barbell_entry.configure(state=DISABLED)
            self.barbells[5].set("0")
        if (self.ItemVar[2].get()==1):
            self.tenkgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[2].get()==0:
            self.tenkgs_barbell_entry.configure(state=DISABLED)
            self.barbells[10].set("0")
        if (self.ItemVar[3].get()==1):
            self.fifteenkgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[3].get()==0:
            self.fifteenkgs_barbell_entry.configure(state=DISABLED)
            self.barbells[15].set("0")
        if (self.ItemVar[4].get()==1):
            self.twentykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[4].get()==0:
            self.twentykgs_barbell_entry.configure(state=DISABLED)
            self.barbells[20].set("0")
        if (self.ItemVar[5].get()==1):
            self.twentyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[5].get()==0:
            self.twentyfivekgs_barbell_entry.configure(state=DISABLED)
            self.barbells[25].set("0")
        if (self.ItemVar[6].get()==1):
            self.thirtykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[6].get()==0:
            self.thirtykgs_barbell_entry.configure(state=DISABLED)
            self.barbells[30].set("0")
        if (self.ItemVar[7].get()==1):
            self.thirtyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[7].get()==0:
            self.thirtyfivekgs_barbell_entry.configure(state=DISABLED)
            self.barbells[35].set("0")
        if (self.ItemVar[8].get()==1):
            self.fourtykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[8].get()==0:
            self.fourtykgs_barbell_entry.configure(state=DISABLED)
            self.barbells[40].set("0")
        if (self.ItemVar[9].get()==1):
            self.fourtyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[9].get()==0:
            self.fourtyfivekgs_barbell_entry.configure(state=DISABLED)
            self.barbells[45].set("0")
        if (self.ItemVar[10].get()==1):
            self.fiftykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[10].get()==0:
            self.fiftykgs_barbell_entry.configure(state=DISABLED)
            self.barbells[50].set("0")
        if (self.ItemVar[11].get()==1):
            self.fiftyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[11].get()==0:
            self.fiftyfivekgs_barbell_entry.configure(state=DISABLED)
            self.barbells[55].set("0")
        if (self.ItemVar[12].get()==1):
            self.sixtykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[12].get()==0:
            self.sixtykgs_barbell_entry.configure(state=DISABLED)
            self.barbells[60].set("0")
        if (self.ItemVar[13].get()==1):
            self.sixtyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[13].get()==0:
            self.sixtyfivekgs_barbell_entry.configure(state=DISABLED)
            self.barbells[65].set("0")
        if (self.ItemVar[14].get()==1):
            self.seventykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[14].get()==0:
            self.seventykgs_barbell_entry.configure(state=DISABLED)
            self.barbells[70].set("0")
        if (self.ItemVar[15].get()==1):
            self.seventyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[15].get()==0:
            self.seventyfivekgs_barbell_entry.configure(state=DISABLED)
            self.barbells[75].set("0")
        if (self.ItemVar[16].get()==1):
            self.eightykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar[16].get()==0:
            self.eightykgs_barbell_entry.configure(state=DISABLED)
            self.barbells[80].set("0")
    
        
#======================================================Dumbells page===================================
class dumbbells_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        dumbbells_top_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue")
        dumbbells_top_border.place(x=0,y=0) #dumbbells top border
        self.TitleImage = PhotoImage(file="images/GymHomeBanner.png") 
        self.title_label = tk.Label(self, image=self.TitleImage, bd=3).place(x=0, y=56) #Banner for dumbbells
        dumbbells_bottom_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue")
        dumbbells_bottom_border.place(x=0, y=156) #dumbbells bottom border 
       
        self.TitleImage2 = PhotoImage(file="images/dumbbellsbanner.png") #Dumbbells banner
        self.title_label2 = tk.Label(self, image=self.TitleImage2, bd=3).place(x=365, y=215)
        FrameOne = tk.Frame(self, width = 500, height = 650, bd = 8, relief = "raise", background = "light blue")
        FrameOne.place(x=0, y=215) #First  frame
        self.FrameTwo = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        self.FrameTwo.place(x=374, y=403) #Second frame
        self.FrameThree = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        self.FrameThree.place(x=960, y=403) #Third frame
        FrameFour = tk.Frame(self, width = 180, height = 359, bd = 8, relief ="raise", background = "light blue")
        FrameFour.place(x=780, y=403) #Fourth frame

       
        home_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Home", command = lambda:manager.show_window("home_page"))
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Barbells", command = lambda:manager.show_window("barbells_page")) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Dumbbells", command = lambda:manager.show_window("dumbbells_page")) 
        dumbbells_button.pack(side=TOP)#Dumbells button
        machines_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Machines", command = lambda:manager.show_window("machines_page")) 
        machines_button.pack(side=TOP)#Machines button
        plates_button = tk.Button(FrameOne, width = 47, height =3, bd = 12, relief = "raise", background = "light blue", text = "Plates", command = lambda:manager.show_window("plates_page")) 
        plates_button.pack(side=TOP)#Plates button
        ordering_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Finish Ordering", command = lambda:manager.show_window("ordering_page")) 
        ordering_button.pack(side=TOP)#Ordering button
        exit_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Exit", command = manager.exit) 
        exit_button.pack(side=TOP)#Exit button
        #===============================================================Variables===================================
        
        
        self.ItemVar = {checkbutton: IntVar() for checkbutton in range(16, 33, 1)}
        
        self.dumbbells = {weight: StringVar() for weight in range(5, 85, 5)}
        dumbbell_items = [self.dumbbells[5], self.dumbbells[10],self.dumbbells[15],self.dumbbells[20],self.dumbbells[25],self.dumbbells[30],self.dumbbells[35],self.dumbbells[40],self.dumbbells[45], self.dumbbells[50], self.dumbbells[55],self.dumbbells[60],self.dumbbells[65],self.dumbbells[70],self.dumbbells[75],self.dumbbells[80]]
        for i in dumbbell_items:
            i.set("0")
        #===================================================Widgets for dumbbell items===========================================
        #===================================================First section for dumbell items=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Dumbbells 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        fivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 5kgs ($10.00)\t\t" ,command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar[17], onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        tenkgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 10kgs ($20.00) " , command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar[18], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fifteenkgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 15kgs ($30.00) " ,command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar[19], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        twentykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 20kgs ($40.00) ",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar[20], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        twentyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 25kgs ($50.00) ",command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar[21], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        thirtykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 30kgs ($60.00) ",command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar[22], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        thirtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 35kgs ($70.00) ", command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar[23], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        fourtykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 40kgs ($80.00) ",command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar[24], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fivekgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.dumbbells[5], state = DISABLED)
        self.fivekgs_dumbbell_entry.grid(row =1, column = 1)
        self.tenkgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.dumbbells[10], state = DISABLED)
        self.tenkgs_dumbbell_entry.grid(row =2, column = 1)
        self.fifteenkgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.dumbbells[15], state = DISABLED)
        self.fifteenkgs_dumbbell_entry.grid(row =3, column = 1)
        self.twentykgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.dumbbells[20], state = DISABLED)
        self.twentykgs_dumbbell_entry.grid(row =4, column = 1)
        self.twentyfivekgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.dumbbells[25], state = DISABLED)
        self.twentyfivekgs_dumbbell_entry.grid(row =5, column = 1)
        self.thirtykgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.dumbbells[30] ,state = DISABLED)
        self.thirtykgs_dumbbell_entry.grid(row =6, column = 1)
        self.thirtyfivekgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.dumbbells[35], state = DISABLED)
        self.thirtyfivekgs_dumbbell_entry.grid(row =7, column = 1)
        self.fourtykgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable = self.dumbbells[40], state = DISABLED)
        self.fourtykgs_dumbbell_entry.grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Dumbbells 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 45kgs ($90.00)\t\t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar[25], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        fiftykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 50kgs ($100.00)\t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar[26], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fiftyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 55kgs ($110.00)\t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar[27], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        sixtykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 60kgs ($120.00)\t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar[28], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        sixtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 65kgs ($130.00) \t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar[29], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        seventyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 70kgs ($140.00) \t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar[30], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        seventyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 75kgs ($150.00) \t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar[31], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        eightykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 80kgs ($160.00) \t",command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar[32], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fourtyfivekgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.dumbbells[45], state = DISABLED)
        self.fourtyfivekgs_dumbbell_entry.grid(row =1, column = 1)
        self.fiftykgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.dumbbells[50], state = DISABLED)
        self.fiftykgs_dumbbell_entry.grid(row =2, column = 1)
        self.fiftyfivekgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.dumbbells[55], state = DISABLED)
        self.fiftyfivekgs_dumbbell_entry.grid(row =3, column = 1)
        self.sixtykgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.dumbbells[60], state = DISABLED)
        self.sixtykgs_dumbbell_entry.grid(row =4, column = 1)
        self.sixtyfivekgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.dumbbells[65], state = DISABLED)
        self.sixtyfivekgs_dumbbell_entry.grid(row =5, column = 1)
        self.seventykgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.dumbbells[70], state = DISABLED)
        self.seventykgs_dumbbell_entry.grid(row =6, column = 1)
        self.seventyfivekgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.dumbbells[75], state = DISABLED)
        self.seventyfivekgs_dumbbell_entry.grid(row =7, column = 1)
        self.eightykgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable = self.dumbbells[80], state = DISABLED)
        self.eightykgs_dumbbell_entry.grid(row =8, column = 1)   
    def dumbbell_checked_checkbuttons(self):
        if (self.ItemVar[17].get()==1):
            self.fivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[17].get()==0:
            self.fivekgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[5].set("0")
        if (self.ItemVar[18].get()==1):
            self.tenkgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[18].get()==0:
            self.tenkgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[10].set("0")
        if (self.ItemVar[19].get()==1):
            self.fifteenkgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[19].get()==0:
            self.fifteenkgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[15].set("0")
        if (self.ItemVar[20].get()==1):
            self.twentykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[20].get()==0:
            self.twentykgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[20].set("0")
        if (self.ItemVar[21].get()==1):
            self.twentyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[21].get()==0:
            self.twentyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[25].set("0")
        if (self.ItemVar[22].get()==1):
            self.thirtykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[22].get()==0:
            self.thirtykgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[30].set("0")
        if (self.ItemVar[23].get()==1):
            self.thirtyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[23].get()==0:
            self.thirtyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[35].set("0")
        if (self.ItemVar[24].get()==1):
            self.fourtykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[24].get()==0:
            self.fourtykgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[40].set("0")
        if (self.ItemVar[25].get()==1):
            self.fourtyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[25].get()==0:
            self.fourtyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[45].set("0")
        if (self.ItemVar[26].get()==1):
            self.fiftykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[26].get()==0:
            self.fiftykgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[50].set("0")
        if (self.ItemVar[27].get()==1):
            self.fiftyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[27].get()==0:
            self.fiftyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[55].set("0")
        if (self.ItemVar[28].get()==1):
            self.sixtykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[28].get()==0:
            self.sixtykgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[60].set("0")
        if (self.ItemVar[29].get()==1):
            self.sixtyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[29].get()==0:
            self.sixtyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[65].set("0")
        if (self.ItemVar[30].get()==1):
            self.seventykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[30].get()==0:
            self.seventykgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[70].set("0")
        if (self.ItemVar[31].get()==1):
            self.seventyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[31].get()==0:
            self.seventyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[75].set("0")
        if (self.ItemVar[32].get()==1):
            self.eightykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar[32].get()==0:
            self.eightykgs_dumbbell_entry.configure(state=DISABLED)
            self.dumbbells[80].set("0")
#======================================================Machines page=======================================
class machines_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        machines_top_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue")
        machines_top_border.place(x=0,y=0) #Machines top border
        self.TitleImage = PhotoImage(file="images/GymHomeBanner.png") 
        self.title_label = tk.Label(self, image=self.TitleImage, bd=3).place(x=0, y=56) #Banner for welcoming
        machines_bottom_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue")
        machines_bottom_border.place(x=0, y=156) #Machines bottom border
       
        self.TitleImage2 = PhotoImage(file="images/machinesbanner.png") #Machines banner
        self.title_label2 = tk.Label(self, image=self.TitleImage2, bd=3).place(x=365, y=215)
        FrameOne = tk.Frame(self, width = 500, height = 650, bd = 8, relief = "raise", background = "light blue")
        FrameOne.place(x=0, y=215) #First  frame
        self.FrameTwo = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        self.FrameTwo.place(x=374, y=403) #Second frame
        self.FrameThree = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        self.FrameThree.place(x=960, y=403) #Third frame
        FrameFour = tk.Frame(self, width = 180, height = 359, bd = 8, relief ="raise", background = "light blue")
        FrameFour.place(x=780, y=403) #Fourth frame

        home_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Home", command = lambda:manager.show_window("home_page"))
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Barbells", command = lambda:manager.show_window("barbells_page")) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Dumbbells", command = lambda:manager.show_window("dumbbells_page")) 
        dumbbells_button.pack(side=TOP)#Dumbells button
        machines_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Machines", command = lambda:manager.show_window("machines_page")) 
        machines_button.pack(side=TOP)#Machines button
        plates_button = tk.Button(FrameOne, width = 47, height =3, bd = 12, relief = "raise", background = "light blue", text = "Plates", command = lambda:manager.show_window("plates_page")) 
        plates_button.pack(side=TOP)#Plates button
        ordering_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Finish Ordering", command = lambda:manager.show_window("ordering_page")) 
        ordering_button.pack(side=TOP)#Ordering button
        exit_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Exit", command = manager.exit) 
        exit_button.pack(side=TOP)#Exit button
        #===============================================================Variables===================================
       
        self.ItemVar = {checkbutton: IntVar() for checkbutton in range(32, 49, 1)}
        
        self.machines = {weight: StringVar() for weight in range(0, 17, 1)}
        machine_items = [self.machines[1] ,self.machines[2] ,self.machines[3] ,self.machines[4] ,self.machines[5],self.machines[6],self.machines[7],self.machines[8],self.machines[9],self.machines[10] ,self.machines[11] ,self.machines[12],self.machines[13] ,self.machines[14] ,self.machines[15],self.machines[16]]
        for i in machine_items:
            i.set("0")
        #===================================================Widgets for machiness==========================================
        #===================================================First section for machines=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Machines 1: ",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0) 
        treadmill_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Treadmill ($900.00)\t\t" ,command = self.machines_checked_checkbuttons,variable = self.ItemVar[33], onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        chestpress_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Chest press ($1000.00)" ,command = self.machines_checked_checkbuttons, variable = self.ItemVar[34], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        pecfly_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Pecfly ($800.00)" , command = self.machines_checked_checkbuttons,variable = self.ItemVar[35], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        seatedrow_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Seated row ($750.00)", command = self.machines_checked_checkbuttons,variable = self.ItemVar[36], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        latpulldown_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Lat pull down ($900.00)",command = self.machines_checked_checkbuttons,variable = self.ItemVar[37], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        ergometer_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Ergometer ($800.00)",command = self.machines_checked_checkbuttons,variable = self.ItemVar[38], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        stairmaster_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Stairmaster ($2000.00)", command = self.machines_checked_checkbuttons,variable = self.ItemVar[39], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        smithmachine_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Smithmachine ($700.00)", command = self.machines_checked_checkbuttons,variable = self.ItemVar[40], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.treadmill_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.machines[1], state = DISABLED)
        self.treadmill_entry.grid(row =1, column = 1)
        self.chestpress_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.machines[2], state = DISABLED)
        self.chestpress_entry.grid(row =2, column = 1)
        self.pecfly_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.machines[3], state = DISABLED)
        self.pecfly_entry.grid(row =3, column = 1)
        self.seatedrow_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.machines[4], state = DISABLED)
        self.seatedrow_entry.grid(row =4, column = 1)
        self.latpulldown_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.machines[5], state = DISABLED)
        self.latpulldown_entry.grid(row =5, column = 1)
        self.ergometer_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.machines[6] ,state = DISABLED)
        self.ergometer_entry.grid(row =6, column = 1)
        self.stairmaster_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.machines[7], state = DISABLED)
        self.stairmaster_entry.grid(row =7, column = 1)
        self.smithmachine_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable = self.machines[8], state = DISABLED)
        self.smithmachine_entry.grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Machines 2: ",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        row_checkbutton = tk.Checkbutton(self.FrameThree, text ="Ab crunch ($650.00)\t\t",command = self.machines_checked_checkbuttons, variable = self.ItemVar[41], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        legextension_checkbutton = tk.Checkbutton(self.FrameThree, text ="Leg extension ($970.00)\t", command = self.machines_checked_checkbuttons,variable = self.ItemVar[42], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        legpress_checkbutton = tk.Checkbutton(self.FrameThree, text ="Leg press ($1300.00)\t",command = self.machines_checked_checkbuttons, variable = self.ItemVar[43], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        elliptical_checkbutton = tk.Checkbutton(self.FrameThree, text ="Elliptical ($1200.00)\t",command = self.machines_checked_checkbuttons, variable = self.ItemVar[44], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        standingcalfraise_checkbutton = tk.Checkbutton(self.FrameThree, text ="Standing calf raise ($740.00)\t",command = self.machines_checked_checkbuttons, variable = self.ItemVar[45], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        shoulderpress_checkbutton = tk.Checkbutton(self.FrameThree, text ="Shoulder press ($1100.00)\t", command = self.machines_checked_checkbuttons,variable = self.ItemVar[46], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        legcurls_checkbutton = tk.Checkbutton(self.FrameThree, text ="Leg curls ($1600.00)\t", command = self.machines_checked_checkbuttons,variable = self.ItemVar[47], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        deltoidraise_checkbutton = tk.Checkbutton(self.FrameThree, text ="Deltoid raise ($840.00)\t",command = self.machines_checked_checkbuttons,variable = self.ItemVar[48], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.abcrunch_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.machines[9], state = DISABLED)
        self.abcrunch_entry.grid(row =1, column = 1)
        self.legextension_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.machines[10], state = DISABLED)
        self.legextension_entry.grid(row =2, column = 1)
        self.legpress_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.machines[11], state = DISABLED)
        self.legpress_entry.grid(row =3, column = 1)
        self.elliptical_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.machines[12], state = DISABLED)
        self.elliptical_entry.grid(row =4, column = 1)
        self.standingcalfraise_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.machines[13], state = DISABLED)
        self.standingcalfraise_entry.grid(row =5, column = 1)
        self.shoulderpress_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.machines[14], state = DISABLED)
        self.shoulderpress_entry.grid(row =6, column = 1)
        self.legcurls_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.machines[15], state = DISABLED)
        self.legcurls_entry.grid(row =7, column = 1)
        self.deltoidraise_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable = self.machines[16], state = DISABLED)
        self.deltoidraise_entry.grid(row =8, column = 1)   
    def machines_checked_checkbuttons(self):
        if (self.ItemVar[33].get()==1):
            self.treadmill_entry.configure(state="normal")
        elif self.ItemVar[33].get()==0:
            self.treadmill_entry.configure(state=DISABLED)
            self.machines[1].set("0")
        if (self.ItemVar[34].get()==1):
            self.chestpress_entry.configure(state="normal")
        elif self.ItemVar[34].get()==0:
            self.chestpress_entry.configure(state=DISABLED)
            self.machines[2].set("0")
        if (self.ItemVar[35].get()==1):
            self.pecfly_entry.configure(state="normal")
        elif self.ItemVar[35].get()==0:
            self.pecfly_entry.configure(state=DISABLED)
            self.machines[3].set("0")
        if (self.ItemVar[36].get()==1):
            self.seatedrow_entry.configure(state="normal")
        elif self.ItemVar[36].get()==0:
            self.seatedrow_entry.configure(state=DISABLED)
            self.machines[4].set("0")
        if (self.ItemVar[37].get()==1):
            self.latpulldown_entry.configure(state="normal")
        elif self.ItemVar[37].get()==0:
            self.latpulldown_entry.configure(state=DISABLED)
            self.machines[5].set("0")
        if (self.ItemVar[38].get()==1):
            self.ergometer_entry.configure(state="normal")
        elif self.ItemVar[38].get()==0:
            self.ergometer_entry.configure(state=DISABLED)
            self.machines[6].set("0")
        if (self.ItemVar[39].get()==1):
            self.stairmaster_entry.configure(state="normal")
        elif self.ItemVar[39].get()==0:
            self.stairmaster_entry.configure(state=DISABLED)
            self.machines[7].set("0")
        if (self.ItemVar[40].get()==1):
            self.smithmachine_entry.configure(state="normal")
        elif self.ItemVar[40].get()==0:
            self.smithmachine_entry.configure(state=DISABLED)
            self.machines[8].set("0")
        if (self.ItemVar[41].get()==1):
            self.abcrunch_entry.configure(state="normal")
        elif self.ItemVar[41].get()==0:
            self.abcrunch_entry.configure(state=DISABLED)
            self.machines[9].set("0")
        if (self.ItemVar[42].get()==1):
            self.legextension_entry.configure(state="normal")
        elif self.ItemVar[42].get()==0:
            self.legextension_entry.configure(state=DISABLED)
            self.machines[10].set("0")
        if (self.ItemVar[43].get()==1):
            self.legpress_entry.configure(state="normal")
        elif self.ItemVar[43].get()==0:
            self.legpress_entry.configure(state=DISABLED)
            self.machines[11].set("0")
        if (self.ItemVar[44].get()==1):
            self.elliptical_entry.configure(state="normal")
        elif self.ItemVar[44].get()==0:
            self.elliptical_entry.configure(state=DISABLED)
            self.machines[12].set("0")
        if (self.ItemVar[45].get()==1):
            self.standingcalfraise_entry.configure(state="normal")
        elif self.ItemVar[45].get()==0:
            self.standingcalfraise_entry.configure(state=DISABLED)
            self.machines[13].set("0")
        if (self.ItemVar[46].get()==1):
            self.shoulderpress_entry.configure(state="normal")
        elif self.ItemVar[46].get()==0:
            self.shoulderpress_entry.configure(state=DISABLED)
            self.machines[14].set("0")
        if (self.ItemVar[47].get()==1):
            self.legcurls_entry.configure(state="normal")
        elif self.ItemVar[47].get()==0:
            self.legcurls_entry.configure(state=DISABLED)
            self.machines[15].set("0")
        if (self.ItemVar[48].get()==1):
            self.deltoidraise_entry.configure(state="normal")
        elif self.ItemVar[48].get()==0:
            self.deltoidraise_entry.configure(state=DISABLED)
            self.machines[16].set("0")
#=====================================================Weight plates page=====================================
class plates_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        plates_top_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue")
        plates_top_border.place(x=0,y=0) #Plates top border
        self.TitleImage = PhotoImage(file="images/GymHomeBanner.png") #Banner for home page
        self.title_label = tk.Label(self, image=self.TitleImage, bd=3).place(x=0, y=56) 
        plates_bottom_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue")
        plates_bottom_border.place(x=0, y=156) #Plates bottom border 
       
        self.TitleImage2 = PhotoImage(file="images/platesbanner.png") #Plates banner
        self.title_label2 = tk.Label(self, image=self.TitleImage2, bd=3).place(x=365, y=215)
        FrameOne = tk.Frame(self, width = 500, height = 650, bd = 8, relief = "raise", background = "light blue")
        FrameOne.place(x=0, y=215) #First  frame
        self.FrameTwo = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        self.FrameTwo.place(x=374, y=403) #Second frame
        self.FrameThree = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        self.FrameThree.place(x=960, y=403) #Third frame
        FrameFour = tk.Frame(self, width = 180, height = 359, bd = 8, relief ="raise", background = "light blue")
        FrameFour.place(x=780, y=403) #Fourth frame

       
        home_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Home", command = lambda:manager.show_window("home_page"))
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Barbells", command = lambda:manager.show_window("barbells_page")) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Dumbbells", command = lambda:manager.show_window("dumbbells_page")) 
        dumbbells_button.pack(side=TOP)#Dumbells button
        machines_button = tk.Button(FrameOne, width = 47, height =3, bd = 12, relief = "raise", background = "light blue", text = "Machines", command = lambda:manager.show_window("machines_page")) 
        machines_button.pack(side=TOP)#Machines button
        plates_button = tk.Button(FrameOne, width = 47, height =3, bd = 12, relief = "raise", background = "light blue", text = "Plates", command = lambda:manager.show_window("plates_page")) 
        plates_button.pack(side=TOP)#Plates button
        ordering_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Finish Ordering", command = lambda:manager.show_window("ordering_page")) 
        ordering_button.pack(side=TOP)#Ordering button
        exit_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Exit", command = manager.exit) 
        exit_button.pack(side=TOP)#Exit button
        #===============================================================Variables===================================
         
        self.ItemVar = {checkbutton: IntVar() for checkbutton in range(48, 65, 1)}
        self.plates = {weight: StringVar() for weight in range(5, 85, 5)}
        plate_items = [self.plates[5], self.plates[10],self.plates[15],self.plates[20],self.plates[25],self.plates[30],self.plates[35],self.plates[40],self.plates[45], self.plates[50], self.plates[55],self.plates[60],self.plates[65],self.plates[70],self.plates[75],self.plates[80]]
        for i in plate_items:
            i.set("0")
        #===================================================Widgets for plate items===========================================
        #===================================================First section for plate items=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Plates 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        fivekgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 5kgs ($10.00)\t\t" , command = self.plate_checked_checkbuttons,variable = self.ItemVar[49], onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        tenkgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 10kgs ($20.00)" , command = self.plate_checked_checkbuttons,variable = self.ItemVar[50], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fifteenkgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 15kgs ($30.00)" , command = self.plate_checked_checkbuttons,variable = self.ItemVar[51], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        twentykgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 20kgs ($40.00)", command = self.plate_checked_checkbuttons,variable = self.ItemVar[52], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        twentyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 25kgs ($50.00)",command = self.plate_checked_checkbuttons,variable = self.ItemVar[53], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        thirtykgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 30kgs ($60.00)",command = self.plate_checked_checkbuttons,variable = self.ItemVar[54], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        thirtyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 35kgs ($70.00)", command = self.plate_checked_checkbuttons,variable = self.ItemVar[55], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        fourtykgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 40kgs ($80.00)",command = self.plate_checked_checkbuttons, variable = self.ItemVar[56], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fivekgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[5], state = DISABLED)
        self.fivekgs_plate_entry.grid(row =1, column = 1)
        self.tenkgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[10], state = DISABLED)
        self.tenkgs_plate_entry.grid(row =2, column = 1)
        self.fifteenkgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable =self.plates[15], state = DISABLED)
        self.fifteenkgs_plate_entry.grid(row =3, column = 1)
        self.twentykgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[20], state = DISABLED)
        self.twentykgs_plate_entry.grid(row =4, column = 1)
        self.twentyfivekgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[25], state = DISABLED)
        self.twentyfivekgs_plate_entry.grid(row =5, column = 1)
        self.thirtykgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[30] ,state = DISABLED)
        self.thirtykgs_plate_entry.grid(row =6, column = 1)
        self.thirtyfivekgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[35], state = DISABLED)
        self.thirtyfivekgs_plate_entry.grid(row =7, column = 1)
        self.fourtykgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable = self.plates[40], state = DISABLED)
        self.fourtykgs_plate_entry.grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Plates 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 45kgs ($90.00)\t\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar[57], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        fiftykgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 50kgs ($100.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar[58], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fiftyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 55kgs ($110.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar[59], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        sixtykgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 60kgs ($120.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar[60], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        sixtyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 65kgs ($130.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar[61], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        seventyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 70kgs ($140.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar[62], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        seventyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 75kgs ($150.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar[63], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        eightykgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 80kgs ($160.00)\t",command = self.plate_checked_checkbuttons,variable = self.ItemVar[64], onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fourtyfivekgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.plates[45], state = DISABLED)
        self.fourtyfivekgs_plate_entry.grid(row =1, column = 1)
        self.fiftykgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.plates[50], state = DISABLED)
        self.fiftykgs_plate_entry.grid(row =2, column = 1)
        self.fiftyfivekgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.plates[55], state = DISABLED)
        self.fiftyfivekgs_plate_entry.grid(row =3, column = 1)
        self.sixtykgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.plates[60], state = DISABLED)
        self.sixtykgs_plate_entry.grid(row =4, column = 1)
        self.sixtyfivekgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.plates[65], state = DISABLED)
        self.sixtyfivekgs_plate_entry.grid(row =5, column = 1)
        self.seventykgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.plates[70], state = DISABLED)
        self.seventykgs_plate_entry.grid(row =6, column = 1)
        self.seventyfivekgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.plates[75], state = DISABLED)
        self.seventyfivekgs_plate_entry.grid(row =7, column = 1)
        self.eightykgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable = self.plates[80], state = DISABLED)
        self.eightykgs_plate_entry.grid(row =8, column = 1)   
    def plate_checked_checkbuttons(self):
        if (self.ItemVar[49].get()==1):
            self.fivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar[49].get()==0:
            self.fivekgs_plate_entry.configure(state=DISABLED)
            self.plates[5].set("0")
        if (self.ItemVar[50].get()==1):
            self.tenkgs_plate_entry.configure(state="normal")
        elif self.ItemVar[50].get()==0:
            self.tenkgs_plate_entry.configure(state=DISABLED)
            self.plates[10].set("0")
        if (self.ItemVar[51].get()==1):
            self.fifteenkgs_plate_entry.configure(state="normal")
        elif self.ItemVar[51].get()==0:
            self.fifteenkgs_plate_entry.configure(state=DISABLED)
            self.plates[15].set("0")
        if (self.ItemVar[52].get()==1):
            self.twentykgs_plate_entry.configure(state="normal")
        elif self.ItemVar[52].get()==0:
            self.twentykgs_plate_entry.configure(state=DISABLED)
            self.plates[20].set("0")
        if (self.ItemVar[53].get()==1):
            self.twentyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar[53].get()==0:
            self.twentyfivekgs_plate_entry.configure(state=DISABLED)
            self.plates[25].set("0")
        if (self.ItemVar[54].get()==1):
            self.thirtykgs_plate_entry.configure(state="normal")
        elif self.ItemVar[54].get()==0:
            self.thirtykgs_plate_entry.configure(state=DISABLED)
            self.plates[30].set("0")
        if (self.ItemVar[55].get()==1):
            self.thirtyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar[55].get()==0:
            self.thirtyfivekgs_plate_entry.configure(state=DISABLED)
            self.plates[35].set("0")
        if (self.ItemVar[56].get()==1):
            self.fourtykgs_plate_entry.configure(state="normal")
        elif self.ItemVar[56].get()==0:
            self.fourtykgs_plate_entry.configure(state=DISABLED)
            self.plates[40].set("0")
        if (self.ItemVar[57].get()==1):
            self.fourtyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar[57].get()==0:
            self.fourtyfivekgs_plate_entry.configure(state=DISABLED)
            self.plates[45].set("0")
        if (self.ItemVar[58].get()==1):
            self.fiftykgs_plate_entry.configure(state="normal")
        elif self.ItemVar[58].get()==0:
            self.fiftykgs_plate_entry.configure(state=DISABLED)
            self.plates[50].set("0")
        if (self.ItemVar[59].get()==1):
            self.fiftyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar[59].get()==0:
            self.fiftyfivekgs_plate_entry.configure(state=DISABLED)
            self.plates[55].set("0")
        if (self.ItemVar[60].get()==1):
            self.sixtykgs_plate_entry.configure(state="normal")
        elif self.ItemVar[60].get()==0:
            self.sixtykgs_plate_entry.configure(state=DISABLED)
            self.plates[60].set("0")
        if (self.ItemVar[61].get()==1):
            self.sixtyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar[61].get()==0:
            self.sixtyfivekgs_plate_entry.configure(state=DISABLED)
            self.plates[65].set("0")
        if (self.ItemVar[62].get()==1):
            self.seventykgs_plate_entry.configure(state="normal")
        elif self.ItemVar[62].get()==0:
            self.seventykgs_plate_entry.configure(state=DISABLED)
            self.plates[70].set("0")
        if (self.ItemVar[63].get()==1):
            self.seventyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar[63].get()==0:
            self.seventyfivekgs_plate_entry.configure(state=DISABLED)
            self.plates[75].set("0")
        if (self.ItemVar[64].get()==1):
            self.eightykgs_plate_entry.configure(state="normal")
        elif self.ItemVar[64].get()==0:
            self.eightykgs_plate_entry.configure(state=DISABLED)
            self.plates[80].set("0")
class ordering_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        plates_top_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue")
        plates_top_border.place(x=0,y=0) #Plates top border
        self.TitleImage = PhotoImage(file="images/GymHomeBanner.png") #Banner for home page
        self.title_label = tk.Label(self, image=self.TitleImage, bd=3).place(x=0, y=56) 
        plates_bottom_border = Frame(self, width = 1366, height = 60, bd = 14, relief ="raise", background = "light blue")
        plates_bottom_border.place(x=0, y=156) #Plates bottom border 
        
            
        self.TitleImage3 = PhotoImage(file="images/finishorderingbanner.png") #Plates banner
        self.title_label3 = tk.Label(self, image=self.TitleImage3, bd=3).place(x=365, y=215)
        FrameOne = tk.Frame(self, width = 500, height = 650, bd = 8, relief = "raise", background = "light blue")
        FrameOne.place(x=0, y=215) #First  frame
        self.FrameTwo = tk.Frame(self, width = 500, height = 350, bd = 8, relief ="raise", background = "light blue")
        self.FrameTwo.place(x=374, y=417) #Second frame
        self.FrameThree = tk.Frame(self, width = 500, height = 350, bd = 8, relief ="raise", background = "light blue")
        self.FrameThree.place(x=870, y=417) #Third frame

        Receipt_Ref = StringVar()
        self.DeliveryTip = StringVar()
        self.SubTotal = StringVar()
        self.TotalCost = StringVar()
    
        home_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Home", command = lambda:manager.show_window("home_page"))
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Barbells", command = lambda:manager.show_window("barbells_page")) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Dumbbells", command = lambda:manager.show_window("dumbbells_page")) 
        dumbbells_button.pack(side=TOP)#Dumbells button
        machines_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Machines", command = lambda:manager.show_window("machines_page")) 
        machines_button.pack(side=TOP)#Machines button
        plates_button = tk.Button(FrameOne, width = 47, height =3, bd = 12, relief = "raise", background = "light blue", text = "Plates", command = lambda:manager.show_window("plates_page")) 
        plates_button.pack(side=TOP)#Plates button
        ordering_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Finish Ordering", command = lambda:manager.show_window("ordering_page")) 
        ordering_button.pack(side=TOP)#Ordering button
        exit_button = tk.Button(FrameOne, width = 47, height = 3, bd = 12, relief = "raise", background = "light blue", text = "Exit", command = manager.exit) 
        exit_button.pack(side=TOP)#Ordering button
 
        ButtonTotal = tk.Button(self, padx = 16, pady = 1, bd =4,font=('arial', 10, 'bold'), width = 14,height = 4,  text = "Total", command = self.total_price, bg = "light blue")
        ButtonTotal.place(x=380, y=420)
        ButtonReset = tk.Button(self, padx = 16, pady = 1, bd =4,font=('arial', 10, 'bold'), width = 14,height = 4, text = "Reset", command =self.reset_data, bg = "light blue")
        ButtonReset.place(x=535, y=420)
        self.ReceiptButton = tk.Button(self, padx = 16, pady = 1, bd =4,font=('arial', 10, 'bold'), width = 14,height = 4, text = "Receipt", command =self.receipt, bg = "light blue", state = DISABLED)
        self.ReceiptButton.place(x=690, y=420)
        self.Receipt_Text = tk.Text(self, font=('arial',10, 'bold'), bd = 8, width = 66, height =20, state = DISABLED)
        self.Receipt_Text.place(x=870, y=420)

        LabelPaidTax=tk.Label(self, font=('arial', 12, 'bold'), text = "Delivery Tip:\t\t\t", bd = 8, background = "light blue")
        LabelPaidTax.place(x=380, y=690)
        EntryDeliveryTip = tk.Entry(self, font=('arial',10, 'bold'), bd = 8, justify='left', insertwidth =1, textvariable =self.DeliveryTip, state = DISABLED)
        EntryDeliveryTip.place(x=380, y=720)

        LabelSubTotal=tk.Label(self, font=('arial', 12, 'bold'), text = "Sub Total:", bd = 8, background = "light blue")
        LabelSubTotal.place(x=535, y=690)
        EntrySubTotal = tk.Entry(self, font=('arial',10, 'bold'), bd = 8, justify='left', insertwidth = 1, textvariable =self.SubTotal, state = DISABLED)
        EntrySubTotal.place(x=535, y=720)

        LabelTotalCost=tk.Label(self, font=('arial', 12, 'bold'), text = "Total Cost: (Inc Tax)", bd = 8, background = "light blue")
        LabelTotalCost.place(x=690, y=690)
        EntryTotalCost = tk.Entry(self, font=('arial',10, 'bold'), bd = 8, justify='left', insertwidth = 1, textvariable = self.TotalCost, state = DISABLED)
        EntryTotalCost.place(x=690, y=720)
    
        self.ReceiptButton = tk.Button(self, padx = 16, pady = 1, bd =4,font=('arial', 10, 'bold'), width = 14,height = 4, text = "Receipt", command =self.receipt, bg = "light blue", state = NORMAL)
        self.ReceiptButton.place(x=690, y=420)
    def total_price(self):
        
        self.price_of_barbells=(float((app.windows["barbells_page"]).barbells[5].get())  * 15) + (float((app.windows["barbells_page"]).barbells[10].get())  * 30) + (float((app.windows["barbells_page"]).barbells[15].get())  * 45) + (float((app.windows["barbells_page"]).barbells[20].get())  * 60) + (float((app.windows["barbells_page"]).barbells[25].get())  * 75) + (float((app.windows["barbells_page"]).barbells[30].get())  * 90) + (float((app.windows["barbells_page"]).barbells[35].get())  * 105) + (float((app.windows["barbells_page"]).barbells[40].get())  * 120)+ (float((app.windows["barbells_page"]).barbells[45].get())  * 135) + (float((app.windows["barbells_page"]).barbells[50].get())  * 150) + (float((app.windows["barbells_page"]).barbells[55].get())  * 165) + (float((app.windows["barbells_page"]).barbells[60].get())  * 180) + (float((app.windows["barbells_page"]).barbells[65].get())  * 195) + (float((app.windows["barbells_page"]).barbells[70].get())  * 210) + (float((app.windows["barbells_page"]).barbells[75].get())  * 225) + (float((app.windows["barbells_page"]).barbells[80].get())  * 240)
        self.price_of_dumbbells= (float((app.windows["dumbbells_page"]).dumbbells[5].get()) * 10) + (float((app.windows["dumbbells_page"]).dumbbells[10].get()) * 20) + (float((app.windows["dumbbells_page"]).dumbbells[15].get()) * 30) + (float((app.windows["dumbbells_page"]).dumbbells[20].get()) * 40) + (float((app.windows["dumbbells_page"]).dumbbells[25].get()) * 50) + (float((app.windows["dumbbells_page"]).dumbbells[30].get())* 60) + (float((app.windows["dumbbells_page"]).dumbbells[35].get()) * 70) + (float((app.windows["dumbbells_page"]).dumbbells[40].get()) * 80)+ (float((app.windows["dumbbells_page"]).dumbbells[45].get()) * 90) + (float((app.windows["dumbbells_page"]).dumbbells[50].get()) * 100) + (float((app.windows["dumbbells_page"]).dumbbells[55].get()) * 110) + (float((app.windows["dumbbells_page"]).dumbbells[60].get()) * 120) + (float((app.windows["dumbbells_page"]).dumbbells[65].get()) * 130) + (float((app.windows["dumbbells_page"]).dumbbells[70].get()) * 140) + (float((app.windows["dumbbells_page"]).dumbbells[75].get()) * 150) + (float((app.windows["dumbbells_page"]).dumbbells[80].get()) * 160)
        self.price_of_machines=(float((app.windows["machines_page"]).machines[1].get()) * 900) + (float((app.windows["machines_page"]).machines[2].get()) * 1000) + (float((app.windows["machines_page"]).machines[3].get()) * 800) + (float((app.windows["machines_page"]).machines[4].get()) * 750) + (float((app.windows["machines_page"]).machines[5].get()) * 900) + (float((app.windows["machines_page"]).machines[6].get()) * 800) + (float((app.windows["machines_page"]).machines[7].get()) * 2000) + (float((app.windows["machines_page"]).machines[8].get()) * 700)+ (float((app.windows["machines_page"]).machines[9].get()) * 650) + (float((app.windows["machines_page"]).machines[10].get()) * 970) + (float((app.windows["machines_page"]).machines[11].get()) * 1300) + (float((app.windows["machines_page"]).machines[12].get()) * 1200) + (float((app.windows["machines_page"]).machines[13].get()) * 740) + (float((app.windows["machines_page"]).machines[14].get()) * 1100) + (float((app.windows["machines_page"]).machines[15].get()) * 1600) + (float((app.windows["machines_page"]).machines[16].get()) * 840)
        self.price_of_plates=(float((app.windows["plates_page"]).plates[5].get()) * 10) + (float((app.windows["plates_page"]).plates[10].get()) * 20) + (float((app.windows["plates_page"]).plates[15].get())* 30) + (float((app.windows["plates_page"]).plates[20].get()) * 40) + (float((app.windows["plates_page"]).plates[25].get()) * 50) + (float((app.windows["plates_page"]).plates[30].get()) * 60) + (float((app.windows["plates_page"]).plates[35].get()) * 70) + (float((app.windows["plates_page"]).plates[40].get()) * 80)+ (float((app.windows["plates_page"]).plates[45].get()) * 90) + (float((app.windows["plates_page"]).plates[50].get()) * 100) + (float((app.windows["plates_page"]).plates[55].get()) * 110) + (float((app.windows["plates_page"]).plates[60].get())* 120) + (float((app.windows["plates_page"]).plates[65].get()) * 130) + (float((app.windows["plates_page"]).plates[70].get()) * 140) + (float((app.windows["plates_page"]).plates[75].get()) * 150) + (float((app.windows["plates_page"]).plates[80].get())* 160) 
        self.delivery = StringVar()
        delivery_ask = messagebox.askquestion("Delivery or pickup", "Would you like us to deliver your items?")
        if delivery_ask == 'yes':
            address_ask = askstring('Address', 'What is your address?')
            if address_ask is not None:
                if address_ask == "":
                    delivery_ask = messagebox.showerror("Invalid input", "Please enter a valid input")
                    return
                else:
                    self.DeliveryTip.set("5.50")
                    tax_float = ((self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates + 5.50 )*0.15)
                    SubTotalofITEMS = '$ ' +str ('%.2f'%(self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates + 5.5))
                    self.SubTotal.set(SubTotalofITEMS)
                    total_cost_float = '$ ' + str ('%.2f'%(self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates + tax_float + 5.5))
                    self.TotalCost.set(total_cost_float)
            else:
                self.DeliveryTip.set("0")
                tax_float = ((self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates )*0.15)
                SubTotalofITEMS = '$ ' +str ('%.2f'%(self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates))
                self.SubTotal.set(SubTotalofITEMS)
                total_cost_float = '$ ' + str ('%.2f'%(self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates + tax_float))
                self.TotalCost.set(total_cost_float)
        else:
            self.DeliveryTip.set("0")
            tax_float = ((self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates )*0.15)
            SubTotalofITEMS = '$ ' +str ('%.2f'%(self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates))
            self.SubTotal.set(SubTotalofITEMS)
            total_cost_float = '$ ' + str ('%.2f'%(self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates + tax_float))
            self.TotalCost.set(total_cost_float)
        

        
    
    def reset_data(self):
        self.DeliveryTip.set("")
        self.SubTotal.set("")
        self.TotalCost.set("")
        self.delivery.set("")
        #=============================================Unchecking checkbuttons=====================================
        for widget in (app.windows["plates_page"]).FrameTwo.winfo_children():
            if widget.winfo_class() == "Checkbutton":
                widget.deselect()
        for widget in (app.windows["barbells_page"]).FrameTwo.winfo_children():
            if widget.winfo_class() == "Checkbutton":
                widget.deselect()
        for widget in (app.windows["machines_page"]).FrameTwo.winfo_children():
            if widget.winfo_class() == "Checkbutton":
                widget.deselect()
        for widget in (app.windows["dumbbells_page"]).FrameTwo.winfo_children():
            if widget.winfo_class() == "Checkbutton":
                widget.deselect()
        for widget in (app.windows["plates_page"]).FrameThree.winfo_children():
            if widget.winfo_class() == "Checkbutton":
                widget.deselect()
        for widget in (app.windows["barbells_page"]).FrameThree.winfo_children():
            if widget.winfo_class() == "Checkbutton":
                widget.deselect()
        for widget in (app.windows["machines_page"]).FrameThree.winfo_children():
            if widget.winfo_class() == "Checkbutton":
                widget.deselect()
        for widget in (app.windows["dumbbells_page"]).FrameThree.winfo_children():
            if widget.winfo_class() == "Checkbutton":
                widget.deselect()
        #============================================Setting entries to zero and disabling entries===========================
        for widget in (app.windows["barbells_page"]).FrameTwo.winfo_children():
            if widget.winfo_class() == "Entry":
                widget.delete(0, "end")
                widget.insert(0, "0")
                widget.config(state="disabled")
        for widget in (app.windows["dumbbells_page"]).FrameTwo.winfo_children():
            if widget.winfo_class() == "Entry":
                widget.delete(0, "end")
                widget.insert(0, "0")
                widget.config(state="disabled")
        for widget in (app.windows["machines_page"]).FrameTwo.winfo_children():
            if widget.winfo_class() == "Entry":
                widget.delete(0, "end")
                widget.insert(0, "0")
                widget.config(state="disabled")
        for widget in (app.windows["plates_page"]).FrameTwo.winfo_children():
            if widget.winfo_class() == "Entry":
                widget.delete(0, "end")
                widget.insert(0, "0")
                widget.config(state="disabled")
            else: 
                print('error')
        for widget in (app.windows["barbells_page"]).FrameThree.winfo_children():
            if widget.winfo_class() == "Entry":
                widget.delete(0, "end")
                widget.insert(0, "0")
                widget.config(state="disabled")
        for widget in (app.windows["dumbbells_page"]).FrameThree.winfo_children():
            if widget.winfo_class() == "Entry":
                widget.delete(0, "end")
                widget.insert(0, "0")
                widget.config(state="disabled")
        for widget in (app.windows["machines_page"]).FrameThree.winfo_children():
            if widget.winfo_class() == "Entry":
                widget.delete(0, "end")
                widget.insert(0, "0")
                widget.config(state="disabled")
        for widget in (app.windows["plates_page"]).FrameThree.winfo_children():
            if widget.winfo_class() == "Entry":
                widget.delete(0, "end")
                widget.insert(0, "0")
                widget.config(state="disabled")
     
    def receipt(self):
        DateofOrder = StringVar()
        Receipt_Ref = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))
        
        self.Receipt_Text = tk.Text(self, font=('arial',10, 'bold'), bd = 8, width = 66, height =20, state = NORMAL)
        self.Receipt_Text.place(x=870, y=420)
        x = random.randint(10908, 500876)
        randomRef = str(x)
        Receipt_Ref.set("BILL"+ randomRef)
        self.Receipt_Text.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get()+'\t\t' + DateofOrder.get()+"\n")
        self.Receipt_Text.insert(END, 'Items:\t\t\t' + "Cost of Items \n\n")
        self.Receipt_Text.insert(END, 'Delivery Tip:\t' + self.DeliveryTip.get() + '\nTotal Cost:\t ' + self.TotalCost.get() + "\n")
        
if __name__ == "__main__": #Prevents parts of code from being run when modules are imported. 
    app = Main()
    app.resizable(width=False, height=False)
    app.geometry("1366x768")
    app.mainloop()