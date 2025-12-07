# Misiones del jugador 
# Lista de misiones 
# Agregar nuevas misiones sin duplicar (usar sets)

lista_misiones = ["Llegar a la capital", "Tomar poción de vida", "Destruir al jefe", "Descansar"]

def agregar(mision):
    lista_extra = []
    lista_extra.append(mision)
    suma = set(lista_extra) | set(lista_misiones)
    lista_misiones.clear()
    lista_misiones.extend(list(suma))

while str(input("desea agregar una mision? (si/no): ")) == "si":
    agregar(str(input("mision: ")))
    print(lista_misiones)

