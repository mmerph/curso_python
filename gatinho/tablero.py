'''
tablero.py: Dibuja el tablero del juego de El gato
'''
import random

lista_combinaciones = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
    ['1','4','7'],
    ['2','5','8'],
    ['3','6','9'],
    ['1','5','9'],
    ['3','5','7']
    ]

def obtenerSimbCompu(simbJugador):
    '''Determina el símbolo de la computadora'''
    return 'O' if simbJugador == 'X' else 'X'

def dibuja_tablero(simbolos: dict):
    '''
    Dibuja el tablero del juego del gato
    '''
    # los tres apostrofes en  permite hacer una cadena con enters
    print(f''' 
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ----------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ----------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')

def ia(simbolos: dict, cNombre: str, simbJugador: str, simbCompu: str, lista_combinaciones: list):
    '''
    Juega la máquina de forma inteligente
    '''
    print(f'Turno de {cNombre} como {simbCompu}')

    # Intentar ganar
    for combinacion in lista_combinaciones:
        valores = [simbolos[casilla] for casilla in combinacion]
        if valores.count(simbCompu) == 2:  # Hay dos de la computadora
            for casilla in combinacion:
                if simbolos[casilla] not in [simbJugador, simbCompu]:  # Si está vacía
                    simbolos[casilla] = simbCompu
                    print(f'{cNombre} seleccionó la casilla: {casilla}')
                    return  

    # Bloquear al jugador si está por ganar
    for combinacion in lista_combinaciones:
        valores = [simbolos[casilla] for casilla in combinacion]
        if valores.count(simbJugador) == 2:  # Hay dos del jugador
            for casilla in combinacion:
                if simbolos[casilla] not in [simbJugador, simbCompu]:  # Si está vacía
                    simbolos[casilla] = simbCompu
                    print(f'{cNombre} seleccionó la casilla: {casilla}')
                    return  

    # Elegir el centro si está disponible
    if simbolos["5"] == "5":
        simbolos["5"] = simbCompu
        print(f'{cNombre} seleccionó la casilla 5')
        return  

    # Elegir una esquina disponible
    esquinas = ["1", "3", "7", "9"]
    esquinas_libres = [e for e in esquinas if simbolos[e] == e]
    if esquinas_libres:
        casilla = random.choice(esquinas_libres)
        simbolos[casilla] = simbCompu
        print(f'{cNombre} seleccionó la casilla {casilla}')
        return  

    # Elegir cualquier casilla libre
    casillas_libres = [c for c in simbolos if simbolos[c] == c]
    if casillas_libres:
        casilla = random.choice(casillas_libres)
        simbolos[casilla] = simbCompu
        print(f'{cNombre} seleccionó la casilla {casilla}')

            

def usuario(simbolos: dict, jNombre: str, simbJugador: str, simbCompu: str):
    '''
    Juega el usuario
    '''
    lista_numeros = [str(i) for i in range(1,10)]
    ocupado = True
    while ocupado is True:
        x = input(f'Turno de {jNombre} como {simbJugador}. Ingresa el número (del 1 al 9) de la casilla: ')
        if x in lista_numeros:
            if simbolos[x] not in [simbJugador, simbCompu]:
                print(f'{jNombre} seleccionó la casilla {x}:')
                simbolos[x] = simbJugador
                ocupado = False
            else: 
                print('Casilla ocupada')
        else:
            print('Número no válido')

def juego(simbolos: dict, jNombre: str, cNombre: str, simbJugador: str):
    '''
    juego del gato
    '''
    simbCompu = obtenerSimbCompu(simbJugador)

    en_juego = True
    dibuja_tablero(simbolos)
    movimientos = 0
    gana = None
    while en_juego:
        usuario(simbolos, jNombre, simbJugador, simbCompu)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_gana(simbolos, lista_combinaciones)
        if gana is not None:
            ganador = jNombre
            en_juego = False
            continue
        if movimientos >= 9:
            en_juego = False
            continue
        ia(simbolos, cNombre, simbJugador, simbCompu, lista_combinaciones)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_gana(simbolos, lista_combinaciones)
        ganador = ''
        if gana is not None:
            ganador = cNombre
            en_juego = False
            continue
        if movimientos >= 9:
            en_juego = False
            continue
    return ganador
        


def checa_gana(simbolos: dict, combinaciones: list):
    '''
    Checa si hay un ganador
    '''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]] and simbolos[c[0]] in ['X', 'O']:
            return simbolos[c[0]]
    return None

def actualiza_score(score: dict, ganador: str, jNombre: str, cNombre: str, simbJugador: str):
    '''Actualiza el score'''
    simbCompu = obtenerSimbCompu(simbJugador)

    USUARIO= score [simbJugador]
    COMPUTADORA = score [simbCompu]
    if ganador is not None:
        print(f'El ganador es {ganador}')
        if ganador == jNombre:
            USUARIO["G"] += 1
            COMPUTADORA["P"] += 1
        elif ganador == cNombre:
            COMPUTADORA["G"] += 1
            USUARIO["P"] += 1
        else: 
            USUARIO["E"] += 1
            COMPUTADORA["E"] += 1
    else:
        print('Empate')
        USUARIO['E'] += 1
        COMPUTADORA["E"] += 1
    
def despliega_tablero(score: dict, simbJugador: str):
    '''Despliega el tablero de score'''
    simbCompu = obtenerSimbCompu(simbJugador)
    
    print(f'''
    {simbJugador} | G: {score[simbJugador]["G"]} | P: {score[simbJugador]["P"]} | E: {score[simbJugador]["E"]}
    {simbCompu} | G: {score[simbCompu]["G"]} | P: {score[simbCompu]["P"]} | E: {score[simbCompu]["E"]}
''')
    

if __name__ == '__main__':
    numeros = [str(x) for x in range(1, 10)]
    dsimbolos = {x:x for x in numeros}
    jNombre = "Usuario"  # Nombre predeterminado del jugador
    cNombre = "IA"       # Nombre predeterminado de la computadora
    g = juego(dsimbolos, jNombre, cNombre, 'X')  # Ahora pasas los argumentos correctamente
    if g is not None: 
        print(f'El ganador es {g}')
    else:
        print('Empate')
