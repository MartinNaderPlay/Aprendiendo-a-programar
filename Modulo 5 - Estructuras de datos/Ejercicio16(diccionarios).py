# Crea una lista llamada "autos" que contenga 3 diccionarios, cada uno repesentando un auto con las claves:
# "Marca" "Modelo" "Año" "Color"
# Muestra solo los modelos de todos los autos usando un for
# Agrega un nuevo auto a la lista
# Cambia el color del segundo auto a "Negro"
# Elimina el primer auto de la lista
# Muestra el contenido completo de la lista final usando un for para recorrer cada diccionario e imprimir sus claves y valores

autos = [

    {"Marca" : "Volkswagen", "Modelo" : "Gol", "Año" : 2010, "Color" : "Gris"}, 
    {"Marca" : "Peugeot", "Modelo" : "206", "Año" : 2008, "Color" : "Rojo"}, 
    {"Marca": "Ford", "Modelo" : "Mondeo", "Año" : 2023, "Color" : "Dorado"}

    ]

print("Modelos de autos:")

for auto in autos:
    print(auto["Modelo"])


autos.append({"Marca" : "Toyota", "Modelo" : "Yaris", "Año" : 2025, "Color" : "Naranja"})

autos[1]["Color"] = "Negro"

autos.pop(0)

print("\n\nLista final de autos:\n")
for auto in autos:
    for clave, valor in auto.items():
        print(f"{clave}: {valor}")
    print()

