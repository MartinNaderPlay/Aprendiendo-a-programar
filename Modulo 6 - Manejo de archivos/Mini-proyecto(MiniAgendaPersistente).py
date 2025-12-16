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
    "Catherine": 3865439856,
    "Reperta": 381095489
}

with open("contactos.json", "w", encoding="utf-8") as f:
    json.dump(contactos, f, indent=4)

def cargar(contact, num):
    with open("contactos.json", "r", encoding="utf-8") as f:
        json.load(f)
        
    contactos[contact] = num
                                            
    with open("contactos.json", "w", encoding="utf-8") as f:
        json.dump(contactos, f, indent=4)

def mostrar():
    with open("contactos.json", "r", encoding="utf-8") as f:
        listado = json.load(f)
    for nombre, numero in listado.items():
        print(f"{nombre} ---> {numero}")

def eliminar(contact):
    del contactos[contact]
    with open("contactos.json", "w", encoding="utf-8") as f:
        json.dump(contactos, f, indent=4)


while str(input("Desea realizar algun cambio en la lista?: (si/no): ")) == "si":

    operacion = str(input("Ingrese la operación que desea realizar (cargar/mostrar/eliminar): "))
    
    if operacion == "cargar":
        cargar(str(input("Nombre: ")), int(input("Numero: ")))
    elif operacion == "mostrar":
        mostrar()
    elif operacion == "eliminar":
        eliminar(str(input("Nombre: ")))


