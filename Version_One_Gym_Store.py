#=====Imports=======
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

creds = 'loginsystem'

#Initializing Gym store class
class GymStore:
    def __init__(self, parent):
        AgeVar = IntVar()
        account_list = []
        #========Welcome frame============
        welcome_frame = Frame(parent,width=400, height=400)
        welcome_frame.pack()
        self.TitleImage = PhotoImage(file="images/workout.png")
        self.title_label = Label(welcome_frame, image=self.TitleImage)
        self.title_label.place(x=0,y=0)
        self.frontLabel1 = Label(welcome_frame, text = "This app is designed to serve a purpose where")
        self.frontLabel1.place(x=65, y = 110)
        self.frontLabel2 = Label(welcome_frame, text = " the user can order gym equipment such as dumbbells, ")
        self.frontLabel2.place(x=50, y=130)
        self.frontLabel3 = Label(welcome_frame, text = "barbells, and so on. In order to use this app, you ")
        self.frontLabel3.place(x=60, y=150)
        self.frontLabel4 = Label(welcome_frame, text = "must log in or register so that the program can ")
        self.frontLabel4.place(x=65, y=170)
        self.frontLabel5 = Label(welcome_frame, text = "recognize the total sum when you finish ordering ")
        self.frontLabel5.place(x=65, y=190)
        self.frontLabel6 = Label(welcome_frame, text = "and so other user's cannot see what you are ordering. ")
        self.frontLabel6.place(x=75, y=210)   
        self.LabelAge = Label(welcome_frame, text = "Age: ").place(x=100, y=240)
        self.EntryAge = Entry(welcome_frame, textvariable = AgeVar).place(x=140, y=240)
            
                
        self.button_sign_up = Button(welcome_frame, text = "Sign up", command = self.check_age).place(x=100, y=270)
        #if os.path.isfile(creds):
        #    self.button_login = Button(welcome_frame, text = "Login", command = self.Login, state = "normal").place(x=190, y=270)
        #    self.button_sign_up = Button(welcome_frame, text = "Sign up", command = self.CheckAge, state = DISABLED).place(x=100, y=270)
        #else:
        #    self.button_login = Button(welcome_frame, text = "Login", command = self.Login, state = DISABLED).place(x=190, y=270)
        #    self.button_sign_up = Button(welcome_frame, text = "Sign up", command = self.CheckAge, state = "normal").place(x=100, y=270)
    def CheckRegister(self):
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
                        FSSignup()
                        self.signup_frame.pack_forget()

                        
                        
               
    def FSSignup(self):
            with open(creds, 'w') as f:
                account_list.append(self)
                print("loginsystem.txt has been created")
                success= messagebox.showinfo("Access Granted","Account has been made")
            Login(self) 
    def DeleteUser(self):
        delete_user_ask = messagebox.askquestion("Delete User","Are you sure you would like to delete your account?")
        if delete_user_ask == 'yes':
            os.remove(creds)
            restart()
        else:
            return
    def restart(self):
        self.login_frame.pack_forget()
        GymStore(root)
    def Login(self):
        #Login frame/function
        welcome_frame.pack_forget()
        login_frame = Frame(parent, width= 400, height =400)
        login_frame.pack()
        self.logintitleimage = PhotoImage(file="images/workout.png")
        self.login_title_label = Label(self.login_frame, image=self.logintitleimage)
        self.login_title_label.place(x=0,y=0)

        self.login_gmail_label = Label(self.login_frame, text = "Gmail: ")
        self.login_gmail_label.place(x=100,y=125)
        self.login_gmail_entry = Entry(self.login_frame)
        self.login_gmail_entry.place(x=160,y=125)

        self.login_password_label = Label(self.login_frame, text = "Password: ")
        self.login_password_label.place(x=100,y=155)
        self.login_password_entry = Entry(self.login_frame)
        self.login_password_entry.place(x=160,y=155)

        self.loginpage_button = Button(self.login_frame, text = "Login", command = self.CheckLogin)
        self.loginpage_button.place(x=160,y=195)

        self.delete_button = Button(self.login_frame, text = "Delete", fg= 'red', command = self.DeleteUser)
        self.delete_button.place(x=15,y=360)

        self.back_to_home_button = Button(self.login_frame, text = "Home", command = self.restart)
        self.back_to_home_button.place(x=240,y=195)
        

    def CheckLogin(self):
        with open(creds) as f:
            data = f.readlines() 
            pword = data[1].rstrip() 
            emaila = data[2].rstrip()
        if self.login_gmail_entry.get() == emaila and self.login_password_entry.get() == pword:
            response = messagebox.showinfo("Access Granted", "Enter Gym store")
            print("Enter gym store")
            return
        while self.login_gmail_entry.get() == "" and self.login_password_entry.get() == "":
            r = Tk() 
            r.title('No Input')
            r.geometry('150x50')         
            rlbl = Label(r, text='\nPlease enter an input') 
            rlbl.pack() 
            r.mainloop()
            print("Please enter an input")
        else:
            r = Tk()
            r.title('Invalid Login')
            r.geometry('150x50')
            rlbl = Label(r, text='\nInvalid Login')
            rlbl.pack()
            r.mainloop()
            print("Invalid login")
    def check_age(self):
        try:
            age = int(AgeVar.get())
        except:
            response = messagebox.showinfo("Access Denied", "Please enter a valid age")
            return
        if 15<AgeVar.get()<91:
            self.button_sign_up = Button(self.welcome_frame, text = "Sign up", command = self.CheckAge).place(x=100, y=270)
            SignUp()
            return
        else:
            response = messagebox.showerror("Access Denied", "You do not meet the age requirements")
            welcome_frame.quit()
    def SignUp(self):
        #SignUp function/frame
        self.welcome_frame.pack_forget()
        self.signup_frame = Frame(parent, width= 400, height =400)
        self.signup_frame.pack()
        self.signuptitleimage = PhotoImage(file="images/workout.png")
        self.signup_title_label = Label(self.signup_frame, image=self.signuptitleimage)
        self.signup_title_label.place(x=0,y=0)

        self.name_label = Label(self.signup_frame, text = "Name: ")
        self.name_label.place(x=100,y=125)
        self.name_entry = Entry(self.signup_frame)
        self.name_entry.place(x=160,y=125)

        self.gmail_label = Label(self.signup_frame, text = "Gmail: ")
        self.gmail_label.place(x=100,y=155)
        self.gmail_entry = Entry(self.signup_frame)
        self.gmail_entry.place(x=160,y=155)

        self.password_label = Label(self.signup_frame, text = "Password: ")
        self.password_label.place(x=100,y=185)
        self.password_entry = Entry(self.signup_frame, show = "*")
        self.password_entry.place(x=160,y=185)

        self.register_button = Button(self.signup_frame, text = "Sign up", command = self.CheckRegister).place(x=100, y=270)
        self.register_button.place(x=140,y=270)

            
#Main module and running script
if __name__ == "__main__":
    root = Tk()
    frames = GymStore(root)
    root.title("Gym Store")
    root.mainloop()