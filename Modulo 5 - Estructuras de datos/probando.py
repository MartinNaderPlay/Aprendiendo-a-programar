lista = [
    {"tarea" : "limpiar", "estado" : "pendiente"},
    {"tarea" : "correr", "estado" : "hecho"},
    {"tarea" : "dormir", "estado" : "pendiente"}
]

def cambiar(tarea, estado):
    for elemento in lista:
        for clave, valor in elemento.items():
            if valor[0] == tarea:
                valor[1] = estado
            

cambiar(str(input("ingrese la tarea a la cual quiere cambiar el valor: ")), str(input("ingrese el estado que le quiere asignar: ")))
print(lista)