import requests

class Comunicacion:
    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/api/biblioteca/'
        self.ventanaPrincipal = ventanaPrincipal

    def guardar(self, titulo, categoria, autor, año):
        try:
            data = {
                'titulo': titulo,
                'categoria': categoria,
                'autor': autor,
                'año': int(año)
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json())
            return resultado
        except Exception as e:
            print(f"Error al guardar: {e}")

    def actualizar(self, id, titulo, categoria, autor, año):
        try:
            data = {
                'titulo': titulo,
                'categoria': categoria,
                'autor': autor,
                'año': int(año)
            }
            resultado = requests.put(f"{self.url}/{id}/", json=data)
            print(resultado.json())
            return resultado
        except Exception as e:
            print(f"Error al actualizar: {e}")

    def consultar(self, id):
        try:
            resultado = requests.get(f"{self.url}/{id}")
            return resultado.json()
        except Exception as e:
            print(f"Error al consultar: {e}")
            return {}

    def consultar_todo(self, titulo='', categoria='', autor='', año=''):
        try:
            params = {}
            if titulo:
                params['titulo'] = titulo
            if categoria:
                params['categoria'] = categoria
            if autor:
                params['autor'] = autor
            if año:
                params['año'] = año
            resultado = requests.get(self.url, params=params)
            return resultado.json()
        except Exception as e:
            print(f"Error al consultar todos: {e}")
            return []

    def eliminar(self, id):
        try:
            resultado = requests.delete(f"{self.url}/{id}")
            return resultado.status_code
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return None

