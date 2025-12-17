# Crear un archivo saludo.txt y escribir tu nombre.

nombre = str(input("Cómo te llamas?: "))
saludo = "Hola "
comentario = ", me alegra saber de tí!"

with open("saludo.txt", "w", encoding="utf-8") as f:
    f.write(saludo + nombre + comentario) 

with open("saludo.txt", "r", encoding="utf-8") as f:
       contenido = f.read()
       print(contenido)