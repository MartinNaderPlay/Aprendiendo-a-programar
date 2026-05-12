# Guardar varios contactos en json

import json

contactos = {
    "Juan" : 386500329,
    "Riki" : 384399101,
    "Jorge": 293482934,
}

with open("contactos_tel.json", "w", encoding="utf-8") as f:
    json.dump(contactos, f)