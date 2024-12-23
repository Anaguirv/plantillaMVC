from tkinter import Frame, Button, Label

class MenuGerenteView(Frame):
    def __init__(self, master, controller=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.user_data = None
        self.setup_ui()
    
    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        
        self.label_bienvenida = Label(self, text="", font=('Arial', 16, 'bold'))
        self.label_bienvenida.grid(row=0, column=0, pady=20, padx=20, sticky="ew")
        
        Button(self, text="Gestionar Usuarios", 
               command=self.gestionar_usuarios).grid(
            row=1, column=0, pady=10, padx=20, sticky="ew"
        )
        Button(self, text="Gestionar Cajas", 
               command=self.gestionar_cajas).grid(
            row=2, column=0, pady=10, padx=20, sticky="ew"
        )
        Button(self, text="Ver Estadísticas", 
               command=self.ver_estadisticas).grid(
            row=3, column=0, pady=10, padx=20, sticky="ew"
        )
        Button(self, text="Cerrar Sesión", 
               command=self.cerrar_sesion).grid(
            row=4, column=0, pady=20, padx=20, sticky="ew"
        )
    
    def update_user_data(self, user_data):
        """
        Actualiza los datos del usuario autenticado y actualiza la interfaz.
        """
        self.user_data = user_data
        self.label_bienvenida.config(text=f"Bienvenido, {self.user_data['username']}")

    def gestionar_usuarios(self):
        print("Gestionar Usurios: Aquí se implementará la funcionalidad.")

    def gestionar_cajas(self):
        print("Gestionar Cajas: Aquí se implementará la funcionalidad.")

    def ver_estadisticas(self):
        print("Ver Estadísticas: Aquí se implementará la funcionalidad.")
    
    def cerrar_sesion(self):
        if self.controller:
            print("Cerrando sesión...")
            # Llama al método logout del modelo
            self.controller.model.gestor_usuarios.logout()
            # Redirige a la vista de inicio de sesión
            self.controller.show_login_view()  # Asegúrate de implementar este método en tu controlador
