import tkinter as tk
import re

root = tk.Tk()
root.title("Computador")
root.geometry("500x900")


def validar_letras(valor):
    patron = re.compile("^[A-Za-zñÑ ]*$")
    return patron.match(valor) is not None


def evento_presionar_tecla(event):
    entrada = event.widget  
    texto = entrada.get()  

    etiqueta_error = entrada.etiqueta_error  

    if validar_letras(texto):
        etiqueta_error.config(text="")
    else:
        etiqueta_error.config(text="Solo se permiten letras", fg="red")


def computador(nombre):
    etiqueta = tk.Label(root, text=nombre, font=("Arial", 16))
    etiqueta.pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 14))
    entry.pack(pady=5)

    etiqueta_error = tk.Label(root, text="", fg="red")
    etiqueta_error.pack()

    entry.etiqueta_error = etiqueta_error 

    entry.bind("<KeyRelease>", evento_presionar_tecla)


computador("Teclado")
computador("Mouse")
computador("Pantalla")
computador("Software")


def salir():
    root.quit()

boton_salir = tk.Button(root, text="Salir", font=("Arial", 14), command=salir)
boton_salir.pack(pady=20)

root.mainloop()
