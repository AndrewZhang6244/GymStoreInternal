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
        button_properties = {'font': ('arial', 12), 'width': 36, 'height': 2, 'bd': 15, 'background': 'light blue'}
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
       
        home_button = tk.Button(FrameOne, text = "Home", command = lambda:manager.show_window("home_page"), **button_properties)
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, text = "Barbells", command = lambda:manager.show_window("barbells_page"), **button_properties) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne, text = "Dumbbells", command = lambda:manager.show_window("dumbbells_page"), **button_properties) 
        dumbbells_button.pack(side=TOP) #Dumbbells button
        machines_button = tk.Button(FrameOne, text = "Machines", command = lambda:manager.show_window("machines_page"), **button_properties) 
        machines_button.pack(side=TOP) #Machines button
        plates_button = tk.Button(FrameOne, text = "Plates", command = lambda:manager.show_window("plates_page"), **button_properties) 
        plates_button.pack(side=TOP) #Plates button
        ordering_button = tk.Button(FrameOne, text = "Finish Ordering", command = lambda:manager.show_window("ordering_page"), **button_properties) 
        ordering_button.pack(side=TOP) #Ordering button.
        exit_button = tk.Button(FrameOne, text = "Exit", command = manager.exit, **button_properties) 
        exit_button.pack(side=TOP)#Exit button
