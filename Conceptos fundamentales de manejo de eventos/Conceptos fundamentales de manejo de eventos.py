import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tasks = []

        self.entry_task = tk.Entry(root, width=40)
        self.entry_task.pack(pady=10)

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_as_completed)
        self.complete_button.pack()

        self.remove_button = tk.Button(root, text="Eliminar Tarea", command=self.remove_task)
        self.remove_button.pack()

        self.populate_listbox()

        # Bind Enter key to add_task function
        self.entry_task.bind("<Return>", lambda event: self.add_task())

    def populate_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.populate_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def mark_as_completed(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.itemconfig(index, {'bg': 'light grey', 'fg': 'green'})
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.populate_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
