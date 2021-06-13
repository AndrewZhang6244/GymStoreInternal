#=========================Imports=====================
import tkinter as tk                
from tkinter import font as tkfont  
from tkinter import *
from tkinter import ttk
from random import *
from tkinter import messagebox
import os
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
        self.windows["barbells_page"] = barbells_page( manager=self, parent=manager) #Creates gym_store window
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
    def check_value_checkbuttons(self):
        if (self.ItemVar49.get()==1):
            self.plates[5].configure(state=NORMAL)
        elif self.ItemVar49.get()==0:
            self.plates[5].configure(state=DISABLED)
            self.plates[5].set("0")
        
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
        FrameTwo = tk.Frame(self, width = 900, height = 350, bd = 8, relief ="raise", background = "light blue")
        FrameTwo.pack(side=RIGHT) #Second frame for the design
        FrameTwoFront = tk.Label(FrameTwo, width = 60, height = 540, bd = 8,text = "Welcome to our gym store, to use this \nprogram, click on the desired windows shown\n to the left and tick the items you would like to buy.\n Once you have ticked the items, please enter\n the number of items you would like to buy\n and then proceed to the finish ordering window \nwhere you can find your receipt and the total price. \nIf you have chosen the delivery option, please enter\n your delivery address." ,relief = "raise", background = "light blue",font=('Helvactical bold', 20))
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
        FrameTwo = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        FrameTwo.place(x=374, y=403) #Second frame
        FrameThree = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        FrameThree.place(x=960, y=403) #Third frame
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

        self.variable_fivekgs_barbell.set("0")
        self.variable_tenkgs_barbell.set("0")
        self.variable_fifteenkgs_barbell.set("0")
        self.variable_twentykgs_barbell.set("0")
        self.variable_twentyfivekgs_barbell.set("0")
        self.variable_thirtykgs_barbell.set("0")
        self.variable_thirtyfivekgs_barbell.set("0")
        self.variable_fourtykgs_barbell.set("0")
        self.variable_fourtyfivekgs_barbell.set("0")
        self.variable_fiftykgs_barbell.set("0")
        self.variable_fiftyfivekgs_barbell.set("0")
        self.variable_sixtykgs_barbell.set("0")
        self.variable_sixtyfivekgs_barbell.set("0")
        self.variable_seventykgs_barbell.set("0")
        self.variable_seventyfivekgs_barbell.set("0")
        self.variable_eightykgs_barbell.set("0")

        
        #===================================================Widgets for barbell items===========================================
        #===================================================First section for barbell items=============================================
        FirstLabel = tk.Label(FrameTwo, font=('arial',15, 'bold'),text = "Barbells 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        fivekgs_barbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Barbell 5kgs ($15.00)\t\t" ,variable = self.ItemVar1, onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        tenkgs_barbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Barbell 10kgs ($30.00) " , variable = self.ItemVar2, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fifteenkgs_barbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Barbell 15kgs ($45.00)" , variable = self.ItemVar3, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        twentykgs_barbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Barbell 20kgs ($60.00) ", variable = self.ItemVar4, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        twentyfivekgs_barbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Barbell 25kg ($75.00) ",variable = self.ItemVar5, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        thirtykgs_barbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Barbell 30kgs ($90.00) ",variable = self.ItemVar6, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        thirtyfivekgs_barbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Barbell 35kgs ($105.00) ", variable = self.ItemVar7, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        fourtykgs_barbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Barbell 40kgs ($120.00) ", variable = self.ItemVar8, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        fivekgs_barbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_fivekgs_barbell, state = DISABLED)
        fivekgs_barbell_entry.grid(row =1, column = 1)
        tenkgs_barbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_tenkgs_barbell, state = DISABLED)
        tenkgs_barbell_entry.grid(row =2, column = 1)
        fifteenkgs_barbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_fifteenkgs_barbell, state = DISABLED)
        fifteenkgs_barbell_entry.grid(row =3, column = 1)
        twentykgs_barbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_twentykgs_barbell, state = DISABLED)
        twentykgs_barbell_entry.grid(row =4, column = 1)
        twentyfivekgs_barbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_twentyfivekgs_barbell, state = DISABLED)
        twentyfivekgs_barbell_entry.grid(row =5, column = 1)
        thirtykgs_barbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_thirtykgs_barbell ,state = DISABLED)
        thirtykgs_barbell_entry.grid(row =6, column = 1)
        thirtyfivekgs_barbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_thirtyfivekgs_barbell, state = DISABLED)
        thirtyfivekgs_barbell_entry.grid(row =7, column = 1)
        fourtykgs_barbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable = self.variable_fourtykgs_barbell, state = DISABLED)
        fourtykgs_barbell_entry.grid(row =8, column = 1)
        #=====================================================================Second section for barbell items================================
        SecondLabel = tk.Label(FrameThree, font=('arial',15, 'bold'),text = "Barbells 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_barbell_checkbutton = tk.Checkbutton(FrameThree, text ="Barbell 45kgs ($135.00) \t\t", variable = self.ItemVar9, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        fiftykgs_barbell_checkbutton = tk.Checkbutton(FrameThree, text ="Barbell 50kgs ($150.00) \t", variable = self.ItemVar10, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fiftyfivekgs_barbell_checkbutton = tk.Checkbutton(FrameThree, text ="Barbell 55kgs ($165.00) \t", variable = self.ItemVar11, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        sixtykgs_barbell_checkbutton = tk.Checkbutton(FrameThree, text ="Barbell 60kgs ($180.00)\t", variable = self.ItemVar12, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        sixtyfivekgs_barbell_checkbutton = tk.Checkbutton(FrameThree, text ="Barbell 65kgs ($195.00) \t", variable = self.ItemVar13, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        seventyfivekgs_barbell_checkbutton = tk.Checkbutton(FrameThree, text ="Barbell 70kgs ($210.00) \t", variable = self.ItemVar14, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        seventyfivekgs_barbell_checkbutton = tk.Checkbutton(FrameThree, text ="Barbell 75kgs ($225.00) \t", variable = self.ItemVar15, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        eightykgs_barbell_checkbutton = tk.Checkbutton(FrameThree, text ="Barbell 80kgs ($240.00) \t",variable = self.ItemVar16, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        fourtyfivekgs_barbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_fourtyfivekgs_barbell, state = DISABLED)
        fourtyfivekgs_barbell_entry.grid(row =1, column = 1)
        fiftykgs_barbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_fiftykgs_barbell, state = DISABLED)
        fiftykgs_barbell_entry.grid(row =2, column = 1)
        fiftyfivekgs_barbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_fiftyfivekgs_barbell, state = DISABLED)
        fiftyfivekgs_barbell_entry.grid(row =3, column = 1)
        sixtykgs_barbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_sixtykgs_barbell, state = DISABLED)
        sixtykgs_barbell_entry.grid(row =4, column = 1)
        sixtyfivekgs_barbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_sixtyfivekgs_barbell, state = DISABLED)
        sixtyfivekgs_barbell_entry.grid(row =5, column = 1)
        seventykgs_barbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_sixtykgs_barbell, state = DISABLED)
        seventykgs_barbell_entry.grid(row =6, column = 1)
        seventyfivekgs_barbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_sixtyfivekgs_barbell, state = DISABLED)
        seventyfivekgs_barbell_entry.grid(row =7, column = 1)
        eightykgs_barbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable = self.variable_seventykgs_barbell, state = DISABLED)
        eightykgs_barbell_entry.grid(row =8, column = 1)   
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
        FrameTwo = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        FrameTwo.place(x=374, y=403) #Second frame
        FrameThree = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        FrameThree.place(x=960, y=403) #Third frame
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

        self.variable_fivekgs_dumbbell.set("0")
        self.variable_tenkgs_dumbbell.set("0")
        self.variable_fifteenkgs_dumbbell.set("0")
        self.variable_twentykgs_dumbbell.set("0")
        self.variable_twentyfivekgs_dumbbell.set("0")
        self.variable_thirtykgs_dumbbell.set("0")
        self.variable_thirtyfivekgs_dumbbell.set("0")
        self.variable_fourtykgs_dumbbell.set("0")
        self.variable_fourtyfivekgs_dumbbell.set("0")
        self.variable_fiftykgs_dumbbell.set("0")
        self.variable_fiftyfivekgs_dumbbell.set("0")
        self.variable_sixtykgs_dumbbell.set("0")
        self.variable_sixtyfivekgs_dumbbell.set("0")
        self.variable_seventykgs_dumbbell.set("0")
        self.variable_seventyfivekgs_dumbbell.set("0")
        self.variable_eightykgs_dumbbell.set("0")
        
        #===================================================Widgets for dumbbell items===========================================
        #===================================================First section for dumbell items=============================================
        FirstLabel = tk.Label(FrameTwo, font=('arial',15, 'bold'),text = "Dumbbells 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        fivekgs_dumbbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Dumbbell 5kgs ($10.00)\t\t" ,variable = self.ItemVar17, onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        tenkgs_dumbbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Dumbbell 10kgs ($20.00) " , variable = self.ItemVar18, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fifteenkgs_dumbbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Dumbbell 15kgs ($30.00) " , variable = self.ItemVar19, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        twentykgs_dumbbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Dumbbell 20kgs ($40.00) ", variable = self.ItemVar20, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        twentyfivekgs_dumbbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Dumbbell 25kgs ($50.00) ",variable = self.ItemVar21, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        thirtykgs_dumbbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Dumbbell 30kgs ($60.00) ",variable = self.ItemVar22, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        thirtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Dumbbell 35kgs ($70.00) ", variable = self.ItemVar23, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        fourtykgs_dumbbell_checkbutton = tk.Checkbutton(FrameTwo, text ="Dumbbell 40kgs ($80.00) ", variable = self.ItemVar24, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        fivekgs_dumbbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_fivekgs_dumbbell, state = DISABLED)
        fivekgs_dumbbell_entry.grid(row =1, column = 1)
        tenkgs_dumbbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_tenkgs_dumbbell, state = DISABLED)
        tenkgs_dumbbell_entry.grid(row =2, column = 1)
        fifteenkgs_dumbbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_fifteenkgs_dumbbell, state = DISABLED)
        fifteenkgs_dumbbell_entry.grid(row =3, column = 1)
        twentykgs_dumbbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_twentykgs_dumbbell, state = DISABLED)
        twentykgs_dumbbell_entry.grid(row =4, column = 1)
        twentyfivekgs_dumbbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_twentyfivekgs_dumbbell, state = DISABLED)
        twentyfivekgs_dumbbell_entry.grid(row =5, column = 1)
        thirtykgs_dumbbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_thirtykgs_dumbbell ,state = DISABLED)
        thirtykgs_dumbbell_entry.grid(row =6, column = 1)
        thirtyfivekgs_dumbbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_thirtyfivekgs_dumbbell, state = DISABLED)
        thirtyfivekgs_dumbbell_entry.grid(row =7, column = 1)
        fourtykgs_dumbbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable = self.variable_fourtykgs_dumbbell, state = DISABLED)
        fourtykgs_dumbbell_entry.grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(FrameThree, font=('arial',15, 'bold'),text = "Dumbbells 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(FrameThree, text ="Dumbbell 45kgs ($90.00)\t\t", variable = self.ItemVar25, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        fiftykgs_dumbbell_checkbutton = tk.Checkbutton(FrameThree, text ="Dumbbell 50kgs ($100.00)\t", variable = self.ItemVar26, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fiftyfivekgs_dumbbell_checkbutton = tk.Checkbutton(FrameThree, text ="Dumbbell 55kgs ($110.00)\t", variable = self.ItemVar27, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        sixtykgs_dumbbell_checkbutton = tk.Checkbutton(FrameThree, text ="Dumbbell 60kgs ($120.00)\t", variable = self.ItemVar28, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        sixtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(FrameThree, text ="Dumbbell 65kgs ($130.00) \t", variable = self.ItemVar29, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        seventyfivekgs_dumbbell_checkbutton = tk.Checkbutton(FrameThree, text ="Dumbbell 70kgs ($140.00) \t", variable = self.ItemVar30, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        seventyfivekgs_dumbbell_checkbutton = tk.Checkbutton(FrameThree, text ="Dumbbell 75kgs ($150.00) \t", variable = self.ItemVar31, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        eightykgs_dumbbell_checkbutton = tk.Checkbutton(FrameThree, text ="Dumbbell 80kgs ($160.00) \t",variable = self.ItemVar32, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        fourtyfivekgs_dumbbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_fourtyfivekgs_dumbbell, state = DISABLED)
        fourtyfivekgs_dumbbell_entry.grid(row =1, column = 1)
        fiftykgs_dumbbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_fiftykgs_dumbbell, state = DISABLED)
        fiftykgs_dumbbell_entry.grid(row =2, column = 1)
        fiftyfivekgs_dumbbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_fiftyfivekgs_dumbbell, state = DISABLED)
        fiftyfivekgs_dumbbell_entry.grid(row =3, column = 1)
        sixtykgs_dumbbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_sixtykgs_dumbbell, state = DISABLED)
        sixtykgs_dumbbell_entry.grid(row =4, column = 1)
        sixtyfivekgs_dumbbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_sixtyfivekgs_dumbbell, state = DISABLED)
        sixtyfivekgs_dumbbell_entry.grid(row =5, column = 1)
        seventykgs_dumbbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_sixtykgs_dumbbell, state = DISABLED)
        seventykgs_dumbbell_entry.grid(row =6, column = 1)
        seventyfivekgs_dumbbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_sixtyfivekgs_dumbbell, state = DISABLED)
        seventyfivekgs_dumbbell_entry.grid(row =7, column = 1)
        eightykgs_dumbbell_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable = self.variable_seventykgs_dumbbell, state = DISABLED)
        eightykgs_dumbbell_entry.grid(row =8, column = 1)   
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
        FrameTwo = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        FrameTwo.place(x=374, y=403) #Second frame
        FrameThree = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        FrameThree.place(x=960, y=403) #Third frame
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
        
        self.variable_treadmill.set("0")
        self.variable_chestpress.set("0")
        self.variable_pecfly.set("0")
        self.variable_seatedrow.set("0")
        self.variable_latpulldown.set("0")
        self.variable_ergometer.set("0")
        self.variable_stairmaster.set("0")
        self.variable_smithmachine.set("0")
        self.variable_abcrunch.set("0")
        self.variable_legextension.set("0")
        self.variable_legpress.set("0")
        self.variable_elliptical.set("0")
        self.variable_standingcalfraise.set("0")
        self.variable_shoulderpress.set("0")
        self.variable_legcurls.set("0")
        self.variable_deltoidraise.set("0")
        #===================================================Widgets for machiness==========================================
        #===================================================First section for machines=============================================
        FirstLabel = tk.Label(FrameTwo, font=('arial',15, 'bold'),text = "Machines 1: ",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        treadmill_checkbutton = tk.Checkbutton(FrameTwo, text ="Treadmill ($900.00)\t\t" ,variable = self.ItemVar33, onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        chestpress_checkbutton = tk.Checkbutton(FrameTwo, text ="Chest press ($1000.00)" , variable = self.ItemVar34, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        pecfly_checkbutton = tk.Checkbutton(FrameTwo, text ="Pecfly ($800.00)" , variable = self.ItemVar35, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        seatedrow_checkbutton = tk.Checkbutton(FrameTwo, text ="Seated row ($750.00)", variable = self.ItemVar36, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        latpulldown_checkbutton = tk.Checkbutton(FrameTwo, text ="Lat pull down ($900.00)",variable = self.ItemVar37, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        ergometer_checkbutton = tk.Checkbutton(FrameTwo, text ="Ergometer ($800.00)",variable = self.ItemVar38, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        stairmaster_checkbutton = tk.Checkbutton(FrameTwo, text ="Stairmaster ($2000.00)", variable = self.ItemVar39, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        smithmachine_checkbutton = tk.Checkbutton(FrameTwo, text ="Smithmachine ($700.00)", variable = self.ItemVar40, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        treadmill_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_treadmill, state = DISABLED)
        treadmill_entry.grid(row =1, column = 1)
        chestpress_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_chestpress, state = DISABLED)
        chestpress_entry.grid(row =2, column = 1)
        pecfly_dumbbell_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_pecfly, state = DISABLED)
        pecfly_dumbbell_entry.grid(row =3, column = 1)
        seatedrow_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_seatedrow, state = DISABLED)
        seatedrow_entry.grid(row =4, column = 1)
        latpulldown_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_latpulldown, state = DISABLED)
        latpulldown_entry.grid(row =5, column = 1)
        ergometer_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_ergometer ,state = DISABLED)
        ergometer_entry.grid(row =6, column = 1)
        stairmaster_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.variable_stairmaster, state = DISABLED)
        stairmaster_entry.grid(row =7, column = 1)
        smithmachine_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable = self.variable_smithmachine, state = DISABLED)
        smithmachine_entry.grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(FrameThree, font=('arial',15, 'bold'),text = "Machines 2: ",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        row_checkbutton = tk.Checkbutton(FrameThree, text ="Ab crunch ($650.00)\t\t", variable = self.ItemVar41, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        legextension_checkbutton = tk.Checkbutton(FrameThree, text ="Leg extension ($970.00)\t", variable = self.ItemVar42, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        legpress_checkbutton = tk.Checkbutton(FrameThree, text ="Leg press ($1300.00)\t", variable = self.ItemVar43, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        elliptical_checkbutton = tk.Checkbutton(FrameThree, text ="Elliptical ($1200.00)\t", variable = self.ItemVar44, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        standingcalfraise_checkbutton = tk.Checkbutton(FrameThree, text ="Standing calf raise ($740.00)\t", variable = self.ItemVar45, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        shoulderpress_checkbutton = tk.Checkbutton(FrameThree, text ="Shoulder press ($1100.00)\t", variable = self.ItemVar46, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        legcurls_checkbutton = tk.Checkbutton(FrameThree, text ="Leg curls ($1600.00)\t", variable = self.ItemVar47, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        deltoidraise_checkbutton = tk.Checkbutton(FrameThree, text ="Deltoid raise ($840.00)\t",variable = self.ItemVar48, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        abcrunch_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_abcrunch, state = DISABLED)
        abcrunch_entry.grid(row =1, column = 1)
        legextension_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_legextension, state = DISABLED)
        legextension_entry.grid(row =2, column = 1)
        legpress_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_legpress, state = DISABLED)
        legpress_entry.grid(row =3, column = 1)
        elliptical_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.variable_elliptical, state = DISABLED)
        elliptical_entry.grid(row =4, column = 1)
        standingcalfraise_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_standingcalfraise, state = DISABLED)
        standingcalfraise_entry.grid(row =5, column = 1)
        shoulderpress_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_shoulderpress, state = DISABLED)
        shoulderpress_entry.grid(row =6, column = 1)
        legcurls_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.variable_legcurls, state = DISABLED)
        legcurls_entry.grid(row =7, column = 1)
        deltoidraise_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable = self.variable_deltoidraise, state = DISABLED)
        deltoidraise_entry.grid(row =8, column = 1)   
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
        FrameTwo = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        FrameTwo.place(x=374, y=403) #Second frame
        FrameThree = tk.Frame(self, width = 500, height = 365, bd = 8, relief ="raise", background = "light blue")
        FrameThree.place(x=960, y=403) #Third frame
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

        self.plates = {}
        for i in range(1, 17):
            self.plates[i*5] = StringVar()
            self.plates[i*5].set("0")
        #===================================================Widgets for plate items===========================================
        #===================================================First section for plate items=============================================
        FirstLabel = tk.Label(FrameTwo, font=('arial',15, 'bold'),text = "Plates 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        fivekgs_plate_checkbutton = tk.Checkbutton(FrameTwo, text ="Plate 5kgs ($10.00)\t\t" ,variable = self.ItemVar49,command = lambda: app.check_value_checkbuttons(), onvalue = 1, background = "light blue", offvalue = 0, font=('arial',13, 'bold')).grid(row=1, sticky =W)
        tenkgs_plate_checkbutton = tk.Checkbutton(FrameTwo, text ="Plate 10kgs ($10.00)" , variable = self.ItemVar50, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fifteenkgs_plate_checkbutton = tk.Checkbutton(FrameTwo, text ="Plate 15kgs ($10.00)" , variable = self.ItemVar51, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        twentykgs_plate_checkbutton = tk.Checkbutton(FrameTwo, text ="Plate 20kgs ($10.00)", variable = self.ItemVar52, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        twentyfivekgs_plate_checkbutton = tk.Checkbutton(FrameTwo, text ="Plate 25kgs ($10.00)",variable = self.ItemVar53, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        thirtykgs_plate_checkbutton = tk.Checkbutton(FrameTwo, text ="Plate 30kgs ($10.00)",variable = self.ItemVar54, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        thirtyfivekgs_plate_checkbutton = tk.Checkbutton(FrameTwo, text ="Plate 35kgs ($10.00)", variable = self.ItemVar55, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        fourtykgs_plate_checkbutton = tk.Checkbutton(FrameTwo, text ="Plate 40kgs ($10.00)", variable = self.ItemVar56, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        fivekgs_plate_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[5], state = DISABLED)
        fivekgs_plate_entry.grid(row =1, column = 1)
        tenkgs_plate_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[10], state = DISABLED)
        tenkgs_plate_entry.grid(row =2, column = 1)
        fifteenkgs_plate_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[15], state = DISABLED)
        fifteenkgs_plate_entry.grid(row =3, column = 1)
        twentykgs_plate_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[20], state = DISABLED)
        twentykgs_plate_entry.grid(row =4, column = 1)
        twentyfivekgs_plate_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[25], state = DISABLED)
        twentyfivekgs_plate_entry.grid(row =5, column = 1)
        thirtykgs_plate_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[30] ,state = DISABLED)
        thirtykgs_plate_entry.grid(row =6, column = 1)
        thirtyfivekgs_plate_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left',textvariable = self.plates[35], state = DISABLED)
        thirtyfivekgs_plate_entry.grid(row =7, column = 1)
        fourtykgs_plate_entry = tk.Entry(FrameTwo, font=('arial',13, 'bold'), bd = 8, width = 6, justify ='left', textvariable = self.plates[40], state = DISABLED)
        fourtykgs_plate_entry.grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(FrameThree, font=('arial',15, 'bold'),text = "Plates 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_plate_checkbutton = tk.Checkbutton(FrameThree, text ="Plate 45kgs ($10.00)\t\t", variable = self.ItemVar57, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=1, sticky =W)
        fiftykgs_plate_checkbutton = tk.Checkbutton(FrameThree, text ="Plate 50kgs ($10.00)\t", variable = self.ItemVar58, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=2, sticky =W)
        fiftyfivekgs_plate_checkbutton = tk.Checkbutton(FrameThree, text ="Plate 55kgs ($10.00)\t", variable = self.ItemVar59, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=3, sticky =W)
        sixtykgs_plate_checkbutton = tk.Checkbutton(FrameThree, text ="Plate 60kgs ($10.00)\t", variable = self.ItemVar60, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=4, sticky =W)
        sixtyfivekgs_plate_checkbutton = tk.Checkbutton(FrameThree, text ="Plate 65kgs ($10.00)\t", variable = self.ItemVar61, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=5, sticky =W)
        seventyfivekgs_plate_checkbutton = tk.Checkbutton(FrameThree, text ="Plate 70kgs ($10.00)\t", variable = self.ItemVar62, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=6, sticky =W)
        seventyfivekgs_plate_checkbutton = tk.Checkbutton(FrameThree, text ="Plate 75kgs ($10.00)\t", variable = self.ItemVar63, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=7, sticky =W)
        eightykgs_plate_checkbutton = tk.Checkbutton(FrameThree, text ="Plate 80kgs ($10.00)\t",variable = self.ItemVar64, onvalue = 1, offvalue = 0, font=('arial',13, 'bold'), background = "light blue").grid(row=8, sticky =W)
        fourtyfivekgs_plate_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.plates[45], state = DISABLED)
        fourtyfivekgs_plate_entry.grid(row =1, column = 1)
        fiftykgs_plate_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.plates[50], state = DISABLED)
        fiftykgs_plate_entry.grid(row =2, column = 1)
        fiftyfivekgs_plate_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.plates[55], state = DISABLED)
        fiftyfivekgs_plate_entry.grid(row =3, column = 1)
        sixtykgs_plate_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable =self.plates[60], state = DISABLED)
        sixtykgs_plate_entry.grid(row =4, column = 1)
        sixtyfivekgs_plate_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.plates[65], state = DISABLED)
        sixtyfivekgs_plate_entry.grid(row =5, column = 1)
        seventykgs_plate_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.plates[70], state = DISABLED)
        seventykgs_plate_entry.grid(row =6, column = 1)
        seventyfivekgs_plate_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6,textvariable = self.plates[75], state = DISABLED)
        seventyfivekgs_plate_entry.grid(row =7, column = 1)
        eightykgs_plate_entry = tk.Entry(FrameThree, font=('arial',13, 'bold'), bd = 8, width = 6, textvariable = self.plates[80], state = DISABLED)
        eightykgs_plate_entry.grid(row =8, column = 1)   

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
        FrameTwo = tk.Frame(self, width = 500, height = 350, bd = 8, relief ="raise", background = "light blue")
        FrameTwo.place(x=374, y=417) #Second frame
        FrameThree = tk.Frame(self, width = 500, height = 350, bd = 8, relief ="raise", background = "light blue")
        FrameThree.place(x=870, y=417) #Third frame


    
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
        ButtonTotal.place(x=380, y=680)
        ButtonReset = tk.Button(self, padx = 16, pady = 1, bd =4,font=('arial', 10, 'bold'), width = 14,height = 4, text = "Reset", command =self.reset_data, bg = "light blue")
        ButtonReset.place(x=535, y=680)
        ReceiptButton = tk.Button(self, padx = 16, pady = 1, bd =4,font=('arial', 10, 'bold'), width = 14,height = 4, text = "Reset", command =self.receipt, bg = "light blue")
        ReceiptButton.place(x=690, y=680)
        Receipt_Text = Text(FrameThree, font=('arial',10, 'bold'), bd = 8, width = 66, height =20)
        Receipt_Text.grid(row =1, column = 0)
    def total_price(self):
        return
    def reset_data(self):
        return
    def receipt(self):
        return
    
if __name__ == "__main__": #Prevents parts of code from being run when modules are imported. 
    app = Main()
    app.resizable(width=False, height=False)
    app.geometry("1366x768")
    app.mainloop()