import random
from tkinter import *
from random import *

def click():
    print("получилось")
    new_x = randint(50, 550)
    new_y = randint(50, 550)
    btn.place(x = new_x, y = new_y)

win = Tk()
win.geometry("600x600")
win.title("Нинзя")

arbuz = PhotoImage(file='melon.png')
btn = Button(image=arbuz, command=click)
btn.place(x=100, y=100)



win.mainloop()

