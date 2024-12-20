from Modelo.monedas_DAO import MonedasDAO

class ProfitController:
    def __init__(self, db_path):
        self.monedas_dao = MonedasDAO(db_path)

    def obtener_ganancias(self):
        """
        Obtiene las ganancias por moneda en pesos y las retorna para la vista.
        """
        ganancias = self.monedas_dao.obtener_ganancias_por_moneda()
        return ganancias

# Ejemplo de uso del controlador
if __name__ == "__main__":
    controlador = ProfitController("acme.db")
    ganancias = controlador.obtener_ganancias()
    for moneda, ganancia in ganancias:
        print(f"Moneda: {moneda}, Ganancia en pesos: {ganancia}")
