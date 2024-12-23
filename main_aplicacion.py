from Modelo.main import Model
from Vista.main import View
from Controlador.main import Controller

def main():
    model = Model()
    view = View(controller=None)  # Inicialmente None
    controller = Controller(model, view)
    view.controller = controller  # Establecer el controlador
    controller.setup_menu_gerente()  # Configurar el menú gerente
    controller.start()

if __name__ == "__main__":
    main()