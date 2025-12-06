# Gestor de tareas
# Lista de tareas.
# Funciones: agregar, marcar como hecha, eliminar, mostrar

lista_tareas = []
n=0

def agregar(tarea):
    lista_tareas.append({})
    lista_tareas[n]["Tarea"] = tarea
    lista_tareas[n]["Estado"] = "Pendiente"

def modificar(tarea, estado):
    for elemento in lista_tareas:
        if elemento["Tarea"] == tarea:
            elemento["Estado"] = estado

def mostrar():
    print("---------------------------")
    for elemento in lista_tareas:
        for tarea, estado in elemento.items():
            print(f"{tarea}: {estado}")
        print("---------------------------")

def eliminar(tarea):
    for elemento in lista_tareas:
        if elemento["Tarea"] == tarea:
            lista_tareas.remove(elemento)


while str(input("Desea agregar una tarea? (si/no): ")) == "si":
    agregar(str(input("Ingrese la tarea que quiere agregar: ")))
    n+=1

mostrar()

modificar(str(input("Ingrese la tarea que desea marcar... ")), str(input("Ingrese el estado en que está la tarea... ")))
   
eliminar(str(input("Ingrese la tarea que desea eliminar... ")))   

mostrar()

