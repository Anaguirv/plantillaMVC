# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:15:46 2024

@author: Carlos Luco Montofré
"""

from .event_handler import ObservableModel
from .cajas_DAO import Cajas_DAO

class Gestor_Cajas(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.cajas_DAO = Cajas_DAO()
                        
    def recuperar_datos(self):
        self.trigger_event("lista_cajas")

    def desplegar_datos(self):
        lista_DTO = self.cajas_DAO.leer_datos()        
        return lista_DTO

    def retornar(self):
        self.trigger_event("home")