from PIL import Image
import subprocess

# Función para ejecutar un comando ADB y capturar la pantalla
def capturarPantalla():
    # Capturar la pantalla y guardarla en el dispositivo
    subprocess.run(['adb', 'exec-out', 'screencap', '-p', '/sdcard/screenshot.png'])
    # Transferir la captura de pantalla a la computadora
    subprocess.run(['adb', 'pull', '/sdcard/screenshot.png', 'screenshot.png'])
    
# Función para recortar el área del tablero en la captura de pantalla
def recortarTablero(imagen, coordenadas):
    x, y, ancho, alto = coordenadas
    area_tablero = imagen.crop((x, y, x + ancho, y + alto))
    return area_tablero

# Función principal
def tableroFlood():
    # Capturar la pantalla
    capturarPantalla()

    # Cargar la imagen completa
    imagen_completa = Image.open('screenshot.png')
    
    # Definir las coordenadas y dimensiones del área del tablero
    coordenadas_tablero = (88, 898, 1264, 1264)  
    
    # Recortar el área del tablero
    area_tablero = recortarTablero(imagen_completa, coordenadas_tablero)
    
    # Guardar la imagen recortada si es necesario
    area_tablero.save('tablero_recortado.png')
    