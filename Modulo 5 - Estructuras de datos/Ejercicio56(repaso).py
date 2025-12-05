# Pequeño sistema de login:
# Diccionario de usuarios y contraseñas
# Pedir usuario y contraseña
# Verificar si coincide 

usuario_contraseña = {}

def ingresar(nombre, contraseña):
    usuario_contraseña[nombre] = contraseña

def verificar(nombre, contraseña):
    if usuario_contraseña[nombre] == contraseña:
        print("El usuario y la contraseña, son correctos.")
    else:
        print("Error de usuario o contraseña.")



while str(input("Desea realizar una operación? (si/no): ")) == "si":
    decidir = int(input("Si desea agregar un usuario escriba (1), si desea ingresar escriba (2): "))
    if decidir == 1:
        ingresar(str(input("Ingrese el nombre: ")), str(input("Ingrese la contraseña: ")))
    elif decidir == 2:
        verificar (str(input("Ingrese el nombre: ")), str(input("Ingrese la contraseña: ")))
    else:
        print("Entrada incorrecta. Reintente nuevamente.")
print("Gracias por su visita!")

