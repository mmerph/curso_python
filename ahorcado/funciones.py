'''
funciones auxiliares del jeugo del ahorcado
'''

def cargaArchivoTexto(archivo:str) -> list:
    '''
    Carga un archivo de texto y devuelve una lista
    con las oraciones del archivo
    '''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def despliegaPlantillas(diccionario: dict, nivel:int):
    '''
    Despliega una plantilla del juego
    '''
    if nivel <= 5: 
        plantilla = diccionario[nivel]
        for renglon in plantilla:
            print(renglon)

def cargaPlantillas(nombre_plantilla)-> dict:
    '''
    Carga las plantillas del juego a partir de un archivo de texto
    '''

    plantillas = {}
    for i in range(6):
        plantillas[i] = cargaArchivoTexto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

if __name__== '__main__':
    plantilla = cargaPlantillas('plantilla')
    despliegaPlantillas(plantilla,5)
    lista_oraciones = cargaArchivoTexto('./datos/pg15532.txt')
    print(lista_oraciones[110:115])
    texto = "".join(lista_oraciones[110:])
    print(texto[:100])