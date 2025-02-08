import argparse
import tablero

def main(jugador: str, compu: str):
    '''
    Función principal
    '''
    X = {"G" : 0, "P" : 0, "E" : 0}
    O = {"G" : 0, "P" : 0, "E" : 0}
    score = {"X": X, "O": O}
    numeros = [str(i) for i in range(1, 10)]
    corriendo = True
    while corriendo:
        dsimbolos = {x:x for x in numeros}
        print(f'Juega {jugador} VS. {compu}')
        g = tablero.juego(dsimbolos, jugador, compu)
        tablero.actualiza_score(score, g, jugador, compu)
        tablero.despliega_tablero(score)
        seguir = input('¿Quieres seguir jugando? (s/n)')
        if seguir.lower() != 's':
            corriendo = False
    '''
    g = juego(dsimbolos)
    if g is not None: 
        print(f'El ganador es {g}')
    else:
        print('Empate')
    '''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', type = str,
    help = 'Nombre del jugador', default = 'Usuario')
    parser.add_argument('-c', type = str,
    help = 'Nombre de la computadora' , default = 'IA')
    args = parser.parse_args()
    main(args.j, args.c)