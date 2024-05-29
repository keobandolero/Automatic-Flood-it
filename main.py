from floodFill import secuenciaColores
from screenCapture import tableroFlood
from matrizColores import llenarMatrizColores
import time
import pyautogui
import cv2

colores = {
        'V': (1400, 935),
        'M': (1620, 935),
        'R': (1250, 935),
        'Y': (1475, 935),
        'A': (1320, 935),
        'N': (1545, 935),
    }

def clickPyautogui(color):
    if color in colores:
        x, y = colores[color]
        pyautogui.click(x, y)
        time.sleep(0.5) 
    else:
        print(f"Color {color} no definido en las coordenadas")


def main():
    while True:
        tableroFlood()
        # Cargar la imagen recortada
        imagen = cv2.imread('tablero_recortado.png')
        
        # Llenar la matriz con los colores del tablero
        matriz_clasificada = llenarMatrizColores(imagen)

        # Ejecuta el algoritmo de Flood Fill en el tablero capturado
        pasos, secuencia_colores = secuenciaColores(matriz_clasificada)

        if pasos <= 21:
            print(f'\nSolución en {pasos} pasos')
            r = input('Presione enter para continuar --> ')
            time.sleep(2)
            if r == "":
                for color in secuencia_colores:
                    clickPyautogui(color)
            print('------- FIN -------')
            exit()
        elif pasos > 21:
            print('\n------- WARNING -------')
            print("\nEste tablero supera el límite de movimientos permitidos")
            seguimos = input("\nPresiona enter para continuar de todas formas, 'R' para reiniciar con un nuevo tablero o cualquier otra tecla para salir --> ")
            if seguimos == "":
                for color in secuencia_colores:
                    clickPyautogui(color)
            elif seguimos.lower() == 'r':
                pyautogui.click(1626, 230)
                time.sleep(2)
                continue  # Reinicia el ciclo
            else:
                exit() 

if __name__ == "__main__":
    main()