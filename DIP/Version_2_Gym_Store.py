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
        self.windows["home_page"] = home_page(manager=self, parent=manager) #Creates home_page window
        self.windows["register_page"] = register_page(manager=self, parent=manager) #Creates register_page window
        self.windows["login_page"] = login_page( manager=self, parent=manager) #Creates login_page window
        self.windows["delivery_or_pickup"] = delivery_or_pickup( manager=self, parent=manager) #Creates delivery_or_pickup window
        self.windows["cafe_menu"] = delivery_or_pickup( manager=self, parent=manager) #Creates cafe_menu window

        self.windows["home_page"].grid(row=0, column=0, sticky="nsew") #Geometry manager organising widgets for home_page
        self.windows["register_page"].grid(row=0, column=0, sticky="nsew")#Geometry manager organising widgets for register_page
        self.windows["login_page"].grid(row=0, column=0, sticky="nsew")#Geometry manager organising widgets for login_page
        self.windows["delivery_or_pickup"].grid(row=0, column=0, sticky="nsew")#Geometry manager organising widgets for delivery_or_pickup
        self.windows["cafe_menu"].grid(row=0, column=0, sticky="nsew")#Geometry manager organising widgets for cafe_menu

        self.show_window("home_page") #Show home page window
    def show_window(self, page_name): #Show_window method 
        window = self.windows[page_name] 
        window.tkraise() #Raises the window to make the desired window to be on top of all the others(shows window).

#====================================Home page class/window===========================
class home_page(tk.Frame):

    def __init__(self, parent, manager): #Initialising attributes of class
        tk.Frame.__init__(self, parent) #Initialising the attributes of the frame.
        self.manager = manager #Retrieving the container variable from Main class
        self.banner() #Calling the banner function
        self.AgeVar = IntVar() #Declaring AgeVar as an integer
        self.frontLabel1 = tk.Label(self, text = "This app is designed to serve a purpose where").place(x=65, y = 110) #Label 1 for description 
        self.frontLabel2 = tk.Label(self, text = " the user can order gym equipment such as dumbbells, ").place(x=50, y=130) #Label 2 for description 
        self.frontLabel3 = tk.Label(self, text = "barbells, and so on. In order to use this app, you ").place(x=60, y=150)#Label 3 for description 
        self.frontLabel4 = tk.Label(self, text = "must log in or register and be between 16 to 90 ").place(x=65, y=170)#Label 4 for description 
        self.frontLabel5 = tk.Label(self, text = "years old when using this app. Please continue ").place(x=65, y=190)#Label 5 for description 
        self.frontLabel6 = tk.Label(self, text = "by entering an age below. ").place(x=75, y=210) #Label 6 for description 
        self.age_entry = tk.Entry(self, textvariable = self.AgeVar).place(x=120, y=230) #Age Entry
        self.register_button = tk.Button(self, text = "Register", command = self.check_age).place(x=120, y=250) #Register button
        self.login_button = tk.Button(self, text = "Login", command = lambda:manager.show_window("login_page")).place(x=200, y=250) #Login button

    def check_age(self): #Function to check the age of the user
        try:
            age = int(self.AgeVar.get()) 
            if 15<self.AgeVar.get()<91: 
                print("Yes")
                self.manager.show_window("register_page") #If user input is between 16 and 90, call the method show_frame to show register_page with regards to manager
                return
            else:
                response1 = messagebox.showerror("Access Denied", "You do not meet the age requirements") #If user input is not within 16 and 90, send messagebox
                print("NO")
        except:
            response3 = messagebox.showinfo("Access Denied", "Please enter a valid age") #If user input is not an integer or is invalid, send messagebox.
            return

    def banner(self): #Banner method
        self.TitleImage = PhotoImage(file="images/workout.png") 
        self.title_label = tk.Label(self, image=self.TitleImage).grid(row=0, column=0)

