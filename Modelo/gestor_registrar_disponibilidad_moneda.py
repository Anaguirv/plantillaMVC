from .event_handler import ObservableModel
from .monedas_DAO import Moneda_DAO

class Gestor_Monedas(ObservableModel):

    def __init__(self):
        super().__init__()
        self.moneda_DAO = Moneda_DAO()

    def editar_cantidad(self, datos_DTO):
        """
        Edita la cantidad de una moneda específica.

        :param datos_DTO: Diccionario con 'id_moneda' y 'nueva_cantidad'.
        :return: True si la operación fue exitosa, False en caso contrario.
        """
        id_moneda = datos_DTO.get("id_moneda")
        nueva_cantidad = datos_DTO.get("nueva_cantidad")

        if id_moneda and nueva_cantidad is not None:
            if self.moneda_DAO.editar_cantidad(id_moneda, nueva_cantidad):
                self.trigger_event("cantidad_actualizada")
                return True
        print("Datos incompletos o error en la operación.")
        return False

    def recuperar_datos(self):
        """
        Recupera la lista de monedas disponibles.
        """
        self.trigger_event("lista_datos")

    def desplegar_datos(self):
        """
        Devuelve la lista de datos DTO obtenida del DAO.
        """
        lista_DTO = self.moneda_DAO.leer_datos()
        return lista_DTO

    def retornar(self):
        """
        Retorna al menú principal.
        """
        self.trigger_event("home")
