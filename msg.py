from tkinter import *
import tkinter.messagebox
a = Tk()
a.title('my first window')
a.geometry("1000x768+100+100")
b = tkinter.messagebox
b.showinfo('this is a message box')
ch = b.askquestion('are you a intern')
if ch == 'yes':
    print('hello')
a.mainloop()


# create a simple calculator using tkinter
# create a window like notepad with full menus
# create a username,password text boxes,create login button ,default username=admin,password=adminadmin
