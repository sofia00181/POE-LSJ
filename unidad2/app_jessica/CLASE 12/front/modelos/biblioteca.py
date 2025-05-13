import tkinter as tk

class Biblioteca:
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = tk.StringVar(ventanaPrincipal)
        self.titulo = tk.StringVar(ventanaPrincipal)
        self.categoria = tk.StringVar(ventanaPrincipal)
        self.autor = tk.StringVar(ventanaPrincipal)
        self.año = tk.StringVar(ventanaPrincipal)
