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
        for F in (StartPage, register_page, login_page, delivery_or_pickup):
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
        frontLabel1 = tk.Label(self, text = "This app is designed to serve a purpose where")
        frontLabel1.place(x=65, y = 110)
        frontLabel2 = tk.Label(self, text = " the user can order gym equipment such as dumbbells, ")
        frontLabel2.place(x=50, y=130)
        frontLabel3 = tk.Label(self, text = "barbells, and so on. In order to use this app, you ")
        frontLabel3.place(x=60, y=150)
        frontLabel4 = tk.Label(self, text = "must log in or register and be between 16 to 90 ")
        frontLabel4.place(x=65, y=170)
        frontLabel5 = tk.Label(self, text = "years old when using this app. Please continue ")
        frontLabel5.place(x=65, y=190)
        frontLabel6 = tk.Label(self, text = "by entering an age below. ")
        frontLabel6.place(x=75, y=210)   
        age_entry = tk.Entry(self, textvariable = self.AgeVar)
        age_entry.place(x=120, y=230)   
        age_button = tk.Button(self, text = "Register", command = self.check_age)
        age_button.place(x=120, y=250)   
        login_button = tk.Button(self, text = "Login", command = lambda:controller.show_frame("login_page"))
        login_button.place(x=200, y=250)   
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
        self.TitleImage = PhotoImage(file="images/workout.png") 
        self.title_label = tk.Label(self, image=self.TitleImage)
        self.title_label.grid(row=0, column=0)


class register_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        StartPage.banner(self)

        self.name_label = tk.Label(self, text = "Name: ")
        self.name_label.place(x=100,y=125)
        self.name_entry = tk.Entry(self)
        self.name_entry.place(x=160,y=125)

        self.gmail_label = tk.Label(self, text = "Gmail: ")
        self.gmail_label.place(x=100,y=155)
        self.gmail_entry = tk.Entry(self)
        self.gmail_entry.place(x=160,y=155)

        self.password_label = tk.Label(self, text = "Password: ")
        self.password_label.place(x=100,y=185)
        self.password_entry = tk.Entry(self, show = "*")
        self.password_entry.place(x=160,y=185)

        login_button = tk.Button(self, text = "Login", command = self.register_check)
        login_button.place(x=160, y=215)
        
        #button = tk.Button(self, text="Go to the start page",
                           #command=lambda: controller.show_frame("StartPage"))
        #button.place
    def register_check(self):
        name_info = self.name_entry.get().strip().isalpha()
        gmail_info = self.gmail_entry.get()
        password_info = self.password_entry.get()
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        if gmail_info == "" or password_info == "" or name_info =="":
            no_input_error = messagebox.showerror("Access Denied", "Please fill out all the entries")
            return
        if (re.search(regex,gmail_info)): 
            print("Email input is valid")
            if (len(password_info)<8):
                passw =messagebox.showerror("Invalid password","Please enter a password that is longer than 8") 
                return
            if name_info == False:
                 b = messagebox.showerror("Name Invalid","Please enter a valid name")
            if name_info == TRUE:
                if gmail_info == "" or password_info == "" or name_info =="":
                    no_input_error = messagebox.showerror("Access Denied", "Please fill out all the entries")
                else:
                    self.register_user()          
        else:
            test= messagebox.showerror("Invalid gmail","Please enter a valid gmail") 
            return  
    def register_user(self):
        file = open(self.gmail_entry.get(), "w")
        file.write(self.gmail_entry.get() + "\n")
        file.write(self.password_entry.get())
        file.close()
        print("Sent to database")
        self.password_entry.delete(0, END)
        self.gmail_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.controller.show_frame("login_page")
        

class login_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        StartPage.banner(self)
        
        self.login_gmail_label = tk.Label(self, text = "Gmail: ")
        self.login_gmail_label.place(x=100,y=125)
        self.login_gmail_entry = tk.Entry(self)
        self.login_gmail_entry.place(x=160,y=125)

        self.login_password_label = tk.Label(self, text = "Password: ")
        self.login_password_label.place(x=100,y=155)
        self.login_password_entry = tk.Entry(self, show = "*")
        self.login_password_entry.place(x=160,y=155)

        self.loginpage_button = tk.Button(self, text = "Login", command = self.login_verify)
        self.loginpage_button.place(x=160,y=195)

        self.back_to_home_button = tk.Button(self, text = "Home", command = lambda: controller.show_frame("StartPage"))
        self.back_to_home_button.place(x=240,y=195)
    def login_verify(self):
        login_page.login_verify = self.login_gmail_entry.get()
        self.verify_gmail = self.login_gmail_entry.get() 
        self.verify_password = self.login_password_entry.get() 
        list_of_files = os.listdir()
        if self.verify_gmail in list_of_files:
            file1 = open(self.verify_gmail, "r")
            verify = file1.read().splitlines()
            if self.verify_password in verify:
                print("SUCCESS")
                account = self.verify_gmail
                self.controller.show_frame("delivery_or_pickup")
            else:   
                password_not_valid = messagebox.showerror("Access Denied", "Please enter a valid password")
        else:
            no_account = messagebox.showerror("Access Denied", "Please enter valid details")
    


class delivery_or_pickup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        StartPage.banner(self)
        self.delivery_button = tk.Button(self, text = "Delivery", height = 5, width = 10, command = self.delivery)
        self.delivery_button.place(x=110, y= 170)
        self.pickup_button = tk.Button(self, text = "Pickup", height = 5, width = 10, command = self.pickup)
        self.pickup_button.place(x=200, y=170)
        self.delete_button = tk.Button(self, text = "Delete", fg= 'red', command = self.delete_account)
        self.delete_button.place(x=15,y=360)
        print(login_page.login_verify)
    def delete_account(self):
        delete_user_ask = messagebox.askquestion("Delete User","Are you sure you would like to delete your account?")
        if delete_user_ask == 'yes':
            os.remove(login_page.login_verify)
            print("DONE DELETING")
            self.controller.show_frame("register_page")
        else:
            return
    def delivery(self):
        return
    
    def pickup(self):
        return
if __name__ == "__main__":
    app = SampleApp()
    app.geometry("400x400")
    app.mainloop()