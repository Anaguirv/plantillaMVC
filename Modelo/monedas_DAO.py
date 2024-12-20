# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:20:31 2024

@author: Carlos Luco Montofré
"""

class Monedas_DAO:
    def __init__(self, conectorBD) -> None:
        self.conectorBD = conectorBD

    def obtener_ganancias_por_moneda(self):
        """
        Consulta las ganancias por moneda en pesos.
        """
        # Activar la conexión
        estado = self.conectorBD.activarConexion()
        if estado[0] == 66:
            del self.conectorBD
            return estado, None

        # Consulta SQL para calcular ganancias
        sql = """
            SELECT moneda, SUM(ganancia * tasa_conversion) AS ganancias_pesos
            FROM transacciones
            GROUP BY moneda
        """
        estado, datos = self.conectorBD.ejecutarSelectAll(sql)

        # Transformar resultados en un diccionario estructurado
        ganancias_por_moneda = {}
        if estado == 0 and datos:
            for i, fila in enumerate(datos):
                registro = {
                    "moneda": fila[0],
                    "ganancias_pesos": fila[1]
                }
                ganancias_por_moneda[i] = registro

        # Cerrar la conexión
        self.conectorBD.desactivarConexion()
        del self.conectorBD

        return estado, ganancias_por_moneda
