"""Comprobador de Conectividad de Sitios Web
La idea de este proyecto es crear un programa que pruebe la conectividad de sitios web.
Puedes usar los modulos urllib y tkinter para crear una interfaz gráfica de usuario (GUI) que
permita a los usuarios ingresar una dirección web. Después de haber recopilado la dirección
web del usuario, puedes pasarla a una función para devolver un código de estado HTTP para
el sitio web actual mediante la función .getcode() del módulo urllib.
En este ejemplo, simplemente determinamos si el código HTTP es 200. Si lo es, sabemos que
el sitio está funcionando; de lo contrario, informamos al usuario de que no está disponible."""

import tkinter as tk  # Importar el módulo tkinter para crear la interfaz gráfica de usuario
from urllib.request import urlopen  # Importar la función urlopen para abrir una URL
from urllib.error import URLError  # Importar URLError para manejar errores de URL

# Definir una función para comprobar la conectividad del sitio web
def check_website():
    url = entry.get()  # Obtener la dirección web ingresada por el usuario desde el widget de entrada
    try:
        response = urlopen(url)  # Intentar abrir la URL
        if response.getcode() == 200:  # Verificar si el código de estado HTTP es 200 (OK)
            result_label.config(text="El sitio está disponible.")  # Si es 200, mostrar que el sitio está disponible
        else:
            result_label.config(text="El sitio no está disponible.")  # Si no es 200, mostrar que el sitio no está disponible
    except URLError as e:
        result_label.config(text=f"Error: {e.reason}")  # Manejar errores de URL y mostrar el motivo del error

# Crear la ventana principal de la interfaz gráfica de usuario
root = tk.Tk()
root.title("Comprobador de Conectividad de Sitios Web")  # Establecer el título de la ventana

# Crear widgets (componentes de la interfaz gráfica de usuario)
label = tk.Label(root, text="Ingrese la dirección web:")  # Etiqueta para instruir al usuario
label.pack(pady=5)  # Colocar la etiqueta en la ventana y establecer un espacio vertical de 5 píxeles

entry = tk.Entry(root, width=40)  # Campo de entrada para que el usuario ingrese la dirección web
entry.pack(pady=5)  # Colocar el campo de entrada en la ventana y establecer un espacio vertical de 5 píxeles

check_button = tk.Button(root, text="Comprobar", command=check_website)  # Botón para iniciar la comprobación
check_button.pack(pady=5)  # Colocar el botón en la ventana y establecer un espacio vertical de 5 píxeles

result_label = tk.Label(root, text="")  # Etiqueta para mostrar el resultado de la comprobación
result_label.pack(pady=5)  # Colocar la etiqueta en la ventana y establecer un espacio vertical de 5 píxeles

root.mainloop()  # Iniciar el bucle principal de la interfaz gráfica de usuario