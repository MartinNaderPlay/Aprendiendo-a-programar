# Matriz simple
# Cree una matríz simple como lista de listas y cambie el elemento central por 999

matriz = [
    [4, 5, 6],
    [1, 0, 9],
    [12, 8, 2]
]

matriz[1][1] = 999

print("La matríz simple con su elemento central modificado es:")
for lista in matriz:
    print(lista)