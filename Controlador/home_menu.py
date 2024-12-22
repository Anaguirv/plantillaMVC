# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:03:10 2024

@author: Carlos Luco Montofré
"""

class HomeController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self):
        self.frame.register_btn.config(command=self.register)
        
        self.frame.list_btn.config(command=self.lists)
        
        self.frame.list_btn_cajas.config(command=self.listsCajas)

        # Nueva función para listar transacciones galindez estuvo por aca
        self.frame.list_btn_transacciones.config(command=self.listsTransacciones)
        self.frame.register_btn_registrarDisponibilidadCajas.config(command=self.registerDisponibilidadCajas)
        self.frame.register_btn_registrarDisponibilidadMonedas.config(command=self.registerDisponibilidadMoneda)


        

        self.frame.register_btn_registrarDisponibilidadCajas.config(command=self.registerDisponibilidadCajas)

        

        self.frame.register_btn_registrarTasaConversion.config(command=self.registerTasaConversion)

        self.frame.signout_btn.config(command=self.logout)


    def register(self):
        self.view.switch("register")
        
    def lists(self):
        self.model.gestor_datos.recuperar_datos()

    def listsCajas(self):
        print("controlador/home_menu.py -> pide recuperar datos")
        self.model.gestor_cajas.recuperar_datos()

    def listsTransacciones(self):
        print("controlador/home_menu.py -> pide recuperar datos")
        self.model.gestor_transacciones.recuperar_datos()

    def registerTasaConversion(self):
        print("controlador/home_menu.py -> pide abrir ventana para ingreso de tasa de conversion")
        self.view.switch("registerTasaConversion")

    def registerDisponibilidadCajas(self):
        print("controlador/home_menu.py -> pide abrir ventana para registrar disponibilidad de cajas")
        self.view.switch("registerDisponibilidad")

    def registerDisponibilidadMoneda(self):
        self.view.switch("registerCantidad")

    def logout(self):
        self.model.gestor_usuarios.logout()

    def update_view(self):
        current_user = self.model.gestor_usuarios.saludo_usuario()
        if current_user:
            username = current_user["username"]
        else:
            username = 'Set-up sistema'
        self.frame.greeting.config(text=f"Bienvenido, {username}!")

            
