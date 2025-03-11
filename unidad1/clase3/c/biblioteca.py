import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title("biblioteca")
root.geometry("700x800")

etiqueta = tk.Label(root, text= "libro", font=("arial",16))
etiqueta.pack(pady=10)

entrada = tk.Entry(root, font=("Arial",14))
entrada.pack(pady=10)

etiqueta = tk.Label(root, text= "revistas", font=("arial",16))
etiqueta.pack(pady=20)

entrada = tk.Entry(root, font=("Arial",14))
entrada.pack(pady=20)

etiqueta = tk.Label(root, text= "diccionaros", font=("arial",16))
etiqueta.pack(pady=30)

entrada = tk.Entry(root, font=("Arial",14))
entrada.pack(pady=30)

etiqueta = tk.Label(root, text= "periodicos", font=("arial",16))
etiqueta.pack(pady=40)

entrada = tk.Entry(root, font=("Arial",14))
entrada.pack(pady=40)


def salir():
    root.quit()

boton_salir = tk.Button(root, text="salir", font=("Arial",14), command=salir)  
boton_salir.pack(pady=20)

root.mainloop()