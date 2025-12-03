# Top 3 palabras más usadas
# Del texto que quiera el usuario, mostrar las 3 palabras más repetidas

print("------------------------------")
texto = str(input("Escriba un texto: "))
lista_palabras = texto.split()

cantidad_palabras = {}

for palabra in lista_palabras:
    if palabra not in cantidad_palabras:
        cantidad_palabras[palabra] = lista_palabras.count(palabra)


for palabra, cantidad in cantidad_palabras.items():
    print(f"{palabra}: {cantidad}")
print("------------------------------")


palabra_mas_usada = {"letras" : "", "numeros" : 0}
segunda_mas_usada = {"letras" : "", "numeros" : 0}
tercera_mas_usada = {"letras" : "", "numeros" : 0}


for palabra, cantidad in cantidad_palabras.items():
    if cantidad > palabra_mas_usada["numeros"]:
        palabra_mas_usada["numeros"] = cantidad
        palabra_mas_usada["letras"] = palabra
        
        
for palabra, cantidad in cantidad_palabras.items():
    if palabra != palabra_mas_usada["letras"]:
        if cantidad > segunda_mas_usada["numeros"]:
            segunda_mas_usada["numeros"] = cantidad
            segunda_mas_usada["letras"] = palabra

for palabra, cantidad in cantidad_palabras.items():
    if palabra != palabra_mas_usada["letras"]:
        if palabra != segunda_mas_usada["letras"]:
            if cantidad > tercera_mas_usada["numeros"]:
                tercera_mas_usada["numeros"] = cantidad
                tercera_mas_usada["letras"] = palabra        


print(f"Las tres palabras más repetidas fueron...")
print(f"'{palabra_mas_usada["letras"]}', {palabra_mas_usada["numeros"]} veces.")
print(f"'{segunda_mas_usada["letras"]}', {segunda_mas_usada["numeros"]} veces.")
print(f"'{tercera_mas_usada["letras"]}', {tercera_mas_usada["numeros"]} veces.")
