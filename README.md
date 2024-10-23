# Comprobador_Conectividad_Sitios_Web
Comprueba si los sitios web están conectados y disponibles
# Comprobador de Conectividad de Sitios Web

Este proyecto es una aplicación gráfica que permite a los usuarios comprobar la disponibilidad de sitios web. Utiliza el módulo `urllib` para verificar el código de estado HTTP de una página web, y si el código es 200, indica que el sitio está disponible. La interfaz gráfica de usuario (GUI) está desarrollada con `Tkinter`.

## Funcionalidades

- **Entrada de URL**: Los usuarios pueden ingresar una dirección web.
- **Comprobación de Conectividad**: La aplicación verifica si el sitio está disponible, comprobando si el código HTTP de respuesta es 200.
- **Manejo de Errores**: Si la URL no es accesible, la aplicación muestra un mensaje con el motivo del error.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado:

- Python 3.x
- Tkinter (incluido con la instalación estándar de Python)

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener `Tkinter` y `urllib` (incluidos en Python) correctamente configurados.
3. Ejecuta el script de la siguiente manera:

```bash
python comprobador_conectividad.py
```

## Uso
1. Al ejecutar el script, aparecerá una ventana gráfica con un campo de entrada.
2. Ingresa una dirección web en el campo (ejemplo: https://www.google.com).
3. Haz clic en el botón Comprobar.
4. La aplicación te mostrará si el sitio está disponible o no.## Uso

## Contribuir
Las contribuciones son bienvenidas. Si tienes sugerencias o mejoras, crea un pull request o abre una issue en el repositorio.
