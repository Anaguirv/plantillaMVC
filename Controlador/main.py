# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:02:35 2024

@author: Carlos Luco Montofré
"""

from .home_menu import HomeController
from .list_datos import ListController
from .signin_usuario import SignInController
from .signup_usuario import SignUpController
from .register_datos import RegisterController

class Controller:
    
    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.signin_controller     = SignInController(model, view)
        self.signup_controller     = SignUpController(model, view)
        self.home_controller       = HomeController(model, view)
        self.register_controller   = RegisterController(model, view)
        self.list_controller       = ListController(model, view)
        

        self.model.gestor_usuarios.add_event_listener(
            "ingreso_sistema", self.autentificacion_signin_listener)
        
        self.model.gestor_usuarios.add_event_listener(
            "salida_sistema", self.autentificacion_signout_listener)

        self.model.gestor_datos.add_event_listener(
            "registro_datos", self.datos_register_listener)
                
        self.model.gestor_datos.add_event_listener(
            "lista_datos", self.datos_list_listener)
              
        self.model.gestor_datos.add_event_listener(
            "retorno_menu_registro", self.datos_retorno_register_listener)
        

    def autentificacion_signin_listener(self, data):
        self.home_controller.update_view()
        self.view.switch("home")
        
    def autentificacion_signout_listener(self, data):
        self.view.switch("signin")

    def datos_register_listener(self, data):
        self.view.switch("register")

    def datos_list_listener(self, data):
        self.list_controller.update_view()
        self.view.switch("list")


    def datos_retorno_register_listener(self, data):
        self.view.switch("home")

    def start(self):
        self.view.switch("signin")
        self.view.start_mainloop()