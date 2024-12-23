# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:23:26 2024

@author: Carlos Luco Montofré
"""

class ListControllerPesosDisponibles:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["listPesosDisponibles"]
        self._bind()

    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)

    def retorno(self):
        self.view.switch("home")
           
    def close(self):
        self.view.stop_mainloop()
        
    def update_view(self, lista_DTO):
        lista_DTO = self.model.gestor_pesos_disponibles.desplegar_datos()
        print("Controlador/list_pesosDisponibles")
        print("pide listar pesos disponibles")
        print("===============================================")
        print(lista_DTO)
        print("===============================================")
        self.frame.listar_datos(lista_DTO)
