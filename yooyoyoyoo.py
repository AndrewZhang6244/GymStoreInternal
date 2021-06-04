import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import *
from tkinter import ttk
from random import *
from tkinter.font import names
import datetime
from tkinter import filedialog
from tkinter import messagebox
import os
from multiprocessing import Process
import re
from typing import NoReturn
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        #app.geometry(width=400, height=400)

        self.frames = {}
        for F in (StartPage, register_page, login_page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.banner()
        self.AgeVar = IntVar()
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.grid(row=1, column = 0)
        age_label = tk.Label(self, text = "YOYOYO")
        age_label.grid(row=2, column = 0)
        age_entry = tk.Entry(self, textvariable = self.AgeVar)
        age_entry.grid(row=3, column = 0)
        age_button = tk.Button(self, text = "Register", command = self.check_age)
        age_button.grid(row=4, column = 0)
    def check_age(self):
        try:
            age = int(self.AgeVar.get())
            if 15<self.AgeVar.get()<91:
                print("Yes")
                self.controller.show_frame("register_page")
                return
            else:
                response1 = messagebox.showerror("Access Denied", "You do not meet the age requirements")
                print("NO")
        except:
            response3 = messagebox.showinfo("Access Denied", "Please enter a valid age")
            return

        #button1 = tk.Button(self, text="Go to Page One",command=lambda: controller.show_frame("PageOne"))
        #button2 = tk.Button(self, text="Go to Page Two",command=lambda: controller.show_frame("PageTwo"))
        #button1.pack()
        #button2.pack()
    def banner(self):
        #creating a function for something that is repeated 
        self.TitleImage = PhotoImage(file="workout.png") 
        self.title_label = tk.Label(self, image=self.TitleImage)
        self.title_label.grid(row=0, column=0)


class register_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        StartPage.banner(self)

        name_label = tk.Label(self, text = "Name: ")
        name_label.place(x=100,y=125)
        name_entry = tk.Entry(self)
        name_entry.place(x=160,y=125)

        gmail_label = tk.Label(self, text = "Gmail: ")
        gmail_label.place(x=100,y=155)
        gmail_entry = tk.Entry(self)
        gmail_entry.place(x=160,y=155)

        password_label = tk.Label(self, text = "Password: ")
        password_label.place(x=100,y=185)
        password_entry = tk.Entry(self, show = "*")
        password_entry.place(x=160,y=185)

        login_button = tk.Button(self, text = "Login", command = self.register_check)
        login_button.place(x=160, y=215)
        #button = tk.Button(self, text="Go to the start page",
                           #command=lambda: controller.show_frame("StartPage"))
        #button.place
    def register_check(self):
        self.name = self.name_entry.get().strip().isalpha()
        gmail = self.gmail_entry.get()
        password = self.password_entry.get()
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        if self.gmail_entry.get() == "" or self.password_entry.get() == "" or self.name_entry.get() =="":
                no_input_error = messagebox.showerror("Access Denied", "Please fill out all the entries")
                return
        elif (re.search(regex,gmail)):   
            print("Email input is valid")
        else:   
            test= messagebox.showerror("Invalid gmail","Please enter a valid gmail")  
            return
        if (len(password)<8):
            passw =messagebox.showerror("Invalid password","Please enter a password that is longer than 8") 
            return
        if self.name == False:
            b = messagebox.showerror("Name Invalid","Please enter a valid name")
        if self.name == TRUE:
            if self.gmail_entry.get() == "" or self.password_entry.get() == "" or self.name_entry.get() =="":
                no_input_error = messagebox.showerror("Access Denied", "Please fill out all the entries")
            else:
                self.controller.show_frame("login_page")


class login_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.grid(row=1,column=0)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=2, column=0)


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("400x400")
    app.mainloop()
    