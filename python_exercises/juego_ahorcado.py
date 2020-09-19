import random




IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [
    'computadora',
    'teclado',
    'mouse',
    'parlantes'
]
def random_word(WORDS):
    idx = random.randint(0,len(WORDS)-1)
    palabra = WORDS[idx]
    return palabra


def mostrar_tablero(palabra_oculta,contador_errores):
    print(IMAGES[contador_errores])
    print(palabra_oculta)
    print('---- * ---- * ---- * ---- * ---- * ---- * ---- * ---- * ---- * ----')


def run():
    palabra = random_word(WORDS)
    print(palabra)
    palabra_oculta = ['_'] * len(palabra)
    contador_errores = 0

    while True:
        mostrar_tablero(palabra_oculta,contador_errores)
        letra_ingresado = input('Ingrese una letra: ')
        
        indice_palabra = []
        for idx in range(len(palabra)):
            if palabra[idx] == letra_ingresado:
                indice_palabra.append(idx)
        
        if len(indice_palabra) == 0:
            contador_errores += 1
            if contador_errores == 6:
                mostrar_tablero(palabra_oculta,contador_errores)
                print('')
                print("¡Perdiste! La palabra correcta era {}".format(palabra))
                break
        else:       #sino agregar a los espacios en que la letra esta
            for idx in indice_palabra: #[1,5]
                palabra_oculta[idx] = letra_ingresado

            indice_palabra = []

        try:
            palabra_oculta.index('_')
        except ValueError:
            print('')
            print('¡Felicidades! Ganaste. La palabra es : {}'.format(palabra))
            break
    

if __name__ == "__main__":
    print("B I E N V E N I D O S  A  A H O R C A D O S")
    run()