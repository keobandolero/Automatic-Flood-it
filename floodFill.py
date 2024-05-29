import numpy as np
from collections import deque, defaultdict
import matrizColores as m

# Función para realizar Flood Fill y obtener la región conectada del color inicial
def obtenerRegionConectada(matriz, x, y):
    filas, columnas = matriz.shape
    color_inicial = matriz[x, y]
    visitadas = np.zeros((filas, columnas), dtype=bool)
    region_conectada = []
    
    # Utilizamos una cola para la búsqueda en anchura (BFS)
    cola = deque([(x, y)])
    while cola:
        cx, cy = cola.popleft()
        if not visitadas[cx, cy] and matriz[cx, cy] == color_inicial:
            visitadas[cx, cy] = True
            region_conectada.append((cx, cy))
            # Añadir las celdas adyacentes a la cola
            for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                if 0 <= nx < filas and 0 <= ny < columnas and not visitadas[nx, ny]:
                    cola.append((nx, ny))
                    
    return region_conectada

# Función para obtener los colores adyacentes a la región conectada
def obtenerColoresAdyacentes(matriz, region):
    filas, columnas = matriz.shape
    coloresAdyacentes = defaultdict(int)
    
    for x, y in region:
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= nx < filas and 0 <= ny < columnas and (nx, ny) not in region:
                color = matriz[nx, ny]
                coloresAdyacentes[color] += 1
                
    return coloresAdyacentes

# Función para realizar Flood Fill
def floodFill(matriz, region, nuevo_color):
    for x, y in region:
        matriz[x, y] = nuevo_color

# Función para simular el cambio de color y obtener el tamaño de la región expandida
def simularExpansion(matriz, region, nuevo_color):
    visitadas = np.zeros_like(matriz, dtype=bool)
    cola = deque(region)
    expansion = set(region)
    
    while cola:
        x, y = cola.popleft()
        if not visitadas[x, y]:
            visitadas[x, y] = True
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= nx < len(matriz) and 0 <= ny < len(matriz) and not visitadas[nx, ny]:
                    if matriz[nx, ny] == nuevo_color or (nx, ny) in region:
                        expansion.add((nx, ny))
                        cola.append((nx, ny))
    
    return len(expansion)

def secuenciaColores(matrizClasificada):

    print("Matriz inicial:")
    print(matrizClasificada)

    secuenciaColores = []

    # Ejecutar el algoritmo de Flood Fill
    pasos = 0
    while len(set(matrizClasificada.flatten())) > 1:  # Mientras haya más de un color
        regionConectada = obtenerRegionConectada(matrizClasificada, 0, 0)
        colores_adyacentes = obtenerColoresAdyacentes(matrizClasificada, regionConectada)
        
        # Simular la expansión para cada color adyacente y encontrar el mejor color
        mejorColor = None
        maxExpansion = -1
        for color in colores_adyacentes:
            tamanio_expansion = simularExpansion(matrizClasificada, regionConectada, color)
            if tamanio_expansion > maxExpansion:
                maxExpansion = tamanio_expansion
                mejorColor = color
        secuenciaColores.append(mejorColor)
        floodFill(matrizClasificada, regionConectada, mejorColor)
        pasos += 1
        print(f'Paso {pasos}, color seleccionado: {mejorColor}')
        print(matrizClasificada)
    return pasos, secuenciaColores
