# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:01:55 2024

@author: Carlos Luco Montofré
"""

from tkinter import Frame, Label, Button

class HomeView(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configurar la columna principal
        self.grid_columnconfigure(0, weight=1)

        # Título del menú principal
        self.header = Label(self, text="Menú Principal", font=("Arial", 16))
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Etiqueta de saludo dinámico
        self.greeting = Label(self, text="", font=("Arial", 12))
        self.greeting.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Botones principales
        self.register_btn = Button(self, text="Registro de datos")
        self.register_btn.grid(row=2, column=0, padx=10, pady=5)

        self.list_btn = Button(self, text="Listar de datos")
        self.list_btn.grid(row=3, column=0, padx=10, pady=5)

        self.list_btn_cajas = Button(self, text="HU1 - Ver cajas activas")
        self.list_btn_cajas.grid(row=4, column=0, padx=10, pady=5)

        self.list_btn_ganancias = Button(self, text="HU2 - Ganancias por Moneda")  # Botón de HU2
        self.list_btn_ganancias.grid(row=5, column=0, padx=10, pady=5)

        self.list_btn_transacciones = Button(self, text="HU4 - Moneda Más Vendida")
        self.list_btn_transacciones.grid(row=6, column=0, padx=10, pady=5)

        self.register_btn_registrarTasaConversion = Button(self, text="HU6 - Registrar tipo de cambio")
        self.register_btn_registrarTasaConversion.grid(row=7, column=0, padx=10, pady=5)

        self.register_btn_registrarDisponibilidadCajas = Button(self, text="HU7 - Registrar disponibilidad de pesos cajas.")
        self.register_btn_registrarDisponibilidadCajas.grid(row=8, column=0, padx=10, pady=5)

        self.register_btn_registrarDisponibilidadMonedas = Button(self, text="HU8 - Registrar Compra Moneda Extranjera.")
        self.register_btn_registrarDisponibilidadMonedas.grid(row=9, column=0, padx=10, pady=5)

        self.signout_btn = Button(self, text="Salir", bg="red", fg="white")
        self.signout_btn.grid(row=10, column=0, padx=10, pady=10, sticky="ew")
