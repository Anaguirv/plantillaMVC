# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:39:06 2024

@author: Carlos Luco Montofré
"""

from tkinter import Frame, Label, Button, Listbox, END

class ListViewPesosDisponibles(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Lista de cajas")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.listaDatos = Listbox(self, width=100)
        self.listaDatos.grid(row=1, column=0, padx=(30, 30), sticky="e")
        
        self.return_btn = Button(self, text="Retornar menu")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")
 
        
    def listar_datos(self, lista_DTO): 
        self.listaDatos.delete(0, END)
        # Encabezados de la tabla
        encabezado = f"{'ID':>5} {'Nombre':>15} {'Pesos disponibles':>25} {'Estado':>20}"
        self.listaDatos.insert(0, encabezado)
        self.listaDatos.insert(1, "-" * 65)
        
        for i in range(0, len(lista_DTO)):
            dato = lista_DTO[i]
            # Formatear los datos para que se muestren en columnas alineadas
            estado = 'Activa' if dato['estado'] == 1 else 'No Activa'
            formatted_dato = f"{dato['id']:>5} {dato['nombre']:>15} {'$' + str(dato['disponibilidad_pesos']):>20} {estado:>38}"
            self.listaDatos.insert(i + 2, formatted_dato)


