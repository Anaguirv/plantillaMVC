# -*- coding: utf-8 -*-
"""
Controlador para listar ganancias por moneda (HU2).
"""

class ListControllerGanancias:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        if "listGanancias" in self.view.frames:
            self.view.frames["listGanancias"].return_btn.config(command=self.volver_menu)
        else:
            print("Error: El frame 'listGanancias' no está registrado en la vista.")

    def update_view(self):
        print("ListControllerGanancias -> Cargando datos de ganancias...")
        try:
            lista_ganancias = self.model.monedas_dao.calcular_ganancias_por_moneda()
            if "listGanancias" in self.view.frames:
                self.view.frames["listGanancias"].listar_datos(lista_ganancias)
                print("ListControllerGanancias -> Vista actualizada con éxito.")
            else:
                print("Error: El frame 'listGanancias' no está registrado en la vista.")
        except Exception as e:
            print(f"ListControllerGanancias -> Error al actualizar la vista: {e}")

    def volver_menu(self):
        self.view.switch("home")
