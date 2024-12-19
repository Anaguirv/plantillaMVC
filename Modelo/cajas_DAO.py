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
        self.conector.activarConexion()
        sql = "SELECT * FROM caja"
        estado, datos = self.conector.ejecutarSelectAll(sql)

        listaCajas_DTO = {}

        if estado == 0:

            for i in range(0, len(datos)):
                registro = {"id": datos[i][0], "nombre": datos[i][1], "estado": datos[i][2], "disponibilidad_pesos": datos[i][3]}
                listaCajas_DTO[i]= registro

        print("----------------------------------------------------------------------")
        print(estado)
        print(listaCajas_DTO)
        print("----------------------------------------------------------------------")
        self.conector.desactivarConexion()

        print("Datos leídos exitosamente.")
        return listaCajas_DTO
