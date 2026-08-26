from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x300")

def msg():
    messagebox.showwarning("Alert!", "Stop! Virus found.")


button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

root.mainloop()

#END