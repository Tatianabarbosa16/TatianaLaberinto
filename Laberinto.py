import  readchar
from readchar import key
nombre_jugador = input("Introduce tu nombre: ")
mensaje = "Bienvenid@ al juego"
print("¡Hola" + nombre_jugador + "!")
print(mensaje)

while True:
    tecla_2 = readchar.readkey()
    if tecla_2 == key.UP:
        break
    print(tecla_2)





nombre_jugador = input("Introduce tu nombre: ")
mensaje = "Bienvenid@ al juego"
print("¡Hola" + nombre_jugador + "!")
print(mensaje)