#=======================================================Barbells page====================================
class barbells_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        button_properties = {'font': ('arial', 12), 'width': 36, 'height': 2, 'bd': 15, 'background': 'light blue'}
        entry_properties = {'font': ('arial', 13, 'bold'), 'bd': 8, 'width': 6, 'justify': 'left', 'state': DISABLED}
        barbell_checkbutton_properties = {'font': ('arial', 13, 'bold'), 'offvalue': 0, 'onvalue': 1, 'background': 'light blue','command' : self.barbell_checked_checkbuttons}
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

       
        home_button = tk.Button(FrameOne, text = "Home", command = lambda:manager.show_window("home_page"), **button_properties)
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, text = "Barbells", command = lambda:manager.show_window("barbells_page"), **button_properties) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne, text = "Dumbbells", command = lambda:manager.show_window("dumbbells_page"), **button_properties) 
        dumbbells_button.pack(side=TOP)#Dumbells button
        machines_button = tk.Button(FrameOne, text = "Machines", command = lambda:manager.show_window("machines_page"), **button_properties) 
        machines_button.pack(side=TOP)#Machines button
        plates_button = tk.Button(FrameOne, text = "Plates", command = lambda:manager.show_window("plates_page"), **button_properties) 
        plates_button.pack(side=TOP)#Plates button
        ordering_button = tk.Button(FrameOne, text = "Finish Ordering", command = lambda:manager.show_window("ordering_page"), **button_properties) 
        ordering_button.pack(side=TOP)#Ordering button
        exit_button = tk.Button(FrameOne, text = "Exit", command = manager.exit, **button_properties) 
        exit_button.pack(side=TOP)#Exit button
        #===============================================================Variables===================================

        self.item_var_barbells = {checkbutton: IntVar() for checkbutton in range(0, 17, 1)}
        
        self.barbells = {weight: StringVar() for weight in range(5, 85, 5)}
        self.barbells_entry = {weight: StringVar() for weight in range(5, 85, 5)}
        barbell_items = [self.barbells[5], self.barbells[10],self.barbells[15],self.barbells[20],self.barbells[25],self.barbells[30],self.barbells[35],self.barbells[40],self.barbells[45], self.barbells[50], self.barbells[55],self.barbells[60],self.barbells[65],self.barbells[70],self.barbells[75],self.barbells[80]]
        for i in barbell_items:
            i.set("0")
        #===================================================Widgets for barbell items===========================================
        #===================================================First section for barbell items=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Barbells 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        
        
        fivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 5kgs ($15.00)\t\t" ,variable = self.item_var_barbells[1],**barbell_checkbutton_properties ).grid(row=1, sticky =W)
        tenkgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 10kgs ($30.00) " , variable = self.item_var_barbells[2],**barbell_checkbutton_properties ).grid(row=2, sticky =W)
        fifteenkgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 15kgs ($45.00)" , variable = self.item_var_barbells[3],**barbell_checkbutton_properties).grid(row=3, sticky =W)
        twentykgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 20kgs ($60.00) ", variable = self.item_var_barbells[4],**barbell_checkbutton_properties).grid(row=4, sticky =W)
        twentyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 25kg ($75.00) ",variable = self.item_var_barbells[5],**barbell_checkbutton_properties ).grid(row=5, sticky =W)
        thirtykgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 30kgs ($90.00) ",variable = self.item_var_barbells[6],**barbell_checkbutton_properties).grid(row=6, sticky =W)
        thirtyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 35kgs ($105.00) ", variable = self.item_var_barbells[7],**barbell_checkbutton_properties ).grid(row=7, sticky =W)
        fourtykgs_barbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Barbell 40kgs ($120.00) ", variable = self.item_var_barbells[8], **barbell_checkbutton_properties).grid(row=8, sticky =W)
        self.barbells_entry[5] = tk.Entry(self.FrameTwo,textvariable = self.barbells[5], **entry_properties)
        self.barbells_entry[5].grid(row =1, column = 1)
        self.barbells_entry[10] = tk.Entry(self.FrameTwo,textvariable =  self.barbells[10], **entry_properties)
        self.barbells_entry[10].grid(row =2, column = 1)
        self.barbells_entry[15] = tk.Entry(self.FrameTwo,textvariable =  self.barbells[15], **entry_properties)
        self.barbells_entry[15].grid(row =3, column = 1)
        self.barbells_entry[20] = tk.Entry(self.FrameTwo,textvariable =  self.barbells[20], **entry_properties)
        self.barbells_entry[20].grid(row =4, column = 1)
        self.barbells_entry[25] = tk.Entry(self.FrameTwo,textvariable =  self.barbells[25], **entry_properties)
        self.barbells_entry[25].grid(row =5, column = 1)
        self.barbells_entry[30] = tk.Entry(self.FrameTwo,textvariable =  self.barbells[30], **entry_properties)
        self.barbells_entry[30].grid(row =6, column = 1)
        self.barbells_entry[35] = tk.Entry(self.FrameTwo,textvariable =  self.barbells[35], **entry_properties)
        self.barbells_entry[35].grid(row =7, column = 1)
        self.barbells_entry[40] = tk.Entry(self.FrameTwo, textvariable =  self.barbells[40], **entry_properties)
        self.barbells_entry[40].grid(row =8, column = 1)
        #=====================================================================Second section for barbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Barbells 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 45kgs ($135.00) \t\t", variable = self.item_var_barbells[9], **barbell_checkbutton_properties).grid(row=1, sticky =W)
        fiftykgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 50kgs ($150.00) \t", variable = self.item_var_barbells[10], **barbell_checkbutton_properties).grid(row=2, sticky =W)
        fiftyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 55kgs ($165.00) \t", variable = self.item_var_barbells[11], **barbell_checkbutton_properties).grid(row=3, sticky =W)
        sixtykgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 60kgs ($180.00)\t", variable = self.item_var_barbells[12],**barbell_checkbutton_properties).grid(row=4, sticky =W)
        sixtyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 65kgs ($195.00) \t", variable = self.item_var_barbells[13],**barbell_checkbutton_properties).grid(row=5, sticky =W)
        seventyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 70kgs ($210.00) \t", variable = self.item_var_barbells[14], **barbell_checkbutton_properties).grid(row=6, sticky =W)
        seventyfivekgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 75kgs ($225.00) \t", variable = self.item_var_barbells[15], **barbell_checkbutton_properties).grid(row=7, sticky =W)
        eightykgs_barbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Barbell 80kgs ($240.00) \t",variable = self.item_var_barbells[16], **barbell_checkbutton_properties).grid(row=8, sticky =W)
        self.barbells_entry[45] = tk.Entry(self.FrameThree,textvariable = self.barbells[45],**entry_properties)
        self.barbells_entry[45].grid(row =1, column = 1)
        self.barbells_entry[50] = tk.Entry(self.FrameThree,textvariable =  self.barbells[50],**entry_properties)
        self.barbells_entry[50].grid(row=2, column=1)
        self.barbells_entry[55] = tk.Entry(self.FrameThree,textvariable = self.barbells[55],**entry_properties)
        self.barbells_entry[55].grid(row =3, column = 1)
        self.barbells_entry[60] = tk.Entry(self.FrameThree,textvariable =self.barbells[60],**entry_properties)
        self.barbells_entry[60].grid(row =4, column = 1)
        self.barbells_entry[65] = tk.Entry(self.FrameThree,textvariable =  self.barbells[65],**entry_properties)
        self.barbells_entry[65].grid(row =5, column = 1)
        self.barbells_entry[70] = tk.Entry(self.FrameThree,textvariable =  self.barbells[70],**entry_properties)
        self.barbells_entry[70].grid(row =6, column = 1)
        self.barbells_entry[75] = tk.Entry(self.FrameThree,textvariable =  self.barbells[75],**entry_properties)
        self.barbells_entry[75].grid(row =7, column = 1)
        self.barbells_entry[80] = tk.Entry(self.FrameThree, textvariable =  self.barbells[80],**entry_properties)
        self.barbells_entry[80].grid(row =8, column = 1)  
        
    def barbell_checked_checkbuttons(self):
        for i in range(1, 17):
            value1 = self.item_var_barbells[i].get()
            if value1 == 1:
                self.barbells_entry[i*5].config(state=NORMAL)
            elif value1 == 0:
                self.barbells[i*5].set("0")
                self.barbells_entry[i*5].configure(state=DISABLED)
                
