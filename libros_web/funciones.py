'''Archivo con las funciones necesarioas de la Aplicación Libro Web'''
import csv

def lee_archivo_csv(archivo: str)-> list:
    '''Lee un archivo CSV y lo convierte en una lista de diccionarios'''
    with open(archivo, "r", encoding= 'utf8') as f:
        return [x for x in csv.DictReader(f)]
    
def crea_diccoinario_titulos(lista:list)->dict:
    '''Crea un diccionario con los títulos como clave y el resto de los datos como valores'''
    return {x['title']: x for x in lista}

def busca_en_titulo(diccionario, palabra)-> list:
    '''Busca palabra en titulo de la lista de diccionarios'''
    lista =[]
    palabra = palabra.lower()
    for titulo, libro in diccionario.items():
        if palabra in titulo.lower():
            lista.append(libro)
    return lista



if __name__ == '__main__':
    archivo_csv = 'booklist2000.csv'
    lista_libros = lee_archivo_csv(archivo_csv)
    diccionario_libros = crea_diccoinario_titulos(lista_libros)
    
    resultado = busca_en_titulo(diccionario_libros, 'rebel')
    print(resultado)