import tkinter as tk

root = tk.Tk()
root.title("Computador")
root.geometry("700x700")

etiqueta = tk.Label(root, text="Teclado", font=("Arial", 16))
etiqueta.pack(pady=10)

entrada = tk.Entry(root, font=("Arial", 14))
entrada.pack(pady=10)

etiqueta = tk.Label(root, text="Mouse", font=("Arial", 16))
etiqueta.pack(pady=20)

entrada = tk.Entry(root, font=("Arial", 14))
entrada.pack(pady=20)

etiqueta = tk.Label(root, text="Pantalla", font=("Arial", 16))
etiqueta.pack(pady=30)

entrada = tk.Entry(root, font=("Arial", 14))
entrada.pack(pady=30)

etiqueta = tk.Label(root, text="Software", font=("Arial", 16))
etiqueta.pack(pady=40)

entrada = tk.Entry(root, font=("Arial", 14))
entrada.pack(pady=40)


def salir():
    root.quit()

boton_salir = tk.Button(root, text="Salir", font=("Arial", 14), command=salir)
boton_salir.pack(pady=20)

root.mainloop()

