# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:01:03 2024

@author: Carlos Luco Montofré
"""

import mysql.connector


class ConectorBD:

    def __init__(self, hostdb, userdb, passwordb, basedatosdb):
        self.__hostdb = hostdb
        self.__userdb = userdb
        self.__passwordb = passwordb
        self.__basedatosdb = basedatosdb
        self.conexion = None  # Inicializar la conexión
        self.cursor = None    # Inicializar el cursor

    def activarConexion(self):
        """
        Intenta activar la conexión con la base de datos.
        Retorna un código de estado y un mensaje en caso de error.
        """
        try:
            self.conexion = mysql.connector.connect(
                host=self.getHost(),
                user=self.getUser(),
                password=self.getPassword(),
                database=self.getBasedatos()
            )
            self.cursor = self.conexion.cursor()
            print("Conexión a la base de datos exitosa.")
            return 0, None  # Retorna éxito
        except mysql.connector.Error as e:
            print(
                'DRIVER={MySQL};SERVER=' + self.getHost() +
                ';DATABASE=' + self.getBasedatos() +
                ';UID=' + self.getUser() +
                ';PWD=' + self.getPassword(),
                "Falló Conexión"
            )
            self.conexion = None  # Asegurar que esté vacío si falla
            self.cursor = None    # Asegurar que esté vacío si falla
            return 66, e  # Retorna error

    def ejecutarSelectOne(self, sql):
        try:
            if not self.cursor:
                raise Exception("No hay conexión activa.")
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            return 0, datos
        except Exception as e:
            self.realizarRollback()
            return 1, e

    def ejecutarSelectAll(self, sql):
        try:
            if not self.cursor:
                raise Exception("No hay conexión activa.")
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return 0, datos
        except Exception as e:
            self.realizarRollback()
            return 1, e

    def ejecutarInsert(self, sql):
        try:
            if not self.cursor:
                raise Exception("No hay conexión activa.")
            self.cursor.execute(sql)
            self.realizarCommit()
            return 0, None  # Devolver 0 y None en caso de éxito
        except Exception as e:
            self.realizarRollback()
            return 1, e

    def ejecutarDelete(self, sql):
        try:
            if not self.cursor:
                raise Exception("No hay conexión activa.")
            self.cursor.execute(sql)
            self.realizarCommit()
            return 0
        except Exception as e:
            self.realizarRollback()
            return 1, e

    def ejecutarUpdate(self, sql):
        try:
            if not self.cursor:
                raise Exception("No hay conexión activa.")
            self.cursor.execute(sql)
            self.realizarCommit()
            return 0
        except Exception as e:
            self.realizarRollback()
            return 1, e

    def getHost(self):
        return self.__hostdb

    def getUser(self):
        return self.__userdb

    def getPassword(self):
        return self.__passwordb

    def getBasedatos(self):
        return self.__basedatosdb

    def realizarCommit(self):
        if self.conexion:
            self.conexion.commit()

    def realizarRollback(self):
        if self.conexion:
            self.conexion.rollback()

    def desactivarConexion(self):
        if self.conexion:
            self.conexion.close()
            self.conexion = None
            self.cursor = None
