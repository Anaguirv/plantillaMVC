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
from .list_ganancias import ListControllerGanancias
from .list_pesos_disponibles import ListControllerPesosDisponibles

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Inicializar controladores específicos
        self.signin_controller = SignInController(model, view)
        self.signup_controller = SignUpController(model, view)
        self.home_controller = HomeController(model, view)
        self.register_controller = RegisterController(model, view)
        self.list_controller = ListController(model, view)
        self.list_controller_cajas = ListControllerCajas(model, view)
        self.list_controller_transacciones = ListControllerTransacciones(model, view)
        self.register_controller_tasa_conversion = RegisterControllerTasaConversion(model, view)
        self.register_controller_disponibilidad_cajas = RegisterControllerDisponibilidad(model, view)
        self.register_controller_cantidad = RegisterControllerCantidad(model, view)
        self.list_controller_ganancias = ListControllerGanancias(model, view)
        self.list_controller_pesos_disponibles = ListControllerPesosDisponibles(model, view)

        

        # Configurar los event listeners
        self.setup_event_listeners()

        # Configurar el menú del gerente
        self.setup_menu_gerente()

    def setup_event_listeners(self):
        """Configura todos los event listeners para manejar eventos del modelo."""
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
        self.model.gestor_pesos_disponibles.add_event_listener(
            "lista_pesosDisponibles", self.pesosDisponibles_list_listener
        )
        self.model.gestor_transacciones.add_event_listener(
            "lista_transacciones", self.transacciones_list_listener
        )
        self.model.gestor_tasa_conversion.add_event_listener(
            "registro_tasa_conversion", self.tasa_conversion_register_listener
        )
        self.model.gestor_monedas.add_event_listener(
            "lista_ganancias", self.ganancias_list_listener
        )

    def setup_menu_gerente(self):
        """Configura la vista del menú gerente."""
        menu_gerente = self.view.frames.get("menu_gerente")
        if menu_gerente:
            print("Configurando el controlador para el menú del gerente.")
            menu_gerente.controller = self
        else:
            print("Error: La vista 'menu_gerente' no está configurada.")

    # Métodos para manejar eventos
    def autentificacion_signin_listener(self, data):
        """Maneja el evento de inicio de sesión exitoso."""
        print("Autenticación exitosa. Cambiando a la vista 'home'.")
        self.home_controller.update_view()
        self.view.switch("home")

    def autentificacion_signout_listener(self, data):
        """Maneja el evento de cierre de sesión."""
        print("Cerrando sesión. Cambiando a la vista 'signin'.")
        self.view.switch("signin")

    def datos_register_listener(self, data):
        """Maneja el evento de registro de datos."""
        print("Evento de registro de datos recibido. Cambiando a la vista 'register'.")
        self.view.switch("register")

    def datos_list_listener(self, data):
        """Maneja el evento de listar datos."""
        print("Evento de listado de datos recibido.")
        self.list_controller.update_view()
        self.view.switch("list")

    def cajas_list_listener(self, data):
        """Maneja el evento de listar cajas."""
        print("Evento 'lista_cajas' recibido.")
        lista_DTO = self.model.gestor_cajas.desplegar_datos()
        self.list_controller_cajas.update_view(lista_DTO)
        self.view.switch("listCajas")

    def pesosDisponibles_list_listener(self, data):
        """Maneja el evento de listar Pesos."""
        print("Evento 'lista_pesosDisponibles' recibido.")
        lista_DTO = self.model.gestor_pesos_disponibles.desplegar_datos()
        self.list_controller_pesos_disponibles.update_view(lista_DTO)
        self.view.switch("listPesosDisponibles")

    def tasa_conversion_register_listener(self, data):
        """Maneja el evento de registro de tasa de conversión."""
        print("Evento 'registro_tasa_conversion' recibido. Cambiando a la vista correspondiente.")
        self.view.switch("registerTasaConversion")

    def transacciones_list_listener(self, data):
        """Maneja el evento de listar transacciones."""
        print("Evento 'list_transacciones' recibido.")
        lista_DTO = self.model.gestor_transacciones.desplegar_datos()
        self.list_controller_transacciones.update_view(lista_DTO)
        self.view.switch("listTransacciones")

    def ganancias_list_listener(self, data):
        """Maneja el evento de listar ganancias."""
        print("Evento 'lista_ganancias' recibido.")
        self.list_controller_ganancias.update_view()
        self.view.switch("listGanancias")

    def start(self):
        """Inicia la aplicación mostrando la vista de inicio de sesión."""
        print("Iniciando aplicación. Mostrando la vista de inicio de sesión.")
        self.view.switch("signin")
        self.view.start_mainloop()
