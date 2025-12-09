# Tablero estilo grid
# Cree un tablero 5x5 con lista de listas
# Colocar el jugador en (2, 2)
# Permita moverlo con instrucciones. "arriba", "abajo", etc.

tablero = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def mostrar():
    for elemento in tablero:
        print(elemento)

fila = 2
columna = 2 

def descolocar():
    tablero[fila][columna] = 0

def colocar():
    pocision_jugador = tablero[fila][columna] = "J"
    return pocision_jugador

def mover(direccion):
    global fila
    global columna
    if direccion == "arriba":
        fila -= 1
        return fila
    elif direccion == "abajo":
        fila += 1
        return fila
    elif direccion == "derecha":
        columna += 1
        return columna
    elif direccion == "izquierda":
        columna -= 1
        return columna

colocar()
mostrar()
while str(input("Desea mover el jugador? (si/no): ")) == "si":
    descolocar()
    mover(str(input("Direccion: ")))
    colocar()
    mostrar()