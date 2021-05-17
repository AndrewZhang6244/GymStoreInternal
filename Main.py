#===========================================Imports==========================================
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import os
from multiprocessing import Process
#========================================Banners, Declaring Tkinter, Icons and Navigational Bar===========
root = Tk()
root.title('Click & Collect App!')# Title of the GUI
root.geometry("400x400")# Size of the GUI
root.iconbitmap('FoodIcon.ico')# Creates GUI Icon 
framebanner = LabelFrame(root) 
framebanner.pack(padx=1, pady=1)

my_img1 = ImageTk.PhotoImage(Image.open("FoodBanner.png")) # Banner
my_label = Label(framebanner, image=my_img1) #Puts banner into a frame
my_label.grid()

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook, width = 400, height = 400)  # Navigation bar
my_frame1.pack(fill="both", expand = 2)
my_notebook.add(my_frame1, text ="Intro")

creds = 'loginsystem' #Creating textfile database

#===========================================Functions===========================================
def Signup(): 
    global passwordZ
    global nameZ
    global emailZ
    global root
 
    root = Tk() 
    root.title('Signup') 
    intruction = Label(root, text='Please Enter new Credidentials\n') 
    intruction.grid(row=0, column=0, sticky=E) 
    nameA = Label(root, text='New Username: ') 
    passwordA = Label(root, text='New Password: ') 
    emailA = Label(root, text ='Email:  ')
    nameA.grid(row=1, column=0, sticky=W) 
    passwordA.grid(row=2, column=0, sticky=W) 
    emailA.grid(row=3, column = 0, sticky = W)
 
    nameZ = Entry(root) 
    passwordZ = Entry(root, show='*') 
    emailZ = Entry(root)
    nameZ.grid(row=1, column=1) 
    passwordZ.grid(row=2, column=1)
    emailZ.grid(row = 3, column =1)
 
    signupButton = Button(root, text='Signup', command=CheckRegister) 
    signupButton.grid(columnspan=2, sticky=W)
        
    root.mainloop() 
def CheckRegister():
    global nameZA
    global passwordZA
    global emailZA
    if nameZ.get() == "" and passwordZ.get() == "" and emailZ.get() =="":
        no_input_error = messagebox.showerror("Access Denied", "No Input")
    else:
        FSSignup()
        root.destroy()
def FSSignup():
    with open(creds, 'w') as f:
        f.write(nameZ.get()) 
        f.write('\n')
        f.write(passwordZ.get()) 
        f.write('\n')
        f.write(emailZ.get())
        f.close()
        print("loginsystem.txt has been created")

    root.destroy()
    Login() 
 
def Login():
    global nameZA
    global passwordZA
    global emailZA
    global rootwindow
 
    rootwindow = Tk() 
    rootwindow.title('Login') 
    intruction = Label(rootwindow, text='Please Login\n') 
    intruction.grid(sticky=E)
  
    nameA = Label(rootwindow, text='Username: ')
    passwordA = Label(rootwindow, text='Password: ') 
    emailA = Label(rootwindow, text = 'Email: ')
    nameA.grid(row=1, sticky=W)
    passwordA.grid(row=2, sticky=W)
    emailA.grid(row = 3, sticky = W)
 
    nameZA = Entry(rootwindow)
    passwordZA = Entry(rootwindow, show='*')
    emailZA = Entry(rootwindow)
    nameZA.grid(row=1, column=1)
    passwordZA.grid(row=2, column=1)
    emailZA.grid(row = 3, column = 1)
 
    loginB = Button(rootwindow, text='Login', command=CheckLogin) 
    loginB.grid(columnspan=2, sticky=W)
 
    deleteuser = Button(rootwindow, text='Delete User', fg='red', command=DelUser) 
    deleteuser.grid(columnspan=2, sticky=W)
    
    rootwindow.mainloop()
 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() 
        uname = data[0].rstrip() 
        pword = data[1].rstrip() 
        emaila = data[2].rstrip()
    if nameZA.get() == uname and passwordZA.get() == pword and emailZA.get() == emaila:
        response = messagebox.showinfo("Access Granted", "Enter Cafe Menu")
        os.system('python OrderingSystem.py')
        root.destroy()
        rootwindow.destroy()
        return
    while nameZA.get() == "" and passwordZA.get() == "" and emailZA.get() == "":
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
 
def DelUser():
    os.remove(creds)
    rootwindow.destroy()
    Signup() 
def CheckAge():
    try:
         age = int(AgeVar.get())
    except:
        response = messagebox.showinfo("Access Denied", "Please enter an input")
        return
    if 12<AgeVar.get()<19:
        AgeButton = Button(my_frame1, text = "Confirm Age", command = CheckAge, state = DISABLED).place(x=145, y=190)
        if os.path.isfile(creds):
            Login()
        else: 
            Signup()
            return
    else:
        response = messagebox.showerror("Access Denied", "You do not meet the age requirements")
        root.quit()
  
#==============================================Variables===========================================
AgeVar = IntVar()
#=====================================Labels for main screen===================================
frontLabel1 = Label(my_frame1, text = "This app is designed to serve a purpose where")
frontLabel1.place(x=65, y = 10)
frontLabel2 = Label(my_frame1, text = " the user can order items such as food, drinks and so on.")
frontLabel2.place(x=50, y=30)
frontLabel3 = Label(my_frame1, text = "In order to use this app, you must log in or register ")
frontLabel3.place(x=60, y=50)
frontLabel4 = Label(my_frame1, text = "so that the program can recognize the total sum")
frontLabel4.place(x=65, y=70)
frontLabel5 = Label(my_frame1, text = "when you finish ordering and so other user's")
frontLabel5.place(x=65, y=90)
frontLabel6 = Label(my_frame1, text = " cannot see what you are ordering. ")
frontLabel6.place(x=75, y=110)   
frontLabel6 = Label(my_frame1, text = "Please enter your age below :")
frontLabel6.place(x=95, y=150)   
LabelAge = Label(my_frame1, text = "Age: ").place(x=100, y=170)
EntryAge = Entry(my_frame1, textvariable = AgeVar).place(x=140, y=170)
AgeButton = Button(my_frame1, text = "Confirm Age", command = CheckAge).place(x=145, y=190)
#====================================================Calling Tkinter GUI function===========================
root.mainloop()
