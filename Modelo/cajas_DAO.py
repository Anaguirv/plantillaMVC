from .conectorBD import ConectorBD

class Cajas_DAO:
    
    def __init__(self):
        
        # Configura la conexión a la base de datos
        self.conector = ConectorBD(
            hostdb='localhost',
            userdb='root',       
            passwordb='',       
            basedatosdb='acme'
        )
    
    
    def leer_datos(self):
        sql = "SELECT * FROM caja"
        result, error = self.conector.ejecutarSelectAll(sql)
        if error:
            print(f"Error al leer datos: {error}")
            return None
        else:
            print("Datos leídos exitosamente.")
            return result
