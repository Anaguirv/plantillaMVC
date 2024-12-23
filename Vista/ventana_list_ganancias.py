from tkinter import Frame, Label, ttk, Button

class ListViewGanancias(Frame):
    def __init__(self, root, controller):
        """
        Inicializa la vista para mostrar las ganancias por moneda.

        :param root: Ventana principal o contenedor padre.
        :param controller: Controlador asociado a esta vista.
        """
        super().__init__(root)
        self.controller = controller

        # Configuración del layout
        self.grid_columnconfigure(0, weight=1)

        # Título
        self.header = Label(self, text="Ganancias por Moneda", font=("Arial", 16))
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Tabla para mostrar las ganancias
        self.tree = ttk.Treeview(self, columns=("moneda", "ganancias"), show="headings", height=10)
        self.tree.heading("moneda", text="Moneda")
        self.tree.heading("ganancias", text="Ganancias en Pesos")
        self.tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Configuración de scroll para la tabla
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=1, sticky="ns")

        # Botón para regresar al menú principal
        self.return_btn = Button(self, text="Volver al Menú", command=self.volver_menu, font=("Arial", 10))
        self.return_btn.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    def listar_datos(self, datos):
        """
        Llena la tabla con los datos proporcionados.

        :param datos: Lista de diccionarios con las ganancias por moneda.
        """
        # Limpiar datos anteriores
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar nuevos datos
        for fila in datos:
            self.tree.insert("", "end", values=(fila["nombre"], f"${fila['ganancias']:,.2f}"))

    def volver_menu(self):
        """
        Regresa al menú principal.
        """
        self.controller.view.switch("home")
