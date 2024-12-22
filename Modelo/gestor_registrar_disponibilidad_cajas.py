from .event_handler import ObservableModel
from .cajas_DAO import Cajas_DAO

class Gestor_Disponibilidad_Cajas(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.cajas_DAO = Cajas_DAO()

    def registrar_disponibilidad(self, datos_DTO):
        """
        Registra o actualiza la disponibilidad de una caja.

        :param datos_DTO: Diccionario con 'numero_caja' y 'monto_disponible'.
        :return: True si el registro fue exitoso, False en caso contrario.
        """
        id_caja = datos_DTO.get("numero_caja")
        monto_disponible = datos_DTO.get("monto_disponible")

        if id_caja and monto_disponible:
            if self.cajas_DAO.editar_datos(id_caja, monto_disponible):
                self.trigger_event("registro_disponibilidad")
                return True
        print("Datos incompletos o error en el registro.")
        return False


    def recuperar_datos(self):
        """
        Recupera la lista de datos de las cajas.
        """
        self.trigger_event("lista_datos")

    def desplegar_datos(self):
        """
        Devuelve la lista de datos DTO obtenida del DAO.
        """
        lista_DTO = self.cajas_DAO.leer_datos()        
        return lista_DTO

    def retornar(self):
        """
        Retorna al menú principal.
        """
        self.trigger_event("home")