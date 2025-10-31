# Crear una lista llamada estudiantes que contenga tres diccionarios, cada uno con la siguiente estructura
#{ "nombre": "", "edad": , "nota": }
# Mostrar los nombres de los estudiantes usando for
# Agrega un nuevo estudiante al final de la lista
# Cambia la nota del segundo estudiante por 10
# Elimina el primer estudiante de la lista 
# recorre la lista final e imprime todos los datos de cada estudiante conun formato claro:

estudiantes = [
    {"Nombre" : "Pedro", "Edad" : 27, "Nota" : 8},
    {"Nombre" : "María", "Edad" : 25, "Nota" : 6},
    {"Nombre" : "Juan", "Edad" : 30, "Nota" : 9}
    ]

print("la lista inicial de estudiantes es:\n")
for nombre in estudiantes:
    print(nombre["Nombre"])
print()
 
estudiantes.append({"Nombre" : "Rita", "Edad": 32, "Nota": 7})

estudiantes[1]["Nota"] = 10

estudiantes.pop(0)

print("la lista de estudiantes con su edad y nota son:")
print()

for estudiante in estudiantes:
    for clave, valor in estudiante.items():
        print(f"{clave}: {valor}")
    print()

