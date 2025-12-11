# Crear un programa capaz de:
# Guardar contactos en un archivo JSON
# Cargar los contactos al iniciar
# Agregar nuevos contactos
# Listarlos
# Eliminar uno
# Salir


import json

contactos = {
    "Martín" : 3865351457,
    "Roberto" : 3865425592,
    "Angela" : 381361568
}

with open("contactos.json", "w", encoding="utf-8") as f:
    json.dump(contactos, f, indent=4)


with open("contactos.json", "r", encoding="utf-8") as f:
    lista = json.load(f)

lista["Germán"] = 11365890

with open("contactos.json", "w", encoding="utf-8") as f:
    json.dump(lista, f, indent=4)