import random
import time

muerto = 0
vivo = 1

def muerto_estado(ancho, alto):
    # Se construye un estado vacío con todas las celdas inactivas.
    #   ancho: el ancho del estado, en celdas
    #   altura: la altura del estado, en celdas devoluciones 
    # Un estado de dimensiones ancho x alto, con todas las celdas inactivas
    # return [[muerto for _ in range(alto)] for _ in range(ancho)]
    return [[muerto for _ in range(alto)] for _ in range(ancho)]

def random_estado(ancho, alto):
    # Construya un estado aleatorio con todas las celdas configuradas aleatoriamente.
    #  ancho: el ancho del estado, en celdas
    #  altura: la altura del estado, en celdas
    #  Devoluciones:
    #  Un estado de dimensiones ancho x alto, con todas las celdas configuradas aleatoriamente
    #  MUERTO o VIVO con igual probabilidad.
    
    estado = muerto_estado(ancho, alto)
    for x in range(0, estado_ancho(estado)):
        for y in range(0, estado_alto(estado)):
            random_number = random.random()
            if random_number > 0.85:
                celda_estado = vivo
            else:
                celda_estado = muerto
            estado[x][y] = celda_estado

    return estado

def estado_ancho(estado):
    # Obtener el ancho de un estado.
    # Parámetros
    #  ----------
    # estado: un juego estado
    # Devoluciones
    # El ancho del estado de entrada
    # return len(estado)
    return len(estado)

def estado_alto(estado):
#       Obtener la altura de un estado.
#      Parámetros
#      ----------
#      estado: un estado del juego
#      Devoluciones
#      -------
#      La altura del estado de entrada
#      
    return len(estado[0])

def next_celda_value(celda_coordenadas, estado):
#       Obtener el siguiente valor de una sola celda en un estado.
#      Parámetros
#      ----------
#      celda_coordenadas: una tupla (x, y) de las coordenadas de una celda
#      estado: el estado actual del tablero de juego
#      Devoluciones
#      -------
#      El nuevo estado de la celda dada, ya sea MUERTO o VIVO.
#      
    ancho = estado_ancho(estado)
    alto = estado_alto(estado)
    x = celda_coordenadas[0]
    y = celda_coordenadas[1]
    n_vivo_vecinos = 0

    # Iterar alrededor de estas celdas vecinas
    for x1 in range((x-1), (x+1)+1):
        # Asegúrate de que no nos salgamos del borde del tablero.
        if x1 < 0 or x1 >= ancho: continue

        for y1 in range((y-1), (y+1)+1):
            # Asegúrate de que no nos salgamos del borde del tablero.
            if y1 < 0 or y1 >= alto: continue
            # ¡Asegúrese de que no contamos la celda como vecina de sí misma!
            if x1 == x and y1 == y: continue

            if estado[x1][y1] == vivo:
                n_vivo_vecinos += 1

    if estado[x][y] == vivo:
        if n_vivo_vecinos <= 1:
            return muerto
        elif n_vivo_vecinos <= 3:
            return vivo
        else:
            return muerto
    else:
        if n_vivo_vecinos == 3:
            return vivo
        else:
            return muerto

def next_tablero_estado(init_estado):
    # Da un solo paso en el Juego de la Vida.
    #  Parámetros
    #  ----------
    #  init_estado: el estado inicial del tablero de Juego
    #  Devoluciones
    #  -------
    #  El siguiente estado del Tablero de Juego, después de dar un paso por cada celda en
    #  el estado anterior.
    ancho = estado_ancho(init_estado)
    alto = estado_alto(init_estado)
    next_estado = muerto_estado(ancho, alto)

    for x in range(0, ancho):
        for y in range(0, alto):
            next_estado[x][y] = next_celda_value((x, y), init_estado)

    return next_estado

def render(estado):
    #  Muestra un estado imprimiéndolo en la terminal.
    #  Devoluciones
    #  Nada: esto es puramente una función de visualización.
    
    mostrar_como = {
        muerto: ' ',
        vivo: u"\u2588"
    }
    lineas = []
    for y in range(0, estado_alto(estado)):
        line = ''
        for x in range(0, estado_ancho(estado)):
            line += mostrar_como[estado[x][y]] * 2
        lineas.append(line)
    print ("\n".join(lineas))

def cargar_tablero_estado(filepath):
    #  Carga un estado de tablero desde la ruta de archivo dada
    #  Parámetros
    #  ----------
    #  ruta del archivo: la ruta del archivo para cargar el estado. células muertas deberían ser
    #      representado por 0s, vivo celdas por 1s
    #  Devoluciones
    #  -------
    #  El estado del tablero cargado desde la ruta de archivo dada
    with open(filepath, 'r') as f:
        lineas = [l.rstrip() for l in f.readlineas()]

    alto = len(lineas)
    ancho = len(lineas[0])
    tablero = muerto_estado(alto, ancho)

    for x, line in enumerate(lineas):
        for y, char in enumerate(line):
            tablero[x][y] = int(char)
    return tablero


def run_forever(init_estado):
    # Ejecuta el Juego de la Vida para siempre, a partir del estado inicial dado.
    #  Parámetros
    #  ----------
    #  init_estado: el estado del juego para comenzar en
    #  Devoluciones
    #  -------
    #  Esta función nunca regresa: ¡el programa debe salir a la fuerza!
    next_estado = init_estado
    while True:
        render(next_estado)
        next_estado = next_tablero_estado(next_estado)
        time.sleep(0.03)

if __name__ == "__main__":
    init_estado = random_estado(100, 50)
    # init_estado = cargar_tablero_estado('./toad.txt')
    run_forever(init_estado)