#======================================================Dumbells page===================================
class dumbbells_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        button_properties = {'font': ('arial', 12), 'width': 36, 'height': 2, 'bd': 15, 'background': 'light blue'}
        entry_properties = {'font': ('arial', 13, 'bold'), 'bd': 8, 'width': 6, 'justify': 'left', 'state': DISABLED}
        dumbbell_checkbutton_properties = {'font': ('arial', 13, 'bold'), 'offvalue': 0, 'onvalue': 1, 'background': 'light blue','command' : self.dumbbell_checked_checkbuttons}
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

       
        home_button = tk.Button(FrameOne, text = "Home", command = lambda:manager.show_window("home_page"), **button_properties)
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, text = "Barbells", command = lambda:manager.show_window("barbells_page"), **button_properties) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne,  text = "Dumbbells", command = lambda:manager.show_window("dumbbells_page"), **button_properties) 
        dumbbells_button.pack(side=TOP)#Dumbells button
        machines_button = tk.Button(FrameOne, text = "Machines", command = lambda:manager.show_window("machines_page"), **button_properties) 
        machines_button.pack(side=TOP)#Machines button
        plates_button = tk.Button(FrameOne, text = "Plates", command = lambda:manager.show_window("plates_page"), **button_properties) 
        plates_button.pack(side=TOP)#Plates button
        ordering_button = tk.Button(FrameOne, text = "Finish Ordering", command = lambda:manager.show_window("ordering_page"), **button_properties) 
        ordering_button.pack(side=TOP)#Ordering button
        exit_button = tk.Button(FrameOne, text = "Exit", command = manager.exit, **button_properties) 
        exit_button.pack(side=TOP)#Exit button
        #===============================================================Variables===================================
        
        
        self.item_var_dumbbells = {checkbutton: IntVar() for checkbutton in range(1, 17, 1)}
        self.dumbbells_entry = {weight: StringVar() for weight in range(5, 85, 5)}
        self.dumbbells = {weight: StringVar() for weight in range(5, 85, 5)}
        dumbbell_items = [self.dumbbells[5], self.dumbbells[10],self.dumbbells[15],self.dumbbells[20],self.dumbbells[25],self.dumbbells[30],self.dumbbells[35],self.dumbbells[40],self.dumbbells[45], self.dumbbells[50], self.dumbbells[55],self.dumbbells[60],self.dumbbells[65],self.dumbbells[70],self.dumbbells[75],self.dumbbells[80]]
        for i in dumbbell_items:
            i.set("0")
        #===================================================Widgets for dumbbell items===========================================
        #===================================================First section for dumbell items=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Dumbbells 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        fivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 5kgs ($10.00)\t\t" ,variable = self.item_var_dumbbells[1], **dumbbell_checkbutton_properties).grid(row=1, sticky =W)
        tenkgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 10kgs ($20.00) " , variable = self.item_var_dumbbells[2], **dumbbell_checkbutton_properties).grid(row=2, sticky =W)
        fifteenkgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 15kgs ($30.00) " , variable = self.item_var_dumbbells[3],**dumbbell_checkbutton_properties).grid(row=3, sticky =W)
        twentykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 20kgs ($40.00) ", variable = self.item_var_dumbbells[4],**dumbbell_checkbutton_properties).grid(row=4, sticky =W)
        twentyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 25kgs ($50.00) ",variable = self.item_var_dumbbells[5], **dumbbell_checkbutton_properties).grid(row=5, sticky =W)
        thirtykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 30kgs ($60.00) ",variable = self.item_var_dumbbells[6], **dumbbell_checkbutton_properties).grid(row=6, sticky =W)
        thirtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 35kgs ($70.00) ", variable = self.item_var_dumbbells[7],**dumbbell_checkbutton_properties).grid(row=7, sticky =W)
        fourtykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Dumbbell 40kgs ($80.00) ",variable = self.item_var_dumbbells[8],**dumbbell_checkbutton_properties).grid(row=8, sticky =W)
        self.dumbbells_entry[5]= tk.Entry(self.FrameTwo,textvariable = self.dumbbells[5], **entry_properties)
        self.dumbbells_entry[5].grid(row =1, column = 1)
        self.dumbbells_entry[10]= tk.Entry(self.FrameTwo,textvariable = self.dumbbells[10], **entry_properties)
        self.dumbbells_entry[10].grid(row =2, column = 1)
        self.dumbbells_entry[15] = tk.Entry(self.FrameTwo,textvariable = self.dumbbells[15], **entry_properties)
        self.dumbbells_entry[15].grid(row =3, column = 1)
        self.dumbbells_entry[20] = tk.Entry(self.FrameTwo,textvariable = self.dumbbells[20], **entry_properties)
        self.dumbbells_entry[20].grid(row =4, column = 1)
        self.dumbbells_entry[25] = tk.Entry(self.FrameTwo, textvariable = self.dumbbells[25], **entry_properties)
        self.dumbbells_entry[25].grid(row =5, column = 1)
        self.dumbbells_entry[30] = tk.Entry(self.FrameTwo,textvariable = self.dumbbells[30] ,**entry_properties)
        self.dumbbells_entry[30].grid(row =6, column = 1)
        self.dumbbells_entry[35] = tk.Entry(self.FrameTwo, textvariable = self.dumbbells[35], **entry_properties)
        self.dumbbells_entry[35].grid(row =7, column = 1)
        self.dumbbells_entry[40] = tk.Entry(self.FrameTwo, textvariable = self.dumbbells[40], **entry_properties)
        self.dumbbells_entry[40].grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Dumbbells 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 45kgs ($90.00)\t\t", variable = self.item_var_dumbbells[9], **dumbbell_checkbutton_properties).grid(row=1, sticky =W)
        fiftykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 50kgs ($100.00)\t", variable = self.item_var_dumbbells[10], **dumbbell_checkbutton_properties).grid(row=2, sticky =W)
        fiftyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 55kgs ($110.00)\t", variable = self.item_var_dumbbells[11], **dumbbell_checkbutton_properties).grid(row=3, sticky =W)
        sixtykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 60kgs ($120.00)\t", variable = self.item_var_dumbbells[12], **dumbbell_checkbutton_properties).grid(row=4, sticky =W)
        sixtyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 65kgs ($130.00) \t", variable = self.item_var_dumbbells[13], **dumbbell_checkbutton_properties).grid(row=5, sticky =W)
        seventyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 70kgs ($140.00) \t", variable = self.item_var_dumbbells[14],**dumbbell_checkbutton_properties).grid(row=6, sticky =W)
        seventyfivekgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 75kgs ($150.00) \t", variable = self.item_var_dumbbells[15],**dumbbell_checkbutton_properties).grid(row=7, sticky =W)
        eightykgs_dumbbell_checkbutton = tk.Checkbutton(self.FrameThree, text ="Dumbbell 80kgs ($160.00) \t",variable = self.item_var_dumbbells[16], **dumbbell_checkbutton_properties).grid(row=8, sticky =W)
        self.dumbbells_entry[45] = tk.Entry(self.FrameThree, textvariable = self.dumbbells[45], **entry_properties)
        self.dumbbells_entry[45].grid(row =1, column = 1)
        self.dumbbells_entry[50]= tk.Entry(self.FrameThree, textvariable = self.dumbbells[50], **entry_properties)
        self.dumbbells_entry[50].grid(row =2, column = 1)
        self.dumbbells_entry[55] = tk.Entry(self.FrameThree,textvariable =self.dumbbells[55], **entry_properties)
        self.dumbbells_entry[55].grid(row =3, column = 1)
        self.dumbbells_entry[60]= tk.Entry(self.FrameThree, textvariable =self.dumbbells[60], **entry_properties)
        self.dumbbells_entry[60].grid(row =4, column = 1)
        self.dumbbells_entry[65] = tk.Entry(self.FrameThree, textvariable = self.dumbbells[65], **entry_properties)
        self.dumbbells_entry[65].grid(row =5, column = 1)
        self.dumbbells_entry[70] = tk.Entry(self.FrameThree, textvariable = self.dumbbells[70], **entry_properties)
        self.dumbbells_entry[70].grid(row =6, column = 1)
        self.dumbbells_entry[75] = tk.Entry(self.FrameThree, textvariable = self.dumbbells[75], **entry_properties)
        self.dumbbells_entry[75].grid(row =7, column = 1)
        self.dumbbells_entry[80] = tk.Entry(self.FrameThree,  textvariable = self.dumbbells[80], **entry_properties)
        self.dumbbells_entry[80].grid(row =8, column = 1)   
    def dumbbell_checked_checkbuttons(self):
        for i in range(1, 17):
            value2 = self.item_var_dumbbells[i].get()
            if value2 == 1:
                self.dumbbells_entry[i*5].config(state=NORMAL)
            elif value2 == 0:
                self.dumbbells[i*5].set("0")
                self.dumbbells_entry[i*5].configure(state=DISABLED)
                
    
        
