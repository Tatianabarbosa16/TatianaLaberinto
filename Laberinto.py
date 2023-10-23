import readchar
import os
from readchar import key

def clear_terminal():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    nombre_jugador = input("Introduce tu nombre: ")
    mensaje = "Bienvenid@ al juego"
    print("¡Hola" + nombre_jugador + "!")
    print(mensaje)
    
    print("para salir del bucle, presiona la flecha arriba")

    while True:
        tecla_2 = readchar.readkey()
        if tecla_2 == key.UP:
            break
        print(tecla_2)

    clear_terminal()
    numero = 0 
    while numero < 50:
        input("Presiona la tecla 'n' para continuar...")
        clear_terminal()
        numero += 1
        print(numero)

if __name__ == "__main__":
    main()

