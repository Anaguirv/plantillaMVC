class RegisterControllerDisponibilidad:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["registerDisponibilidad"]
        self._bind()

    def _bind(self):
        """
        Vincula las acciones de los botones a los métodos correspondientes.
        """
        self.frame.register_btn.config(command=self.registro)
        self.frame.return_btn.config(command=self.retorno)

    def registro(self):
        """
        Solicita al modelo que registre la disponibilidad de la caja.
        """
        print("Controlador/register_disponibilidad -> Solicitando registro de disponibilidad de caja")
        data = self.frame.data_register()

        # Intenta registrar los datos
        registro_exitoso = self.model.gestor_disponibilidad_cajas.registrar_disponibilidad(data)
        
        if registro_exitoso:
            print("Datos registrados correctamente.")
            # Limpia los campos después de registrar
            self.frame.caja_input.delete(0, 'end')
            self.frame.monto_input.delete(0, 'end')
        else:
            print("Error al registrar los datos.")


    def retorno(self):
        """
        Cambia la vista al menú principal.
        """
        self.view.switch("home")
           
    def close(self):
        """
        Detiene el bucle principal de la vista.
        """
        self.view.stop_mainloop()
