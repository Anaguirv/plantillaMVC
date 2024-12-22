

from tkinter import Frame, Label, Button, Entry

class RegisterViewDisponibilidad(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Registrar Disponibilidad de Caja")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Campo para el número de caja
        self.caja_label = Label(self, text="Número de Caja")
        self.caja_input = Entry(self)
        self.caja_label.grid(row=1, column=0, padx=10, sticky="w")
        self.caja_input.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        # Campo para el monto disponible
        self.monto_label = Label(self, text="Monto Disponible")
        self.monto_input = Entry(self)
        self.monto_label.grid(row=2, column=0, padx=10, sticky="w")
        self.monto_input.grid(row=2, column=1, padx=(0, 20), sticky="ew")

        self.greeting = Label(self, text="")
        self.greeting.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.register_btn = Button(self, text="Registrar Datos")
        self.register_btn.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        
        self.return_btn = Button(self, text="Retornar Menú")
        self.return_btn.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        
    def data_register(self):
        numero_caja = self.caja_input.get()
        monto_disponible = self.monto_input.get()
        
        data_dto = {
            "numero_caja": numero_caja,
            "monto_disponible": monto_disponible
        }
        
        # Limpiar los campos de entrada
        self.caja_input.delete(0, last=len(numero_caja))
        self.monto_input.delete(0, last=len(monto_disponible))

        return data_dto
