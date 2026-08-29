from tkinter import *
from tkinter.filedialog import *

w = Tk()
w.title("Text Editor")
w.geometry("600x400")

def open_file():
    f = askopenfile(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if f:
        t.delete(1.0, END)
        with open(f) as x:
            t.insert(END, x.read())
        w.title(f"Codingal's Text Editor - {f}")

def save_file():
    f = asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if f:
        with open(f, "w") as x:
            x.write(t.get(1.0, END))
        w.title(f"Codingal's Text Editor - {f}")


b = Frame(w)
Button(b, text="Open", command=open_file).pack(padx=5, pady=5)
Button(b, text="Save As...", command=save_file).pack(padx=5)
b.pack(side=LEFT, fill=Y)

t = Text(w)
t.pack(side=RIGHT, fill=BOTH, expand=True)

w.mainloop()