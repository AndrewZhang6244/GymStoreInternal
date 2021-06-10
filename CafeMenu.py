#=========================Imports=====================
import tkinter as tk                
from tkinter import font as tkfont  
from tkinter import *
from tkinter import ttk
from random import *
from tkinter import messagebox
import os
import re
#====================Main Class===========================
class Main(tk.Tk):

    def __init__(self, *args, **kwargs): #Initialising attributes of class
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic") #Font

        manager = tk.Frame(self) #Stacking all the classes/windows/frames. 
        manager.pack(side="top", fill="both", expand=True) 
        manager.grid_rowconfigure(0, weight=1) #The weight will increase for the window/frame when it is showing so that it overlaps over the other frames/windows.
        manager.grid_columnconfigure(0, weight=1) #Or in simpler terms, the window that is showing will be raised. 

        self.windows = {} #List for all the windows

        self.windows["cafe_menu"] = cafe_menu( manager=self, parent=manager) #Creates cafe_menu window
        self.windows["cafe_menu"].grid(row=0, column=0, sticky="nsew")#Geometry manager organising widgets for cafe_menu

        self.show_window("cafe_menu") #Show home page window
    def show_window(self, page_name): #Show_window method 
        window = self.windows[page_name] 
        window.tkraise() #Raises the window to make the desired window to be on top of all the others(shows window).
class cafe_menu(tk.Frame):

    def __init__(self, parent, manager): #Initialising attributes of class
        tk.Frame.__init__(self, parent) #Initialising the attributes of the frame.
        self.manager = manager #Retrieving the container variable from Main class
        self.TitleImage = PhotoImage(file="images/sale.png") 
        self.title_label = tk.Label(self, image=self.TitleImage).place(x=0,y=0)
        MainFrame = tk.Frame(self, width = 970, height = 768, bd = 8, background = "light blue")
        MainFrame.place(x=401, y=0)
        SubMainFrameOne = tk.Frame(self, width = 440, height = 400, bd = 8, background = "blue")
        SubMainFrameOne.place(x=970, y=0)
        SubMainFrameTwo = tk.Frame(self, width = 440, height = 400, bd = 8, background = "orange")
        SubMainFrameTwo.place(x=401, y=0)
        SubMainFrameThree = tk.Frame(self, width = 440, height = 400, bd = 8, background = "red")
        SubMainFrameThree.place(x=401, y=0)
        SubMainFrameFour = tk.Frame(self, width = 440, height = 400, bd = 8, background = "green")
        SubMainFrameFour.place(x=401, y=0)
        #FrameOneFront = Frame(FrameOne, width = 900, height = 330, bd = 8, relief = "raise", background = "light blue")
        #FrameOneFront.place(x=50, y=0)
        #FrameTwoFront = Frame(FrameOne, width = 900, height = 320, bd = 6, relief = "raise", background = "light blue")
        #FrameTwoFront.place(x=50, y=0)
        #TextFrame = Frame(FrameTwo, width = 440, height = 450, bd = 12, relief = "raise", background = "light blue")
        #TextFrame.pack(side=BOTTOM)
        #MainFrontOne = Frame(FrameTwo, width = 440, height = 330, bd = 16, relief = "raise", background = "light blue") # Top left left
        #MainFrontOne.pack(side=TOP)
        #MainFrontTwo = Frame(FrameOneFront, width = 450, height = 425, bd = 16, relief = "raise", background = "light blue")# Top Left
        #MainFrontTwo.pack(side=LEFT)
        #MainFrontThird = Frame(FrameOneFront, width = 450, height = 425, bd = 16, relief = "raise", background = "light blue")# Top Right
        #MainFrontThird.pack(side=RIGHT)
        #MainFrontFourth = Frame(FrameTwoFront, width = 450, height = 175, bd = 14, relief = "raise", background = "light blue")#Botom left
        #MainFrontFourth.pack(side=LEFT)
        #MainFrontFifth = Frame(FrameTwoFront, width = 450, height = 175, bd = 14, relief = "raise", background = "light blue")#Bottom right 
        #MainFrontFifth.pack(side=RIGHT)
if __name__ == "__main__": #Prevents parts of code from being run when modules are imported. 
    app = Main()
    app.geometry("1366x768")
    app.resizable(False, False)
    app.mainloop()