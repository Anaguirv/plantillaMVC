# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:15:46 2024

@author: Carlos Luco Montofré
"""

from .event_handler import ObservableModel
from .datos_DAO import Datos_DAO

class Gestor_Datos(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.datos_DAO = Datos_DAO()

    def registrar(self, datos_DTO):
        if self.datos_DAO.grabar_datos(datos_DTO):
            self.trigger_event("registro_datos")
                        
    def recuperar_datos(self):
        self.trigger_event("lista_datos")

    def desplegar_datos(self):
        lista_DTO = self.datos_DAO.leer_datos()        
        return lista_DTO

    def retornar(self):
        self.trigger_event("home")