#======================================================Machines page=======================================
class machines_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        button_properties = {'font': ('arial', 12), 'width': 36, 'height': 2, 'bd': 15, 'background': 'light blue'}
        entry_properties = {'font': ('arial', 13, 'bold'), 'bd': 8, 'width': 6, 'justify': 'left', 'state': DISABLED}
        machine_checkbutton_properties = {'font': ('arial', 13, 'bold'), 'offvalue': 0, 'onvalue': 1, 'background': 'light blue','command' : self.machine_checked_checkbuttons}
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

        home_button = tk.Button(FrameOne,text = "Home",command = lambda:manager.show_window("home_page"),**button_properties)
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, text = "Barbells",command = lambda:manager.show_window("barbells_page"),**button_properties) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne, text = "Dumbbells",command = lambda:manager.show_window("dumbbells_page"),**button_properties) 
        dumbbells_button.pack(side=TOP)#Dumbells button
        machines_button = tk.Button(FrameOne, text = "Machines",command = lambda:manager.show_window("machines_page"),**button_properties) 
        machines_button.pack(side=TOP)#Machines button
        plates_button = tk.Button(FrameOne,text = "Plates", command = lambda:manager.show_window("plates_page"),**button_properties) 
        plates_button.pack(side=TOP)#Plates button
        ordering_button = tk.Button(FrameOne, text = "Finish Ordering",command = lambda:manager.show_window("ordering_page"),**button_properties) 
        ordering_button.pack(side=TOP)#Ordering button
        exit_button = tk.Button(FrameOne, text = "Exit",command = manager.exit, **button_properties) 
        exit_button.pack(side=TOP)#Exit button
        #===============================================================Variables===================================
       
        
        self.item_var_machines = {checkbutton: IntVar() for checkbutton in range(0, 17, 1)}
        self.machines_entry = {weight: StringVar() for weight in range(5, 85, 5)}
        self.machines = {weight: StringVar() for weight in range(5, 85, 5)}
        machine_items = [self.machines[5] ,self.machines[10] ,self.machines[15] ,self.machines[20] ,self.machines[25],self.machines[30],self.machines[35],self.machines[40],self.machines[45],self.machines[50] ,self.machines[55] ,self.machines[60],self.machines[65] ,self.machines[70] ,self.machines[75],self.machines[80]]
        for i in machine_items:
            i.set("0")
        #===================================================Widgets for machiness==========================================
        #===================================================First section for machines=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Machines 1: ",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0) 
        treadmill_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Treadmill ($900.00)\t\t" ,variable = self.item_var_machines[1], **machine_checkbutton_properties).grid(row=1, sticky =W)
        chestpress_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Chest press ($1000.00)" , variable = self.item_var_machines[2],**machine_checkbutton_properties).grid(row=2, sticky =W)
        pecfly_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Pecfly ($800.00)" ,variable = self.item_var_machines[3], **machine_checkbutton_properties).grid(row=3, sticky =W)
        seatedrow_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Seated row ($750.00)",variable = self.item_var_machines[4], **machine_checkbutton_properties).grid(row=4, sticky =W)
        latpulldown_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Lat pull down ($900.00)",variable = self.item_var_machines[5],**machine_checkbutton_properties).grid(row=5, sticky =W)
        ergometer_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Ergometer ($800.00)",variable = self.item_var_machines[6],**machine_checkbutton_properties).grid(row=6, sticky =W)
        stairmaster_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Stairmaster ($2000.00)",variable = self.item_var_machines[7], **machine_checkbutton_properties).grid(row=7, sticky =W)
        smithmachine_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Smithmachine ($700.00)",variable = self.item_var_machines[8],**machine_checkbutton_properties).grid(row=8, sticky =W)
        self.machines_entry[5]= tk.Entry(self.FrameTwo,textvariable = self.machines[5], **entry_properties)
        self.machines_entry[5].grid(row =1, column = 1) 
        self.machines_entry[10] = tk.Entry(self.FrameTwo,textvariable = self.machines[10],**entry_properties)
        self.machines_entry[10].grid(row =2, column = 1)
        self.machines_entry[15]=tk.Entry(self.FrameTwo,textvariable = self.machines[15], **entry_properties)
        self.machines_entry[15].grid(row =3, column = 1)
        self.machines_entry[20] = tk.Entry(self.FrameTwo,textvariable = self.machines[20], **entry_properties)
        self.machines_entry[20].grid(row =4, column = 1)
        self.machines_entry[25] = tk.Entry(self.FrameTwo,textvariable = self.machines[25],**entry_properties)
        self.machines_entry[25].grid(row =5, column = 1)
        self.machines_entry[30] = tk.Entry(self.FrameTwo,textvariable = self.machines[30] ,**entry_properties)
        self.machines_entry[30].grid(row =6, column = 1)
        self.machines_entry[35] = tk.Entry(self.FrameTwo,textvariable = self.machines[35], **entry_properties)
        self.machines_entry[35].grid(row =7, column = 1)
        self.machines_entry[40] = tk.Entry(self.FrameTwo, textvariable = self.machines[40],**entry_properties)
        self.machines_entry[40].grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Machines 2: ",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        row_checkbutton = tk.Checkbutton(self.FrameThree, text ="Ab crunch ($650.00)\t\t", variable = self.item_var_machines[9],**machine_checkbutton_properties).grid(row=1, sticky =W)
        legextension_checkbutton = tk.Checkbutton(self.FrameThree, text ="Leg extension ($970.00)\t",variable = self.item_var_machines[10], **machine_checkbutton_properties).grid(row=2, sticky =W)
        legpress_checkbutton = tk.Checkbutton(self.FrameThree, text ="Leg press ($1300.00)\t", variable = self.item_var_machines[11], **machine_checkbutton_properties).grid(row=3, sticky =W)
        elliptical_checkbutton = tk.Checkbutton(self.FrameThree, text ="Elliptical ($1200.00)\t", variable = self.item_var_machines[12], **machine_checkbutton_properties).grid(row=4, sticky =W)
        standingcalfraise_checkbutton = tk.Checkbutton(self.FrameThree, text ="Standing calf raise ($740.00)\t", variable = self.item_var_machines[13], **machine_checkbutton_properties).grid(row=5, sticky =W)
        shoulderpress_checkbutton = tk.Checkbutton(self.FrameThree, text ="Shoulder press ($1100.00)\t",variable = self.item_var_machines[14], **machine_checkbutton_properties).grid(row=6, sticky =W)
        legcurls_checkbutton = tk.Checkbutton(self.FrameThree, text ="Leg curls ($1600.00)\t", variable = self.item_var_machines[15], **machine_checkbutton_properties).grid(row=7, sticky =W)
        deltoidraise_checkbutton = tk.Checkbutton(self.FrameThree, text ="Deltoid raise ($840.00)\t",variable = self.item_var_machines[16], **machine_checkbutton_properties).grid(row=8, sticky =W)
        self.machines_entry[45]= tk.Entry(self.FrameThree,textvariable = self.machines[45], **entry_properties)
        self.machines_entry[45].grid(row =1, column = 1)
        self.machines_entry[50] = tk.Entry(self.FrameThree,textvariable = self.machines[50],**entry_properties)
        self.machines_entry[50].grid(row =2, column = 1)
        self.machines_entry[55]= tk.Entry(self.FrameThree,textvariable =self.machines[55], **entry_properties)
        self.machines_entry[55].grid(row =3, column = 1)
        self.machines_entry[60] = tk.Entry(self.FrameThree,textvariable =self.machines[60],**entry_properties)
        self.machines_entry[60].grid(row =4, column = 1)
        self.machines_entry[65] = tk.Entry(self.FrameThree,textvariable = self.machines[65],**entry_properties)
        self.machines_entry[65].grid(row =5, column = 1)
        self.machines_entry[70] = tk.Entry(self.FrameThree,textvariable = self.machines[70], **entry_properties)
        self.machines_entry[70].grid(row =6, column = 1)
        self.machines_entry[75]= tk.Entry(self.FrameThree,textvariable = self.machines[75], **entry_properties)
        self.machines_entry[75].grid(row =7, column = 1)
        self.machines_entry[80] = tk.Entry(self.FrameThree, textvariable = self.machines[80],**entry_properties)
        self.machines_entry[80].grid(row =8, column = 1)   
    def machine_checked_checkbuttons(self):
        for i in range(1, 17):
            value3 = self.item_var_machines[i].get()
            if value3 == 1:
                self.machines_entry[i*5].config(state=NORMAL)
            elif value3 == 0:
                self.machines[i*5].set("0")
                self.machines_entry[i*5].configure(state=DISABLED)
