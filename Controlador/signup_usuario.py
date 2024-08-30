# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:03:00 2024

@author: Carlos Luco Montofré
"""

class SignUpController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["signup"]
        self._bind()

    def _bind(self):
        self.frame.signup_btn.config(command=self.signup)
        self.frame.signin_btn.config(command=self.signin)

    def signup(self):
        data = self.frame.data_signup()
        self.model.gestor_usuarios.logup(data)

    def signin(self):
        self.view.switch("signin")