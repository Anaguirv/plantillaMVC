# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:36:15 2024

@author: Carlos Luco Montofré
"""

from Modelo.main import Model
from Vista.main import View
from Controlador.main import Controller

def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()

if __name__ == "__main__":
    main()