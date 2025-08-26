def compararNumeros(a, b, c):
    if a > b and a > c:
        return print("el numero mas alto es: ", a)
    elif b > a and b > c:
        return print("el numero mas alto es: ", b)
    else:
        return print("el numero mas alto es: ", c)
    
compararNumeros (int(input("ingrese el primer numero: ")), int(input("ingrese un segundo numero: ")), int(input("ingrese un tercer numero: ")))