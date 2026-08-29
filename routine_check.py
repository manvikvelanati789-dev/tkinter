import tkinter as tk
from tkinter import messagebox

class RoutineCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("After-School Routine Checker")
        self.root.geometry("400x350")
        
        self.routine_tasks = ["Do Homework", "Eat a Snack", "Pack School Bag", "Read a Book", "Relax"]
        self.task_index = 0

        self.entry_label = tk.Label(root, text="Type your current task:", font=("Arial", 10, "bold"))
        self.entry_label.pack(pady=5)
        
        self.task_entry = tk.Entry(root, width=30, font=("Arial", 11))
        self.task_entry.pack(pady=5)

        self.task_entry.bind("<KeyRelease>", self.on_key_release)

        self.char_label = tk.Label(root, text="Last character typed: None", fg="blue")
        self.char_label.pack(pady=5)

        self.canvas_label = tk.Label(root, text="Click inside the box below:", font=("Arial", 10))
        self.canvas_label.pack(pady=5)
        
        self.routine_area = tk.Canvas(root, width=300, height=80, bg="lightgray", highlightthickness=1, highlightbackground="gray")
        self.routine_area.pack(pady=5)
       
        self.routine_area.bind("<Button-1>", self.on_canvas_click)
        
        self.canvas_text = self.routine_area.create_text(150, 40, text="Routine Area", font=("Arial", 12))

        self.next_btn = tk.Button(root, text="Show Next Routine Task", command=self.show_next_task, bg="green", fg="white", font=("Arial", 10, "bold"))
        self.next_btn.pack(pady=15)

    def on_key_release(self, event):
        """Displays the last character typed into the entry box."""
        current_text = self.task_entry.get()
        if current_text:
            last_char = current_text[-1]
            self.char_label.config(text=f"Last character typed: '{last_char}'")
        else:
            self.char_label.config(text="Last character typed: None")

    def on_canvas_click(self, event):
        """Reacts to a mouse click inside the routine canvas area."""
        if not self.task_entry.get().strip():
            messagebox.showwarning("Warning", "Please enter a task first before interacting!")
        else:
            self.routine_area.config(bg="lightblue")
            self.routine_area.itemconfig(self.canvas_text, text="Active Routine Mode")

    def show_next_task(self):
        """Displays the next sequential task from the routine list."""
        current_task = self.routine_tasks[self.task_index]
        messagebox.showinfo("Next Task", f"Your next routine task is:\n👉 {current_task}")
        
        self.task_index = (self.task_index + 1) % len(self.routine_tasks)

if __name__ == "__main__":
    root = tk.Tk()
    app = RoutineCheckerApp(root)
    root.mainloop()