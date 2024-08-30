# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:59:45 2024

@author: Carlos Luco Montofré
"""

from .event_handler import ObservableModel
from .usuarios_DAO import Usuario_DAO

class Gestor_Usuarios(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.current_user = None
        self.usuario_DAO = Usuario_DAO()

    def login(self, datos_DTO):
        if self.usuario_DAO.busca_user(datos_DTO):
            self.current_user = datos_DTO
            self.trigger_event("ingreso_sistema")

    def logup(self, datos_DTO):
        if self.usuario_DAO.crea_user(datos_DTO):
            self.current_user = datos_DTO
            self.trigger_event("salida_sistema")
            
    def saludo_usuario(self):
        return self.current_user

    def logout(self):
        self.trigger_event("salida_sistema")