import cv2
import numpy as np

def extraerColoresUbicacion(imagen, size):
    alto, ancho, _ = imagen.shape
    alto_casilla = alto // size
    ancho_casilla = ancho // size
    
    coloresUbicacion = []
    
    for fila in range(size):
        for columna in range(size):
            x1 = columna * ancho_casilla
            y1 = fila * alto_casilla
            x2 = (columna + 1) * ancho_casilla
            y2 = (fila + 1) * alto_casilla
            
            casilla = imagen[y1:y2, x1:x2]
            color = tuple(map(int, cv2.mean(casilla)[:3]))
            
            coloresUbicacion.append((color[::-1]))
            
            # Dibujar el contorno de la casilla en la imagen
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
    return coloresUbicacion #, imagen


def esColor(color):
    r, g, b = color
    if r > 200 and g < 100 and b < 100:
        return "R"
    elif r > 100 and g < 100 and b > 100:
        return "M"
    elif b > r + 70 and b > g + 70:
        return "A"
    elif g > r and g > b:
        return "V"
    elif 150 < r <= 255 and 150 < g <= 255 and b < 100:
        return "Y"
    elif r > 200 and 100 <= g <= 200 and b < 100 and r - g > 50:
        return "N"
    else:
        return "O"

def llenarMatrizColores(imagen):
    size=12
    # Redimensionar la imagen a 540x540 píxeles
    imagenRedimensionada = cv2.resize(imagen, (540, 540))

    # Calcular el número de filas y columnas para una división perfecta
    alto, ancho, _ = imagenRedimensionada.shape
    size = alto // (alto // size)

    # Extraer colores, ubicaciones y dibujar los contornos de las casillas
    coloresUbicacion = extraerColoresUbicacion(imagenRedimensionada, size)
    
    # Crear una matriz de 12x12 para almacenar las letras correspondientes a los colores
    matrizClasificada = np.empty((size, size), dtype=str)

    # Llenar la matriz con las letras clasificadas
    index = 0
    for fila in range(12):
        for columna in range(12):
            matrizClasificada[fila, columna] = esColor(coloresUbicacion[index])
            index += 1

    return matrizClasificada #imagen_con_contornos
