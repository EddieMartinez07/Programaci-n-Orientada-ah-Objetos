import tkinter as tk
from tkinter import messagebox

class AplicacionGestorTareas:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Tareas")

        self.tareas = []
        self.tareas_completadas = []

        self.entrada = tk.Entry(master, width=50)
        self.entrada.pack(pady=10)

        self.boton_agregar = tk.Button(master, text="Agregar Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack()

        self.boton_completar = tk.Button(master, text="Marcar como Completada", command=self.marcar_como_completada)
        self.boton_completar.pack()

        self.boton_eliminar = tk.Button(master, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack()

        self.lista_tareas = tk.Listbox(master, width=50)
        self.lista_tareas.pack(pady=10)

        self.llenar_lista()

        # Enlazar eventos
        self.entrada.bind("<Return>", lambda event: self.agregar_tarea())
        self.master.bind("c", lambda event: self.marcar_como_completada())
        self.master.bind("d", lambda event: self.eliminar_tarea())
        self.master.bind("<Escape>", lambda event: self.master.quit())

    def llenar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            self.lista_tareas.insert(tk.END, tarea)
        for tarea in self.tareas_completadas:
            self.lista_tareas.insert(tk.END, tarea + " (Completada)")

    def agregar_tarea(self):
        tarea = self.entrada.get().strip()
        if tarea:
            self.tareas.append(tarea)
            self.llenar_lista()
            self.entrada.delete(0, tk.END)

    def marcar_como_completada(self):
        indice_tarea_seleccionada = self.lista_tareas.curselection()
        if indice_tarea_seleccionada:
            tarea = self.lista_tareas.get(indice_tarea_seleccionada)
            if tarea in self.tareas:
                self.tareas.remove(tarea)
                self.tareas_completadas.append(tarea)
                self.llenar_lista()

    def eliminar_tarea(self):
        indice_tarea_seleccionada = self.lista_tareas.curselection()
        if indice_tarea_seleccionada:
            tarea = self.lista_tareas.get(indice_tarea_seleccionada)
            if tarea in self.tareas:
                self.tareas.remove(tarea)
            elif tarea in self.tareas_completadas:
                self.tareas_completadas.remove(tarea)
            self.llenar_lista()

def main():
    root = tk.Tk()
    app = AplicacionGestorTareas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
