'''
funciones auxiliares del jeugo del ahorcado
'''

def cargaArchivoTexto(archivo:str) -> list:
    '''
    Carga un archivo de texto y devuelve una lista
    con las oraciones del archivo
    '''
    with open(archivo, 'r') as file:
        oraciones = file.readlines()
    return oraciones

if __name__== '__main__':
    lista = cargaArchivoTexto('./plantillas/plantilla-0.txt')
    for elemento in lista:
        print(elemento)