from tkinter import *
a = Tk()
a.title("LOGIN PAGE")
# a.geometry("500x500+100+100")
l1 = Label(text='LOGIN', fg='black', font=300).pack()
l2 = Label(text='username', fg='black', font=100)
l2.pack(side=LEFT)
E1 = Entry(a, bd=5)
E1.pack(side=RIGHT)
l3 = Label(text='\n password', fg='black', font=100)
l3.pack(anchor=SW)
# l3.pack(after=l2, side=LEFT)
E2 = Entry(a, bd=5)
E2.pack(side=RIGHT)
a.mainloop()
