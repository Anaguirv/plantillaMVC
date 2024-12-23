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
        """
        Valida las credenciales del usuario.
        :param datos_DTO: Diccionario con 'username' y 'password'.
        :return: Diccionario con datos del usuario si las credenciales son correctas, None si no lo son.
        """
        usuario = self.usuario_DAO.busca_user(datos_DTO)  # Obtén el usuario de la base de datos
        print("Resultado de busca_user:", usuario)  # Imprime el resultado para depurar

        if usuario:  # Si el usuario existe
            print("Contraseña ingresada:", datos_DTO["password"])
            print("Contraseña en BD:", usuario["password"])

            if usuario["password"] == datos_DTO["password"]:  # Comparación de contraseña
                self.current_user = usuario
                self.trigger_event("ingreso_sistema")
                return usuario  # Retorna el usuario si las credenciales son correctas
            else:
                print("Contraseña incorrecta.")  # Mensaje de depuración
                return None
        else:
            print("Usuario no encontrado.")  # Mensaje de depuración
            return None 

    def logup(self, datos_DTO):
        if self.usuario_DAO.crea_user(datos_DTO):
            self.current_user = datos_DTO
            self.trigger_event("salida_sistema")
            
    def saludo_usuario(self):
        return self.current_user

    def logout(self):
        self.trigger_event("salida_sistema")
