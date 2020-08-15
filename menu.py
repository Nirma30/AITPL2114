from tkinter import *
a = Tk()
a.title("my first window")
a.geometry("500x500+100+100")
m1 = Menu()
m1.add_cascade(label='file')# create menu
m1.add_cascade(label='edit')
m1.add_cascade(label='format')
m1.add_cascade(label='view')
m1.add_cascade(label='help')
a.config(menu=m1)
a.mainloop()