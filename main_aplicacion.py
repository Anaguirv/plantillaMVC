from Modelo.main import Model
from Vista.main import View
from Controlador.main import Controller

def main():
    model = Model()
    view = View(controller=None)  # Cambiará una vez instanciado el controlador
    controller = Controller(model, view)
    view.controller = controller  # Establecer el controlador después de inicializarlo
    controller.start()

if __name__ == "__main__":
    main()
