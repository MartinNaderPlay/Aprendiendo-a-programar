# Contador de enemigos
# Lista con nombres de enemigos.
# Mostrar cuántos enemigos únicos hay (set)
# y cuántos totales (len de lista)

lista_enemigos = ["Jack", "Cocodrilo", "Lucifer", "LaMuerte"]
lista_enemigos2 = ["Jack", "ElCarnicero", "ElSindicalista", "Lucifer"]

enemigos_unicos = set(lista_enemigos) ^ set(lista_enemigos2)

print("Los enemigos únicos son:\n------------------")
for enemigos in enemigos_unicos:
    print(enemigos)

lista_total = len(lista_enemigos) + len(lista_enemigos2)

print("\nLa cantidad total de enemigos es: ",lista_total)