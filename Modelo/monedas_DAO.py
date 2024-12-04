# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:20:31 2024

@author: Carlos Luco Montofré
"""


class Monedas_DAO:

    def __init__(self, conectorBD) -> None:

        self.conectorBD = conectorBD


    def recuperar_listaMonedas(self):
        estado = self.conectorBD.activarConexion()

        if estado == 66:
            del self.conectorBD
            return estado, None
        
        sql = "select cod_moneda, nom_moneda, tipo_cambio from monedas"
        estado, datos = self.conectorBD.ejecutarSelectAll(sql)

        listaMonedas_DTO = {}

        if estado == 0:

            for i in range(0, len(datos)):
                registro = {"codigo": datos[i][0], "nombre": datos[i][1], "tipo": datos[i][2]}
                listaMonedas_DTO[i]= registro


        self.conectorBD.desactivarConexion()

        del self.conectorBD

        return estado, listaMonedas_DTO

