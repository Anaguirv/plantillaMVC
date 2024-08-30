# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:02:49 2024

@author: Carlos Luco Montofré
"""

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
        data = self.frame.data_signin()
        self.model.gestor_usuarios.login(data)

    def signup(self):
        self.view.switch("signup")
           
    def close(self):
        self.view.stop_mainloop()
        