#=====================================================Weight plates page=====================================
class plates_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        button_properties = {'font': ('arial', 12), 'width': 36, 'height': 2, 'bd': 15, 'background': 'light blue'}
        entry_properties = {'font': ('arial', 13, 'bold'), 'bd': 8, 'width': 6, 'justify': 'left', 'state': DISABLED}
        plate_checkbutton_properties = {'font': ('arial', 13, 'bold'), 'offvalue': 0, 'onvalue': 1, 'background': 'light blue','command' : self.plate_checked_checkbuttons}
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

       
        home_button = tk.Button(FrameOne,  text = "Home", command = lambda:manager.show_window("home_page"),**button_properties)
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, text = "Barbells", command = lambda:manager.show_window("barbells_page"),**button_properties) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne, text = "Dumbbells", command = lambda:manager.show_window("dumbbells_page"),**button_properties) 
        dumbbells_button.pack(side=TOP)#Dumbells button
        machines_button = tk.Button(FrameOne, text = "Machines", command = lambda:manager.show_window("machines_page"),**button_properties) 
        machines_button.pack(side=TOP)#Machines button
        plates_button = tk.Button(FrameOne, text = "Plates", command = lambda:manager.show_window("plates_page"),**button_properties) 
        plates_button.pack(side=TOP)#Plates button
        ordering_button = tk.Button(FrameOne, text = "Finish Ordering", command = lambda:manager.show_window("ordering_page"),**button_properties) 
        ordering_button.pack(side=TOP)#Ordering button
        exit_button = tk.Button(FrameOne, text = "Exit", command = manager.exit,**button_properties) 
        exit_button.pack(side=TOP)#Exit button
        #===============================================================Variables===================================
         
        self.item_var_plates = {checkbutton: IntVar() for checkbutton in range(1, 17, 1)}
        self.plates_entry = {weight: StringVar() for weight in range(5, 85, 5)}
        self.plates = {weight: StringVar() for weight in range(5, 85, 5)}
        plate_items = [self.plates[5], self.plates[10],self.plates[15],self.plates[20],self.plates[25],self.plates[30],self.plates[35],self.plates[40],self.plates[45], self.plates[50], self.plates[55],self.plates[60],self.plates[65],self.plates[70],self.plates[75],self.plates[80]]
        for i in plate_items:
            i.set("0")
        #===================================================Widgets for plate items===========================================
        #===================================================First section for plate items=============================================
        FirstLabel = tk.Label(self.FrameTwo, font=('arial',15, 'bold'),text = "Plates 5-40 kgs",bd=10, background = "light blue")
        FirstLabel.grid(row=0,column=0)
        fivekgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 5kgs ($10.00)\t\t" ,variable = self.item_var_plates[1], **plate_checkbutton_properties).grid(row=1, sticky =W)
        tenkgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 10kgs ($20.00)" ,variable = self.item_var_plates[2], **plate_checkbutton_properties).grid(row=2, sticky =W)
        fifteenkgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 15kgs ($30.00)" ,variable = self.item_var_plates[3], **plate_checkbutton_properties).grid(row=3, sticky =W)
        twentykgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 20kgs ($40.00)",variable = self.item_var_plates[4], **plate_checkbutton_properties).grid(row=4, sticky =W)
        twentyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 25kgs ($50.00)",variable = self.item_var_plates[5],**plate_checkbutton_properties).grid(row=5, sticky =W)
        thirtykgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 30kgs ($60.00)",variable = self.item_var_plates[6], **plate_checkbutton_properties).grid(row=6, sticky =W)
        thirtyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 35kgs ($70.00)",variable = self.item_var_plates[7], **plate_checkbutton_properties).grid(row=7, sticky =W)
        fourtykgs_plate_checkbutton = tk.Checkbutton(self.FrameTwo, text ="Plate 40kgs ($80.00)", variable = self.item_var_plates[8],**plate_checkbutton_properties).grid(row=8, sticky =W)
        self.plates_entry[5] = tk.Entry(self.FrameTwo,textvariable = self.plates[5], **entry_properties)
        self.plates_entry[5].grid(row =1, column = 1)
        self.plates_entry[10]= tk.Entry(self.FrameTwo,textvariable = self.plates[10], **entry_properties)
        self.plates_entry[10].grid(row =2, column = 1)
        self.plates_entry[15] = tk.Entry(self.FrameTwo,textvariable =self.plates[15],**entry_properties)
        self.plates_entry[15].grid(row =3, column = 1)
        self.plates_entry[20] = tk.Entry(self.FrameTwo,textvariable = self.plates[20], **entry_properties)
        self.plates_entry[20].grid(row =4, column = 1)
        self.plates_entry[25] = tk.Entry(self.FrameTwo,textvariable = self.plates[25], **entry_properties)
        self.plates_entry[25].grid(row =5, column = 1)
        self.plates_entry[30] = tk.Entry(self.FrameTwo,textvariable = self.plates[30] ,**entry_properties)
        self.plates_entry[30].grid(row =6, column = 1)
        self.plates_entry[35] = tk.Entry(self.FrameTwo,textvariable = self.plates[35], **entry_properties)
        self.plates_entry[35].grid(row =7, column = 1)
        self.plates_entry[40]= tk.Entry(self.FrameTwo, textvariable = self.plates[40], **entry_properties)
        self.plates_entry[40].grid(row =8, column = 1)
        #=====================================================================Second section for dumbbell items================================
        SecondLabel = tk.Label(self.FrameThree, font=('arial',15, 'bold'),text = "Plates 45-80 kgs",bd=10, background = "light blue")
        SecondLabel.grid(row=0,column=0)
        fourtyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 45kgs ($90.00)\t\t",variable = self.item_var_plates[9],**plate_checkbutton_properties).grid(row=1, sticky =W)
        fiftykgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 50kgs ($100.00)\t",variable = self.item_var_plates[10], **plate_checkbutton_properties).grid(row=2, sticky =W)
        fiftyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 55kgs ($110.00)\t",variable = self.item_var_plates[11], **plate_checkbutton_properties).grid(row=3, sticky =W)
        sixtykgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 60kgs ($120.00)\t",variable = self.item_var_plates[12],**plate_checkbutton_properties).grid(row=4, sticky =W)
        sixtyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 65kgs ($130.00)\t",variable = self.item_var_plates[13], **plate_checkbutton_properties).grid(row=5, sticky =W)
        seventyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 70kgs ($140.00)\t",variable = self.item_var_plates[14], **plate_checkbutton_properties).grid(row=6, sticky =W)
        seventyfivekgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 75kgs ($150.00)\t",variable = self.item_var_plates[15], **plate_checkbutton_properties).grid(row=7, sticky =W)
        eightykgs_plate_checkbutton = tk.Checkbutton(self.FrameThree, text ="Plate 80kgs ($160.00)\t",variable = self.item_var_plates[16], **plate_checkbutton_properties).grid(row=8, sticky =W)
        self.plates_entry[45] = tk.Entry(self.FrameThree,textvariable = self.plates[45], **entry_properties)
        self.plates_entry[45].grid(row =1, column = 1)
        self.plates_entry[50] = tk.Entry(self.FrameThree,textvariable = self.plates[50], **entry_properties)
        self.plates_entry[50].grid(row =2, column = 1)
        self.plates_entry[55]= tk.Entry(self.FrameThree,textvariable =self.plates[55],**entry_properties)
        self.plates_entry[55].grid(row =3, column = 1)
        self.plates_entry[60] = tk.Entry(self.FrameThree,textvariable =self.plates[60], **entry_properties)
        self.plates_entry[60].grid(row =4, column = 1)
        self.plates_entry[65] = tk.Entry(self.FrameThree,textvariable = self.plates[65], **entry_properties)
        self.plates_entry[65].grid(row =5, column = 1)
        self.plates_entry[70] = tk.Entry(self.FrameThree,textvariable = self.plates[70], **entry_properties)
        self.plates_entry[70].grid(row =6, column = 1)
        self.plates_entry[75]= tk.Entry(self.FrameThree,textvariable = self.plates[75], **entry_properties)
        self.plates_entry[75].grid(row =7, column = 1)
        self.plates_entry[80] = tk.Entry(self.FrameThree, textvariable = self.plates[80], **entry_properties)
        self.plates_entry[80].grid(row =8, column = 1)   
    def plate_checked_checkbuttons(self):
        for i in range(1,17):
            value4 = self.item_var_plates[i].get()
            if value4 == 1:
                self.plates_entry[i*5].config(state=NORMAL)
            elif value4 == 0:
                self.plates[i*5].set("0")
                self.plates_entry[i*5].configure(state=DISABLED)
