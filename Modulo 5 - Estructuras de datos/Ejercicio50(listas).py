# Sin repetir
# Convertir una lista de listas en una sola lista sin elementos repetidos. 

comidasTradicionales = [
    ["Empanadas", "Humita", "Locro", "Tamales"],
    ["Tamales", "Chupín", "Cordero", "Trucha"]
]

union = comidasTradicionales[0] + comidasTradicionales[1]
comidasTradicionales = set(union)


print("La lista unificada de comidas tradicionales es:")
for comida in comidasTradicionales:
    print(comida)