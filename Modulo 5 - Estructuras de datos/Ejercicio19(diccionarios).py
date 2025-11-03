# Hacer un programa que gestione una lista de alumnos, donde cada alumno sea un diccionario 
# con esta información: Nombre, Edad, Notas(una lista con tres calificaciones)
# Crear una lista llamada alumnos, con tres alumnos iniciales 
# Agrega un nuevo alumno con su información 
# Calcula y muestra el promedio de notas de cada alumno 
# Determina y muestra: El alumno con el promedio mas alto y el alumno con el promedio mas bajo
# Finalmente, muestra el listado actualizado con nombre, edad su promedio.
# Pista: usa un for para recorrer la lista de alumnos y un sum() para obtener el promedio

alumnos = [
    {"Nombre": "Roberto", "Edad": 20, "Notas": [5, 7, 9]},
    {"Nombre": "Jonatan", "Edad": 23, "Notas": [6, 9, 10]},
    {"Nombre": "Ailen", "Edad": 25, "Notas": [4, 5, 3]}
]

# Agregar un nuevo alumno
alumnos.append({"Nombre": "Esteban", "Edad": 30, "Notas": [6, 7, 9]})

print("\nPromedios de los alumnos:\n")

# Calcular y guardar el promedio en cada alumno
for a in alumnos:
    promedio = sum(a["Notas"]) / len(a["Notas"])
    a["Promedio"] = promedio
    print(f"El promedio de {a['Nombre']} es: {promedio:.2f}")

# Encontrar el alumno con el promedio más alto y más bajo
alumno_max = max(alumnos, key=lambda a: a["Promedio"])
alumno_min = min(alumnos, key=lambda a: a["Promedio"])

print(f"\nEl promedio más alto es de {alumno_max['Nombre']} ({alumno_max['Promedio']:.2f})")
print(f"El promedio más bajo es de {alumno_min['Nombre']} ({alumno_min['Promedio']:.2f})")

