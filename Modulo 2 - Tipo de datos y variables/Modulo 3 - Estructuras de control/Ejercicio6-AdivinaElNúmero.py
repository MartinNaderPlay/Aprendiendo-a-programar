numero_secreto = 7
intento = 0 

while intento != numero_secreto:
    intento = int(input("Adivina el numero del 1 al 10:"))
    if intento < numero_secreto:
        print("No, número demasiado bajo")
        
    elif intento > numero_secreto:
        print("No, número demasiado alto")
    else: 
        print("Adivinaste!")
