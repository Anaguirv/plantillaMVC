# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 21:09:02 2024

@author: Carlos Luco Montofré
"""

from .conectorBD import ConectorBD


class Tasa_Conversion_DAO:
    
    def __init__(self):
        # Configura la conexión a la base de datos
        self.conector = ConectorBD(
            hostdb='localhost',
            userdb='root',       
            passwordb='',       
            basedatosdb='acme'
        )

    def grabar_datos(self, data_DTO):
        dato     = data_DTO['dato']
        print("modelo/tasa_conversion -> Datos preparados para ser insertados en tabla 'tasa_conversion'= ", dato)

        # Crear en la base de datos
        self.conector.activarConexion()
        sql = f"INSERT INTO tasa_conversion (tipo_cambio) VALUES ('{dato}')"
        result, error = self.conector.ejecutarInsert(sql)
        self.conector.desactivarConexion()

        if result == 0:
            print("Tasa de cambio registrado exitosamente en la base de datos.")
            return True
        else:
            print(f"Error al registrar Tasa de Cambio en la base de datos: {error}")
            return False
    
        