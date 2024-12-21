# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:15:46 2024

@author: Carlos Luco Montofré
"""

from .event_handler import ObservableModel
from .tasa_conversion_DAO import Tasa_Conversion_DAO

class Gestor_Tasa_Conversion(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.tasa_conversion_DAO = Tasa_Conversion_DAO()

    def registrar(self, datos_DTO):
        if self.tasa_conversion_DAO.grabar_datos(datos_DTO):
            self.trigger_event("registro_tasa_conversion")
                        
    def recuperar_datos(self):
        self.trigger_event("lista_datos")

    def desplegar_datos(self):
        lista_DTO = self.datos_DAO.leer_datos()        
        return lista_DTO

    def retornar(self):
        self.trigger_event("home")