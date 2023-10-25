import os, random, readchar
from dataclasses import dataclass
from typing import List


def lectura_de_mapas(ruta: str):
    
    with open(ruta, 'r', encoding='utf-8') as archivo:
        next(archivo) 
        mapa = [list(linea.rstrip()) for linea in archivo]
    return mapa

@dataclass

class Juego:
    
    nombre: str
    mapa: List[List] = None
    pos_inicial: tuple = None
    pos_final: tuple = None
    
    def clean_pantalla(self):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_mapa(self):
        
        self.clean_pantalla()
        for row in self.mapa:
            print(' '.join(row))
            
    def main_loop(self):
        
        px, py = self.pos_inicial
        while (px, py) != self.pos_final:
            self.mapa[py][px] = "P"
            self.print_mapa()
            self.mapa[py][px] = '.'
            px, py = self.mover(px, py)
        print("El juego termino!!")
        print(f'Lo lograste!! {self.nombre},\nFelicidades pudiste escapar!')
            
    def mover(self, px, py):
        
        new_px, new_py = px, py
        
        move_pj = readchar.readkey()
        if move_pj == readchar.key.UP:
            new_py = py - 1
            if new_py >= 0 and self.mapa[new_py][px] != '#':
                py = new_py
            
        elif move_pj == readchar.key.DOWN:
            new_py = py + 1
            if new_py < len(self.mapa) and self.mapa[new_py][px] != '#':
                py = new_py
                
        elif move_pj == readchar.key.LEFT:
            new_px = px - 1
            if new_px >= 0 and self.mapa[py][new_px] != '#':
                px = new_px
                
        elif move_pj == readchar.key.RIGHT:
            new_px = px + 1
            if new_px < len(self.mapa[py]) and self.mapa[py][new_px] != '#':
                px = new_px
                
        return px, py

def main():
    
    nombre= input("Introduzca su nombre: ")
    
    print("!Podras escapar del laberinto mas potente de toda la historia, {}?".format(nombre))
    
    lista_mapas = os.listdir("TatianaLaberinto/mapas/")
    
    ruta_mapa = random.choice(lista_mapas)
    
    mapa = lectura_de_mapas("TatianaLaberinto/mapas/"+ruta_mapa)
    
    pos_inicial = (1, 1)  
    
    pos_final = (19, 20)
    
    juego = Juego(nombre, mapa, pos_inicial, pos_final)
    
    juego.main_loop()


if __name__ == "__main__":
    main()