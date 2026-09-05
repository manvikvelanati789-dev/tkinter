from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("650x400")
root.configure(bg="light blue")

img = ImageTk.PhotoImage(Image.open("messi.png").resize((200, 200)))
Label(root, image=img, bg="light blue").pack(x=180, y=20)
Label(root, text="Welcome to the Messi fan club", font=("Arial", 20), bg="light blue").place(relx=0.5, y=340, anchor=CENTER)

def topwin():
    t = Toplevel(root)
    t.geometry("400x300")
    t.configure(bg="light green")

    Label(t, text="Amount", font=("Arial", 16), bg="light green").place(x=230, y=50)
    en = Entry(t)
    