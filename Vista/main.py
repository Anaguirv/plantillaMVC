# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:51:41 2024

@author: Carlos Luco Montofré
"""

from .root import Root
from .ventana_list import ListView
from .ventana_home import HomeView
from .ventana_signin import SignInView
from .ventana_signup import SignUpView
from .ventana_register import RegisterView

class View:
    
    def __init__(self):
        self.root = Root()
        self.frames = {}

        self._add_frame(SignUpView, "signup")
        self._add_frame(SignInView, "signin")
        self._add_frame(HomeView, "home")
        self._add_frame(RegisterView, "register")
        self._add_frame(ListView, "list")

    def _add_frame(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()
        
    def stop_mainloop(self):
         self.root.destroy()