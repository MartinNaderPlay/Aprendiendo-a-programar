# Agregar una linea al final del archivo del ejercicio 1

comentario = " ...estamos avanzando!"

with open("saludo.txt", "a", encoding="utf-8") as f:
    f.write(comentario)