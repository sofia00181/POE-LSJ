import tkinter as tk
import re

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Información del Conejo")
ventanaPrincipal.geometry("400x500")

def validar_letras(valor):
    patron = re.compile("^[A-Za-zñÑ ]*$")
    return patron.match(valor.get()) is not None

def validar_numeros(valor):
    patron = re.compile("^[0-9]*$")
    return patron.match(valor.get()) is not None

def evento_presionar_tecla(event, tipo, label):
    if tipo == "letras" and not validar_letras(event.widget):
        label.config(text="Solo se permiten letras", fg="red")
    elif tipo == "numeros" and not validar_numeros(event.widget):
        label.config(text="Solo se permiten números", fg="red")
    else:
        label.config(text="")

# Nombre
labelValidacionNombre = tk.Label(ventanaPrincipal, text="", fg="red")
labelValidacionNombre.pack()
labelNombre = tk.Label(ventanaPrincipal, text="Nombre", font=("Arial", 16))
labelNombre.pack(pady=5)
entryNombre = tk.Entry(ventanaPrincipal, font=("Arial", 14))
entryNombre.pack(pady=5)
entryNombre.bind("<KeyRelease>", lambda e: evento_presionar_tecla(e, "letras", labelValidacionNombre))

# Raza
labelValidacionRaza = tk.Label(ventanaPrincipal, text="", fg="red")
labelValidacionRaza.pack()
labelRaza = tk.Label(ventanaPrincipal, text="Raza", font=("Arial", 16))
labelRaza.pack(pady=10)
entryRaza = tk.Entry(ventanaPrincipal, font=("Arial", 14))
entryRaza.pack(pady=10)
entryRaza.bind("<KeyRelease>", lambda e: evento_presionar_tecla(e, "letras", labelValidacionRaza))

# Color
labelValidacionColor = tk.Label(ventanaPrincipal, text="", fg="red")
labelValidacionColor.pack()
labelColor = tk.Label(ventanaPrincipal, text="Color", font=("Arial", 16))
labelColor.pack(pady=15)
entryColor = tk.Entry(ventanaPrincipal, font=("Arial", 14))
entryColor.pack(pady=15)
entryColor.bind("<KeyRelease>", lambda e: evento_presionar_tecla(e, "letras", labelValidacionColor))

# Edad
labelValidacionEdad = tk.Label(ventanaPrincipal, text="", fg="red")
labelValidacionEdad.pack()
labelEdad = tk.Label(ventanaPrincipal, text="Edad", font=("Arial", 16))
labelEdad.pack(pady=20)
entryEdad = tk.Entry(ventanaPrincipal, font=("Arial", 14))
entryEdad.pack(pady=20)
entryEdad.bind("<KeyRelease>", lambda e: evento_presionar_tecla(e, "numeros", labelValidacionEdad))

def salir():
    ventanaPrincipal.quit()

boton_salir = tk.Button(ventanaPrincipal, text="Salir", font=("Arial", 14), command=salir)
boton_salir.pack(pady=20)

ventanaPrincipal.mainloop()
