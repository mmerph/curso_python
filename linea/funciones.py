# archivo con todas las funciones necesarias para la aplicación "línea"
import matplotlib.pyplot as plt

def calcular_y(x: float, m: float , b: float) -> float:
    '''
    Calcula el valor de t en una línea recta 
    x: valor de x 
    m: pendiente
    b: intersección en y
    regresa el valor de y
    '''
    return m*x + b

def grafica_linea (X:list,Y:list, m: float, b: float):
    '''
    Función principal qu e calcula las coordenadas de una línea recta.
    Recibimos m y b 
    Regresa: nada   
    '''   
    plt.plot(X,Y)
    plt.title(f'Linea con pendiente {m} y ordenada en el origen {b}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def test_linea():
    y = calcular_y(0.0, 2.0, 3.0)
    return y

if __name__ == '__main__':
    if test_linea() == 3.0:
        print('Test exitoso')
    else:
        print('Algo salió mal')
        