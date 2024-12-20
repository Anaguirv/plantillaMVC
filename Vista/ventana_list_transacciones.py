from tkinter import Frame, Label, Button
from tkinter import ttk

class ListViewTransacciones(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Encabezado
        self.header = Label(self, text="Lista Monedas Mas Vendidas")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Treeview para mostrar los datos
        self.treeview = ttk.Treeview(self, columns=("Nombre Moneda", "Cantidad de Moneda Extranjera", "Monto Total en Pesos Chilenos"), show="headings")
        self.treeview.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Configuración de columnas
        self.treeview.column("Nombre Moneda", anchor="w", width=200)
        self.treeview.column("Cantidad de Moneda Extranjera", anchor="center", width=150)
        self.treeview.column("Monto Total en Pesos Chilenos", anchor="center", width=200)

        # Encabezados de las columnas
        self.treeview.heading("Nombre Moneda", text="Nombre Moneda", anchor="w")
        self.treeview.heading("Cantidad de Moneda Extranjera", text="Cantidad de Moneda Extranjera", anchor="center")
        self.treeview.heading("Monto Total en Pesos Chilenos", text="Monto Total en Pesos Chilenos", anchor="center")

        # Botón para retornar al menú
        self.return_btn = Button(self, text="Volver al Menú")
        self.return_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")  # Botón alineado a la izquierda

    def listar_datos(self, lista_DTO): 
        # Limpia los datos previos en la tabla
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Inserta los datos en la tabla
        for key in lista_DTO:
            dato = lista_DTO[key]
            self.treeview.insert(
                "", "end", 
                values=(dato["moneda_nombre"], dato["cantidad"], f"{dato['monto_total']:.2f}")
            )
