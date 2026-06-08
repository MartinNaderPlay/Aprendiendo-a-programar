# Crear un archivo de logs que registre fecha/hora de cada ejecución

import json
import datetime

with open("logs.txt", "a", encoding="utf-8") as f:
    f.write(f"{datetime.datetime.now()}\n")
