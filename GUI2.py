from tkinter import *
a = Tk()
a.title('my first window')
a.geometry("500x500+100+100")
l1 = Label(text='label1')
l2 = Label(text='label2')
l1.pack()
l2.pack()
a.mainloop()
