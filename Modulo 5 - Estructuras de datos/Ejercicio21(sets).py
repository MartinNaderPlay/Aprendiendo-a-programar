# Crea dos conjuntos, club A y club B con nombres de socios (al menos 5 en cada uno)
# Asegurate de que algunos nombres se repitan entre ambos clubes (para simular socios que están en los dos)
# Muestra socios del club A y los socios del club B
# Calcula y muestra: 
# Los socios en común (intersección) 
# Los socios exclusivos del Club A 
# Los socios exclusivos del Club B
# Todos los socios de ambos clubes sin repetir nombres
# Simula que se fusionan los clubes en un nuevo conjunto y agrega dos socios nuevos 
# Finalmente:
# Elimina un socio usando discard()
# Intenta eliminar otro usando remove() (elige un nombre que no esté para que veas la diferencia)
# Muestra el total de socios luego de todos los cambios 

clubA = {"Pablo", "Rafael", "Ernesto", "Maximiliano", "Dante"}
clubB = {"Cristian", "Dante", "Javier", "Pablo", "Muricio"}

print("\nLos socios del club A son:\n")

[print(socio) for socio in clubA]

print("\nLos socios del club B son:\n")

[print(socio) for socio in clubB]

print("\nLos socios que tienen en común los clubes son:\n")

[print(socio) for socio in clubA & clubB]

print("\nLos socios exclusivos del clubA son:\n")

[print(socio) for socio in clubA - clubB]

print("\nLos socios exclusivos del clubB son:\n")

[print(socio) for socio in clubB - clubA]

print("\nTodos los Socios son:\n")

[print(socio) for socio in clubA | clubB]

clubMayor = clubA | clubB 

clubMayor.add("Jorge")
clubMayor.add("Tomás")

clubMayor.discard("Pablo")

clubMayor.remove("Cristian")

print("\nLos Socios resultantes son:\n")

[print(socio) for socio in clubMayor]


