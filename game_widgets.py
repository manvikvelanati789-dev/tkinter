from tkinter import *
from datetime import date

root = Tk()
root.title("demo Window")
root.geometry("400x300")

Label(root, text="Hello!", fg="white", bg="#072F5F").pack()
Label(root, text="Full name", fg="white", bg="#DE1010").pack()

name = Entry(root)
name.pack()

text = Text(root, height=3)
text.pack()

def display():
    text.insert(END, f"Hello {name.get()}\n")
    text.insert(END, f"Welcome to the application!\nToday's date is {date.today()}\n")

Button(root, text="Submit", command=display, bg="#1261A0", fg="white").pack()

root.mainloop()

#END