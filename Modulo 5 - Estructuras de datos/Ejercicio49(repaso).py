# Intersección
# Dados dos sets, obtener su intersección sin usar el merodo .intersection()

poderSuperMan = {"Volar", "SuperFuerza", "VisionLáser"}
poderMisterIncreible = {"SuperFuerza", "ResistenciaExtrema", "AgilidadMejorada"}

poderEnComun = poderSuperMan&poderMisterIncreible


print(f"Los poderes en común de ambos superheroes es la: {iter(poderEnComun)}")