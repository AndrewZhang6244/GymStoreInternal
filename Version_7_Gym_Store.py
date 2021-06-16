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
        self.ItemVar1 = IntVar()
        self.ItemVar2 = IntVar()
        self.ItemVar3 = IntVar()
        self.ItemVar4 = IntVar()
        self.ItemVar5 = IntVar()
        self.ItemVar6 = IntVar()
        self.ItemVar7 = IntVar()
        self.ItemVar8 = IntVar()
        self.ItemVar9 = IntVar()
        self.ItemVar10 = IntVar()
        self.ItemVar11 = IntVar()
        self.ItemVar12 = IntVar()
        self.ItemVar13 = IntVar()
        self.ItemVar14 = IntVar()
        self.ItemVar15 = IntVar()
        self.ItemVar16 = IntVar()
        self.variable_fivekgs_barbell = StringVar()
        self.variable_tenkgs_barbell = StringVar()
        self.variable_fifteenkgs_barbell = StringVar()
        self.variable_twentykgs_barbell = StringVar()
        self.variable_twentyfivekgs_barbell = StringVar()
        self.variable_thirtykgs_barbell = StringVar()
        self.variable_thirtyfivekgs_barbell = StringVar()
        self.variable_fourtykgs_barbell = StringVar()
        self.variable_fourtyfivekgs_barbell = StringVar()
        self.variable_fiftykgs_barbell = StringVar()
        self.variable_fiftyfivekgs_barbell = StringVar()
        self.variable_sixtykgs_barbell = StringVar()
        self.variable_sixtyfivekgs_barbell = StringVar()
        self.variable_seventykgs_barbell = StringVar()
        self.variable_seventyfivekgs_barbell = StringVar()
        self.variable_eightykgs_barbell = StringVar()

        barbell_items = [self.variable_fivekgs_barbell ,self.variable_tenkgs_barbell ,self.variable_fifteenkgs_barbell ,self.variable_twentykgs_barbell ,self.variable_twentyfivekgs_barbell ,self.variable_thirtykgs_barbell ,self.variable_thirtyfivekgs_barbell ,self.variable_fourtykgs_barbell ,self.variable_fourtyfivekgs_barbell ,self.variable_fiftykgs_barbell ,self.variable_fiftyfivekgs_barbell,self.variable_sixtykgs_barbell ,self.variable_sixtyfivekgs_barbell, self.variable_seventykgs_barbell, self.variable_seventyfivekgs_barbell, self.variable_eightykgs_barbell,self.variable_eightykgs_barbell, self.variable_seventyfivekgs_barbell]
        for i in barbell_items:
            i.set(StringVar())
            i.set("0")

        #===================================================Widgets for barbell items===========================================
        #===================================================First section for barbell items=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Barbells 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        fivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 5kgs ($15.00)\t\t" ,variable = self.ItemVar1,command = self.barbell_checked_checkbuttons, onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        tenkgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 10kgs ($30.00) " , variable = self.ItemVar2,command = self.barbell_checked_checkbuttons, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fifteenkgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 15kgs ($45.00)" , variable = self.ItemVar3, command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        twentykgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 20kgs ($60.00) ", variable = self.ItemVar4, command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        twentyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 25kg ($75.00) ",variable = self.ItemVar5,command = self.barbell_checked_checkbuttons, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        thirtykgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 30kgs ($90.00) ",variable = self.ItemVar6, command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        thirtyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 35kgs ($105.00) ", variable = self.ItemVar7,command = self.barbell_checked_checkbuttons, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        fourtykgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 40kgs ($120.00) ", variable = self.ItemVar8, command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fivekgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_fivekgs_barbell, state = DISABLED)
        self.fivekgs_barbell_entry.grid(row =1, column = 1)
        self.tenkgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_tenkgs_barbell, state = DISABLED)
        self.tenkgs_barbell_entry.grid(row =2, column = 1)
        self.fifteenkgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_fifteenkgs_barbell, state = DISABLED)
        self.fifteenkgs_barbell_entry.grid(row =3, column = 1)
        self.twentykgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_twentykgs_barbell, state = DISABLED)
        self.twentykgs_barbell_entry.grid(row =4, column = 1)
        self.twentyfivekgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_twentyfivekgs_barbell, state = DISABLED)
        self.twentyfivekgs_barbell_entry.grid(row =5, column = 1)
        self.thirtykgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_thirtykgs_barbell ,state = DISABLED)
        self.thirtykgs_barbell_entry.grid(row =6, column = 1)
        self.thirtyfivekgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_thirtyfivekgs_barbell, state = DISABLED)
        self.thirtyfivekgs_barbell_entry.grid(row =7, column = 1)
        self.fourtykgs_barbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable = self.variable_fourtykgs_barbell, state = DISABLED)
        self.fourtykgs_barbell_entry.grid(row =8, column = 1)
        #=====================================================================Second section for barbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Barbells 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 45kgs ($135.00) \t\t", variable = self.ItemVar9, command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        fiftykgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 50kgs ($150.00) \t", variable = self.ItemVar10, command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fiftyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 55kgs ($165.00) \t", variable = self.ItemVar11, command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        sixtykgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 60kgs ($180.00)\t", variable = self.ItemVar12,command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        sixtyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 65kgs ($195.00) \t", variable = self.ItemVar13,command = self.barbell_checked_checkbuttons, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        seventyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 70kgs ($210.00) \t", variable = self.ItemVar14, command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        seventyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 75kgs ($225.00) \t", variable = self.ItemVar15,command = self.barbell_checked_checkbuttons, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        eightykgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 80kgs ($240.00) \t",variable = self.ItemVar16, command = self.barbell_checked_checkbuttons,onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fourtyfivekgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_fourtyfivekgs_barbell, state = DISABLED)
        self.fourtyfivekgs_barbell_entry.grid(row =1, column = 1)
        self.fiftykgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_fiftykgs_barbell, state = DISABLED)
        self.fiftykgs_barbell_entry.grid(row=2, column=1)
        self.fiftyfivekgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_fiftyfivekgs_barbell, state = DISABLED)
        self.fiftyfivekgs_barbell_entry.grid(row =3, column = 1)
        self.sixtykgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_sixtykgs_barbell, state = DISABLED)
        self.sixtykgs_barbell_entry.grid(row =4, column = 1)
        self.sixtyfivekgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_sixtyfivekgs_barbell, state = DISABLED)
        self.sixtyfivekgs_barbell_entry.grid(row =5, column = 1)
        self.seventykgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_seventykgs_barbell, state = DISABLED)
        self.seventykgs_barbell_entry.grid(row =6, column = 1)
        self.seventyfivekgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_seventyfivekgs_barbell, state = DISABLED)
        self.seventyfivekgs_barbell_entry.grid(row =7, column = 1)
        self.eightykgs_barbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable = self.variable_eightykgs_barbell, state = DISABLED)
        self.eightykgs_barbell_entry.grid(row =8, column = 1)  
    def barbell_checked_checkbuttons(self):
        if (self.ItemVar1.get()==1):
            self.fivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar1.get()==0:
            self.fivekgs_barbell_entry.configure(state=DISABLED)
            self.variable_fivekgs_barbell.set("0")
        if (self.ItemVar2.get()==1):
            self.tenkgs_barbell_entry.configure(state="normal")
        elif self.ItemVar2.get()==0:
            self.tenkgs_barbell_entry.configure(state=DISABLED)
            self.variable_tenkgs_barbell.set("0")
        if (self.ItemVar3.get()==1):
            self.fifteenkgs_barbell_entry.configure(state="normal")
        elif self.ItemVar3.get()==0:
            self.fifteenkgs_barbell_entry.configure(state=DISABLED)
            self.variable_fifteenkgs_barbell.set("0")
        if (self.ItemVar4.get()==1):
            self.twentykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar4.get()==0:
            self.twentykgs_barbell_entry.configure(state=DISABLED)
            self.variable_twentykgs_barbell.set("0")
        if (self.ItemVar5.get()==1):
            self.twentyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar5.get()==0:
            self.twentyfivekgs_barbell_entry.configure(state=DISABLED)
            self.variable_twentyfivekgs_barbell.set("0")
        if (self.ItemVar6.get()==1):
            self.thirtykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar6.get()==0:
            self.thirtykgs_barbell_entry.configure(state=DISABLED)
            self.variable_thirtykgs_barbell.set("0")
        if (self.ItemVar7.get()==1):
            self.thirtyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar7.get()==0:
            self.thirtyfivekgs_barbell_entry.configure(state=DISABLED)
            self.variable_thirtyfivekgs_barbell.set("0")
        if (self.ItemVar8.get()==1):
            self.fourtykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar8.get()==0:
            self.fourtykgs_barbell_entry.configure(state=DISABLED)
            self.variable_fourtykgs_barbell.set("0")
        if (self.ItemVar9.get()==1):
            self.fourtyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar9.get()==0:
            self.fourtyfivekgs_barbell_entry.configure(state=DISABLED)
            self.variable_fourtyfivekgs_barbell.set("0")
        if (self.ItemVar10.get()==1):
            self.fiftykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar10.get()==0:
            self.fiftykgs_barbell_entry.configure(state=DISABLED)
            self.variable_fiftykgs_barbell.set("0")
        if (self.ItemVar11.get()==1):
            self.fiftyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar11.get()==0:
            self.fiftyfivekgs_barbell_entry.configure(state=DISABLED)
            self.variable_fiftyfivekgs_barbell.set("0")
        if (self.ItemVar12.get()==1):
            self.sixtykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar12.get()==0:
            self.sixtykgs_barbell_entry.configure(state=DISABLED)
            self.variable_sixtykgs_barbell.set("0")
        if (self.ItemVar13.get()==1):
            self.sixtyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar13.get()==0:
            self.sixtyfivekgs_barbell_entry.configure(state=DISABLED)
            self.variable_sixtyfivekgs_barbell.set("0")
        if (self.ItemVar14.get()==1):
            self.seventykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar14.get()==0:
            self.seventykgs_barbell_entry.configure(state=DISABLED)
            self.variable_seventykgs_barbell.set("0")
        if (self.ItemVar15.get()==1):
            self.seventyfivekgs_barbell_entry.configure(state="normal")
        elif self.ItemVar15.get()==0:
            self.seventyfivekgs_barbell_entry.configure(state=DISABLED)
            self.variable_seventyfivekgs_barbell.set("0")
        if (self.ItemVar16.get()==1):
            self.eightykgs_barbell_entry.configure(state="normal")
        elif self.ItemVar16.get()==0:
            self.eightykgs_barbell_entry.configure(state=DISABLED)
            self.variable_eightykgs_barbell.set("0")

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
        self.ItemVar17 = IntVar()
        self.ItemVar18 = IntVar()
        self.ItemVar19 = IntVar()
        self.ItemVar20 = IntVar()
        self.ItemVar21 = IntVar()
        self.ItemVar22 = IntVar()
        self.ItemVar23 = IntVar()
        self.ItemVar24 = IntVar()
        self.ItemVar25 = IntVar()
        self.ItemVar26 = IntVar()
        self.ItemVar27 = IntVar()
        self.ItemVar28 = IntVar()
        self.ItemVar29 = IntVar()
        self.ItemVar30 = IntVar()
        self.ItemVar31 = IntVar()
        self.ItemVar32 = IntVar()
        self.variable_fivekgs_dumbbell = StringVar()
        self.variable_tenkgs_dumbbell = StringVar()
        self.variable_fifteenkgs_dumbbell = StringVar()
        self.variable_twentykgs_dumbbell = StringVar()
        self.variable_twentyfivekgs_dumbbell = StringVar()
        self.variable_thirtykgs_dumbbell = StringVar()
        self.variable_thirtyfivekgs_dumbbell = StringVar()
        self.variable_fourtykgs_dumbbell = StringVar()
        self.variable_fourtyfivekgs_dumbbell = StringVar()
        self.variable_fiftykgs_dumbbell = StringVar()
        self.variable_fiftyfivekgs_dumbbell = StringVar()
        self.variable_sixtykgs_dumbbell = StringVar()
        self.variable_sixtyfivekgs_dumbbell = StringVar()
        self.variable_seventykgs_dumbbell = StringVar()
        self.variable_seventyfivekgs_dumbbell = StringVar()
        self.variable_eightykgs_dumbbell = StringVar()

        
        
        dumbbell_items = [self.variable_fivekgs_dumbbell ,self.variable_tenkgs_dumbbell ,self.variable_fifteenkgs_dumbbell ,self.variable_twentykgs_dumbbell ,self.variable_twentyfivekgs_dumbbell,self.variable_thirtykgs_dumbbell,self.variable_thirtyfivekgs_dumbbell,self.variable_fourtykgs_dumbbell,self.variable_fourtyfivekgs_dumbbell,self.variable_fiftykgs_dumbbell ,self.variable_fiftyfivekgs_dumbbell ,self.variable_sixtykgs_dumbbell,self.variable_sixtyfivekgs_dumbbell ,self.variable_seventykgs_dumbbell ,self.variable_seventyfivekgs_dumbbell,self.variable_eightykgs_dumbbell ]
        for i in dumbbell_items:
            i.set("0")
        #===================================================Widgets for dumbbell items===========================================
        #===================================================First section for dumbell items=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Dumbbells 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        fivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 5kgs ($10.00)\t\t" ,command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar17, onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        tenkgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 10kgs ($20.00) " , command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar18, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fifteenkgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 15kgs ($30.00) " ,command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar19, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        twentykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 20kgs ($40.00) ",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar20, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        twentyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 25kgs ($50.00) ",command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar21, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        thirtykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 30kgs ($60.00) ",command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar22, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        thirtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 35kgs ($70.00) ", command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar23, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        fourtykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 40kgs ($80.00) ",command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar24, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fivekgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_fivekgs_dumbbell, state = DISABLED)
        self.fivekgs_dumbbell_entry.grid(row =1, column = 1)
        self.tenkgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_tenkgs_dumbbell, state = DISABLED)
        self.tenkgs_dumbbell_entry.grid(row =2, column = 1)
        self.fifteenkgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_fifteenkgs_dumbbell, state = DISABLED)
        self.fifteenkgs_dumbbell_entry.grid(row =3, column = 1)
        self.twentykgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_twentykgs_dumbbell, state = DISABLED)
        self.twentykgs_dumbbell_entry.grid(row =4, column = 1)
        self.twentyfivekgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_twentyfivekgs_dumbbell, state = DISABLED)
        self.twentyfivekgs_dumbbell_entry.grid(row =5, column = 1)
        self.thirtykgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_thirtykgs_dumbbell ,state = DISABLED)
        self.thirtykgs_dumbbell_entry.grid(row =6, column = 1)
        self.thirtyfivekgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_thirtyfivekgs_dumbbell, state = DISABLED)
        self.thirtyfivekgs_dumbbell_entry.grid(row =7, column = 1)
        self.fourtykgs_dumbbell_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable = self.variable_fourtykgs_dumbbell, state = DISABLED)
        self.fourtykgs_dumbbell_entry.grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Dumbbells 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 45kgs ($90.00)\t\t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar25, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        fiftykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 50kgs ($100.00)\t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar26, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fiftyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 55kgs ($110.00)\t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar27, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        sixtykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 60kgs ($120.00)\t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar28, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        sixtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 65kgs ($130.00) \t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar29, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        seventyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 70kgs ($140.00) \t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar30, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        seventyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 75kgs ($150.00) \t",command = self.dumbbell_checked_checkbuttons, variable = self.ItemVar31, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        eightykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 80kgs ($160.00) \t",command = self.dumbbell_checked_checkbuttons,variable = self.ItemVar32, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fourtyfivekgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_fourtyfivekgs_dumbbell, state = DISABLED)
        self.fourtyfivekgs_dumbbell_entry.grid(row =1, column = 1)
        self.fiftykgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_fiftykgs_dumbbell, state = DISABLED)
        self.fiftykgs_dumbbell_entry.grid(row =2, column = 1)
        self.fiftyfivekgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_fiftyfivekgs_dumbbell, state = DISABLED)
        self.fiftyfivekgs_dumbbell_entry.grid(row =3, column = 1)
        self.sixtykgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_sixtykgs_dumbbell, state = DISABLED)
        self.sixtykgs_dumbbell_entry.grid(row =4, column = 1)
        self.sixtyfivekgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_sixtyfivekgs_dumbbell, state = DISABLED)
        self.sixtyfivekgs_dumbbell_entry.grid(row =5, column = 1)
        self.seventykgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_sixtykgs_dumbbell, state = DISABLED)
        self.seventykgs_dumbbell_entry.grid(row =6, column = 1)
        self.seventyfivekgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_sixtyfivekgs_dumbbell, state = DISABLED)
        self.seventyfivekgs_dumbbell_entry.grid(row =7, column = 1)
        self.eightykgs_dumbbell_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable = self.variable_seventykgs_dumbbell, state = DISABLED)
        self.eightykgs_dumbbell_entry.grid(row =8, column = 1)   
    def dumbbell_checked_checkbuttons(self):
        if (self.ItemVar17.get()==1):
            self.fivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar17.get()==0:
            self.fivekgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_fivekgs_dumbbell.set("0")
        if (self.ItemVar18.get()==1):
            self.tenkgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar18.get()==0:
            self.tenkgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_tenkgs_dumbbell.set("0")
        if (self.ItemVar19.get()==1):
            self.fifteenkgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar19.get()==0:
            self.fifteenkgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_fifteenkgs_dumbbell.set("0")
        if (self.ItemVar20.get()==1):
            self.twentykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar20.get()==0:
            self.twentykgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_twentykgs_dumbbell.set("0")
        if (self.ItemVar21.get()==1):
            self.twentyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar21.get()==0:
            self.twentyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_twentyfivekgs_dumbbell.set("0")
        if (self.ItemVar22.get()==1):
            self.thirtykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar22.get()==0:
            self.thirtykgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_thirtykgs_dumbbell.set("0")
        if (self.ItemVar23.get()==1):
            self.thirtyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar23.get()==0:
            self.thirtyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_thirtyfivekgs_dumbbell.set("0")
        if (self.ItemVar24.get()==1):
            self.fourtykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar24.get()==0:
            self.fourtykgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_fourtykgs_dumbbell.set("0")
        if (self.ItemVar25.get()==1):
            self.fourtyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar25.get()==0:
            self.fourtyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_fourtyfivekgs_dumbbell.set("0")
        if (self.ItemVar26.get()==1):
            self.fiftykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar26.get()==0:
            self.fiftykgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_fiftykgs_dumbbell.set("0")
        if (self.ItemVar27.get()==1):
            self.fiftyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar27.get()==0:
            self.fiftyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_fiftyfivekgs_dumbbell.set("0")
        if (self.ItemVar28.get()==1):
            self.sixtykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar28.get()==0:
            self.sixtykgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_sixtykgs_dumbbell.set("0")
        if (self.ItemVar29.get()==1):
            self.sixtyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar29.get()==0:
            self.sixtyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_sixtyfivekgs_dumbbell.set("0")
        if (self.ItemVar30.get()==1):
            self.seventykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar30.get()==0:
            self.seventykgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_seventykgs_dumbbell.set("0")
        if (self.ItemVar31.get()==1):
            self.seventyfivekgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar31.get()==0:
            self.seventyfivekgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_seventyfivekgs_dumbbell.set("0")
        if (self.ItemVar32.get()==1):
            self.eightykgs_dumbbell_entry.configure(state="normal")
        elif self.ItemVar32.get()==0:
            self.eightykgs_dumbbell_entry.configure(state=DISABLED)
            self.variable_eightykgs_dumbbell.set("0")
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
        self.ItemVar33 = IntVar()
        self.ItemVar34 = IntVar()
        self.ItemVar35 = IntVar()
        self.ItemVar36 = IntVar()
        self.ItemVar37 = IntVar()
        self.ItemVar38 = IntVar()
        self.ItemVar39 = IntVar()
        self.ItemVar40 = IntVar()
        self.ItemVar41 = IntVar()
        self.ItemVar42 = IntVar()
        self.ItemVar43 = IntVar()
        self.ItemVar44 = IntVar()
        self.ItemVar45 = IntVar()
        self.ItemVar46 = IntVar()
        self.ItemVar47 = IntVar()
        self.ItemVar48 = IntVar()
        self.variable_treadmill = StringVar()
        self.variable_chestpress = StringVar()
        self.variable_pecfly = StringVar()
        self.variable_seatedrow = StringVar()
        self.variable_latpulldown = StringVar()
        self.variable_ergometer = StringVar()
        self.variable_stairmaster = StringVar()
        self.variable_smithmachine = StringVar()
        self.variable_abcrunch = StringVar()
        self.variable_legextension = StringVar()
        self.variable_legpress = StringVar()
        self.variable_elliptical = StringVar()
        self.variable_standingcalfraise = StringVar()
        self.variable_shoulderpress = StringVar()
        self.variable_legcurls = StringVar()
        self.variable_deltoidraise = StringVar()
        
        

        machine_items = [self.variable_treadmill,self.variable_chestpress,self.variable_pecfly,self.variable_seatedrow,self.variable_latpulldown,self.variable_ergometer,self.variable_stairmaster,self.variable_smithmachine,self.variable_abcrunch,self.variable_legextension,self.variable_legpress,self.variable_elliptical,self.variable_standingcalfraise,self.variable_shoulderpress,self.variable_legcurls,self.variable_deltoidraise]
        for i in machine_items:
            i.set("0")
        #===================================================Widgets for machiness==========================================
        #===================================================First section for machines=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Machines 1: ",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0) 
        treadmill_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Treadmill ($900.00)\t\t" ,command = self.machines_checked_checkbuttons,variable = self.ItemVar33, onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        chestpress_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Chest press ($1000.00)" ,command = self.machines_checked_checkbuttons, variable = self.ItemVar34, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        pecfly_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Pecfly ($800.00)" , command = self.machines_checked_checkbuttons,variable = self.ItemVar35, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        seatedrow_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Seated row ($750.00)", command = self.machines_checked_checkbuttons,variable = self.ItemVar36, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        latpulldown_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Lat pull down ($900.00)",command = self.machines_checked_checkbuttons,variable = self.ItemVar37, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        ergometer_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Ergometer ($800.00)",command = self.machines_checked_checkbuttons,variable = self.ItemVar38, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        stairmaster_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Stairmaster ($2000.00)", command = self.machines_checked_checkbuttons,variable = self.ItemVar39, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        smithmachine_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Smithmachine ($700.00)", command = self.machines_checked_checkbuttons,variable = self.ItemVar40, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.treadmill_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_treadmill, state = DISABLED)
        self.treadmill_entry.grid(row =1, column = 1)
        self.chestpress_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_chestpress, state = DISABLED)
        self.chestpress_entry.grid(row =2, column = 1)
        self.pecfly_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_pecfly, state = DISABLED)
        self.pecfly_entry.grid(row =3, column = 1)
        self.seatedrow_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_seatedrow, state = DISABLED)
        self.seatedrow_entry.grid(row =4, column = 1)
        self.latpulldown_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_latpulldown, state = DISABLED)
        self.latpulldown_entry.grid(row =5, column = 1)
        self.ergometer_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_ergometer ,state = DISABLED)
        self.ergometer_entry.grid(row =6, column = 1)
        self.stairmaster_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_stairmaster, state = DISABLED)
        self.stairmaster_entry.grid(row =7, column = 1)
        self.smithmachine_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable = self.variable_smithmachine, state = DISABLED)
        self.smithmachine_entry.grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Machines 2: ",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        row_checkbutton = tk.Checkbutton(self.FrameThree, text ="Ab crunch ($650.00)\t\t",command = self.machines_checked_checkbuttons, variable = self.ItemVar41, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        legextension_checkbutton = tk.Checkbutton(self.FrameThree, text ="Leg extension ($970.00)\t", command = self.machines_checked_checkbuttons,variable = self.ItemVar42, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        legpress_checkbutton = tk.Checkbutton(self.FrameThree, text ="Leg press ($1300.00)\t",command = self.machines_checked_checkbuttons, variable = self.ItemVar43, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        elliptical_checkbutton = tk.Checkbutton(self.FrameThree, text ="Elliptical ($1200.00)\t",command = self.machines_checked_checkbuttons, variable = self.ItemVar44, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        standingcalfraise_checkbutton = tk.Checkbutton(self.FrameThree, text ="Standing calf raise ($740.00)\t",command = self.machines_checked_checkbuttons, variable = self.ItemVar45, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        shoulderpress_checkbutton = tk.Checkbutton(self.FrameThree, text ="Shoulder press ($1100.00)\t", command = self.machines_checked_checkbuttons,variable = self.ItemVar46, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        legcurls_checkbutton = tk.Checkbutton(self.FrameThree, text ="Leg curls ($1600.00)\t", command = self.machines_checked_checkbuttons,variable = self.ItemVar47, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        deltoidraise_checkbutton = tk.Checkbutton(self.FrameThree, text ="Deltoid raise ($840.00)\t",command = self.machines_checked_checkbuttons,variable = self.ItemVar48, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.abcrunch_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_abcrunch, state = DISABLED)
        self.abcrunch_entry.grid(row =1, column = 1)
        self.legextension_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_legextension, state = DISABLED)
        self.legextension_entry.grid(row =2, column = 1)
        self.legpress_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_legpress, state = DISABLED)
        self.legpress_entry.grid(row =3, column = 1)
        self.elliptical_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_elliptical, state = DISABLED)
        self.elliptical_entry.grid(row =4, column = 1)
        self.standingcalfraise_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_standingcalfraise, state = DISABLED)
        self.standingcalfraise_entry.grid(row =5, column = 1)
        self.shoulderpress_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_shoulderpress, state = DISABLED)
        self.shoulderpress_entry.grid(row =6, column = 1)
        self.legcurls_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_legcurls, state = DISABLED)
        self.legcurls_entry.grid(row =7, column = 1)
        self.deltoidraise_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable = self.variable_deltoidraise, state = DISABLED)
        self.deltoidraise_entry.grid(row =8, column = 1)   
    def machines_checked_checkbuttons(self):
        if (self.ItemVar33.get()==1):
            self.treadmill_entry.configure(state="normal")
        elif self.ItemVar33.get()==0:
            self.treadmill_entry.configure(state=DISABLED)
            self.variable_treadmill.set("0")
        if (self.ItemVar34.get()==1):
            self.chestpress_entry.configure(state="normal")
        elif self.ItemVar34.get()==0:
            self.chestpress_entry.configure(state=DISABLED)
            self.variable_chestpress.set("0")
        if (self.ItemVar35.get()==1):
            self.pecfly_entry.configure(state="normal")
        elif self.ItemVar35.get()==0:
            self.pecfly_entry.configure(state=DISABLED)
            self.variable_pecfly.set("0")
        if (self.ItemVar36.get()==1):
            self.seatedrow_entry.configure(state="normal")
        elif self.ItemVar36.get()==0:
            self.seatedrow_entry.configure(state=DISABLED)
            self.variable_seatedrow.set("0")
        if (self.ItemVar37.get()==1):
            self.latpulldown_entry.configure(state="normal")
        elif self.ItemVar37.get()==0:
            self.latpulldown_entry.configure(state=DISABLED)
            self.variable_latpulldown.set("0")
        if (self.ItemVar38.get()==1):
            self.ergometer_entry.configure(state="normal")
        elif self.ItemVar38.get()==0:
            self.ergometer_entry.configure(state=DISABLED)
            self.variable_ergometer.set("0")
        if (self.ItemVar39.get()==1):
            self.stairmaster_entry.configure(state="normal")
        elif self.ItemVar39.get()==0:
            self.stairmaster_entry.configure(state=DISABLED)
            self.variable_stairmaster.set("0")
        if (self.ItemVar40.get()==1):
            self.smithmachine_entry.configure(state="normal")
        elif self.ItemVar40.get()==0:
            self.smithmachine_entry.configure(state=DISABLED)
            self.variable_smithmachine.set("0")
        if (self.ItemVar41.get()==1):
            self.abcrunch_entry.configure(state="normal")
        elif self.ItemVar41.get()==0:
            self.abcrunch_entry.configure(state=DISABLED)
            self.variable_abcrunch.set("0")
        if (self.ItemVar42.get()==1):
            self.legextension_entry.configure(state="normal")
        elif self.ItemVar42.get()==0:
            self.legextension_entry.configure(state=DISABLED)
            self.variable_legextension.set("0")
        if (self.ItemVar43.get()==1):
            self.legpress_entry.configure(state="normal")
        elif self.ItemVar43.get()==0:
            self.legpress_entry.configure(state=DISABLED)
            self.variable_legpress.set("0")
        if (self.ItemVar44.get()==1):
            self.elliptical_entry.configure(state="normal")
        elif self.ItemVar44.get()==0:
            self.elliptical_entry.configure(state=DISABLED)
            self.variable_elliptical.set("0")
        if (self.ItemVar45.get()==1):
            self.standingcalfraise_entry.configure(state="normal")
        elif self.ItemVar45.get()==0:
            self.standingcalfraise_entry.configure(state=DISABLED)
            self.variable_standingcalfraise.set("0")
        if (self.ItemVar46.get()==1):
            self.shoulderpress_entry.configure(state="normal")
        elif self.ItemVar46.get()==0:
            self.shoulderpress_entry.configure(state=DISABLED)
            self.variable_shoulderpress.set("0")
        if (self.ItemVar47.get()==1):
            self.legcurls_entry.configure(state="normal")
        elif self.ItemVar47.get()==0:
            self.legcurls_entry.configure(state=DISABLED)
            self.variable_legcurls.set("0")
        if (self.ItemVar48.get()==1):
            self.deltoidraise_entry.configure(state="normal")
        elif self.ItemVar48.get()==0:
            self.deltoidraise_entry.configure(state=DISABLED)
            self.variable_deltoidraise.set("0")
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
        self.ItemVar49 = IntVar()
        self.ItemVar50 = IntVar()
        self.ItemVar51 = IntVar()
        self.ItemVar52 = IntVar()
        self.ItemVar53 = IntVar()
        self.ItemVar54 = IntVar()
        self.ItemVar55 = IntVar()
        self.ItemVar56 = IntVar()
        self.ItemVar57 = IntVar()
        self.ItemVar58 = IntVar()
        self.ItemVar59 = IntVar()
        self.ItemVar60 = IntVar()
        self.ItemVar61 = IntVar()
        self.ItemVar62 = IntVar()
        self.ItemVar63 = IntVar()
        self.ItemVar64 = IntVar()

    
        self.variable_fivekgs_plate = StringVar()
        self.variable_tenkgs_plate = StringVar()
        self.variable_fifteenkgs_plate = StringVar()
        self.variable_twentykgs_plate = StringVar()
        self.variable_twentyfivekgs_plate = StringVar()
        self.variable_thirtykgs_plate = StringVar()
        self.variable_thirtyfivekgs_plate = StringVar()
        self.variable_fourtykgs_plate = StringVar()
        self.variable_fourtyfivekgs_plate = StringVar()
        self.variable_fiftykgs_plate = StringVar()
        self.variable_fiftyfivekgs_plate = StringVar()
        self.variable_sixtykgs_plate = StringVar()
        self.variable_sixtyfivekgs_plate = StringVar()
        self.variable_seventykgs_plate = StringVar()
        self.variable_seventyfivekgs_plate =  StringVar()
        self.variable_eightykgs_plate = StringVar()

        plate_items = [self.variable_fivekgs_plate,self.variable_tenkgs_plate ,self.variable_fifteenkgs_plate ,self.variable_twentykgs_plate ,self.variable_twentyfivekgs_plate ,self.variable_thirtykgs_plate,self.variable_thirtyfivekgs_plate ,self.variable_fourtykgs_plate ,self.variable_fourtyfivekgs_plate ,self.variable_fiftykgs_plate ,self.variable_fiftyfivekgs_plate ,self.variable_sixtykgs_plate,self.variable_sixtyfivekgs_plate,self.variable_seventykgs_plate,self.variable_seventyfivekgs_plate,self.variable_eightykgs_plate ]
        for i in plate_items:
            i.set("0")
        #===================================================Widgets for plate items===========================================
        #===================================================First section for plate items=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Plates 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        fivekgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 5kgs ($10.00)\t\t" ,variable = self.ItemVar49, command = self.plate_checked_checkbuttons, onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        tenkgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 10kgs ($20.00)" , command = self.plate_checked_checkbuttons,variable = self.ItemVar50, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fifteenkgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 15kgs ($30.00)" , command = self.plate_checked_checkbuttons,variable = self.ItemVar51, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        twentykgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 20kgs ($40.00)", command = self.plate_checked_checkbuttons,variable = self.ItemVar52, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        twentyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 25kgs ($50.00)",command = self.plate_checked_checkbuttons,variable = self.ItemVar53, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        thirtykgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 30kgs ($60.00)",command = self.plate_checked_checkbuttons,variable = self.ItemVar54, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        thirtyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 35kgs ($70.00)", command = self.plate_checked_checkbuttons,variable = self.ItemVar55, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        fourtykgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 40kgs ($80.00)",command = self.plate_checked_checkbuttons, variable = self.ItemVar56, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fivekgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_fivekgs_plate, state = DISABLED)
        self.fivekgs_plate_entry.grid(row =1, column = 1)
        self.tenkgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_tenkgs_plate, state = DISABLED)
        self.tenkgs_plate_entry.grid(row =2, column = 1)
        self.fifteenkgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_fifteenkgs_plate, state = DISABLED)
        self.fifteenkgs_plate_entry.grid(row =3, column = 1)
        self.twentykgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_twentykgs_plate, state = DISABLED)
        self.twentykgs_plate_entry.grid(row =4, column = 1)
        self.twentyfivekgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_twentyfivekgs_plate, state = DISABLED)
        self.twentyfivekgs_plate_entry.grid(row =5, column = 1)
        self.thirtykgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_thirtykgs_plate ,state = DISABLED)
        self.thirtykgs_plate_entry.grid(row =6, column = 1)
        self.thirtyfivekgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_thirtyfivekgs_plate, state = DISABLED)
        self.thirtyfivekgs_plate_entry.grid(row =7, column = 1)
        self.fourtykgs_plate_entry = tk.Entry(self.FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable = self.variable_fourtykgs_plate, state = DISABLED)
        self.fourtykgs_plate_entry.grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Plates 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 45kgs ($90.00)\t\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar57, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        fiftykgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 50kgs ($100.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar58, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fiftyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 55kgs ($110.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar59, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        sixtykgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 60kgs ($120.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar60, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        sixtyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 65kgs ($130.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar61, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        seventyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 70kgs ($140.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar62, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        seventyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 75kgs ($150.00)\t", command = self.plate_checked_checkbuttons,variable = self.ItemVar63, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        eightykgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 80kgs ($160.00)\t",command = self.plate_checked_checkbuttons,variable = self.ItemVar64, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        self.fourtyfivekgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_fourtyfivekgs_plate, state = DISABLED)
        self.fourtyfivekgs_plate_entry.grid(row =1, column = 1)
        self.fiftykgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_fiftykgs_plate, state = DISABLED)
        self.fiftykgs_plate_entry.grid(row =2, column = 1)
        self.fiftyfivekgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_fiftyfivekgs_plate, state = DISABLED)
        self.fiftyfivekgs_plate_entry.grid(row =3, column = 1)
        self.sixtykgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_sixtykgs_plate, state = DISABLED)
        self.sixtykgs_plate_entry.grid(row =4, column = 1)
        self.sixtyfivekgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_sixtyfivekgs_plate, state = DISABLED)
        self.sixtyfivekgs_plate_entry.grid(row =5, column = 1)
        self.seventykgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_seventykgs_plate, state = DISABLED)
        self.seventykgs_plate_entry.grid(row =6, column = 1)
        self.seventyfivekgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_seventyfivekgs_plate, state = DISABLED)
        self.seventyfivekgs_plate_entry.grid(row =7, column = 1)
        self.eightykgs_plate_entry = tk.Entry(self.FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable = self.variable_eightykgs_plate, state = DISABLED)
        self.eightykgs_plate_entry.grid(row =8, column = 1)   
    def plate_checked_checkbuttons(self):
        if (self.ItemVar49.get()==1):
            self.fivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar49.get()==0:
            self.fivekgs_plate_entry.configure(state=DISABLED)
            self.variable_fivekgs_plate.set("0")
        if (self.ItemVar50.get()==1):
            self.tenkgs_plate_entry.configure(state="normal")
        elif self.ItemVar50.get()==0:
            self.tenkgs_plate_entry.configure(state=DISABLED)
            self.variable_tenkgs_plate.set("0")
        if (self.ItemVar51.get()==1):
            self.fifteenkgs_plate_entry.configure(state="normal")
        elif self.ItemVar51.get()==0:
            self.fifteenkgs_plate_entry.configure(state=DISABLED)
            self.variable_fifteenkgs_plate.set("0")
        if (self.ItemVar52.get()==1):
            self.twentykgs_plate_entry.configure(state="normal")
        elif self.ItemVar52.get()==0:
            self.twentykgs_plate_entry.configure(state=DISABLED)
            self.variable_twentykgs_plate.set("0")
        if (self.ItemVar53.get()==1):
            self.twentyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar53.get()==0:
            self.twentyfivekgs_plate_entry.configure(state=DISABLED)
            self.variable_twentyfivekgs_plate.set("0")
        if (self.ItemVar54.get()==1):
            self.thirtykgs_plate_entry.configure(state="normal")
        elif self.ItemVar54.get()==0:
            self.thirtykgs_plate_entry.configure(state=DISABLED)
            self.variable_thirtykgs_plate.set("0")
        if (self.ItemVar55.get()==1):
            self.thirtyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar55.get()==0:
            self.thirtyfivekgs_plate_entry.configure(state=DISABLED)
            self.variable_thirtyfivekgs_plate.set("0")
        if (self.ItemVar56.get()==1):
            self.fourtykgs_plate_entry.configure(state="normal")
        elif self.ItemVar56.get()==0:
            self.fourtykgs_plate_entry.configure(state=DISABLED)
            self.variable_fourtykgs_plate.set("0")
        if (self.ItemVar57.get()==1):
            self.fourtyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar57.get()==0:
            self.fourtyfivekgs_plate_entry.configure(state=DISABLED)
            self.variable_fourtyfivekgs_plate.set("0")
        if (self.ItemVar58.get()==1):
            self.fiftykgs_plate_entry.configure(state="normal")
        elif self.ItemVar58.get()==0:
            self.fiftykgs_plate_entry.configure(state=DISABLED)
            self.variable_fiftykgs_plate.set("0")
        if (self.ItemVar59.get()==1):
            self.fiftyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar59.get()==0:
            self.fiftyfivekgs_plate_entry.configure(state=DISABLED)
            self.variable_fiftyfivekgs_plate.set("0")
        if (self.ItemVar60.get()==1):
            self.sixtykgs_plate_entry.configure(state="normal")
        elif self.ItemVar60.get()==0:
            self.sixtykgs_plate_entry.configure(state=DISABLED)
            self.variable_sixtykgs_plate.set("0")
        if (self.ItemVar61.get()==1):
            self.sixtyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar61.get()==0:
            self.sixtyfivekgs_plate_entry.configure(state=DISABLED)
            self.variable_sixtyfivekgs_plate.set("0")
        if (self.ItemVar62.get()==1):
            self.seventykgs_plate_entry.configure(state="normal")
        elif self.ItemVar62.get()==0:
            self.seventykgs_plate_entry.configure(state=DISABLED)
            self.variable_seventykgs_plate.set("0")
        if (self.ItemVar63.get()==1):
            self.seventyfivekgs_plate_entry.configure(state="normal")
        elif self.ItemVar63.get()==0:
            self.seventyfivekgs_plate_entry.configure(state=DISABLED)
            self.variable_seventyfivekgs_plate.set("0")
        if (self.ItemVar64.get()==1):
            self.eightykgs_plate_entry.configure(state="normal")
        elif self.ItemVar64.get()==0:
            self.eightykgs_plate_entry.configure(state=DISABLED)
            self.variable_eightykgs_plate.set("0")
