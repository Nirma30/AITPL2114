from tkinter import *
a = Tk()
p = PhotoImage(file="test.jpg")
l1 = Label(a, image=p).pack()
a.mainloop()
