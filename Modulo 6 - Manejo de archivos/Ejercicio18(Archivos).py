# Dividir un archivo en lineas pares e impares en archivos separados

with open("nombres.txt", "r", encoding="utf-8") as f:
    contenido = f.readlines()

with open("lineas_impares", "w", encoding="utf-8") as impares, \
    open("lineas_pares", "w", encoding="utf-8") as pares:
    
    for i, linea in enumerate(contenido, start=1):
        if i % 2 == 0:
            pares.write(linea)
        else:
            impares.write(linea)