class ordering_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
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
    def total_price(self):
        self.ReceiptButton = tk.Button(self, padx = 16, pady = 1, bd =4,font=('arial', 10, 'bold'), width = 14,height = 4, text = "Receipt", command =self.receipt, bg = "light blue", state = NORMAL)
        self.ReceiptButton.place(x=690, y=420)
        Item1=float((app.windows["barbells_page"]).variable_fivekgs_barbell.get()) 
        Item2=float((app.windows["barbells_page"]).variable_tenkgs_barbell.get()) 
        Item3=float((app.windows["barbells_page"]).variable_fifteenkgs_barbell.get())
        Item4=float((app.windows["barbells_page"]).variable_twentykgs_barbell.get())
        Item5=float((app.windows["barbells_page"]).variable_twentyfivekgs_barbell.get())
        Item6=float((app.windows["barbells_page"]).variable_thirtykgs_barbell.get())
        Item7=float((app.windows["barbells_page"]).variable_thirtykgs_barbell.get())
        Item8=float((app.windows["barbells_page"]).variable_fourtykgs_barbell.get())
        Item9=float((app.windows["barbells_page"]).variable_fourtyfivekgs_barbell.get())
        Item10=float((app.windows["barbells_page"]).variable_fiftykgs_barbell.get())
        Item11=float((app.windows["barbells_page"]).variable_fiftyfivekgs_barbell.get())
        Item12=float((app.windows["barbells_page"]).variable_sixtykgs_barbell.get())
        Item13=float((app.windows["barbells_page"]).variable_sixtyfivekgs_barbell.get())
        Item14=float((app.windows["barbells_page"]).variable_seventykgs_barbell.get())
        Item15=float((app.windows["barbells_page"]).variable_seventyfivekgs_barbell.get())
        Item16=float((app.windows["barbells_page"]).variable_eightykgs_barbell.get())

        Item17=float((app.windows["dumbbells_page"]).variable_fivekgs_dumbbell.get())
        Item18=float((app.windows["dumbbells_page"]).variable_tenkgs_dumbbell.get())
        Item19=float((app.windows["dumbbells_page"]).variable_fifteenkgs_dumbbell.get())
        Item20=float((app.windows["dumbbells_page"]).variable_twentykgs_dumbbell.get())
        Item21=float((app.windows["dumbbells_page"]).variable_twentyfivekgs_dumbbell.get())
        Item22=float((app.windows["dumbbells_page"]).variable_thirtykgs_dumbbell.get())
        Item23=float((app.windows["dumbbells_page"]).variable_thirtyfivekgs_dumbbell.get())
        Item24=float((app.windows["dumbbells_page"]).variable_fourtykgs_dumbbell.get())
        Item25=float((app.windows["dumbbells_page"]).variable_fourtyfivekgs_dumbbell.get())
        Item26=float((app.windows["dumbbells_page"]).variable_fiftykgs_dumbbell.get())
        Item27=float((app.windows["dumbbells_page"]).variable_fiftyfivekgs_dumbbell.get())
        Item28=float((app.windows["dumbbells_page"]).variable_sixtykgs_dumbbell.get())
        Item29=float((app.windows["dumbbells_page"]).variable_sixtyfivekgs_dumbbell.get())
        Item30=float((app.windows["dumbbells_page"]).variable_seventykgs_dumbbell.get())
        Item31=float((app.windows["dumbbells_page"]).variable_seventyfivekgs_dumbbell.get())
        Item32=float((app.windows["dumbbells_page"]).variable_eightykgs_dumbbell.get())

        Item33=float((app.windows["machines_page"]).variable_treadmill.get())
        Item34=float((app.windows["machines_page"]).variable_chestpress.get())
        Item35=float((app.windows["machines_page"]).variable_pecfly.get())
        Item36=float((app.windows["machines_page"]).variable_seatedrow.get())
        Item37=float((app.windows["machines_page"]).variable_latpulldown.get())
        Item38=float((app.windows["machines_page"]).variable_ergometer.get())
        Item39=float((app.windows["machines_page"]).variable_stairmaster.get())
        Item40=float((app.windows["machines_page"]).variable_smithmachine.get())
        Item41=float((app.windows["machines_page"]).variable_abcrunch.get())
        Item42=float((app.windows["machines_page"]).variable_legextension.get())
        Item43=float((app.windows["machines_page"]).variable_legpress.get())
        Item44=float((app.windows["machines_page"]).variable_elliptical.get())
        Item45=float((app.windows["machines_page"]).variable_standingcalfraise.get())
        Item46=float((app.windows["machines_page"]).variable_shoulderpress.get())
        Item47=float((app.windows["machines_page"]).variable_legcurls.get())
        Item48=float((app.windows["machines_page"]).variable_deltoidraise.get())

        Item49=float((app.windows["plates_page"]).variable_fivekgs_plate.get())
        Item50=float((app.windows["plates_page"]).variable_tenkgs_plate.get())
        Item51=float((app.windows["plates_page"]).variable_fifteenkgs_plate.get())
        Item52=float((app.windows["plates_page"]).variable_twentykgs_plate.get())
        Item53=float((app.windows["plates_page"]).variable_twentyfivekgs_plate.get())
        Item54=float((app.windows["plates_page"]).variable_thirtykgs_plate.get())
        Item55=float((app.windows["plates_page"]).variable_thirtyfivekgs_plate.get())
        Item56=float((app.windows["plates_page"]).variable_fourtykgs_plate.get())
        Item57=float((app.windows["plates_page"]).variable_fourtyfivekgs_plate.get())
        Item58=float((app.windows["plates_page"]).variable_fiftykgs_plate.get())
        Item59=float((app.windows["plates_page"]).variable_fiftyfivekgs_plate.get())
        Item60=float((app.windows["plates_page"]).variable_sixtykgs_plate.get())
        Item61=float((app.windows["plates_page"]).variable_sixtyfivekgs_plate.get())
        Item62=float((app.windows["plates_page"]).variable_seventykgs_plate.get())
        Item63=float((app.windows["plates_page"]).variable_seventyfivekgs_plate.get())
        Item64=float((app.windows["plates_page"]).variable_eightykgs_plate.get())

       
            


        self.price_of_barbells=(Item1 * 15) + (Item2 * 30) + (Item3 * 45) + (Item4 * 60) + (Item5 * 75) + (Item6 * 90) + (Item7 * 105) + (Item8 * 120)+ (Item9 * 135) + (Item10 * 150) + (Item11 * 165) + (Item12 * 180) + (Item13 * 195) + (Item14 * 210) + (Item15 * 225) + (Item16 * 240)
        self.price_of_dumbbells= (Item17 * 10) + (Item18 * 20) + (Item19 * 30) + (Item20 * 40) + (Item21 * 50) + (Item22 * 60) + (Item23 * 70) + (Item24 * 80)+ (Item25 * 90) + (Item26 * 100) + (Item27 * 110) + (Item28 * 120) + (Item29 * 130) + (Item30 * 140) + (Item31 * 150) + (Item32 * 160)
        self.price_of_machines=(Item33 * 900) + (Item34 * 1000) + (Item35 * 800) + (Item36 * 750) + (Item37 * 900) + (Item38 * 800) + (Item39 * 2000) + (Item40 * 700)+ (Item41 * 650) + (Item42 * 970) + (Item43 * 1300) + (Item44 * 1200) + (Item45 * 740) + (Item46 * 1100) + (Item47 * 1600) + (Item48 * 840)
        self.price_of_plates=(Item49 * 10) + (Item50 * 20) + (Item51 * 30) + (Item52 * 40) + (Item53 * 50) + (Item54 * 60) + (Item55 * 70) + (Item56 * 80)+ (Item57 * 90) + (Item58 * 100) + (Item59 * 110) + (Item60 * 120) + (Item61 * 130) + (Item62 * 140) + (Item63 * 150) + (Item64 * 160)

        SubTotalofITEMS = '$ ' +str ('%.2f'%(self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates + 5.50))
        self.SubTotal.set(SubTotalofITEMS)
        delivery_tip_float = '$ ' + str('%.2f'%(5.50))
        self.DeliveryTip.set(delivery_tip_float)

        tax_float = ((self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates + 5.50)*0.15)
        total_cost_float = '$ ' + str ('%.2f'%(self.price_of_barbells + self.price_of_dumbbells + self.price_of_machines + self.price_of_plates + 5.50 + tax_float))
        self.TotalCost.set(total_cost_float)
    
    def reset_data(self):
        self.DeliveryTip.set("")
        self.SubTotal.set("")
        self.TotalCost.set("")
        #=============================================Unchecking checkbuttons=====================================
        for widget in (app.windows["plates_page"]).FrameTwo.winfo_children() and (app.windows["barbells_page"]).FrameTwo.winfo_children():
            if widget.winfo_class() == "Checkbutton":
                widget.deselect()
        for widget in (app.windows["machines_page"]).FrameTwo.winfo_children() and (app.windows["dumbbells_page"]).FrameTwo.winfo_children():
            if widget.winfo_class() == "Checkbutton":
                widget.deselect()
        for widget in (app.windows["plates_page"]).FrameThree.winfo_children() and (app.windows["barbells_page"]).FrameThree.winfo_children():
            if widget.winfo_class() == "Checkbutton":
                widget.deselect()
        for widget in (app.windows["machines_page"]).FrameThree.winfo_children() and (app.windows["dumbbells_page"]).FrameThree.winfo_children():
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
     
        
      #  for widget in (app.windows["plates_page"]).winfo_children():
         #   if widget.winfo_class() == "Entry":
       #         print('detected entry widget')
        #        print(f'widget type: {widget.winfo_class()}')
        #    else:
       #         print(f'widget type: {widget.winfo_class()}')

    def receipt(self):
        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))
        self.Receipt_Text = tk.Text(self, font=('arial',10, 'bold'), bd = 8, width = 66, height =20, state = NORMAL)
        self.Receipt_Text.place(x=870, y=420)
        self.Receipt_Text.insert(END, 'Delivery Tip:\t' + self.DeliveryTip.get() + '\nTotal Cost:\t ' + self.TotalCost.get() + "\n")
        
if __name__ == "__main__": #Prevents parts of code from being run when modules are imported. 
    app = Main()
    app.resizable(width=False, height=False)
    app.geometry("1366x768")
    app.mainloop()