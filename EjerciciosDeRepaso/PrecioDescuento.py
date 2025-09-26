# Pedir al usuario que ingrese un precio y el numero de descuento para darle el precio final.

precio = int(input("Ingrese el precio del producto: "))

descuento = int(input("ingrese el porcentaje de descuento: "))

precioFinal = precio - ( precio * descuento ) / 100 

print("El precio final del producto es de: ",precioFinal)
