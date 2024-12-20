import tkinter as tk
from tkinter import ttk
from Controlador.profit_controller import ProfitController

class VentanaGanancias:
    def __init__(self, root, db_path):
        self.root = root
        self.root.title("Ganancias por Moneda")
        self.root.geometry("600x400")

        self.controlador = ProfitController(db_path)

        # Crear tabla para mostrar datos
        self.tabla = ttk.Treeview(root, columns=("Moneda", "Ganancia en Pesos"), show="headings")
        self.tabla.heading("Moneda", text="Moneda")
        self.tabla.heading("Ganancia en Pesos", text="Ganancia en Pesos")
        self.tabla.pack(fill=tk.BOTH, expand=True)

        # Botón para cargar datos
        btn_cargar = tk.Button(root, text="Cargar Ganancias", command=self.cargar_ganancias)
        btn_cargar.pack(pady=10)

    def cargar_ganancias(self):
        # Limpiar tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # Obtener ganancias desde el controlador
        datos = self.controlador.obtener_ganancias()

        # Insertar datos en la tabla
        for moneda, ganancia in datos:
            self.tabla.insert("", tk.END, values=(moneda, f"${ganancia:,.2f}"))

# Ejecutar la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaGanancias(root, "acme.db")
    root.mainloop()
