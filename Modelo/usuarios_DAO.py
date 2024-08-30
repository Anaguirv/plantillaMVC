# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:49:32 2024

@author: Carlos Luco Montofré
"""

class Usuario_DAO:
    
    def __init__(self):
        self.lista_usuarios = {'administrador':'123'}
    
    def busca_user(self,data_DTO):
        user     = data_DTO['username']
        password = data_DTO['password']

        if user in self.lista_usuarios and self.lista_usuarios[user] == password:
            return True
        else:
            return False
        
        
    def crea_user(self, data_DTO):
        user     = data_DTO['username']
        password = data_DTO['password']

        if user not in self.lista_usuarios:
            self.lista_usuarios[user] = password
            return True
        else:
            return False