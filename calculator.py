from tkinter import *


a = Tk()
a.title("Calculator")
z = Entry(a, width=35, borderwidth=5)
z.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# def add():
# c = Label(text='you have pressed enter', fg='red', font=20).pack()


# a.title("Calculator")
a.geometry("500x500+100+100")
l1 = Label(text='BASIC CALCULATOR', fg='black', font=200).pack()
# l2 = Label(text='label2', fg='blue', bg='green', font=20).pack()
button1 = Button(a, text='enter', fg='red', bg='yellow', font=20)
# button1.grid(row=1, column=0)
button2 = Button(a, text='enter', fg='red', bg='yellow', font=20)
# button2.grid(row=1, column=1)
'''button3 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button4 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button5 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button6 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button7 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button8 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button9 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button10 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button11 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button12 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button13 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button14 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button15 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()
button16 = Button(text='enter', fg='red', bg='yellow', command=hello, font=20).pack()'''
a.mainloop()
