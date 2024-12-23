from .conectorBD import ConectorBD

class PesosDisponibles_DAO:
    
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
    
    def editar_datos(self, id_caja, nuevo_monto):
        """
        Inserta o actualiza el monto disponible de una caja.

        :param id_caja: ID de la caja.
        :param nuevo_monto: Monto disponible.
        :return: True si la operación fue exitosa, False en caso contrario.
        """
        self.conector.activarConexion()
        sql = f"UPDATE caja SET disponibilidad_pesos = {nuevo_monto} WHERE id = {id_caja}"

        # Cambiar a recibir un solo valor
        estado = self.conector.ejecutarUpdate(sql)
        self.conector.desactivarConexion()

        if estado == 0:
            print(f"Datos de la caja con ID {id_caja} actualizados correctamente.")
            return True
        else:
            print(f"Error al actualizar los datos de la caja con ID {id_caja}.")
            return False



    


    
