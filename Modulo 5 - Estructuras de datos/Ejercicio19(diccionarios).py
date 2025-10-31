# Hacer un programa que gestione una lista de alumnos, donde cada alumno sea un diccionario 
# con esta información: Nombre, Edad, Notas(una lista con tres calificaciones)
# Crear una lista llamada alumnos, con tres alumnos iniciales 
# Agrega un nuevo alumno con su información 
# Calcula y muestra el promedio de notas de cada alumno 
# Determina y muestra: El alumno con el promedio mas alto y el alumno con el promedio mas bajo
# Finalmente, muestra el listado actualizado con nombre, edad yu promedio.
# Pïsta: usa un for para recorrer la lista de alumnos y un sum() para obtener el promedio

alumnos = [
    {"Nombre" : "Roberto", "Edad": 20, "Nota1": 5, "Nota2": 7, "Nota3": 9},
    {"Nombre": "Jonatan", "Edad": 23, "Nota1": 6, "Nota2": 4, "Nota3": 10},
    {"Nombre": "Ailen", "Edad": 25, "Nota1": 8, "Nota2": 5, "Nota3": 9}
]

alumnos.append({"Nombre": "Esteban", "Edad": 30, "Nota1": 6, "Nota2": 7, "Nota3": 9})

promedio = 