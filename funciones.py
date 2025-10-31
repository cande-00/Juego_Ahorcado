import random
import csv
from datetime import date

def seleccionar_categoria(lista_palabras: dict) -> str:
    categorias = list(lista_palabras.keys())
    indice_random = random.randint(0, len(categorias) - 1)
    
    return categorias[indice_random]

def seleccionar_palabra(lista_palabras: dict, categoria: str) -> str:
    palabras = lista_palabras[categoria]
    indice_random = random.randint(0, len(palabras) - 1)

    return palabras[indice_random]

def validate_length(string: str, minimo_len: int, maximo_len: int) -> bool:
    return minimo_len <= len(string) <= maximo_len

def get_string(msg: str, msg_error: str, minimo_len: int, maximo_len: int) -> str:
    while True:
        string = input(msg)
        if validate_length(string, minimo_len, maximo_len):
            return string
        print(f"{msg_error}. La cadena debe tener minimo: {minimo_len} y maximo {maximo_len} caracteres.")

def guardar_puntuacion(nombre_usuario: str, puntuacion_total: int):
    with open('puntuaciones.csv', 'a', newline='') as csvfile:
        fieldnames = ['nombre_usuario', 'puntuacion', 'fecha']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        fecha = date.today()

        # writer.writeheader()

        writer.writerow({'nombre_usuario': f'{nombre_usuario}', 'puntuacion': f'{puntuacion_total}', 'fecha': f'{fecha}'})
