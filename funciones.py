def rebanar(cadena: str, inicio: int, finalizacion: int) -> str:
    """summary

    Args:
        cadena (str): String recibido por parametro.
        inicio (int): Entero que recibido por parametro que marca el inicio.
        finalizacion (int): Entero recibido por parametro que marca la finalizacion

    Returns:
        str: La funcion retorna un nuevo string, recortando el anterior desde el inicio hasta la finalizacion. 
    """
    cadena_auxiliar = ""
    for caracter in range(inicio, finalizacion):
        cadena_auxiliar += cadena[caracter]

    return cadena_auxiliar


def mostrar_palabra_oculta(palabra_secreta, letras_adivinadas: list) -> list:
    """con esta funcion logro que se muestren _ por cada letra dentro de la palabra oculta

    Args:
        palabra_secreta (_type_): palabra a adivinar del usuario
        letras_adivinadas (list): letras que si adivino el usuario

    Returns:
        list: devuelve una lista con las posiciones a mostrar de la palabra secreta
    """
    retorno = None
    palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        letra_actual = palabra_secreta[i]
        letra_encontrada = False
        k = 0

        while k < len(letras_adivinadas):
            if letra_actual == letras_adivinadas[k]:
                letra_encontrada = True
                break
            k += 1

        caracter_mostrar = "_"
        
        if letra_encontrada:
            caracter_mostrar = letra_actual
        
        palabra_mostrada += caracter_mostrar + " "
    
    retorno = rebanar(palabra_mostrada, 0, len(palabra_mostrada) - 1)

    return retorno


def calcular_puntuacion_parcial(letras_correctas: list, letras_incorrectas: list) -> list:
    """en una lista, acumulo los puntajes que vaya logrando el usuario

    Args:
        letras_correctas (list): cantidad de puntos * 3 que obtiene el jugador
        letras_incorrectas (list): cantidad de puntos * 1 que se le restan al jugador

    Returns:
        list: lista de puntajes por cada posicion es un puntaje distinto si gano o perdio
    """
    puntajes = list()
    puntuacion = 0
    puntuacion += len(letras_correctas) * 3
    puntuacion -= len(letras_incorrectas)

    if puntuacion < 0:
        puntuacion = 0

    puntajes.append(puntuacion)

    return puntajes

def verificar_estado_juego(intentos: int, palabra_secreta: str, letras_correctas: list) -> bool:
    bandera = True
    if intentos == 0:
        bandera = False
    

    for i in range(len(palabra_secreta)):
        letra_actual = palabra_secreta[i]
        letra_encontrada = False

        for j in range(len(letras_correctas)):
            if letra_actual == letras_correctas[j]:
                letra_encontrada = True
                break
    
        if not letra_encontrada:
            bandera = False
    
