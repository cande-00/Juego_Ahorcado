from categorias import *
from prueba import *

def jugar_ahorcado()->None:
  while True:
      
    opcion = input("----------\nJugar\n---------\nSalir\n--------\n")
    match opcion:
        case "Jugar":
            mostrar_palabra_oculta(palabra,letras_encontradas)
            break
        case "Salir":
               break
        case _:
            break
  
  
            
if __name__ == "__main__":
   jugar_ahorcado()
                