class SignInController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["signin"]
        self._bind()

    def _bind(self):
        self.frame.signin_btn.config(command=self.signin)
        self.frame.signup_btn.config(command=self.signup)
        self.frame.close_btn.config(command=self.close)

    def signin(self):
        data = self.frame.data_signin()  # Obtén datos de inicio de sesión (usuario y contraseña)
        usuario = self.model.gestor_usuarios.login(data)  # Valida las credenciales con el modelo
        
        if usuario:  # Si el usuario existe
            if usuario['rol'] == 'gerente':
                print(f"Acceso concedido: Gerente ({usuario['username']})")
                
                # Cambia a la vista del menú del gerente, pasando los datos del usuario
                self.view.frames["menu_gerente"].update_user_data(usuario)
                self.view.switch("menu_gerente")
            elif usuario['rol'] == 'usuario':
                print(f"Acceso concedido: Usuario estándar ({usuario['username']})")
                self.view.switch("home")  # Cambia a la vista estándar
            else:
                self.frame.show_error("Rol desconocido. Contacta al administrador.")
        else:
            self.frame.show_error("Credenciales incorrectas. Inténtalo de nuevo.")

    def signup(self):
        self.view.switch("signup")
           
    def close(self):
        self.view.stop_mainloop()
