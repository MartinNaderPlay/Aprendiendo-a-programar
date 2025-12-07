# Analizador de texto
# Contar palabras
# Palabras unicas
# Palabra más larga
# Frecuencia de cada una

texto = str(input("Ingrese un texto para ser analizado: "))

palabras_texto = texto.split()
cantidad_palabras = len(palabras_texto)
palabras_unicas = []
frecuencia_palabras = {}
cantidad_letras = 0
palabra_mas_larga = ""
print("--------------------")
print(f"La cantidad de palabras que hay en el texto son:", cantidad_palabras)
print("--------------------")
for palabra in palabras_texto:
    if palabra not in frecuencia_palabras:
        frecuencia_palabras[palabra] = palabras_texto.count(palabra)
        
for palabra in texto.split():
    if len(list(palabra)) > cantidad_letras:
        cantidad_letras = len(list(palabra))
        palabra_mas_larga = palabra

print(f"la palabra mas larga es:", palabra_mas_larga)
print("--------------------")
for palabra, cantidad in frecuencia_palabras.items():
    print(f"la palabra {palabra}, se repite {cantidad} veces")
    if cantidad == 1:
        palabras_unicas.append(palabra)
print("--------------------")
print(f"Las palabras unicas son: {palabras_unicas}")