class ordering_page(tk.Frame):  
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        button_properties = {'font': ('arial', 12), 'width': 36, 'height': 2, 'bd': 15, 'background': 'light blue'}
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
    
        home_button = tk.Button(FrameOne,  text = "Home", command = lambda:manager.show_window("home_page"),**button_properties)
        home_button.pack(side=TOP) #Home button
        barbells_button = tk.Button(FrameOne, text = "Barbells", command = lambda:manager.show_window("barbells_page"),**button_properties) 
        barbells_button.pack(side=TOP) #Barbells button
        dumbbells_button = tk.Button(FrameOne, text = "Dumbbells", command = lambda:manager.show_window("dumbbells_page"),**button_properties) 
        dumbbells_button.pack(side=TOP)#Dumbells button
        machines_button = tk.Button(FrameOne, text = "Machines", command = lambda:manager.show_window("machines_page"),**button_properties) 
        machines_button.pack(side=TOP)#Machines button
        plates_button = tk.Button(FrameOne, text = "Plates", command = lambda:manager.show_window("plates_page"),**button_properties) 
        plates_button.pack(side=TOP)#Plates button
        ordering_button = tk.Button(FrameOne, text = "Finish Ordering", command = lambda:manager.show_window("ordering_page"),**button_properties) 
        ordering_button.pack(side=TOP)#Ordering button
        exit_button = tk.Button(FrameOne, text = "Exit", command = manager.exit, **button_properties) 
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
        try:
            self.price_of_barbells=(float((app.windows["barbells_page"]).barbells[5].get())  * 15) + (float((app.windows["barbells_page"]).barbells[10].get())  * 30) + (float((app.windows["barbells_page"]).barbells[15].get())  * 45) + (float((app.windows["barbells_page"]).barbells[20].get())  * 60) + (float((app.windows["barbells_page"]).barbells[25].get())  * 75) + (float((app.windows["barbells_page"]).barbells[30].get())  * 90) + (float((app.windows["barbells_page"]).barbells[35].get())  * 105) + (float((app.windows["barbells_page"]).barbells[40].get())  * 120)+ (float((app.windows["barbells_page"]).barbells[45].get())  * 135) + (float((app.windows["barbells_page"]).barbells[50].get())  * 150) + (float((app.windows["barbells_page"]).barbells[55].get())  * 165) + (float((app.windows["barbells_page"]).barbells[60].get())  * 180) + (float((app.windows["barbells_page"]).barbells[65].get())  * 195) + (float((app.windows["barbells_page"]).barbells[70].get())  * 210) + (float((app.windows["barbells_page"]).barbells[75].get())  * 225) + (float((app.windows["barbells_page"]).barbells[80].get())  * 240)
            self.price_of_dumbbells= (float((app.windows["dumbbells_page"]).dumbbells[5].get()) * 10) + (float((app.windows["dumbbells_page"]).dumbbells[10].get()) * 20) + (float((app.windows["dumbbells_page"]).dumbbells[15].get()) * 30) + (float((app.windows["dumbbells_page"]).dumbbells[20].get()) * 40) + (float((app.windows["dumbbells_page"]).dumbbells[25].get()) * 50) + (float((app.windows["dumbbells_page"]).dumbbells[30].get())* 60) + (float((app.windows["dumbbells_page"]).dumbbells[35].get()) * 70) + (float((app.windows["dumbbells_page"]).dumbbells[40].get()) * 80)+ (float((app.windows["dumbbells_page"]).dumbbells[45].get()) * 90) + (float((app.windows["dumbbells_page"]).dumbbells[50].get()) * 100) + (float((app.windows["dumbbells_page"]).dumbbells[55].get()) * 110) + (float((app.windows["dumbbells_page"]).dumbbells[60].get()) * 120) + (float((app.windows["dumbbells_page"]).dumbbells[65].get()) * 130) + (float((app.windows["dumbbells_page"]).dumbbells[70].get()) * 140) + (float((app.windows["dumbbells_page"]).dumbbells[75].get()) * 150) + (float((app.windows["dumbbells_page"]).dumbbells[80].get()) * 160)
            self.price_of_machines=(float((app.windows["machines_page"]).machines[5].get()) * 900) + (float((app.windows["machines_page"]).machines[10].get()) * 1000) + (float((app.windows["machines_page"]).machines[15].get()) * 800) + (float((app.windows["machines_page"]).machines[20].get()) * 750) + (float((app.windows["machines_page"]).machines[25].get()) * 900) + (float((app.windows["machines_page"]).machines[30].get()) * 800) + (float((app.windows["machines_page"]).machines[35].get()) * 2000) + (float((app.windows["machines_page"]).machines[40].get()) * 700)+ (float((app.windows["machines_page"]).machines[45].get()) * 650) + (float((app.windows["machines_page"]).machines[50].get()) * 970) + (float((app.windows["machines_page"]).machines[55].get()) * 1300) + (float((app.windows["machines_page"]).machines[60].get()) * 1200) + (float((app.windows["machines_page"]).machines[65].get()) * 740) + (float((app.windows["machines_page"]).machines[70].get()) * 1100) + (float((app.windows["machines_page"]).machines[75].get()) * 1600) + (float((app.windows["machines_page"]).machines[80].get()) * 840)
            self.price_of_plates=(float((app.windows["plates_page"]).plates[5].get()) * 10) + (float((app.windows["plates_page"]).plates[10].get()) * 20) + (float((app.windows["plates_page"]).plates[15].get())* 30) + (float((app.windows["plates_page"]).plates[20].get()) * 40) + (float((app.windows["plates_page"]).plates[25].get()) * 50) + (float((app.windows["plates_page"]).plates[30].get()) * 60) + (float((app.windows["plates_page"]).plates[35].get()) * 70) + (float((app.windows["plates_page"]).plates[40].get()) * 80)+ (float((app.windows["plates_page"]).plates[45].get()) * 90) + (float((app.windows["plates_page"]).plates[50].get()) * 100) + (float((app.windows["plates_page"]).plates[55].get()) * 110) + (float((app.windows["plates_page"]).plates[60].get())* 120) + (float((app.windows["plates_page"]).plates[65].get()) * 130) + (float((app.windows["plates_page"]).plates[70].get()) * 140) + (float((app.windows["plates_page"]).plates[75].get()) * 150) + (float((app.windows["plates_page"]).plates[80].get())* 160) 
        except:
            error = messagebox.showerror("Error", "Please enter a number of items you would like")
            return
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
                self.pickupcost()
        else:
            self.pickupcost()
    def pickupcost(self):
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
        pages = "barbells dumbbells machines plates"
        self.reset_checkbutton(pages, "FrameTwo")
        self.reset_checkbutton(pages, "FrameThree")
        self.reset_entry(pages, "FrameTwo")
        self.reset_entry(pages, "FrameThree")
        #=============================================Unchecking checkbuttons=====================================
    def reset_checkbutton(self, pages, frame):
        for page in pages.split():
            f = getattr(app.windows[page + '_page'], frame)
            for widget in f.winfo_children():
                if widget.winfo_class() == "Checkbutton":
                    widget.deselect()

        #============================================Setting entries to zero and disabling entries===========================
    def reset_entry(self, pages, frame):
        for page in pages.split():
            f = getattr(app.windows[page + '_page'], frame)
            for widget in f.winfo_children():
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
    app.geometry("1366x768")
    app.mainloop()