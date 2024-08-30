# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 21:09:02 2024

@author: Carlos Luco Montofré
"""

class Datos_DAO:
    
    def __init__(self):
        self.codigo = 0
        self.lista_datos = {}
    
        
    def grabar_datos(self, data_DTO):
        dato     = data_DTO['dato']

        self.lista_datos[self.codigo]= dato
        self.codigo = self.codigo + 1
        print(self.lista_datos)
        return True
    
    def leer_datos(self):
        lista_DTO = self.lista_datos
        print("pide transferir")
        return lista_DTO
        