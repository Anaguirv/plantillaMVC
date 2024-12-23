# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:15:46 2024

@author: Carlos Luco Montofré
"""

from .event_handler import ObservableModel
from .pesosDisponibles_DAO import PesosDisponibles_DAO

class Gestor_Pesos_Disponibles(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.pesosDisponibles_DAO = PesosDisponibles_DAO()
                        
    def recuperar_datos(self):
        print("Recuperando datos...")
        self.trigger_event("lista_pesosDisponibles")
        print("...Datos recuperados")

    def desplegar_datos(self):
        print("Desplegando datos...")
        lista_DTO = self.pesosDisponibles_DAO.leer_datos()  
        print("===____________________________________________________________________")
        print("Modulo Modelo/gestor_pesos_disponibles")
        print(lista_DTO)
        print("===____________________________________________________________________")      
        return lista_DTO

    def retornar(self):
        self.trigger_event("home")