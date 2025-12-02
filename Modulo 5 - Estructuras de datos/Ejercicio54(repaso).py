# Top 3 palabras más usadas
# Del texto que quiera el usuario, mostrar las 3 palabras más repetidas

print("------------------------------")
texto = str(input("Escriba un texto: "))
lista_palabras = texto.split()

cantidad_palabras = {}

for palabra in lista_palabras:
    if palabra not in cantidad_palabras:
        cantidad_palabras[palabra] = lista_palabras.count(palabra)


palabra_mas_usada = 0
segunda_mas_usada = 0
tercera_mas_usada = 0

for palabra, cantidad in cantidad_palabras.items():
    print(f"{palabra}: {cantidad}")
print("------------------------------")


