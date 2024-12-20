from .conectorBD import ConectorBD

class Transacciones_DAO:
    
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

        # Consulta para obtener todos los registros de transacciones
        sql = "SELECT id, cantidad, monto_total, moneda_id FROM transaccion"
        estado, datos = self.conector.ejecutarSelectAll(sql)

        # Inicializar el diccionario de datos
        listaTransacciones_DTO = {}

        if estado == 0:
            for i in range(len(datos)):
                registro = {
                    "id": datos[i][0], 
                    "cantidad": datos[i][1], 
                    "monto_total": datos[i][2], 
                    "moneda_id": datos[i][3]
                }
                listaTransacciones_DTO[i] = registro

        # Desactivar la conexión
        print("----------------------------------------------------------------------")
        print(estado)
        print(listaTransacciones_DTO)
        print("----------------------------------------------------------------------")
        self.conector.desactivarConexion()

        print("Datos leídos exitosamente.")
        return listaTransacciones_DTO