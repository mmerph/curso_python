'''
    Programa principal
'''
import funciones as fn
from random import choice
import string
import argparse
import unicodedata
import os

def main(archivo_texto: str, nombre_plantilla = 'plantilla'):

    #cargamos las plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)
    lista_oraciones = fn.carga_archivo_texto(archivo_texto)
    palabras = fn.obtenPalabras(lista_oraciones)
    o = 5 #5 oportunidades 
    abcdario = {letra: letra for letra in string.ascii_lowercase}
    adivinadas = set()
    p = choice(palabras)
    while o > 0:
        fn.despliega_plantilla(plantillas, o)
        o = fn.adivinaLetra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Felicidades, ganaste')
            break
    fn.despliega_plantilla(plantillas, o)
    print(f'La palabra era: {p}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'Juego del ahorcado')
    parser.add_argument('-a', '--archivo', help= 'Archivo de texto con palabras', default= './datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo) == False:
        print(f'El archivo "{archivo}" no existe')
    main(archivo)