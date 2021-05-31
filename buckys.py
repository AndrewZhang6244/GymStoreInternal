from tkinter import*

class BuckyButtons:

    def __init__(self, parent):
        home_frame = Frame(parent)
        home_frame.pack()
        self.print_button = Button(home_frame, text="Print", command = PageTwo)
        self.print_button.pack(side = LEFT)
     

class PageTwo:

    def __init__(self,parent):
        
        second_frame = Frame(parent)
        second_frame.pack()
        self.LOL = Button(second_frame,text = "LOL")
        self.LOL.pack(side = RIGHT)

        

root = Tk()
b = BuckyButtons(root)
root.mainloop()