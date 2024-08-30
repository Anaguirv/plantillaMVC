# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:53:53 2024

@author: Carlos Luco Montofré
"""

from .gestor_usuarios import Gestor_Usuarios
from .gestor_datos import Gestor_Datos

class Model:
    def __init__(self):
        self.gestor_usuarios = Gestor_Usuarios()
        self.gestor_datos = Gestor_Datos()