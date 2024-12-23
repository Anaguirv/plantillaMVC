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
        """
        Obtiene todos los registros de monedas desde la base de datos.
        """
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

        self.conector.desactivarConexion()

        return listaMonedas_DTO

    def calcular_ganancias_por_moneda(self):
        """
        Consulta las ganancias totales en pesos por cada moneda.
        """
        self.conector.activarConexion()

        # Consulta SQL para calcular ganancias por moneda
        sql = """
            SELECT m.nombre, SUM(t.ganancia) AS ganancias
            FROM transaccion t
            JOIN moneda m ON t.moneda_id = m.id
            GROUP BY m.nombre
        """
        estado, datos = self.conector.ejecutarSelectAll(sql)

        listaGanancias_DTO = []

        if estado == 0:
            for fila in datos:
                registro = {
                    "nombre": fila[0],
                    "ganancias": fila[1]
                }
                listaGanancias_DTO.append(registro)

        self.conector.desactivarConexion()

        return listaGanancias_DTO
