# Diccionario inverso
# Dado un diccionario: paises = {"Argentina" : "AR", "Brasil" : "BR", "Chile", "CH"}, 
# Crea un diccionario inverso {"Ar" : "Argentina" ...} 

paises = {
    "Argentina" : "AR",
    "Brasil" : "BR",
    "Chile" : "CH"
}

paisesInv = {}

for pais, inicial in paises.items():
    paisesInv[inicial] = pais

print("La lista inicial, paises con sus iniciales es:")
for pais, inicial in paises.items():
    print(f"Pais: {pais}, Inicial: {inicial}")

print("La lista inicial invertida, inicial con su pais, es:")
for inicial, pais in paisesInv.items():
    print(f"Inicial: {inicial}, País: {pais}")
