from tkinter import *
a = Tk()
a.title("my first window")
a.geometry("500x500+100+100")
m1 = Menu()
l1 = Menu()
l1.add_command(label="New File")
l1.add_command(label="Open File")
l1.add_command(label="Save File")
l2 = Menu()
l2.add_command(label="copy")
l2.add_command(label="paste")
l2.add_command(label="undo")
l3 = Menu()
l3.add_command(label="word wrap")
l3.add_command(label="font")
l4 = Menu()
l4.add_command(label="zoom")
l4.add_command(label="status bar")
l5 = Menu()
l5.add_command(label="view help")
l5.add_command(label="feedback")
m1.add_cascade(label='file', menu=l1)
m1.add_cascade(label='edit', menu=l2)
m1.add_cascade(label='format', menu=l3)
m1.add_cascade(label='view', menu=l4)
m1.add_cascade(label='help', menu=l5)
a.config(menu=m1)
a.mainloop()
