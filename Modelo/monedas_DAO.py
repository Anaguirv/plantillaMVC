import sqlite3

class MonedasDAO:
    def __init__(self, db_path):
        self.db_path = db_path

    def obtener_ganancias_por_moneda(self):
        """
        Consulta las ganancias por moneda en pesos.
        """
        try:
            conexion = sqlite3.connect(self.db_path)
            cursor = conexion.cursor()

            consulta = """
                SELECT moneda, SUM(ganancia * tasa_conversion) AS ganancias_pesos
                FROM transacciones
                GROUP BY moneda
            """

            cursor.execute(consulta)
            resultados = cursor.fetchall()

            conexion.close()
            return resultados

        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return []

# Ejemplo de uso
if __name__ == "__main__":
    dao = MonedasDAO("acme.db")
    ganancias = dao.obtener_ganancias_por_moneda()
    for moneda, ganancia in ganancias:
        print(f"Moneda: {moneda}, Ganancia en pesos: {ganancia}")
