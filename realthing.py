# Multi-frame tkinter application v2.3
import tkinter as tk
from tkinter import font as tkfont
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
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        AgeVar = IntVar()
        #banner
        self.TitleImage = PhotoImage(file="workout.png")
        self.title_label = tk.Label(self, image=self.TitleImage)
        self.title_label.grid(row=0,column=0)
        #labels
        tk.Label(self, text="This is the start page").grid(row=2, column = 0)
        tk.Label(self,text = "Enter age").grid(row=3, column = 0)
        #entries
        self.entry_age = tk.Entry(self, textvariable = AgeVar).grid(row=4, column = 0)
        #buttons
        tk.Button(self, text="Open page one",
                  command=lambda: master.switch_frame(PageOne)).grid(row=5, column=0)
        tk.Button(self, text="Register", 
                    command = self.check_age).grid(row=6, column=0)

    def check_age(self):
        try:
            age = int(AgeVar.get())
        except:
            response = messagebox.showinfo("Access Denied", "Please enter a valid age")
            return 
        if 15<AgeVar.get()<91:
            print("DONE")
            return
        else:
            response = messagebox.showerror("Access Denied", "You do not meet the age requirements")
            app.destroy()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()