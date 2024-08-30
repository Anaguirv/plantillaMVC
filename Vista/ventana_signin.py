# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:01:25 2024

@author: Carlos Luco Montofré
"""

from tkinter import Frame, Label, Entry, Button


class SignInView(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Ingreso a una cuenta existente")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.username_label = Label(self, text="Username")
        self.username_input = Entry(self)
        self.username_label.grid(row=1, column=0, padx=10, sticky="w")
        self.username_input.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_input = Entry(self, show="*")
        self.password_label.grid(row=2, column=0, padx=10, sticky="w")
        self.password_input.grid(row=2, column=1, padx=(0, 20), sticky="ew")

        self.signin_btn = Button(self, text="Iniciar sesión")
        self.signin_btn.grid(row=3, column=1, padx=0, pady=10, sticky="w")

        self.signup_option_label = Label(self, text="No tiene cuenta?")
        self.signup_btn = Button(self, text="Crear cuenta")
        self.signup_option_label.grid(row=4, column=1, sticky="w")
        self.signup_btn.grid(row=5, column=1, sticky="w")
             
        self.close_btn = Button(self, text="Cerrar sistema")
        self.close_btn.grid(row=7, column=1, padx=0, pady=10, sticky="w")
        
        
    def data_signin(self):
        username = self.username_input.get()
        pasword  = self.password_input.get()
        data_dto = {"username": username, "password": pasword}
        self.password_input.delete(0, last=len(pasword))
        return data_dto
                    