# Flood Fill Game Automation

Este proyecto automatiza el juego de Flood Fill utilizando captura de pantalla, procesamiento de imágenes y clics automáticos.

## Requisitos

Asegúrate de tener instaladas las siguientes librerías de Python:

- `opencv-python`
- `numpy`
- `pyautogui`


Puedes instalarlas usando `pip`:

```bash
pip install opencv-python numpy pyautogui

Configuración
Coordenadas para Clics
Para ajustar las coordenadas de los clics en tu teléfono, edita el archivo config.json en el directorio del proyecto. Este archivo contiene las coordenadas de los colores y la opción para reiniciar el juego. Esto lo puedes hacer con el archivo pyautoguiClick.py que te da las coordenadas para hacer click.

Ejemplo de config.json:

{
    "coloresUbicacion": {
        "V": [1400, 935],
        "M": [1620, 935],
        "R": [1250, 935],
        "Y": [1475, 935],
        "A": [1320, 935],
        "N": [1545, 935]
    }
}

Reemplaza los valores [x, y] con las coordenadas correctas para tu dispositivo.

Definición de Colores
Abre el archivo matrizColores.py y modifica la función es_color para que coincida con los colores de tu juego. Aquí hay un ejemplo de la función:

def es_color(color):
    r, g, b = color
    if r > 200 and g < 100 and b < 100:
        return "R"  # Rojo
    elif r > 100 and g < 100 and b > 100:
        return "M"  # Magenta
    elif b > r + 70 y b > g + 70:
        return "A"  # Azul
    elif g > r y g > b:
        return "V"  # Verde
    elif 150 < r <= 255 y 150 < g <= 255 y b < 100:
        return "Y"  # Amarillo
    elif r > 200 y 100 <= g <= 200 y b < 100 y r - g > 50:
        return "N"  # Naranja
    else:
        return "O"  # Otro

Uso
Para ejecutar el proyecto, corre el archivo main.py:

python main.py
El proyecto capturará la pantalla, procesará el tablero del juego y realizará los clics automáticos basados en los colores detectados y su secuencia óptima.

Nota Importante
El proyecto está diseñado para tableros de 12x12. Si tu tablero tiene un tamaño diferente, asegúrate de ajustar el tamaño en el código ademas de agregar los demas colores que se agreguen en caso de cambiar esta opcion.

Opciones Adicionales
Si el número de pasos necesarios para resolver el tablero supera los 21, se te ofrecerán opciones para continuar, reiniciar o salir del juego.

