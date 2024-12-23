# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:51:41 2024

@author: Carlos Luco Montofré
"""

from .root import Root
from .ventana_list import ListView
from .ventana_list_cajas import ListViewCajas
from .ventana_home import HomeView
from .ventana_signin import SignInView
from .ventana_signup import SignUpView
from .ventana_register import RegisterView
from .ventana_list_transacciones import ListViewTransacciones
from .ventana_tasa_conversion import RegisterViewTasaConversion
from .ventana_registrar_disponibilidad_cajas import RegisterViewDisponibilidad
from .ventana_registrar_disponibilidad_moneda import RegisterViewCantidad
from .ventana_list_ganancias import ListViewGanancias
from .ventana_menu_gerente import MenuGerenteView
# Importar la vista de ganancias

class View:
    
    def __init__(self, controller):
        self.root = Root()
        self.frames = {}
        self.controller = controller  # Pasar el controlador principal

        self._add_frame(SignUpView, "signup")
        self._add_frame(SignInView, "signin")
        self._add_frame(HomeView, "home")
        self._add_frame(RegisterView, "register")
        self._add_frame(ListView, "list")
        self._add_frame(ListViewCajas, "listCajas")
        self._add_frame(MenuGerenteView, "menu_gerente")
        self._add_frame(ListViewTransacciones, "listTransacciones")
        self._add_frame(RegisterViewTasaConversion, "registerTasaConversion")
        self._add_frame(RegisterViewDisponibilidad, "registerDisponibilidad")
        self._add_frame(RegisterViewCantidad, "registerCantidad")
        self._add_frame(ListViewGanancias, "listGanancias", self.controller)  # Agregar vista de ganancias

    def _add_frame(self, Frame, name, *args):
        self.frames[name] = Frame(self.root, *args)  # Pasar argumentos adicionales
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()
        
    def stop_mainloop(self):
        self.root.destroy()
        
