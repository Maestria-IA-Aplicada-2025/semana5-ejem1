# from __future__ import print_function # In python 2.7
# Este código es un comentario, la línea anterior es útil para asegurar que la función `print` en Python 2.7 se comporte de manera similar a Python 3.
# En versiones más modernas de Python (3.x), no es necesario, por lo que está comentada.

from flask import Flask  # Importa el objeto Flask desde la librería Flask, que permite crear la aplicación web.

# Crear una instancia de la aplicación Flask
app = Flask(
    __name__)  # Crea una aplicación Flask. '__name__' es el nombre del módulo actual, utilizado por Flask para determinar la ruta del proyecto.


# Definir una ruta en la aplicación Flask
@app.route('/presentacion/datos/personales/<nombre>/<apellido>/<numero>')
# Este decorador define una ruta de la URL que acepta tres parámetros:
# - 'nombre' (primer parámetro),
# - 'apellido' (segundo parámetro),
# - 'numero' (tercer parámetro).
# Los valores de estos parámetros se pasaran a la función `index` cuando se acceda a la URL correspondiente.

def index(nombre, apellido, numero):
    # La función 'index' recibe los tres parámetros de la URL: nombre, apellido, y numero
    c = ""  # Inicializa una cadena vacía para construir la respuesta.

    # Ciclo que se ejecuta 'numero' veces para generar la cadena 'c'
    for i in range(0, int(numero)):
        # Convierte 'numero' a entero y lo usa como límite del bucle (por ejemplo, si numero=3, el bucle se ejecuta 3 veces).

        c = '%s<b>%s %s</b><br/>' % (c, nombre, apellido)
        # En cada iteración, agrega a la cadena 'c' el nombre y apellido en negrita (<b>) seguido de un salto de línea (<br/>).
        # El uso de '%s' es para concatenar dinámicamente las variables 'nombre' y 'apellido' con la cadena 'c'.

    return c  # Devuelve la cadena 'c' como respuesta de la ruta, la cual contiene repeticiones del nombre y apellido en formato HTML.


# Verifica si este archivo se está ejecutando directamente (no como módulo)
if __name__ == '__main__':
    # Este bloque solo se ejecuta cuando el archivo se corre directamente, no cuando es importado como módulo.

    app.run(host="127.0.0.1", port=8080)
    # Ejecuta la aplicación Flask, escuchando en la dirección IP local '127.0.0.1' (localhost) en el puerto 8080.
    # Esto hace que la aplicación esté disponible en el navegador en 'http://127.0.0.1:8080'.
