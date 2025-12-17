# Crear un programa capaz de:
# Guardar contactos en un archivo JSON
# Cargar los contactos al iniciar
# Agregar nuevos contactos
# Listarlos
# Eliminar uno
# Salir

import json

archivo = "contactos.json"

def leer_contactos():
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def guardar_contactos(contactos):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(contactos, f, indent=4)

#-------------------------------------------------------------------

def cargar(nombre, numero):
    contactos = leer_contactos()
    contactos[nombre] = numero
    guardar_contactos(contactos)

def mostrar():
    contacto = leer_contactos()
    print("\n---Lista de contactos---\n")
    for nombre, numero in contacto.items():
        print(f"{nombre}: {numero}")

def eliminar(nombre):
    contactos = leer_contactos()
    if nombre in contactos:
        del contactos[nombre]
        guardar_contactos(contactos)
    else:
        print("El contacto no existe...")

#-------------------------------------------------------------------

while str(input("\nDesea ver o modificar la agenda? (si/no): ")) == "si":
    operacion = str(input("\nEscriba la operación que quiere realizar (ver-agregar-eliminar): ")) 
    if operacion == "ver":
        mostrar()
    elif operacion == "agregar":
        cargar(str(input("Nombre: ")), int(input("Número: ")))
    elif operacion == "eliminar":
        eliminar(str(input("Nombre: ")))