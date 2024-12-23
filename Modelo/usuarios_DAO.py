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

    def busca_user(self, datos_DTO):
        """
        Busca al usuario por su nombre de usuario en la base de datos.
        :param datos_DTO: Diccionario con 'username' y 'password'.
        :return: Diccionario con datos del usuario si existe, None si no existe.
        """
        username = datos_DTO["username"]

        try:
            # Activa la conexión
            self.conector.activarConexion()

            # Ejecuta la consulta
            query = "SELECT username, password, rol FROM usuario WHERE username = %s"
            cursor = self.conector.conexion.cursor()  # Usa el cursor del conector
            cursor.execute(query, (username,))
            resultado = cursor.fetchone()

            # Cierra la conexión
            self.conector.desactivarConexion()

            # Procesa el resultado
            if resultado:
                return {
                    "username": resultado[0],
                    "password": resultado[1],  # Contraseña (podría estar cifrada)
                    "rol": resultado[2]
                }
            else:
                return None
        except Exception as e:
            # Maneja errores en la conexión o consulta
            print(f"Error al buscar usuario: {e}")
            self.conector.desactivarConexion()
            return None

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
