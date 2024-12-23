# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:53:53 2024

@author: Carlos Luco Montofré
"""

from .gestor_usuarios import Gestor_Usuarios
from .gestor_datos import Gestor_Datos
from .gestor_cajas import Gestor_Cajas
from .gestor_transacciones import Gestor_Transacciones
from .gestor_tasa_conversion import Gestor_Tasa_Conversion
from .gestor_registrar_disponibilidad_cajas import Gestor_Disponibilidad_Cajas
from .gestor_registrar_disponibilidad_moneda import Gestor_Monedas
from .monedas_DAO import Moneda_DAO  # Importar Moneda_DAO
from .gestor_pesos_disponibles import Gestor_Pesos_Disponibles


class Model:
    def __init__(self):
        self.gestor_usuarios = Gestor_Usuarios()
        self.gestor_datos = Gestor_Datos()
        self.gestor_cajas = Gestor_Cajas()
        self.gestor_transacciones = Gestor_Transacciones()
        self.gestor_tasa_conversion = Gestor_Tasa_Conversion()
        self.gestor_disponibilidad_cajas = Gestor_Disponibilidad_Cajas()
        self.gestor_monedas = Gestor_Monedas()
        self.monedas_dao = Moneda_DAO()  # Instanciar Moneda_DAO
        self.gestor_pesos_disponibles = Gestor_Pesos_Disponibles()
