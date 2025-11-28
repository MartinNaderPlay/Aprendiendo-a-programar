# Sistema de notas 
# Diccionario con alumnos y sus notas.
# Mostrar promedio, nota más alta y más baja.

planillaNotas = {
    "German" : [8, 6, 7],
    "Pedro" : [5, 9, 10],
    "Ludmila" : [9, 3, 1],
    "Rita" : [6, 7, 6],
    "José" : [7, 7, 10],
    "Ruperta" : [10, 9, 10]
}

print("---Planilla de notas y promedios---\n")
for nombre, notas in planillaNotas.items():
    print(f"_{nombre}_\nnota más alta: {max(notas)}\nnota más baja: {min(notas)}\npromedio: {(sum(notas))/len(notas)}\n")