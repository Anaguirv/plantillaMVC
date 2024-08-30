# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 19:30:43 2024

@author: Carlos Luco Montofré
"""

from tkinter import Frame, Label, Button, Entry

class RegisterView(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Registro de datos")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.dato_label = Label(self, text="Datos")
        self.dato_input = Entry(self)
        self.dato_label.grid(row=1, column=0, padx=10, sticky="w")
        self.dato_input.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        self.greeting = Label(self, text="")
        self.greeting.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.register_btn = Button(self, text="Registro de datos")
        self.register_btn.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        
        self.return_btn = Button(self, text="Retornar menu")
        self.return_btn.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        
        
    def data_register(self):
        dato = self.dato_input.get()
        data_dto = {"dato": dato}
        self.dato_input.delete(0, last=len(dato))
        return data_dto