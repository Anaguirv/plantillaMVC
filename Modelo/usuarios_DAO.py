# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:49:32 2024

@author: Carlos Luco Montofré
"""

from .conectorBD import ConectorBD

class Usuario_DAO:
    
    def __init__(self):
        # Lista de usuarios para pruebas locales
        self.lista_usuarios = {'administrador': '123'}
        
        # Configura la conexión a la base de datos
        self.conector = ConectorBD(
            hostdb='localhost',
            userdb='root',       
            passwordb='',       
            basedatosdb='acme'
        )

    def busca_user(self, data_DTO):
        user = data_DTO['username']
        password = data_DTO['password']

        # Buscar usuario en la lista local
        if user in self.lista_usuarios and self.lista_usuarios[user] == password:
            return True

        # Buscar usuario en la base de datos
        self.conector.activarConexion()
        sql = f"SELECT * FROM usuario WHERE username = '{user}' AND password = '{password}'"
        result, datos = self.conector.ejecutarSelectOne(sql)
        self.conector.desactivarConexion()

        return result == 0 and datos is not None

    def crea_user(self, data_DTO):
        user = data_DTO['username']
        password = data_DTO['password']

        # Crear usuario en la lista local (para pruebas)
        if user not in self.lista_usuarios:
            self.lista_usuarios[user] = password

        # Crear usuario en la base de datos
        self.conector.activarConexion()
        sql = f"INSERT INTO usuario (username, password) VALUES ('{user}', '{password}')"
        result, error = self.conector.ejecutarInsert(sql)
        self.conector.desactivarConexion()

        if result == 0:
            print("Usuario creado exitosamente en la base de datos.")
            return True
        else:
            print(f"Error al crear usuario en la base de datos: {error}")
            return False
