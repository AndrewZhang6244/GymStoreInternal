import tkinter as tk
from tkinter import *
from tkinter import font as tkfont  # python 3
from tkinter.ttk import *

class InterimMain(tk.Tk):

  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)

    # Requested dimension of main window
    windowWidth = 800
    windowHeight = 600

    # Info for centering the window in the screen
    offsetLeft = int( (self.winfo_screenwidth() - windowWidth) / 2 )
    offsetTop  = int( (self.winfo_screenheight() - windowHeight) / 2 )

    # Positions the window in the center of the screen
    self.geometry('{}x{}+{}+{}'.format(windowWidth, windowHeight, offsetLeft, offsetTop))

    # set the window title
    self.title('Using the grid geometry manager, propagate(0) and tkraise() to show/hide frames') 

    # set a minimun window size, in order to preserve the container frame
    self.minsize(600, 400)

    # create a Frame widget in the main window, requested dimensions 600 x 400
    container = tk.Frame(self, width = 600, height = 400)
    # the frame should have a red background
    container.config(background='red')
    # the frame will go in row 0, column 0 of the grid in the windows
    container.grid(row=0, column=0)

    # this frame will not auto-size to fit its contents
    # in other words, its dimensions will always honor the ones requested for its width and size
    container.grid_propagate(0)

    # the grid in the root window (self here) is stretchable
    self.rowconfigure(0, weight=1)
    self.columnconfigure(0, weight=1)
                    
    self.frames = {}
    
    # create the needed frame (WelcomeScreen frame and Login frame)
    for F in (WelcomeScreen, Login):
      # this is the frame "name"
      page_name = F.__name__
      # create the frame in the red container frame. This current window is the controller (responsible for showing hidding frames)
      frame = F(container, self)
      # add the created frame to our list of controlled frames
      self.frames[page_name] = frame

      # the created frame will gon in row 0, colum 0, of its parent (the red container frame)
      frame.grid(row=0, column=0)

    # the grid in red container frame should stretch
    container.rowconfigure(0, weight=1)
    container.columnconfigure(0, weight=1)

    # ask the controller (this window) to show the WelcomeScreen frame (and hide all the others in the list of controlled frames)
    self.show_frame('WelcomeScreen')
    
  def show_frame(self, page_name):
    # since the controlled frames were made to be of the same size,
    # raising a frame will make it apeear 'in front' of the others, hiding them
    frame = self.frames[page_name]
    frame.tkraise()
    
class WelcomeScreen(tk.Frame):

  # this WelcomeScreen frame has a parent and a controller
  def __init__(self, parent, controller):
    
    # we initialize the base Frame class with some standard arguments. we request specific width and height
    tk.Frame.__init__(self, parent, width = 360, height = 360)
    
    # this frame will not auto-size to fit its contents
    # in other words, its dimensions will always honor the ones requested for its width and size
    self.grid_propagate(0)

    # add a label to this frame (in row 0, column 0)
    Label(self,text='WELCOME TO THE INTRIM REPORT',font=('Arial Bold',16)).grid(row=0, pady=20)

    
    
    # add another label to this frame (in row 2, column 0)
    Label(self,text='Press the button to proceed',font=('Arial Bold',10)).grid(row=2, column=0, padx=5, pady=10)

    # add an 'proceed to login screen'  button to this frame (in row 3, column 0)
    # when this button is pressed, the Login frame should be shown and the WelcomeScreen frame should be hidden
    Button = tk.Button(self,text='Sign In',font=('Arial Bold',16),command=lambda: controller.show_frame('Login'))
    Button.grid(row=3, column=0, padx=20,pady=20)

    # the grid in this frame should stretch
    self.rowconfigure(0, weight=1)
    self.columnconfigure(0, weight=1)

class Login(tk.Frame):

  # this Login frame has a parent and a controller
  def __init__(self, parent, controller):
    # we initialize the base Frame class with some standard arguments. we request specific width and height
    tk.Frame.__init__(self, parent, width = 360, height = 360)
    
    # this frame will have a blue background
    self.config(background='blue')
    # this frame will not auto-size to fit its contents
    # in other words, its dimensions will always honor the ones requested for its width and size
    self.grid_propagate(0)

    # add a label to this frame (in row 0, column 0)
    Label(self,text='LOGIN SCREEN',font=('Arial Bold',16)).grid(row=0, column=0, padx=5, pady=5, columnspan=3)

    # add a label to this frame (in row 1, column 0)
    Label(self,text='Username',font=('Arial',12)).grid(row=1,column=0, padx=5, sticky='w')
    # add a label to this frame (in row 2, column 0)
    Label(self,text='Password',font=('Arial',12)).grid(row=2,column=0, padx=5, sticky='w')
    # add an Entry widget to this frame
    user = Entry(self)
    # the Entry widget will go in row 1, column 1, will span for 2 columns and will stretch left and right
    user.grid(row=1,column=1,padx=5, pady=5,columnspan=2,sticky='we')
    # add another Entry widget to this frame
    pwd = Entry(self)
    # the Entry widget go in row 2, column 1, will span for 2 columns and will stretch left and right
    pwd.grid(row=2,column=1,padx=5, pady=5,columnspan=2,sticky='we')
    
    # add a button to this frame
    # when this button is pressed, the checkLogin() function should be called with the stated parameters
    Button = tk.Button(self,text='LOGIN',command=lambda:checkLogin(str(user.get()),str(pwd.get())))
    # the button widget will go in row 3, column 2 and will stick to the rigth side of the grid cell
    Button.grid(row=3,column=2,columnspan=3,padx=5, pady=5, sticky='e')
    
    # add a button to this frame
    # when this button is pressed, the WelcomeScreen frame should be shown and the Login frame should be hidden
    Button = tk.Button(self,text='CANCEL',command=lambda: controller.show_frame('WelcomeScreen'))
    # the button widget will go in row 3, column 0 and will stick to the left of the grid cell
    Button.grid(row=3,column=0,columnspan=3,padx=5, pady=5,sticky='w')

    # the grid in this frame should stretch
    self.rowconfigure(0, weight=1)
    self.columnconfigure(0, weight=1)

if __name__ == '__main__':
    app = InterimMain()
    app.mainloop()