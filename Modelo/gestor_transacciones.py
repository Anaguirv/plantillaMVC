from .event_handler import ObservableModel 
from .transacciones_DAO import Transacciones_DAO
from .monedas_DAO import Moneda_DAO

class Gestor_Transacciones(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.transacciones_DAO = Transacciones_DAO()
        self.moneda_DAO = Moneda_DAO()

    def recuperar_datos(self):
        print("Recuperando datos...")
        self.trigger_event("lista_transacciones")

    def desplegar_datos(self):
        lista_transacciones = self.transacciones_DAO.leer_datos()
        lista_monedas = self.moneda_DAO.leer_datos()
        
        for i in lista_transacciones:
            moneda_id = lista_transacciones[i]['moneda_id']
            nombre_moneda = next((moneda['nombre'] for moneda in lista_monedas.values() if moneda['id'] == moneda_id), "Desconocido")
            lista_transacciones[i]['moneda_nombre'] = nombre_moneda

        # Ordenar de mayor a menor por la cantidad
        lista_transacciones_ordenada = dict(sorted(lista_transacciones.items(), key=lambda x: x[1]['cantidad'], reverse=True))

        print("____________________________________________________________________")
        print("Modulo Modelo/gestor_transacciones")
        print(lista_transacciones_ordenada)
        print("____________________________________________________________________")      
        return lista_transacciones_ordenada

    def retornar(self):
        self.trigger_event("home")
