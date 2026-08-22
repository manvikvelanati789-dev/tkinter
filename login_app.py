from tkinter import *

r = Tk()
r.title("Login App")
r.geometry("400x400")
e = []


for i,x in enumerate(["Name", "Email", "Password"]):
    Label(r, text=x).grid(row=i)
    a = Entry(r, show="*" if i == 2 else "")
    a.grid(row=i, column=1)
    e.append(a)

t = Text(r, height=5, width=40)
t.grid(row=4, columnspan=2)
Button(
    r,
    text="create",
    command=lambda: t.insert(END, "Hey " + e[0].get() + "\nCongratulations!"),
).grid(row=3, columnspan=2)

r.mainloop()

#END