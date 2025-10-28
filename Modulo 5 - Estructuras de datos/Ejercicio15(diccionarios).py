# Crear un diccionario llamado "auto" con las siguientes claves y valores:
# Marca : Toyota
# Modelo : Corolla
# Año : 2022
# Color : Blanco
# Mostrar el modelo del auto 
# Agregar una nueva clave llamada "kilometraje" con valor 50000
# Modificar el color a "negro"
# Eliminar la clave "año"
# Mostrar el diccionario fian completo

auto = {
    "Marca" : "Toyota",
    "Modelo" : "Corolla",
    "Año" : 2022,
    "Color" : "Blanco"
}

print("El modelo del auto es:", auto["Modelo"])

auto["kilometraje"] = 50000

auto["Color"] = "Negro"

del auto["Año"]

for clave, valor in auto.items():                           # Usando 'for' para conseguir un mejor orden del diccionario 
    print(f"{clave}: {valor}")                              # cuando se muestra en el terminal