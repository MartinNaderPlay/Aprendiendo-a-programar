# Con los siguientes conjuntos muestra en pantalla:
# Si frutas tropicales es un subconjunto de frutas
# Si frutas es un subconjunto de frutas tropicales
# Si frutas citricas es disjunto de frutas
# Agrega "naranja" a frutas y vuelve a comprobar si sigue siendo disjunto de frutas citricas 
# Imprime un resumen final indicando que relacion tienen los conjuntos (subconjunto, superoconjunto o disjunto)

frutas = {"Manzana", "Banana", "Pera", "Uva", "Kiwi"}
frutasTropicales = {"Banana", "Kiwi"}
frutasCitricas = {"Naranja", "Limón", "Pomelo"}

print("Es 'Frutas tropicales' un subconjunto de 'Frutas'?", frutasTropicales.issubset(frutas))
print("Es 'Frutas' un subconjunto de 'Frutas tropicales'", frutas.issubset(frutasTropicales))
print("Es 'Frutas citricas' un conjunto disjunto de 'frutas'", frutasCitricas.isdisjoint(frutas))

print("\nEn resumen:\n")

if frutasTropicales.issubset(frutas):
    print("frutas tropicales es un subconjunto de frutas")
else:
    print("frutas tropicales no es un subconjunto de frutas")

print()

if frutas.issubset(frutasTropicales):
    print("furtas es un subconjunto de frutas tropicales")
else:
    print("frutas no es un subconjunto de frutas tropicales")
   
print()

if frutasCitricas.isdisjoint(frutas):
    print("frutasCitricas es un conjunto disjunto de frutas")
else:
    print("frutasCitricas es conjunto dijunto de frutas")

frutas.add("Naranja")

print()

if frutasCitricas.isdisjoint(frutas):
    print("frutasCitricas es un conjunto disjunto de frutas con el agregado de naranja")
else:
    print("frutasCitricas no es un conjunto dijunto de frutas con el agregado de naranja")
