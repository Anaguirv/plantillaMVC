# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:01:42 2024

@author: Carlos Luco Montofré
"""

from tkinter import Frame, Label, Entry, Checkbutton, Button, BooleanVar

class SignUpView(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Creación de una nueva cuenta")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.fullname_label = Label(self, text="Full Name")
        self.fullname_input = Entry(self)
        self.fullname_label.grid(row=1, column=0, padx=10, sticky="w")
        self.fullname_input.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        self.username_label = Label(self, text="Username")
        self.username_input = Entry(self)
        self.username_label.grid(row=2, column=0, padx=10, sticky="w")
        self.username_input.grid(row=2, column=1, padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_input = Entry(self, show="*")
        self.password_label.grid(row=3, column=0, padx=10, sticky="w")
        self.password_input.grid(row=3, column=1, padx=(0, 20), sticky="ew")

        self.has_agreed = BooleanVar()
        self.agreement = Checkbutton(
            self,
            text="Yo estoy de acuerdo con los Términos & Condiciones",
            variable=self.has_agreed,
            onvalue=True,
            offvalue=False,
        )
        self.agreement.grid(row=4, column=1, padx=0, sticky="w")

        self.signup_btn = Button(self, text="Crear cuenta")
        self.signup_btn.grid(row=5, column=1, padx=0, pady=10, sticky="w")

        self.signin_option_label = Label(self, text="Tiene ya una cuenta?")
        self.signin_btn = Button(self, text="Ir a inicio sesión")
        self.signin_option_label.grid(row=6, column=1, sticky="w")
        self.signin_btn.grid(row=7, column=1, sticky="w")
        
            
    def data_signup(self):
        fullname   = self.fullname_input.get()
        username   = self.username_input.get()
        pasword    = self.password_input.get()
        has_agreed = self.has_agreed.get()
        data_dto = {"fullname": fullname, "username": username, "password": pasword, "has_agreed": has_agreed}
        self.password_input.delete(0, last=len(pasword))
        return data_dto        