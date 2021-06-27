import json

def guardar(persona):
    archivo = open("registros.json","a")
    archivo.write(f"{json.dumps(persona)}\n")
    archivo.close()

def leer():
    archivo = open("registros.json", "r")
    lista = archivo.readlines()
    personas = [ json.loads(l.strip()) for l in archivo.readlines()]
    archivo.close()
    return personas