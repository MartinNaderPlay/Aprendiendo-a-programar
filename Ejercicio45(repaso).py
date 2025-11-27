# Frecuencia de palabras
# Contar cuantas veces aparece cada palabra en un texto usando un diccionario

fraseInicial = "Había una vez en un bosque oscuro y en él había un oso que rara vez se dejaba ver"

frase = fraseInicial.lower()

palabraCount = {}

for palabra in frase.split():
    if palabra in palabraCount:
        palabraCount[palabra] += 1
    else:
        palabraCount[palabra] = 1

for clave, valor in palabraCount.items():
    print(f"{clave} = {valor}")
    