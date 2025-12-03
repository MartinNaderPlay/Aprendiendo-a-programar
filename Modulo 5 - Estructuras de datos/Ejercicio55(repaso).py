# Lista telefonica
# Diccionario: nombre ---> numero
# Funciones: agregar, borrar, buscar, mostrar todo.

lista_contactos = {}

def agregar(nombre, numero):
    lista_contactos[nombre] = numero
    print()
    

def borrar(nombre):
    del lista_contactos[nombre]
    print()
    

def buscar(nombre):
    print(f"El numero de telefono de '{nombre}' es: {lista_contactos[nombre]}")
    print()
    

def mostrar():
    print("Lista de contactos\n------------------")
    for nombre, numero in lista_contactos.items():
        print(f"{nombre}: {numero}")
    print()    
    

print()
decision = str(input("Desea realizar alguna función? (si/no): "))
print()

while decision == "si":
    
    funcion = int(input("Qué función desea realizar?\n\nPara agregar ingrese (1)...\nPara borrar ingrese (2)...\nPara buscar ingrese (3)...\nPara ver la lista completa ingrese (4)...\n\nEntrada: "))
    print()
    if funcion == 1:
        agregar(str(input("ingrese el nombre del contacto: ")), int(input("Ingrese su numero: ")))
    elif funcion == 2:
        borrar(str(input("Ingrese el nombre que desea borrar: ")))
    elif funcion == 3:
        buscar(str(input("Ingrese el nombre del contacto que busca: ")))
    elif funcion == 4:
        mostrar()
print("El programa ha finalizado.")


