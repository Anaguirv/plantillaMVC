from .home_menu import HomeController
from .list_datos import ListController
from .list_caja import ListControllerCajas
from .list_transacciones import ListControllerTransacciones
from .signin_usuario import SignInController
from .signup_usuario import SignUpController
from .register_datos import RegisterController
from .register_tasa_conversion import RegisterControllerTasaConversion
from .register_disponibilidad_cajas import RegisterControllerDisponibilidad
from .register_disponibilidad_moneda import RegisterControllerCantidad
from .list_ganancias import ListControllerGanancias  # Nuevo controlador de ganancias

class Controller:
    
    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.signin_controller     = SignInController(model, view)
        self.signup_controller     = SignUpController(model, view)
        self.home_controller       = HomeController(model, view)
        self.register_controller   = RegisterController(model, view)
        self.list_controller       = ListController(model, view)
        self.list_controller_cajas = ListControllerCajas(model, view)
        self.list_controller_transacciones = ListControllerTransacciones(model, view)
        self.register_controller_tasa_conversion = RegisterControllerTasaConversion(model, view)
        self.register_controller_disponibilidad_cajas = RegisterControllerDisponibilidad(model, view)
        self.register_controller_cantidad = RegisterControllerCantidad(model, view)
        self.list_controller_ganancias = ListControllerGanancias(model, view)  # Controlador de ganancias

        # Asignar eventos a los métodos
        self.model.gestor_usuarios.add_event_listener(
            "ingreso_sistema", self.autentificacion_signin_listener
        )
        self.model.gestor_usuarios.add_event_listener(
            "salida_sistema", self.autentificacion_signout_listener
        )
        self.model.gestor_datos.add_event_listener(
            "registro_datos", self.datos_register_listener
        )
        self.model.gestor_datos.add_event_listener(
            "lista_datos", self.datos_list_listener
        )
        self.model.gestor_cajas.add_event_listener(
            "lista_cajas", self.cajas_list_listener
        )
        self.model.gestor_transacciones.add_event_listener(
            "lista_transacciones", self.transacciones_list_listener
        )
        self.model.gestor_tasa_conversion.add_event_listener(
            "registro_tasa_conversion", self.tasa_conversion_register_listener
        )
        self.model.gestor_monedas.add_event_listener(
            "lista_ganancias", self.ganancias_list_listener  # Evento para ganancias por moneda
        )

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

    def cajas_list_listener(self, data):
        print("Evento list_cajas recibido")
        lista_DTO = self.model.gestor_cajas.desplegar_datos()
        self.list_controller_cajas.update_view(lista_DTO)
        self.view.switch("listCajas")

    def tasa_conversion_register_listener(self, data):
        print("Controlador/main.py -> pide registrar tasa de cambio")
        self.view.switch("registerTasaConversion")

    def transacciones_list_listener(self, data):
        print("Evento list_transacciones recibido")
        lista_DTO = self.model.gestor_transacciones.desplegar_datos()
        self.list_controller_transacciones.update_view(lista_DTO)
        self.view.switch("listTransacciones")

    def ganancias_list_listener(self, data):
        print("Evento lista_ganancias recibido")
        self.list_controller_ganancias.update_view()
        self.view.switch("listGanancias")

    def start(self):
        self.view.switch("signin")
        self.view.start_mainloop()
