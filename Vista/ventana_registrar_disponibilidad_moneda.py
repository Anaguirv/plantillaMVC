from tkinter import Frame, Label, Button, Entry

class RegisterViewCantidad(Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Editar Cantidad de Moneda")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Campo para el ID de la moneda
        self.moneda_id_label = Label(self, text="ID de Moneda")
        self.moneda_id_input = Entry(self)
        self.moneda_id_label.grid(row=1, column=0, padx=10, sticky="w")
        self.moneda_id_input.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        # Campo para la nueva cantidad
        self.cantidad_label = Label(self, text="Nueva Cantidad")
        self.cantidad_input = Entry(self)
        self.cantidad_label.grid(row=2, column=0, padx=10, sticky="w")
        self.cantidad_input.grid(row=2, column=1, padx=(0, 20), sticky="ew")

        self.greeting = Label(self, text="")
        self.greeting.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.register_btn = Button(self, text="Actualizar Cantidad")
        self.register_btn.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.return_btn = Button(self, text="Retornar Menú")
        self.return_btn.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    def data_register(self):
        id_moneda = self.moneda_id_input.get()
        nueva_cantidad = self.cantidad_input.get()

        data_dto = {
            "id_moneda": id_moneda,
            "nueva_cantidad": nueva_cantidad
        }

        # Limpiar los campos de entrada
        self.moneda_id_input.delete(0, last=len(id_moneda))
        self.cantidad_input.delete(0, last=len(nueva_cantidad))

        return data_dto
