import tkinter as tk
from tkinter import ttk


class AplicacionGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplicación de Eddie Martinez")

        # Etiqueta
        self.etiqueta = ttk.Label(master, text="Ingrese la información:")
        self.etiqueta.grid(row=0, column=0, padx=10, pady=10)

        # Campo de texto
        self.campo_texto = ttk.Entry(master)
        self.campo_texto.grid(row=0, column=1, padx=10, pady=10)

        # Botón Agregar
        self.boton_agregar = ttk.Button(master, text="Agregar", command=self.agregar)
        self.boton_agregar.grid(row=0, column=2, padx=10, pady=10)

        # Lista
        self.lista = tk.Listbox(master)
        self.lista.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Botón Limpiar
        self.boton_limpiar = ttk.Button(master, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def agregar(self):
        # Obtener texto del campo de texto
        texto = self.campo_texto.get()
        if texto:
            # Agregar texto a la lista
            self.lista.insert(tk.END, texto)
            # Limpiar campo de texto después de agregar
            self.campo_texto.delete(0, tk.END)

    def limpiar(self):
        # Limpiar la lista
        self.lista.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
