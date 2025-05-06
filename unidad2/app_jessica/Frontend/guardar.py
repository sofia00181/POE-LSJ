import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://localhost:8000/biblioteca/"

def buscar():
    libro_id = entry_id.get()
    if libro_id:
        response = requests.get(API_URL + libro_id + "/")
        if response.status_code == 200:
            data = response.json()
            entry_titulo.delete(0, tk.END)
            entry_titulo.insert(0, data['titulo'])
            entry_categoria.delete(0, tk.END)
            entry_categoria.insert(0, data['categoria'])
            entry_autor.delete(0, tk.END)
            entry_autor.insert(0, data['autor'])
            entry_anio.delete(0, tk.END)
            entry_anio.insert(0, data['año'])
        else:
            messagebox.showerror("Error", "Libro no encontrado")

def guardar():
    data = {
        "titulo": entry_titulo.get(),
        "categoria": entry_categoria.get(),
        "autor": entry_autor.get(),
        "año": int(entry_anio.get())
    }
    response = requests.post(API_URL, json=data)
    if response.status_code in (200, 201):
        messagebox.showinfo("Éxito", "Libro guardado")
    limpiar_campos()

def actualizar():
    libro_id = entry_id.get()
    if libro_id:
        data = {
            "titulo": entry_titulo.get(),
            "categoria": entry_categoria.get(),
            "autor": entry_autor.get(),
            "año": int(entry_anio.get())
        }
        response = requests.put(API_URL + libro_id + "/", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Éxito", "Libro actualizado")
    limpiar_campos()

def eliminar():
    libro_id = entry_id.get()
    if libro_id:
        response = requests.delete(API_URL + libro_id + "/")
        if response.status_code == 204:
            messagebox.showinfo("Éxito", "Libro eliminado")
    limpiar_campos()

def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_titulo.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_anio.delete(0, tk.END)


root = tk.Tk()
root.title("Gestión de Biblioteca")

tk.Label(root, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)
tk.Button(root, text="Buscar", command=buscar).grid(row=0, column=2)

tk.Label(root, text="Título").grid(row=1, column=0)
entry_titulo = tk.Entry(root)
entry_titulo.grid(row=1, column=1)

tk.Label(root, text="Categoría").grid(row=2, column=0)
entry_categoria = tk.Entry(root)
entry_categoria.grid(row=2, column=1)

tk.Label(root, text="Autor").grid(row=3, column=0)
entry_autor = tk.Entry(root)
entry_autor.grid(row=3, column=1)

tk.Label(root, text="Año").grid(row=4, column=0)
entry_anio = tk.Entry(root)
entry_anio.grid(row=4, column=1)

tk.Button(root, text="Guardar", command=guardar).grid(row=5, column=0)
tk.Button(root, text="Actualizar", command=actualizar).grid(row=5, column=1)
tk.Button(root, text="Eliminar", command=eliminar).grid(row=5, column=2)

root.mainloop()
