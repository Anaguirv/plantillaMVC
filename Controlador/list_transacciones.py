class ListControllerTransacciones:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["listTransacciones"]
        self._bind()

    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)

    def retorno(self):
        self.view.switch("home")
           
    def close(self):
        self.view.stop_mainloop()
        
    def update_view(self, lista_DTO):
        lista_DTO = self.model.gestor_transacciones.desplegar_datos()
        print("Controlador/list_transacciones")
        print("pide listar transacciones")
        print("===============================================")
        print(lista_DTO)
        print("===============================================")
        self.frame.listar_datos(lista_DTO)