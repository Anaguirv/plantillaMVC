from .event_handler import ObservableModel
from .transacciones_DAO import Transacciones_DAO

class Gestor_Transacciones(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.transacciones_DAO = Transacciones_DAO()

    def recuperar_datos(self):
        print("Recuperando datos...")
        self.trigger_event("lista_transacciones")

    def desplegar_datos(self):
        lista_DTO = self.transacciones_DAO.leer_datos()  
        print("____________________________________________________________________")
        print("Modulo Modelo/gestor_transacciones")
        print(lista_DTO)
        print("____________________________________________________________________")      
        return lista_DTO

    def retornar(self):
        self.trigger_event("home")
