import tkinter as tk
import re

def validar_letras(valor):
    patron = re.compile("^[A-Za-zñÑ ]*$")
    return patron.match(valor.get()) is not None

def evento_presionar_tecla(event, variable, label):
    if validar_letras(variable):
        label.config(text="")
    else:
        label.config(text="Solo se permiten letras")

root = tk.Tk()
root.title("Biblioteca")
root.geometry("700x700")

categorias = ["Libro", "Revistas", "Diccionarios", "Periódicos"]
entradas = []
validaciones = []

for categoria in categorias:
    etiqueta = tk.Label(root, text=categoria, font=("Arial", 16))
    etiqueta.pack(pady=10)

    var_texto = tk.StringVar()
    entrada = tk.Entry(root, font=("Arial", 14), textvariable=var_texto)
    entrada.pack(pady=5)

    etiqueta_validacion = tk.Label(root, text="", font=("Arial", 12), fg="red")
    etiqueta_validacion.pack()

    entrada.bind("<KeyRelease>", lambda event, v=var_texto, l=etiqueta_validacion: evento_presionar_tecla(event, v, l))

    entradas.append(entrada)
    validaciones.append(etiqueta_validacion)

def salir():
    root.quit()

boton_salir = tk.Button(root, text="Salir", font=("Arial", 14), command=salir)
boton_salir.pack(pady=20)

root.mainloop()