#============================================================Register class/window===================
class register_page(tk.Frame): #Register page class/window

    def __init__(self, parent, manager): #Initiliazing attributes 
        tk.Frame.__init__(self, parent) #Initiliazing frame attributes
        self.manager = manager
        home_page.banner(self) #Calling banner method from home page class

        self.name_label = tk.Label(self, text = "Name: ") #Label for name
        self.name_label.place(x=100,y=125)
        self.name_entry = tk.Entry(self) #Entry for name
        self.name_entry.place(x=160,y=125)

        self.gmail_label = tk.Label(self, text = "Gmail: ") #Label for gmail
        self.gmail_label.place(x=100,y=155)
        self.gmail_entry = tk.Entry(self) #Entry for gmail
        self.gmail_entry.place(x=160,y=155)

        self.password_label = tk.Label(self, text = "Password: ") #Label for password
        self.password_label.place(x=100,y=185)
        self.password_entry = tk.Entry(self, show = "*") #Entry for password
        self.password_entry.place(x=160,y=185)
   
        self.login_button = tk.Button(self, text = "Login", command = self.register_check).place(x=160, y=215) #Login button

        self.back_to_home_button1 = tk.Button(self, text = "Home", command = lambda: manager.show_window("home_page"))#Back to startpage button
        self.back_to_home_button1.place(x=240,y=215) 
       
    
    def register_check(self): #Checks if the entries for register is valid (Register_check method)
        name_info = self.name_entry.get().strip().isalpha() #Assigns name_info to the values of name while also removing any spaces, and makes sure their input is a string.
        gmail_info = self.gmail_entry.get() #Assigns gmail_info to the values of gmail
        password_info = self.password_entry.get() #Assigns password_info to the values of password.
        check_symbols = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #Assigns check_symbols to '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' so we can use it to check if the gmail is valid.
        if gmail_info == "" or password_info == "" or name_info =="": 
            no_input_error = messagebox.showerror("Access Denied", "Please fill out all the entries") #If all entries are blank, send message
            return
        if (re.search(check_symbols,gmail_info)): #Checks the gmail through 'check_symbols' to see if the user's input has any symbols from the list.
            print("Email input is valid")
            if (len(password_info)<8):
                invalid_password =messagebox.showerror("Invalid password","Please enter a password that is longer than 8") #If password is less than 8, sends message
                return
            if name_info == False:
                 invalid_name = messagebox.showerror("Name Invalid","Please enter a valid name") #If name is a integer, send message 
            if name_info == TRUE:
                if gmail_info == "" or password_info == "" or name_info =="": #Checks if the entries are blank once more for errors and if it's blank, send message
                    no_input_error = messagebox.showerror("Access Denied", "Please fill out all the entries")
                else:
                    self.register_user() #If all the entries are valid, call the register_user method.   
        else:
            invalid_gmail = messagebox.showerror("Invalid gmail","Please enter a valid gmail") #If gmail is invalid, send message
            return  
    def register_user(self): #(Register user method)
        file = open(self.gmail_entry.get(), "w") #Creates file with the name being the user's gmail
        file.write(self.gmail_entry.get() + "\n") #Writes the user's gmail and creates a new line
        file.write(self.password_entry.get()) #Writes the user's password
        file.close() #Closes file
        self.password_entry.delete(0, END) #Deletes entry values from user for password
        self.gmail_entry.delete(0, END) #Deletes entry values from user for gmail
        self.name_entry.delete(0, END) #Deletes entry values from user for name
        self.manager.show_window("login_page") #Calls show_frame method with regards to manager and shows login_page window
        

class login_page(tk.Frame): #Login class/window

    def __init__(self, parent, manager): #Initiliazing attributes
        tk.Frame.__init__(self, parent) #Initializing the frame of login_page
        self.manager = manager #Declares self.manageras manager(argument).
        home_page.banner(self) #Banner
        
        self.login_gmail_label = tk.Label(self, text = "Gmail: ") #Label for gmail login
        self.login_gmail_label.place(x=100,y=125)
        self.login_gmail_entry = tk.Entry(self) #Entry for gmail login
        self.login_gmail_entry.place(x=160,y=125)

        self.login_password_label = tk.Label(self, text = "Password: ") #Label for password login
        self.login_password_label.place(x=100,y=155)
        self.login_password_entry = tk.Entry(self, show = "*") #Entry for password login
        self.login_password_entry.place(x=160,y=155)

        self.loginpage_button = tk.Button(self, text = "Login", command = self.login_verify) #Login buttn
        self.loginpage_button.place(x=160,y=195)
        self.back_to_home_button = tk.Button(self, text = "Home", command = lambda: manager.show_window("home_page"))#Back to startpage button
        self.back_to_home_button.place(x=240,y=195) 

    def login_verify(self):
        login_page.login_verify = self.login_gmail_entry.get()
        self.verify_gmail = self.login_gmail_entry.get()  #Declares that verify_gmail is the user's entry for gmail
        self.verify_password = self.login_password_entry.get() #Declares that verifify_password is the user's entry for password
        list_of_files = os.listdir() #Declares that list_of_files is os.listrdir() which gets all the files in the specified directory.
        if self.verify_gmail in list_of_files: 
            file1 = open(self.verify_gmail, "r")
            verify = file1.read().splitlines()
            if self.verify_password in verify:
                print("SUCCESS")#If the account is in the list of files, and their input matches the password inside that text file, print("SUCCESS")
                self.manager.show_window("delivery_or_pickup")
            else:   
                password_not_valid = messagebox.showerror("Access Denied", "Please enter a valid password") #If it's not, then send message
        else:
            no_account = messagebox.showerror("Access Denied", "Please enter valid details") #If there is no account/no input, send message
    
class delivery_or_pickup(tk.Frame): #delivery_or_pickup class
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        home_page.banner(self) #Banner
        self.delivery_button = tk.Button(self, text = "Delivery", height = 5, width = 10, command = self.delivery) #Delivery button
        self.delivery_button.place(x=110, y= 170)
        self.pickup_button = tk.Button(self, text = "Pickup", height = 5, width = 10, command = self.pickup) #Pickup button
        self.pickup_button.place(x=200, y=170)
        self.delete_button = tk.Button(self, text = "Delete", fg= 'red', command = self.delete_account) #Delete account button
        self.delete_button.place(x=15,y=360)
    def delete_account(self): #Delete account method
        delete_user_ask = messagebox.askquestion("Delete User","Are you sure you would like to delete your account?")
        if delete_user_ask == 'yes':
            os.remove(login_page.login_verify) 
            print("DONE DELETING")
            self.manager.show_window("register_page")
        else:
            return
    def delivery(self):
        self.total_price += 5.50
        self.manager.show_window("cafe_menu")
    
    def pickup(self):
        self.manager.show_window("cafe_menu")
class cafe_menu(tk.Frame):
    def __init__(self, parent, manager): #Initializes attributes
        tk.Frame.__init__(self, parent) #Initializes frame 
        self.manager = manager #Declares self.manager as manager (for window controlling)
        


if __name__ == "__main__": #Prevents parts of code from being run when modules are imported. 
    app = Main()
    app.geometry("400x400")
    app.mainloop()