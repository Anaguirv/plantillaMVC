# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 19:59:54 2024

@author: Carlos Luco Montofré
"""

class RegisterControllerTasaConversion:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["registerTasaConversion"]
        self._bind()

    def _bind(self):
        self.frame.register_btn.config(command=self.registro)
        self.frame.return_btn.config(command=self.retorno)

    def registro(self):
        print("Controlador/register_tasa_conversion -> Pide registrar tasa de cambio")
        data = self.frame.data_register()
        self.model.gestor_tasa_conversion.registrar(data)

    def retorno(self):
        self.view.switch("home")
           
    def close(self):
        self.view.stop_mainloop()