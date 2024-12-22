class RegisterControllerCantidad:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["registerCantidad"]
        self._bind()

    def _bind(self):
        """
        Vincula las acciones de los botones a los métodos correspondientes.
        """
        self.frame.register_btn.config(command=self.actualizar_cantidad)
        self.frame.return_btn.config(command=self.retorno)

    def actualizar_cantidad(self):
        """
        Solicita al modelo que actualice la cantidad de una moneda.
        """
        print("Controlador/register_cantidad -> Solicitando actualización de cantidad de moneda")
        data = self.frame.data_register()

        # Intenta actualizar los datos
        actualizacion_exitosa = self.model.gestor_monedas.editar_cantidad(data)
        
        if actualizacion_exitosa:
            print("Cantidad actualizada correctamente.")
            # Limpia los campos después de actualizar
            self.frame.moneda_id_input.delete(0, 'end')
            self.frame.cantidad_input.delete(0, 'end')
        else:
            print("Error al actualizar la cantidad.")

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
