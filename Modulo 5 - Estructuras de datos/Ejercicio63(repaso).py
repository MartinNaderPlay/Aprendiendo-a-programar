# Tabla de puntuaciones
# Diccionario: jugador ---> puntaje
# Actualiza puntajes y mostrar top 3

puntuaciones_jugadores = {
    "Amadeo17": 984,
    "ElDemoledor_54": 1202,
    "Dexter3000": 1500,
    "ElChavoDel-8": 5421,
    "Goku-fase3": 450,
    "topoGIGIO": 2300
}

def mostrar():
    for jugador, puntaje in puntuaciones_jugadores.items():
        print(f"{jugador}: {puntaje}")

def actualizar(jugador, puntaje):
    puntuaciones_jugadores[jugador] += puntaje
            
def mostrar_top_3():
    for jugador, puntaje in top_3:
        print(f"{jugador}: {puntaje}")


mostrar()
print("----------------------------")
while str(input("Sumar puntaje a un jugador? (si/no)")) == "si":
    actualizar(str(input("Nombre del jugador: ")), int(input("Puntaje adquirido: ")))
print("----------------------------")
mostrar()
print("----------------------------")
print("'TOP 3'")
top_3 = sorted(puntuaciones_jugadores.items(), key=lambda x: x[1], reverse=True)[:3]
mostrar_top_3()