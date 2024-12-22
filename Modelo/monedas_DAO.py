from .conectorBD import ConectorBD

class Moneda_DAO:
    
    def __init__(self):
        # Configura la conexión a la base de datos
        self.conector = ConectorBD(
            hostdb='localhost',
            userdb='root',       
            passwordb='',       
            basedatosdb='acme'
        )
    
    def leer_datos(self):
        # Activar la conexión
        self.conector.activarConexion()

        # Consulta para obtener todos los registros de moneda
        sql = "SELECT id, nombre, simbolo FROM moneda"
        estado, datos = self.conector.ejecutarSelectAll(sql)

        # Inicializar el diccionario de datos
        listaMonedas_DTO = {}

        if estado == 0:
            for i in range(len(datos)):
                registro = {
                    "id": datos[i][0], 
                    "nombre": datos[i][1], 
                    "simbolo": datos[i][2]
                }
                listaMonedas_DTO[i] = registro

        # Desactivar la conexión
        print("----------------------------------------------------------------------")
        print(estado)
        print(listaMonedas_DTO)
        print("----------------------------------------------------------------------")
        self.conector.desactivarConexion()

        print("Datos leídos exitosamente.")
        return listaMonedas_DTO

    def editar_cantidad(self, id_moneda, nueva_cantidad):
        """
        Actualiza la cantidad de una moneda específica en la base de datos.

        :param id_moneda: ID de la moneda.
        :param nueva_cantidad: Nueva cantidad disponible.
        :return: True si la operación fue exitosa, False en caso contrario.
        """
        self.conector.activarConexion()
        sql = f"UPDATE moneda SET cantidad = {nueva_cantidad} WHERE id = {id_moneda}"

        estado = self.conector.ejecutarUpdate(sql)
        self.conector.desactivarConexion()

        if estado == 0:
            print(f"Cantidad de la moneda con ID {id_moneda} actualizada a {nueva_cantidad}.")
            return True
        else:
            print(f"Error al actualizar la cantidad de la moneda con ID {id_moneda}.")
            return False
