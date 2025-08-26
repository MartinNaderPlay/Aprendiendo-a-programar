def contar_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    cont = 0
    for letra in texto:
        if letra in vocales:
            cont += 1
    return cont 

frase = str(input("Escriba una frase: "))
total = contar_vocales(frase)
print(f"la frase tiene {total} vocales.")
    