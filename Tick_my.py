from tkinter import *
import time

def tick1():
    # local time
    time2 = time.strftime("%H:%M:%S")

    # if time string has changed
    clock1.config(text=time2)
    clock1.after(200, tick1)


root = Tk()
clock1 = Label(root, font = ("times", 20, "bold"), bg="yellow")
clock1.pack(fill=BOTH, expand=1)
tick1()

root.mainloop()
