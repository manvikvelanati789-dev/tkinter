from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("400x300")

def handle_keypress(event):
    """Print character associated to the key pressed"""
    print(event.char)


window.bind("<Key>", handle_keypress)


def handle_click(event):
    """Print a message when the button is clicked"""
    print("\nThe button was clicked!")

button = Button(text="Click me")
button.pack()

button.bind("<Button-1>", handle_click)
window.mainloop()

