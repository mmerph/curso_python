'''Programa que busca una lista de palabras en las frases celebres de películas'''

import csv
import os
import argparse

# Función para leer el archivo csv y devolver una lista de frases
def leer_csv(archivo):
    '''Lee un archivo csv y devuelve una lista de frases'''
    frases = []
    with open(archivo, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            frases.append(fila[0])
        print (frases)
    return frases

# función para buscar palabras en las frases 
def buscar_palabras(frases, palabras):
    '''Buscar una lista de palabras en una lista de frases'''
    frases_encontradas = []
    for frase in frases:
        for palabra in palabras:
            if palabra.lower() in frase.lower():
                frases_encontradas.append(frase)
                break  # Si se encuentra una palabra, no es necesario seguir buscando en la misma frase
    return frases_encontradas

# Funicón  par amostrar las frases encontradas
def mostrar_frases(frases_encontradas):
    '''Muestra las frases encontradas'''
    for frase in frases_encontradas:
        print(frase)

# Función principal
def main(archivo, lista_palabras):
    '''Función princpal del programa'''
    #Leer el archivo CSV 
    frases = leer_csv(archivo)
    # Buscar las palabras en las frases
    frases_encontradas = buscar_palabras(frases, lista_palabras)
    # Mostrar las frases encontradas
    mostrar_frases(frases_encontradas)


if __name__ == '__main__':    
    #Crear el parser
    parser = argparse.ArgumentParser(description='Busca una o varias palabras en frases de películas.')

    #añadir argumentos
    parser.add_argument('palabras', nargs='+', help='Palabras a buscar (una o más)')
    #parsear los argumentos
    args = parser.parse_args()
    archivo_frases = os.path.join(os.path.dirname(__file__),'frases.csv')

    




