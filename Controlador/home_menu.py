# -*- coding: utf-8 -*-
"""
Controlador del menú principal.
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
        self.frame.list_btn_ganancias.config(command=self.listsGanancias)  # Botón para HU2
        self.frame.list_btn_transacciones.config(command=self.listsTransacciones)
        self.frame.register_btn_registrarDisponibilidadCajas.config(command=self.registerDisponibilidadCajas)
        self.frame.register_btn_registrarDisponibilidadMonedas.config(command=self.registerDisponibilidadMoneda)
        self.frame.register_btn_registrarTasaConversion.config(command=self.registerTasaConversion)
        self.frame.signout_btn.config(command=self.logout)
        self.frame.list_btn_pesosDisponibles.config(command=self.listPesosDisponibles)


    def register(self):
        self.view.switch("register")
        
    def lists(self):
        self.model.gestor_datos.recuperar_datos()

    def listsCajas(self):
        print("controlador/home_menu.py -> pide recuperar datos")
        self.model.gestor_cajas.recuperar_datos()

    def listPesosDisponibles(self):
        print("controlador/home_menu.py -> pide recuperar datos")
        self.model.gestor_pesos_disponibles.recuperar_datos()

    def listsGanancias(self):
        """
        Cambia a la vista de ganancias por moneda.
        """
        print("controlador/home_menu.py -> Navegando a la vista de ganancias por moneda")
        # Actualiza la vista con los datos de ganancias
        lista_ganancias = self.model.monedas_dao.calcular_ganancias_por_moneda()
        self.view.frames["listGanancias"].listar_datos(lista_ganancias)
        self.view.switch("listGanancias")

    def listsTransacciones(self):
        print("controlador/home_menu.py -> pide recuperar datos")
        self.model.gestor_transacciones.recuperar_datos()

    def registerTasaConversion(self):
        print("controlador/home_menu.py -> pide abrir ventana para ingreso de tasa de conversión")
        self.view.switch("registerTasaConversion")

    def registerDisponibilidadCajas(self):
        print("controlador/home_menu.py -> pide abrir ventana para registrar disponibilidad de cajas")
        self.view.switch("registerDisponibilidad")

    def registerDisponibilidadMoneda(self):
        print("controlador/home_menu.py -> pide abrir ventana para registrar compra de moneda extranjera")
        self.view.switch("registerCantidad")

    def logout(self):
        self.model.gestor_usuarios.logout()

    def update_view(self):
        """
        Actualiza el saludo en el menú principal.
        """
        current_user = self.model.gestor_usuarios.saludo_usuario()
        username = current_user["username"] if current_user else "Usuario"
        self.frame.greeting.config(text=f"Bienvenido, {username}!")
