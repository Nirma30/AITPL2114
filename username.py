from tkinter import *
a = Tk()
a.title("LOGIN PAGE")
# a.geometry('500x500')
a.configure(background="grey")
x = Label(a, text="username", font=20).grid(row=0, column=0)
y = Label(a, text="password", font=20).grid(row=1, column=0)
x1 = Entry(a).grid(row=0, column=1)
y1 = Entry(a).grid(row=1, column=1)


def clicked():
    res = "welcome"


bt = Button(a, text="submit").grid(row=3, column=0)
a.mainloop()
