# Agrupar por inicial
# Dada una lista de nombres, agrupalos por su letra inicial en un diccionario

listaNombres = ["Juan", "Pablo", "Jorge", "Marcos", "Lucas", "Maximo", "Jonatan", "Martín", "Lazaro", "Lorenzo", "Pepe"]
separador = ", "
grupoNombres = {}

for nombre in listaNombres:
    for letra in nombre[0]:
        if letra in grupoNombres:
            grupoNombres[letra] += separador + nombre 
        else:
            grupoNombres[letra] = nombre
        
print("Lista de nombres ordenados por grupo de letras")      
for letra, nombre in grupoNombres.items():
    print(f"Grupo {letra}: {nombre}.")