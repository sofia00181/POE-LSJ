import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.biblioteca import Biblioteca
from .tabla import Tabla

class Interfaz:
    def __init__(self):
        titulos = ['Título', 'Categoría', 'Autor', 'Año']
        columnas = ['id', 'titulo', 'categoria', 'autor', 'año']
        data = []

        self.ventanaPrincipal = tk.Tk()
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.tabla = Tabla(self.ventanaPrincipal, titulos, columnas, data)

    def accion_guardar_boton(self, id, titulo, categoria, autor, año):
        if id == '':
            self.comunicacion.guardar(titulo, categoria, autor, año)
        else:
            self.comunicacion.actualizar(id, titulo, categoria, autor, año)

    def accion_consultar_boton(self, labelConsulta, id):
        resultado = self.comunicacion.consultar(id)
        if resultado:
            labelConsulta.config(text=resultado.get('año', 'No encontrado'))

    def accion_consultar_todo(self, titulo, categoria, autor, año):
        resultado = self.comunicacion.consultar_todo(titulo, categoria, autor, año)
        data = []
        for elemento in resultado:
            data.append((
                elemento.get('id'),
                elemento.get('titulo'),
                elemento.get('categoria'),
                elemento.get('autor'),
                elemento.get('año')
            ))
        self.tabla.refrescar(data)
        print(data)

    def mostrar_interfaz(self):
        usuario = Biblioteca(self.ventanaPrincipal)

        labelId = tk.Label(self.ventanaPrincipal, text="ID")
        entryId = tk.Entry(self.ventanaPrincipal, textvariable=usuario.id)

        labelTitulo = tk.Label(self.ventanaPrincipal, text="Título")
        entryTitulo = tk.Entry(self.ventanaPrincipal, textvariable=usuario.titulo)

        labelCategoria = tk.Label(self.ventanaPrincipal, text="Categoría")
        entryCategoria = tk.Entry(self.ventanaPrincipal, textvariable=usuario.categoria)

        labelAutor = tk.Label(self.ventanaPrincipal, text="Autor")
        entryAutor = tk.Entry(self.ventanaPrincipal, textvariable=usuario.autor)

        labelAño = tk.Label(self.ventanaPrincipal, text="Año")
        entryAño = tk.Entry(self.ventanaPrincipal, textvariable=usuario.año)

        boton_guardar = tk.Button(
            self.ventanaPrincipal,
            text="Guardar",
            command=lambda: self.accion_guardar_boton(
                entryId.get(),
                entryTitulo.get(),
                entryCategoria.get(),
                entryAutor.get(),
                entryAño.get()
            )
        )

        boton_consultar_1 = tk.Button(
            self.ventanaPrincipal,
            text="Consultar por ID",
            command=lambda: self.accion_consultar_boton(labelAño, entryId.get())
        )

        boton_consultar_todos = tk.Button(
            self.ventanaPrincipal,
            text="Consultar todos",
            command=lambda: self.accion_consultar_todo(
                entryTitulo.get(),
                entryCategoria.get(),
                entryAutor.get(),
                entryAño.get()
            )
        )

        # Configuración de la ventana
        self.ventanaPrincipal.title("Gestión de Biblioteca")
        self.ventanaPrincipal.geometry("800x600")

        # Empaquetar widgets
        labelId.pack()
        entryId.pack()
        labelTitulo.pack()
        entryTitulo.pack()
        labelCategoria.pack()
        entryCategoria.pack()
        labelAutor.pack()
        entryAutor.pack()
        labelAño.pack()
        entryAño.pack()
        boton_guardar.pack()
        boton_consultar_1.pack()
        boton_consultar_todos.pack()
        self.tabla.tabla.pack()

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                entryId.delete(0, tk.END)
                entryId.insert(0, str(valores[0]))
                entryTitulo.delete(0, tk.END)
                entryTitulo.insert(0, str(valores[1]))
                entryCategoria.delete(0, tk.END)
                entryCategoria.insert(0, str(valores[2]))
                entryAutor.delete(0, tk.END)
                entryAutor.insert(0, str(valores[3]))
                entryAño.delete(0, tk.END)
                entryAño.insert(0, str(valores[4]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        self.ventanaPrincipal.mainloop()
