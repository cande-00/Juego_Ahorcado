import random

def actualizar_palabra_oculta(lista_palabras: dict, tematica: str) -> str:
    """_summary_

    Args:
        lista_palabras (dict): Diccionario recibido por parametro.
        tematica (str): String recibido por parametro.

    Returns:
        str: La funcion busca la tematica en el diccionario y recorre una lista de palabras para luego tomar una al azar.
    """
    palabras = []

    for categoria in lista_palabras:
        if categoria == tematica:
            palabras = lista_palabras[categoria]

    if len(palabras) == 0:
        print("no se encontro la categoria")

    indice = random.randint(0, len(palabras) - 1)
    actualizacion_palabra = palabras[indice]

    return actualizacion_palabra
