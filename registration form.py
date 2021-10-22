from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to Ourpage")
window.geometry('900x300')
window.configure(background =  "maroon");
a = Label(window ,text ="First Name").grid(row = 0,column = 0)
b = Label(window ,text ="Last Name").grid(row = 1,column = 0)
c = Label(window ,text ="Date Of Birth").grid(row = 2,column = 0)
d = Label(window ,text ="Email ID").grid(row = 3,column = 0)
e= Label(window ,text ="Password").grid(row = 4,column = 0)
f = Label(window ,text ="Contact").grid(row = 5,column = 0)
a1 = Entry(window).grid(row = 0,column = 1)
b2 = Entry(window).grid(row = 1,column = 1)
c3 = Entry(window).grid(row = 2,column = 1)
d4 = Entry(window).grid(row = 3,column = 1)
e5 = Entry(window).grid(row = 4,column = 1)
e6 = Entry(window).grid(row = 5,column = 1)
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text = res)
button = ttk.Button(window,text="Submit").grid(row=6,column=0)
button = ttk.Button(window,text="Back").grid(row=6,column=1)
window.mainloop()