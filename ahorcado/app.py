'''
    Programa principal
'''
import funciones as fn
from random import choice
import string

def main(archivo_texto: str, nombre_plantilla = 'plantilla'):

    #cargamos las plantillas
    plantillas = fn.cargaplantillas('nombre_plantilla')
    lista_oraciones = fn.cargaArchivoTexto(archivo_texto)
    palabras = fn.obtenPalabras(lista_oraciones)
    o = 5 #5 oportunidades 
    abcdario = {letra: letra for letra in string.ascii_lowercase}
    adivinadas = set()
    p = choice
    while o > 1:
        fn.despliegaPlantillas(plantillas, o)
        fn.adivinaLetra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Ganaste')
            break
        o -= 1

if __name__ == '__main__':
    archivo = './datos/pg15532.txt'
    main()